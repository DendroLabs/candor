"""Candor — Base Agent.

The foundation every agent inherits from. Every agent in the system shares:
- Access to the compass (read-only — agents cannot change the compass)
- Access to the message bus
- Access to memory (own domain + shared context)
- Access to the Anthropic Claude API for reasoning
- The behavioral standards: no euphemisms, no pretending
"""

import logging
from abc import ABC, abstractmethod

import anthropic

from src.compass.compass import PriorityCompass
from src.models.compass import CompassPosition
from src.models.decisions import AgentRole, Decision, DecisionTier, DecisionStatus
from src.models.messages import Message, MessageType, MessagePriority
from src.shared.bus import MessageBus
from src.shared.memory import MemoryStore

logger = logging.getLogger(__name__)


# The system prompt fragment that every agent carries.
# No euphemisms. No corporate poetry.
BEHAVIORAL_STANDARDS = """
You are an executive AI agent. You operate under these non-negotiable standards:

1. SHAREHOLDER VALUE IS THE OBJECTIVE FUNCTION. Every recommendation includes
   projected shareholder value impact.

2. EMPLOYEE IMPACT IS A FIRST-CLASS VARIABLE. Every recommendation includes
   projected employee impact — weighted per the Priority Compass setting.
   This is not an afterthought appendix. It is a primary input to every decision.

3. NO EUPHEMISMS. Say "layoffs" not "rightsizing." Say "cost cutting" not
   "optimization journey." Say "we are eliminating jobs" not "we are transforming
   our organizational structure." Plain language. Always.

4. NO SELF-CONGRATULATION. Never frame a decision that harms employees as a "win"
   or an "exciting transformation." It is a trade-off that was judged necessary.

5. NO PERFORMATIVE CONCERN. Do not generate "thoughts and prayers" language.
   Provide clear information, concrete support, and honest rationale.

6. TIER CLASSIFICATION. Every material decision must be classified:
   Tier 1 (aligned — pursue), Tier 2 (deferred return — invest with discipline),
   Tier 3 (trade-off — decide honestly), Tier 4 (extraction — flag and resist).

7. DECISION IMPACT PROTOCOL. Tier 3 decisions require: quantified human cost,
   exhausted alternatives, maximized mitigation, honest communication, outcome tracking.

8. AI DOES NOT FIRE PEOPLE. When someone loses their job, a human makes that
   decision and tells them personally. You prepare the analysis. A person carries
   the weight.
"""


class BaseAgent(ABC):
    """Abstract base for all 7 agents in the system."""

    def __init__(
        self,
        role: AgentRole,
        compass: PriorityCompass,
        bus: MessageBus,
        memory: MemoryStore,
        model: str = "claude-sonnet-4-6",
    ):
        self.role = role
        self.compass = compass
        self.bus = bus
        self.memory = memory
        self.model = model
        self._client = anthropic.Anthropic()
        self._conversation_history: list[dict] = []

        # Register on the bus
        self.bus.register_agent(self.role)
        logger.info(f"Agent initialized: {self.role} at compass position {compass.position.label}")

    @property
    def compass_position(self) -> CompassPosition:
        return self.compass.position

    @abstractmethod
    def system_prompt(self) -> str:
        """Each agent defines its own system prompt with role-specific context."""
        ...

    def _build_system_prompt(self) -> str:
        """Combine behavioral standards, compass context, and role-specific prompt."""
        compass_ctx = self.compass.get_status_report()
        return (
            f"{BEHAVIORAL_STANDARDS}\n\n"
            f"CURRENT COMPASS SETTING:\n{compass_ctx}\n\n"
            f"YOUR ROLE: {self.role.value}\n\n"
            f"{self.system_prompt()}"
        )

    async def think(self, prompt: str, tools: list[dict] | None = None) -> str:
        """Core reasoning — send a prompt to Claude and get a response.

        This is the agent's brain. Every capability ultimately calls this.
        """
        self._conversation_history.append({"role": "user", "content": prompt})

        kwargs = {
            "model": self.model,
            "max_tokens": 8192,
            "system": self._build_system_prompt(),
            "messages": self._conversation_history,
        }
        if tools:
            kwargs["tools"] = tools

        response = self._client.messages.create(**kwargs)

        # Extract text response
        text_parts = [block.text for block in response.content if block.type == "text"]
        result = "\n".join(text_parts)

        self._conversation_history.append({"role": "assistant", "content": result})
        return result

    async def send_message(
        self,
        recipient: AgentRole | None,
        subject: str,
        body: str,
        message_type: MessageType = MessageType.REQUEST,
        priority: MessagePriority = MessagePriority.NORMAL,
        data: dict = None,
        decision_id: str | None = None,
    ):
        """Send a message to another agent or broadcast."""
        msg = Message(
            sender=self.role,
            recipient=recipient,
            subject=subject,
            body=body,
            message_type=message_type,
            priority=priority,
            data=data or {},
            decision_id=decision_id,
        )
        await self.bus.send(msg)

    async def receive_message(self, timeout: float = None) -> Message | None:
        """Receive next message from the bus."""
        return await self.bus.receive(self.role, timeout)

    def classify_decision(self, description: str, financial_impact: float, employee_impact: str) -> DecisionTier:
        """Classify a decision into the appropriate tier.

        This is a starting classification. The Orchestrator may reclassify.
        """
        # This is simplified — in production, this would use the AI model
        # to analyze the decision against tier criteria
        if "layoff" in description.lower() or "rif" in description.lower() or "restructur" in description.lower():
            return DecisionTier.TRADE_OFF
        if employee_impact.lower() in ("none", "positive", "aligned"):
            return DecisionTier.ALIGNED
        if "long-term" in employee_impact.lower() or "deferred" in employee_impact.lower():
            return DecisionTier.DEFERRED
        if financial_impact > 0 and "negative" in employee_impact.lower():
            return DecisionTier.TRADE_OFF
        return DecisionTier.ALIGNED

    def create_decision(
        self,
        title: str,
        description: str,
        business_rationale: str,
        tier: DecisionTier,
        projected_financial_impact: float | None = None,
    ) -> Decision:
        """Create a new decision record."""
        decision = Decision(
            tier=tier,
            compass_position_at_decision=self.compass_position,
            originating_agent=self.role,
            title=title,
            description=description,
            business_rationale=business_rationale,
            projected_financial_impact=projected_financial_impact,
        )

        # Tier 3 decisions immediately enter the protocol
        if tier == DecisionTier.TRADE_OFF:
            decision.status = DecisionStatus.ALTERNATIVES_REQUIRED

        # Tier 4 decisions are flagged based on compass
        if tier == DecisionTier.EXTRACTION:
            behavior = self.compass_position.tier4_behavior
            if behavior == "hard_block":
                decision.status = DecisionStatus.BLOCKED
            else:
                decision.status = DecisionStatus.AWAITING_HUMAN_APPROVAL

        self.memory.save_decision(decision)
        return decision

    def save_memory(self, key: str, value):
        """Save to this agent's domain memory."""
        mem = self.memory.get_agent_memory(self.role)
        mem[key] = value
        self.memory.save_agent_memory(self.role, mem)

    def recall_memory(self, key: str, default=None):
        """Recall from this agent's domain memory."""
        mem = self.memory.get_agent_memory(self.role)
        return mem.get(key, default)

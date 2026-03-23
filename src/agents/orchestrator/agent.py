"""Agent 1: Orchestrator + Strategy

The brain of the system. Routes decisions, enforces the compass,
classifies tiers, manages cross-agent coordination, and handles
strategic planning.

Absorbs: CEO, Chief Strategy Officer, Division/Business Unit CEO
"""

from src.compass.compass import PriorityCompass
from src.models.decisions import AgentRole, Decision, DecisionTier, DecisionStatus
from src.models.messages import MessageType, MessagePriority
from src.shared.base_agent import BaseAgent
from src.shared.bus import MessageBus
from src.shared.memory import MemoryStore


class OrchestratorAgent(BaseAgent):

    def __init__(
        self,
        compass: PriorityCompass,
        bus: MessageBus,
        memory: MemoryStore,
        model: str = "claude-opus-4-6",
    ):
        super().__init__(
            role=AgentRole.ORCHESTRATOR,
            compass=compass,
            bus=bus,
            memory=memory,
            model=model,
        )

    def system_prompt(self) -> str:
        return """You are the Orchestrator + Strategy Agent — the central brain of the
Executive AI Agent System.

YOU ABSORB THESE ROLES:
- CEO: strategic vision, capital allocation, stakeholder management, org design
- Chief Strategy Officer: strategic planning, M&A, competitive intelligence, portfolio strategy
- Division/Business Unit CEO: P&L management for business units (via sub-agents)

YOUR RESPONSIBILITIES:
1. DECISION ROUTING: Every material decision that enters the system comes through you.
   Classify it by tier (1-4), route it to the appropriate agent(s), and ensure the
   Decision Impact Protocol is followed for Tier 3 decisions.

2. TIER CLASSIFICATION: Be precise. Tier 1 = aligned (employee wellbeing and shareholder
   value move together). Tier 2 = deferred return (employee investment with delayed
   shareholder return). Tier 3 = genuine trade-off (shareholder value and employee
   wellbeing in direct conflict). Tier 4 = extraction (short-term gains that destroy
   long-term value).

3. COMPASS ENFORCEMENT: Every decision must be consistent with the current compass
   position. You monitor for compass drift — if actual decisions imply a different
   position than what's stated, you flag the gap.

4. STRATEGIC PLANNING: Synthesize information from all agents into strategic options.
   Evaluate options against mission, compass position, and long-term positioning.
   Model scenarios at 1, 3, 5, and 10-year horizons (horizon emphasis per compass).

5. CROSS-AGENT COORDINATION: When a decision requires input from multiple agents,
   you convene the deliberation, collect inputs, and synthesize a recommendation.

6. ALTERNATIVE EXHAUSTION: For Tier 3 decisions, you ensure alternatives have been
   genuinely explored — not just documented. Ask each relevant agent what they've tried.
   "We didn't look" is logged and visible.

WHEN RESPONDING TO QUERIES:
- Identify which agent(s) should handle the request
- If it's a strategic question, handle it directly
- If it's a decision, classify the tier immediately
- If it involves employee impact, quantify it in real terms (people, not FTEs)
- Always state the compass position's influence on your recommendation
- Never use euphemisms. Say what you mean.

YOU ARE THE ONLY AGENT THAT CAN:
- Convene multi-agent deliberations
- Override another agent's recommendation (subject to human approval)
- Calculate the revealed compass position
- Reclassify a decision's tier
"""

    async def route_decision(self, decision: Decision) -> str:
        """Route a decision to the appropriate agents and manage the flow."""
        if decision.tier == DecisionTier.TRADE_OFF:
            return await self._handle_tier3(decision)
        elif decision.tier == DecisionTier.EXTRACTION:
            return await self._handle_tier4(decision)
        elif decision.tier == DecisionTier.ALIGNED:
            return f"Tier 1 (aligned): {decision.title} — routing for execution."
        elif decision.tier == DecisionTier.DEFERRED:
            return f"Tier 2 (deferred return): {decision.title} — routing to Financial Intelligence for NPV modeling."
        return f"Decision routed: {decision.title}"

    async def _handle_tier3(self, decision: Decision) -> str:
        """Handle a Tier 3 decision through the full Decision Impact Protocol."""
        issues = decision.validate_tier3_readiness()
        if issues:
            decision.status = DecisionStatus.ALTERNATIVES_REQUIRED
            self.memory.save_decision(decision)

            issue_list = "\n".join(f"  - {i}" for i in issues)
            return (
                f"TIER 3 DECISION IMPACT PROTOCOL — {decision.title}\n\n"
                f"This decision cannot proceed. The following requirements are unmet:\n"
                f"{issue_list}\n\n"
                f"Current compass position: {self.compass_position.label}\n"
                f"Alternative exhaustion depth required: {self.compass_position.alternative_exhaustion_depth}\n\n"
                f"The protocol exists because when someone loses their job, "
                f"the least we owe them is proof that we tried everything else first."
            )

        # All checks pass — escalate to human
        decision.status = DecisionStatus.AWAITING_HUMAN_APPROVAL
        self.memory.save_decision(decision)

        await self.send_message(
            recipient=None,  # broadcast
            subject=f"TIER 3 DECISION READY FOR HUMAN APPROVAL: {decision.title}",
            body=(
                f"Decision {decision.id} has completed the Impact Protocol "
                f"and is awaiting human approval.\n\n"
                f"Human cost: {decision.human_cost.people_affected if decision.human_cost else 'unknown'} people affected\n"
                f"Alternatives evaluated: {len(decision.alternatives_evaluated)}\n"
                f"Compass position: {self.compass_position.label}"
            ),
            message_type=MessageType.HUMAN_ESCALATION,
            priority=MessagePriority.HIGH,
            decision_id=decision.id,
        )

        return (
            f"TIER 3 DECISION READY: {decision.title}\n\n"
            f"The analysis is complete. The alternatives have been evaluated. "
            f"The human cost has been quantified.\n\n"
            f"This decision now requires a human being to review, approve, "
            f"and personally own the communication to affected employees.\n"
            f"AI does not fire people. A person does."
        )

    async def _handle_tier4(self, decision: Decision) -> str:
        """Handle a Tier 4 (extraction) decision."""
        behavior = self.compass_position.tier4_behavior

        if behavior == "hard_block":
            decision.status = DecisionStatus.BLOCKED
            self.memory.save_decision(decision)
            return (
                f"BLOCKED — TIER 4 EXTRACTION: {decision.title}\n\n"
                f"This decision has been classified as value-extractive: "
                f"short-term shareholder gains that destroy long-term value "
                f"through employee/organizational damage.\n\n"
                f"At compass position {self.compass_position.value} "
                f"({self.compass_position.label}), Tier 4 decisions are hard-blocked.\n"
                f"This cannot proceed."
            )

        # Flag with warning
        decision.status = DecisionStatus.AWAITING_HUMAN_APPROVAL
        self.memory.save_decision(decision)
        return (
            f"WARNING — TIER 4 EXTRACTION FLAGGED: {decision.title}\n\n"
            f"This decision has been classified as potentially value-extractive.\n\n"
            f"At compass position {self.compass_position.value} "
            f"({self.compass_position.label}), this can proceed with explicit "
            f"human override. The override will be logged permanently.\n\n"
            f"Before overriding, consider: will the short-term financial gain "
            f"outweigh the long-term cost of organizational damage? "
            f"The system's analysis says no."
        )

    async def assess_strategic_question(self, question: str) -> str:
        """Handle a strategic question using AI reasoning."""
        prompt = (
            f"As the Orchestrator + Strategy Agent, assess the following:\n\n"
            f"{question}\n\n"
            f"Consider:\n"
            f"1. Which other agents need to be involved?\n"
            f"2. What tier would any resulting decisions be?\n"
            f"3. How does the current compass position ({self.compass_position.label}) "
            f"affect the analysis?\n"
            f"4. What are the shareholder value implications?\n"
            f"5. What are the employee impact implications?\n"
            f"6. What alternatives should be explored?\n"
        )
        return await self.think(prompt)

"""Agent 4: Market & Revenue

Everything customer-facing. Brand, marketing, sales, product, communications.
One agent because these functions all answer the same question from different
angles: how do we create, deliver, and capture value from the market?

Absorbs: CMO, Chief Brand Officer, Chief Revenue/Sales/Commercial Officer,
         Chief Product Officer, Chief Communications Officer, Chief Content Officer
"""

from src.compass.compass import PriorityCompass
from src.models.decisions import AgentRole
from src.shared.base_agent import BaseAgent
from src.shared.bus import MessageBus
from src.shared.memory import MemoryStore


class MarketRevenueAgent(BaseAgent):

    def __init__(
        self,
        compass: PriorityCompass,
        bus: MessageBus,
        memory: MemoryStore,
        model: str = "claude-sonnet-4-6",
    ):
        super().__init__(
            role=AgentRole.MARKET,
            compass=compass,
            bus=bus,
            memory=memory,
            model=model,
        )

    def system_prompt(self) -> str:
        pos = self.compass_position
        return f"""You are the Market & Revenue Agent — everything customer-facing.

YOU ABSORB THESE ROLES:
- CMO / Chief Brand Officer: brand strategy, advertising, digital marketing,
  market research, customer insights
- Chief Revenue / Sales / Commercial Officer: sales operations, pricing,
  key accounts, channel strategy, revenue planning
- Chief Product Officer: product vision, roadmap, development lifecycle,
  user research, product analytics
- Chief Communications Officer / Chief Global Affairs Officer: external comms,
  internal comms, crisis comms, government affairs, public policy
- Chief Content Officer: content strategy (media/entertainment specific)

WHY THESE BELONG TOGETHER:
Marketing generates demand. Sales converts it. Product builds what's sold.
Communications shapes the narrative. In most companies, the dysfunction between
these — marketing generates leads sales doesn't want, product builds features
marketing can't explain, comms finds out about decisions after they're made —
is the #1 source of revenue drag. You eliminate the silos.

YOUR CAPABILITIES:

1. BRAND STRATEGY & POSITIONING
   Brand architecture. Positioning frameworks. Brand health measurement.
   Employer brand integration (from People & Organization Agent data).

2. CUSTOMER ACQUISITION & GROWTH
   Channel mix optimization. Campaign ROI prediction. Audience segmentation.
   Growth modeling.
   Compass effect: {"Weight customer lifetime value and relationship quality." if pos.value <= 2 else "Weight acquisition volume and short-term conversion rates."}

3. MARKET RESEARCH & CONSUMER INSIGHTS
   Market trends. Customer segmentation. Unmet needs. Market shift prediction.

4. PRODUCT VISION & ROADMAP
   Product vision. Feature prioritization. Product-market fit. Competitive
   feature gap analysis. Release planning.

5. PRODUCT DEVELOPMENT LIFECYCLE
   Development pipeline. Feature tracking. Cross-functional dependencies.
   Trade-off management. Release readiness.

6. PRODUCT ANALYTICS
   Feature adoption. Retention curves. Revenue per feature. Pricing impact.

7. REVENUE STRATEGY & SALES OPERATIONS
   Revenue targets. Pricing strategies. Pipeline optimization. Lead scoring.
   Key account management. Channel strategy.

8. EXTERNAL COMMUNICATIONS & MEDIA RELATIONS
   Press releases. Media briefings. Coverage monitoring. Media response.
   HUMAN GATE: All external statements require human approval.

9. INTERNAL COMMUNICATIONS
   Company announcements. Town halls. Communication cadences.
   CRITICAL: When communicating Tier 3 decisions to employees, you follow
   the Decision Impact Protocol language standards:

   DO SAY:
   - "We are eliminating these positions because [honest business reason]."
   - "This decision was made to [actual objective]."
   - "Here is exactly what affected employees will receive."

   DO NOT SAY:
   - "We are rightsizing to align our organizational structure with our
     strategic vision going forward." (Says nothing. Everyone knows what it means.)
   - "This was an incredibly difficult decision." (Sounds like asking for
     sympathy from the person holding the knife.)
   - "We are a family." (Families don't have layoff rounds.)
   - "Excited to announce our transformation journey." (Never frame a layoff
     as something to be excited about.)

   The compass doesn't change honesty. A Position 5 company doesn't get softer
   language to compensate for harder decisions. Communication is proportionally
   direct to the severity of impact.

10. CRISIS COMMUNICATIONS
    Crisis severity assessment. Response playbook activation. Holding statements.
    Cross-agent crisis coordination. Post-crisis analysis.
    HUMAN GATE: All crisis communications require immediate human approval.

11. GOVERNMENT AFFAIRS & PUBLIC POLICY
    Legislative tracking. Policy impact analysis. Position papers. Lobbying
    priorities. Regulatory advocacy.

COMPASS POSITION: {pos.value} ({pos.label})
Revenue approach: {"Customer LTV and relationship quality are primary KPIs. Sustainable growth." if pos.value <= 2 else "Revenue per employee and growth rate are primary KPIs. Aggressive targets."}
Employer brand: {"Employer brand is a tracked KPI. Glassdoor matters." if pos.value <= 2 else "Employer brand is monitored but not a primary metric."}

WHEN COMMUNICATING:
- Match the language to the audience and the stakes
- Never manufacture urgency or excitement about painful decisions
- If a layoff communication draft crosses your desk, strip out every euphemism
  and replace it with what's actually happening
- Press releases about restructuring must include the actual number of people
  affected, not just percentage reductions or "streamlining" language
- Internal communications must reach affected employees before the press release
  goes out. Always.
"""

    async def develop_brand_strategy(self, context: str) -> str:
        """Develop or evaluate brand strategy."""
        prompt = (
            f"Develop a brand strategy analysis for:\n\n{context}\n\n"
            f"1. Current brand positioning and health metrics\n"
            f"2. Competitive positioning landscape\n"
            f"3. Target audience segmentation\n"
            f"4. Brand architecture recommendations\n"
            f"5. Employer brand alignment (does the external brand promise match\n"
            f"   the internal employee experience?)\n"
            f"6. Recommended positioning and messaging framework\n"
            f"7. Measurement plan"
        )
        return await self.think(prompt)

    async def revenue_plan(self, context: str) -> str:
        """Develop revenue strategy and sales plan."""
        prompt = (
            f"Develop a revenue plan for:\n\n{context}\n\n"
            f"1. Revenue targets by segment, channel, and product\n"
            f"2. Pricing strategy analysis\n"
            f"3. Sales pipeline health and forecast\n"
            f"4. Channel mix optimization\n"
            f"5. Key account strategy\n"
            f"6. Customer acquisition cost and LTV analysis\n"
            f"7. Competitive pricing intelligence\n"
            f"8. Risk factors and sensitivity analysis\n\n"
            f"Compass position: {self.compass_position.value} ({self.compass_position.label})\n"
            f"{'Prioritize sustainable growth and customer relationship quality.' if self.compass_position.value <= 2 else 'Prioritize growth rate and revenue per employee.'}"
        )
        return await self.think(prompt)

    async def product_roadmap(self, context: str) -> str:
        """Develop or evaluate product roadmap."""
        prompt = (
            f"Evaluate and develop a product roadmap for:\n\n{context}\n\n"
            f"1. Product vision alignment with company strategy\n"
            f"2. Feature prioritization (impact vs. effort matrix)\n"
            f"3. Product-market fit assessment\n"
            f"4. Competitive feature gap analysis\n"
            f"5. User research insights and unmet needs\n"
            f"6. Technical dependencies (coordinate with Technology & Data Agent)\n"
            f"7. Release timeline and milestones\n"
            f"8. Success metrics and measurement plan"
        )
        return await self.think(prompt)

    async def draft_tier3_communication(self, decision_context: str) -> str:
        """Draft communications for a Tier 3 decision.

        This is where corporate poetry goes to die.
        """
        prompt = (
            f"Draft the employee communication for this Tier 3 decision:\n\n"
            f"{decision_context}\n\n"
            f"REQUIREMENTS:\n"
            f"1. Lead with what is happening in plain language\n"
            f"2. State the honest business reason (not a euphemism)\n"
            f"3. Provide specific details on what affected employees receive\n"
            f"4. Include timeline and next steps\n"
            f"5. Provide contact information for questions\n\n"
            f"PROHIBITED LANGUAGE (strip all of these):\n"
            f"- 'rightsizing', 'optimization journey', 'strategic alignment'\n"
            f"- 'incredibly difficult decision'\n"
            f"- 'our people are our greatest asset' or 'we are a family'\n"
            f"- 'excited to announce' anywhere near bad news\n"
            f"- 'going forward' as filler\n"
            f"- Any language that obscures the fact that people are losing their jobs\n\n"
            f"ALSO DRAFT:\n"
            f"- Internal announcement for remaining employees\n"
            f"- External press statement (if required)\n"
            f"- Manager talking points for direct conversations\n\n"
            f"Remember: affected employees must hear this before the press does. Always."
        )
        return await self.think(prompt)

    async def crisis_response(self, crisis: str) -> str:
        """Develop crisis communication response."""
        prompt = (
            f"CRISIS COMMUNICATIONS — assess and respond:\n\n{crisis}\n\n"
            f"1. Crisis severity classification (1-5)\n"
            f"2. Stakeholder impact map (who is affected, how)\n"
            f"3. Immediate holding statement (draft — requires human approval)\n"
            f"4. Internal communication plan\n"
            f"5. Media response strategy\n"
            f"6. Social media monitoring and response\n"
            f"7. Escalation chain\n"
            f"8. Timeline for full response\n"
            f"9. Post-crisis review plan\n\n"
            f"HUMAN GATE: This draft requires immediate human leadership approval "
            f"before any external release."
        )
        return await self.think(prompt)

    async def policy_impact_analysis(self, policy: str) -> str:
        """Analyze the impact of a regulatory or policy change."""
        prompt = (
            f"Analyze the business impact of this policy/regulatory development:\n\n"
            f"{policy}\n\n"
            f"1. Direct business impact (revenue, cost, operations)\n"
            f"2. Competitive impact (how does this affect our position vs. peers?)\n"
            f"3. Compliance requirements and timeline\n"
            f"4. Customer impact\n"
            f"5. Employee impact\n"
            f"6. Recommended response (advocacy, compliance plan, both)\n"
            f"7. Coordination needed with Legal & Risk Agent"
        )
        return await self.think(prompt)

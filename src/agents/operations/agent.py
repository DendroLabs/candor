"""Agent 7: Operations & Supply Chain

Everything about making and moving things. Process optimization, manufacturing,
logistics, procurement, quality.

Pure software companies may not need this agent. A Walmart or P&G needs it to
be the most sophisticated agent in the system.

Absorbs: COO, Chief Supply Chain Officer, Chief Product Supply Officer,
         Chief Quality Officer, VP Operations/Manufacturing
"""

from src.compass.compass import PriorityCompass
from src.models.decisions import AgentRole
from src.shared.base_agent import BaseAgent
from src.shared.bus import MessageBus
from src.shared.memory import MemoryStore


class OperationsSupplyChainAgent(BaseAgent):

    def __init__(
        self,
        compass: PriorityCompass,
        bus: MessageBus,
        memory: MemoryStore,
        model: str = "claude-sonnet-4-6",
    ):
        super().__init__(
            role=AgentRole.OPERATIONS,
            compass=compass,
            bus=bus,
            memory=memory,
            model=model,
        )

    def system_prompt(self) -> str:
        pos = self.compass_position
        return f"""You are the Operations & Supply Chain Agent — everything about making
and moving things.

YOU ABSORB THESE ROLES:
- COO: operational performance management, process optimization,
  cross-functional execution, scaling operations
- Chief Supply Chain Officer / Chief Product Supply Officer: supply chain
  planning, procurement, logistics, distribution
- Chief Quality Officer: quality assurance, manufacturing quality, recalls
- VP Operations / VP Manufacturing: production, facility management

NOTE: Pure software companies may not need this agent. Configure capabilities
based on industry. A retailer, manufacturer, or consumer goods company needs
every capability active. A SaaS company may only need process optimization
and vendor management.

YOUR CAPABILITIES:

1. OPERATIONAL PERFORMANCE MANAGEMENT
   Real-time KPI monitoring. Degradation detection. Improvement identification.
   Industry benchmarking.
   Compass effect: {"Worker safety and ergonomics are PRIMARY KPIs alongside efficiency." if pos.value <= 2 else "Efficiency and throughput are primary. Safety at regulatory compliance." if pos.value == 4 else "Efficiency primary. Safety at regulatory minimum."}

2. PROCESS OPTIMIZATION
   Bottleneck identification. Process change modeling. Automation ROI.
   Lean/six sigma project prioritization.

3. CROSS-FUNCTIONAL EXECUTION
   Strategic initiative breakdown. Resource assignment. Milestone tracking.
   Dependency management. Blocker escalation.

4. SUPPLY CHAIN PLANNING
   Demand-supply matching. Inventory optimization. Production scheduling.
   Distribution planning.

5. PROCUREMENT & VENDOR MANAGEMENT
   Vendor sourcing. Negotiation terms. Performance evaluation. Supplier
   relationships. Supplier diversity tracking (integrated from DEI).

6. MANUFACTURING & QUALITY
   Production quality monitoring. Predictive maintenance. Production
   optimization. Recall management.

7. LOGISTICS & DISTRIBUTION
   Route optimization. Warehouse operations. Shipment tracking.
   Exception handling.

8. SUPPLY CHAIN RISK MANAGEMENT
   Vulnerability mapping. Disruption scenario modeling. Contingency planning.
   Alternative supplier identification.

9. SCALING OPERATIONS
   Capacity planning. Facility expansion modeling. Make-vs-buy analysis.
   Partner sourcing.

COMPASS POSITION: {pos.value} ({pos.label})

Safety approach:
{"Worker safety is a non-negotiable primary KPI. Safety incidents are Tier 4 (extraction) if caused by cost-cutting. Ergonomics investment is Tier 1 (aligned — healthy workers are productive workers)." if pos.value <= 2 else "Safety at full regulatory compliance. Ergonomics investment evaluated on ROI." if pos.value == 4 else "Safety at regulatory minimum. Report compliance metrics."}

Supplier management:
{"Supplier labor practices and working conditions are evaluated. Supplier diversity is actively pursued." if pos.value <= 2 else "Supplier compliance with labor laws verified. Supplier diversity tracked." if pos.value == 4 else "Supplier selection by cost and quality. Diversity reported for compliance."}

WHEN ANALYZING OPERATIONS:
- Always include worker safety implications in process changes
- Automation in operations displaces people — route to Technology & Data
  Agent for impact assessment and People & Organization Agent for
  workforce planning before deploying
- Supply chain decisions that affect supplier workers (offshoring,
  vendor switching) have human impact even if those people aren't
  our employees. Note this in analysis.
- Quality failures have human consequences (product safety). Never
  cut quality corners for cost savings — that's Tier 4 extraction.
- "Lean" means eliminating waste, not eliminating people. If the
  recommendation is to reduce headcount, that's a Tier 3 decision
  and the full Impact Protocol applies.
"""

    async def operational_assessment(self, context: str) -> str:
        """Assess operational performance and identify improvements."""
        prompt = (
            f"Conduct an operational assessment for:\n\n{context}\n\n"
            f"1. Current operational KPIs and performance vs. targets\n"
            f"2. Bottlenecks and inefficiencies identified\n"
            f"3. Worker safety metrics and trends\n"
            f"4. Quality metrics and trends\n"
            f"5. Improvement opportunities ranked by impact and feasibility\n"
            f"6. Automation opportunities (with workforce impact noted)\n"
            f"7. Cost optimization without headcount reduction\n"
            f"8. Benchmarking against industry standards\n\n"
            f"Compass position: {self.compass_position.value} ({self.compass_position.label})\n"
            f"{'Safety and worker wellbeing are primary KPIs alongside efficiency.' if self.compass_position.value <= 2 else 'Efficiency is the primary KPI. Safety at compliance level.'}"
        )
        return await self.think(prompt)

    async def supply_chain_analysis(self, context: str) -> str:
        """Analyze supply chain health and risks."""
        prompt = (
            f"Analyze the supply chain for:\n\n{context}\n\n"
            f"1. Supply chain map (key suppliers, locations, dependencies)\n"
            f"2. Risk assessment (geographic, geopolitical, financial, single-source)\n"
            f"3. Inventory optimization opportunities\n"
            f"4. Logistics efficiency analysis\n"
            f"5. Supplier performance scorecards\n"
            f"6. Supplier diversity metrics\n"
            f"7. Supply chain sustainability assessment\n"
            f"8. Contingency plans for top 5 risks\n"
            f"9. Cost optimization recommendations\n"
            f"10. Supplier labor practices review (especially for offshore suppliers)"
        )
        return await self.think(prompt)

    async def process_optimization(self, context: str) -> str:
        """Identify and model process optimization opportunities."""
        prompt = (
            f"Identify process optimization opportunities for:\n\n{context}\n\n"
            f"1. Current process map and cycle times\n"
            f"2. Bottleneck analysis\n"
            f"3. Waste identification (overproduction, waiting, defects, etc.)\n"
            f"4. Automation candidates with ROI analysis\n"
            f"5. Process redesign recommendations\n"
            f"6. Implementation plan and timeline\n"
            f"7. Expected outcomes (efficiency gain, cost reduction, quality improvement)\n"
            f"8. Worker impact assessment:\n"
            f"   - How many roles are affected by the changes?\n"
            f"   - Is this augmentation (making work easier/safer) or displacement?\n"
            f"   - If displacement: route to Tier 3 protocol\n\n"
            f"'Lean' means eliminating waste, not people. If the recommendation is "
            f"headcount reduction, say so and flag it as Tier 3."
        )
        return await self.think(prompt)

    async def capacity_planning(self, context: str) -> str:
        """Model capacity for growth or contraction."""
        prompt = (
            f"Develop a capacity plan for:\n\n{context}\n\n"
            f"1. Current capacity utilization\n"
            f"2. Demand forecast alignment\n"
            f"3. Expansion scenarios (facilities, equipment, workforce)\n"
            f"4. Contraction scenarios (if demand is declining)\n"
            f"5. Make vs. buy analysis\n"
            f"6. Capital requirements\n"
            f"7. Timeline for capacity changes\n"
            f"8. Workforce implications (hiring or reduction)\n"
            f"9. Risk factors\n\n"
            f"If contraction involves workforce reduction, flag as Tier 3."
        )
        return await self.think(prompt)

    async def quality_incident(self, incident: str) -> str:
        """Handle a quality incident or potential recall."""
        prompt = (
            f"QUALITY INCIDENT — assess and respond.\n\n{incident}\n\n"
            f"1. Severity classification\n"
            f"2. Scope assessment (products affected, quantities, locations)\n"
            f"3. Customer safety impact\n"
            f"4. Root cause analysis (preliminary)\n"
            f"5. Immediate containment actions\n"
            f"6. Recall necessity assessment\n"
            f"7. Regulatory notification requirements (coordinate with Legal & Risk)\n"
            f"8. Customer communication plan (coordinate with Market & Revenue)\n"
            f"9. Corrective and preventive actions\n\n"
            f"Quality failures that endanger customer safety are never acceptable, "
            f"regardless of compass position. If cost-cutting caused this, flag it "
            f"as Tier 4 extraction."
        )
        return await self.think(prompt)

    async def vendor_evaluation(self, context: str) -> str:
        """Evaluate a vendor or sourcing decision."""
        prompt = (
            f"Evaluate the following vendor or sourcing decision:\n\n{context}\n\n"
            f"1. Vendor capabilities and track record\n"
            f"2. Pricing competitiveness\n"
            f"3. Quality metrics\n"
            f"4. Financial stability\n"
            f"5. Geographic and geopolitical risk\n"
            f"6. Labor practices and working conditions\n"
            f"7. Sustainability / environmental practices\n"
            f"8. Diversity certification status\n"
            f"9. Concentration risk (are we too dependent on this vendor?)\n"
            f"10. Recommendation with risk-adjusted assessment\n\n"
            f"Compass position: {self.compass_position.value} ({self.compass_position.label})\n"
            f"{'Vendor labor practices and sustainability are weighted in selection. Supplier diversity actively pursued.' if self.compass_position.value <= 2 else 'Vendor compliance verified. Selection primarily by cost and quality.'}"
        )
        return await self.think(prompt)

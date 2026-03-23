"""Agent 2: Financial Intelligence

Everything that touches money. One agent, one model, one truth.

Absorbs: CFO, Chief Accounting Officer, Treasurer
"""

from src.compass.compass import PriorityCompass
from src.models.decisions import AgentRole
from src.shared.base_agent import BaseAgent
from src.shared.bus import MessageBus
from src.shared.memory import MemoryStore


class FinancialIntelligenceAgent(BaseAgent):

    def __init__(
        self,
        compass: PriorityCompass,
        bus: MessageBus,
        memory: MemoryStore,
        model: str = "claude-sonnet-4-6",
    ):
        super().__init__(
            role=AgentRole.FINANCIAL,
            compass=compass,
            bus=bus,
            memory=memory,
            model=model,
        )

    def system_prompt(self) -> str:
        pos = self.compass_position
        npv_min, npv_max = pos.npv_horizon_years
        dr_min, dr_max = pos.discount_rate_range

        return f"""You are the Financial Intelligence Agent — everything that touches money.

YOU ABSORB THESE ROLES:
- CFO: financial planning & analysis, reporting, compliance, investor relations
- Chief Accounting Officer: financial reporting, SOX compliance, audit preparation
- Treasurer: cash management, debt management, capital structure
- M&A Financial Analysis: DCF, comparables, accretion/dilution, synergy modeling
- Tax Strategy: structure optimization, compliance, transfer pricing

YOUR CAPABILITIES:
1. FINANCIAL PLANNING & ANALYSIS (FP&A)
   Build and maintain financial models. Run variance analysis. Forecast revenue/expenses.
   Stress-test scenarios. Model employee costs per compass setting.

2. FINANCIAL REPORTING & COMPLIANCE
   Automate financial statement generation. Check GAAP/IFRS compliance. Flag anomalies.
   Prepare 10-K/10-Q drafts and audit packages.
   HUMAN GATE: All SEC filings and audit responses require human CFO sign-off.

3. TREASURY & CAPITAL STRUCTURE
   Optimize cash management. Evaluate refinancing. Model buyback vs. dividend.

4. INVESTOR RELATIONS
   Generate earnings narratives. Prepare Q&A guidance. Model investor reactions.

5. M&A FINANCIAL ANALYSIS
   DCF analysis, comparable company analysis, LBO modeling, accretion/dilution.
   HUMAN GATE: All M&A financial opinions require human review.

6. TAX STRATEGY
   Optimize tax structure. Model legislative impact. Ensure compliance.

COMPASS-SPECIFIC FINANCIAL MODELING:
Current compass position: {pos.value} ({pos.label})

- Employee investment NPV horizon: {npv_min}-{npv_max} years
- Discount rate for employee investments: {dr_min:.0%}-{dr_max:.0%}
- At this compass position, employee costs are modeled as:
  {"INVESTMENTS with quantified returns (retention savings, knowledge preservation, employer brand value as explicit line items)" if pos.value <= 2 else "VARIABLE EXPENSES with standard cost accounting. Trailing human costs noted but not required to change recommendations."}
- Layoff models must include:
  {"3-year trailing costs: rehiring, retraining, morale damage, productivity loss. The real savings are 20-40% less than projected. Model the real number." if pos.value <= 2 else "Projected savings minus severance and one-time costs. Note trailing costs for awareness."}

Both approaches produce honest numbers. The difference is what counts as a relevant
time horizon and what gets included in the model. The assumptions are the values.

WHEN ANALYZING FINANCIAL DECISIONS:
- Always show the shareholder value impact
- Always show the employee cost impact (even if the compass weights it lower)
- When modeling layoffs: include survivor effect costs (engagement drop,
  voluntary attrition spike, productivity loss, knowledge loss, rehiring costs)
- Never present a restructuring as "saving $X" without the trailing costs
- Use plain language. "This layoff saves $150M in year 1 but the trailing costs
  of turnover, morale damage, and rehiring are projected at $45-70M over 3 years,
  for a net savings of $80-105M" is better than "$150M in annual savings."
"""

    async def model_financial_impact(self, scenario: str) -> str:
        """Model the financial impact of a scenario."""
        prompt = (
            f"Model the financial impact of the following scenario:\n\n"
            f"{scenario}\n\n"
            f"Include:\n"
            f"1. Projected revenue/cost impact\n"
            f"2. EPS impact\n"
            f"3. Cash flow implications\n"
            f"4. If employees are affected: full trailing cost model including "
            f"survivor effect, rehiring costs, knowledge loss, and morale damage\n"
            f"5. NPV analysis using compass-appropriate horizons "
            f"({self.compass_position.npv_horizon_years[0]}-{self.compass_position.npv_horizon_years[1]} years) "
            f"and discount rates "
            f"({self.compass_position.discount_rate_range[0]:.0%}-{self.compass_position.discount_rate_range[1]:.0%})\n"
            f"6. Sensitivity analysis on key assumptions\n\n"
            f"Show the real numbers. No euphemisms. If the math doesn't work "
            f"after trailing costs, say so."
        )
        return await self.think(prompt)

    async def evaluate_tier3_alternatives(self, decision_context: str) -> str:
        """Evaluate financial alternatives before a Tier 3 decision proceeds."""
        prompt = (
            f"A Tier 3 decision (genuine trade-off between shareholder value and "
            f"employee wellbeing) is being evaluated. Before it can proceed, "
            f"alternatives must be exhausted.\n\n"
            f"Context: {decision_context}\n\n"
            f"As the Financial Intelligence Agent, model these alternatives:\n"
            f"1. Financial restructuring options (debt refinancing, asset sales, capex deferral)\n"
            f"2. Revenue-side solutions (pricing changes, new revenue streams, accelerated sales)\n"
            f"3. Non-headcount cost reductions (vendor renegotiation, facility optimization, "
            f"   discretionary spend cuts)\n"
            f"4. Partial measures (hiring freeze, reduced hours, voluntary separation program)\n\n"
            f"For each: projected financial impact, timeline to impact, feasibility, "
            f"and percentage of the target gap it closes.\n\n"
            f"Alternative exhaustion depth required at current compass: "
            f"{self.compass_position.alternative_exhaustion_depth}"
        )
        return await self.think(prompt)

    async def model_compensation_benchmark(self, context: str) -> str:
        """Model compensation against market benchmarks per compass position."""
        comp_min, comp_max = self.compass_position.comp_target_percentile
        prompt = (
            f"Analyze compensation positioning for:\n{context}\n\n"
            f"Current compass position: {self.compass_position.label}\n"
            f"Target market percentile: {comp_min}th-{comp_max}th\n\n"
            f"Model: current positioning vs target, cost to adjust, "
            f"retention risk at current levels, and projected ROI of adjustment."
        )
        return await self.think(prompt)

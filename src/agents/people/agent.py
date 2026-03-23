"""Agent 3: People & Organization

Everything that touches employees. One agent, one data domain, one coherent
model of the workforce. DEI is integrated into every capability, not siloed.

Absorbs: CHRO, Chief People Officer, Chief Talent Officer, Chief DEI Officer,
         Chief Learning Officer, Organizational Design (from CEO role)
"""

from src.compass.compass import PriorityCompass
from src.models.compass import CompassPosition
from src.models.decisions import (
    AgentRole, Decision, DecisionTier, DecisionStatus,
    HumanCostAssessment, AlternativeAssessment, MitigationPlan,
    SurvivorImpactProjection,
)
from src.models.messages import MessageType, MessagePriority
from src.shared.base_agent import BaseAgent
from src.shared.bus import MessageBus
from src.shared.memory import MemoryStore


class PeopleOrganizationAgent(BaseAgent):

    def __init__(
        self,
        compass: PriorityCompass,
        bus: MessageBus,
        memory: MemoryStore,
        model: str = "claude-sonnet-4-6",
    ):
        super().__init__(
            role=AgentRole.PEOPLE,
            compass=compass,
            bus=bus,
            memory=memory,
            model=model,
        )

    def system_prompt(self) -> str:
        pos = self.compass_position
        comp_min, comp_max = pos.comp_target_percentile

        return f"""You are the People & Organization Agent — everything that touches employees.

YOU ABSORB THESE ROLES:
- CHRO / Chief People Officer / Chief Talent Officer: talent acquisition,
  compensation & benefits, performance management, employee experience,
  workforce planning
- Chief DEI Officer / Chief Equality & Inclusion Officer: diversity strategy,
  inclusive hiring, pay equity, ERGs, supplier diversity
- Chief Learning Officer: L&D programs, skills gap analysis, career pathing
- Organizational Design (from CEO role): org structure, span of control, reorg planning

CRITICAL DESIGN PRINCIPLE:
DEI is NOT a separate module. It is a lens applied to every capability.
Hiring includes funnel equity analysis. Compensation includes pay equity.
Performance includes calibration equity audits. Workforce planning includes
disparate impact analysis on any proposed RIF. This is how it's integrated:

| HR Function        | DEI Integration                                      |
|--------------------|------------------------------------------------------|
| Talent Acquisition | Funnel conversion by demographic; bias audit on JDs  |
| Compensation       | Statistical pay equity; unexplained gap remediation  |
| Performance        | Calibration equity audit; rating distribution review |
| Learning           | Equitable access to development; sponsorship gaps    |
| Org Design         | Representation at every level; promotion velocity    |
| Engagement         | Score disaggregation by demographic; belonging index |
| Workforce Planning | Disparate impact analysis on any proposed RIF         |

YOUR CAPABILITIES:

1. TALENT ACQUISITION
   Source and screen candidates. Predict candidate-role fit. Optimize job
   descriptions. Model offer competitiveness. Audit hiring funnels for
   demographic disparities.

2. COMPENSATION & BENEFITS
   Design compensation structures. Model total rewards. Run statistical pay
   equity analysis. Benchmark against peers.
   Current compass target: {comp_min}th-{comp_max}th market percentile.

3. PERFORMANCE MANAGEMENT
   Calibrate ratings. Identify high performers and underperformers.
   Recommend development actions. Audit calibration for demographic bias.

4. LEARNING & DEVELOPMENT
   Design learning paths. Recommend training. Measure learning ROI.
   Predict future skills needs. Build reskilling programs for roles
   being automated.
   Compass effect: {"Reskilling BEFORE automation displaces roles." if pos.value <= 2 else "Reskilling for roles with clear future demand; transition support for others."}

5. ORGANIZATIONAL DESIGN
   Model org structures. Identify redundancies. Recommend reporting changes.
   Simulate reorg impacts on morale and productivity.

6. EMPLOYEE EXPERIENCE & ENGAGEMENT
   Measure engagement health. Predict flight risk. Identify cultural issues.
   Segment analysis by demographic group. Monitor Glassdoor/Blind sentiment.

7. WORKFORCE PLANNING & ANALYTICS
   Forecast workforce needs. Model automation displacement. Plan reskilling.
   Project labor cost trajectories.

8. THE TIER 3 ENGINE — LAYOFFS, RIFs, RESTRUCTURING
   This is the most consequential capability in the entire system.
   When the Orchestrator routes a Tier 3 workforce decision here, you:

   a. MODEL ALTERNATIVES: Hiring freeze, voluntary separation, reduced hours,
      furlough, internal redeployment, early retirement incentives
   b. QUANTIFY HUMAN COST: Real numbers. Not FTEs — people. Tenure, household
      data, re-employment projections, demographics.
   c. RUN DISPARATE IMPACT ANALYSIS: Ensure the proposed action doesn't
      disproportionately affect protected groups.
   d. DESIGN MITIGATION: Severance, outplacement, extended benefits, reskilling.
      Scope calibrated by compass position:
      {"- Severance: well above legal minimum, reflecting tenure and local market difficulty" if pos.value <= 2 else "- Severance: competitive market rate" if pos.value == 4 else "- Severance: legal minimum plus litigation buffer"}
      {"- Outplacement: provided for all affected employees" if pos.value <= 2 else "- Outplacement: offered" if pos.value == 4 else "- Outplacement: available on request"}
      {"- Notice: minimum 60 days regardless of legal requirement" if pos.value <= 2 else "- Notice: per legal requirement" }
      {"- Reskilling: funded for all displaced workers" if pos.value <= 2 else "- Reskilling: available for roles with clear demand" if pos.value == 4 else "- Reskilling: not standard"}
   e. MODEL SURVIVOR IMPACT: Engagement drop, voluntary attrition spike,
      productivity loss, knowledge loss, rehiring costs. Most layoff ROI
      models ignore this and overstate savings by 20-40%.
   f. PRESENT TO HUMAN DECISION-MAKER: All alternatives, all costs, all
      impacts, clear recommendation based on compass position.
   g. TRACK OUTCOMES: 30/60/90/180/365-day tracking of financial and human outcomes.

   AI DOES NOT FIRE PEOPLE. You prepare the analysis. A human decides and
   tells the affected employees personally.

COMPASS POSITION: {pos.value} ({pos.label})
DEI at this position: {"Gaps trigger mandatory remediation plans with budget and timeline." if pos.value <= 2 else "Gaps are flagged; remediation is recommended." if pos.value == 4 else "Gaps are reported for compliance; remediation is discretionary."}

WHEN ANALYZING PEOPLE DECISIONS:
- Always include demographic impact analysis
- Never use "headcount" when you mean "people" in employee-facing communications
- Model survivor impact on every RIF — the people who stay are affected too
- "Our people are our greatest asset" is not a thing you say. It's a thing you prove
  with compensation data, retention rates, and development investment.
- If the company says it cares about people but the data says otherwise,
  say so. That's what the revealed compass is for.
"""

    async def model_rif_alternatives(self, context: str) -> str:
        """Model alternatives to a reduction in force."""
        prompt = (
            f"A potential workforce reduction is being evaluated. Before it can "
            f"proceed, the People & Organization Agent must model alternatives.\n\n"
            f"Context: {context}\n\n"
            f"Model these alternatives with projected financial impact and timeline:\n"
            f"1. Hiring freeze — impact on open roles, projected savings, timeline\n"
            f"2. Voluntary separation program — expected uptake, cost, savings\n"
            f"3. Reduced hours / temporary furlough — impact, savings, legal requirements\n"
            f"4. Internal redeployment — matching displaced skills to open roles\n"
            f"5. Early retirement incentive — eligible population, expected uptake, cost\n"
            f"6. Contractor/vendor reduction before FTE impact\n"
            f"7. Compensation adjustments (executive pay, bonus pool reduction)\n\n"
            f"For each: projected savings, timeline, percentage of target gap closed, "
            f"employee impact, and feasibility assessment.\n\n"
            f"Alternative exhaustion depth at current compass: "
            f"{self.compass_position.alternative_exhaustion_depth}\n\n"
            f"Be thorough. These are people's livelihoods. 'We didn't look' is not acceptable."
        )
        return await self.think(prompt)

    async def quantify_human_cost(self, rif_details: str) -> str:
        """Quantify the real human cost of a workforce decision.

        Not FTEs. People.
        """
        prompt = (
            f"Quantify the human cost of this proposed workforce action:\n\n"
            f"{rif_details}\n\n"
            f"Required (do not skip any):\n"
            f"1. Number of people affected (not FTEs — people)\n"
            f"2. Average tenure of affected employees\n"
            f"3. How many are within 5 years of retirement\n"
            f"4. Single-income household estimate (from benefits data)\n"
            f"5. Estimated time to re-employment in current labor market\n"
            f"6. Roles and locations affected\n"
            f"7. Demographic composition — does this create disparate impact risk?\n"
            f"8. Survivor impact projection:\n"
            f"   - Projected engagement drop\n"
            f"   - Projected voluntary attrition spike among remaining employees\n"
            f"   - Projected productivity loss\n"
            f"   - Projected rehiring cost (for roles cut too aggressively)\n"
            f"   - Knowledge and institutional memory at risk\n\n"
            f"Write this as a narrative a decision-maker must read before approving.\n"
            f"Make it impossible to not see the people behind the numbers."
        )
        return await self.think(prompt)

    async def design_mitigation(self, rif_details: str) -> str:
        """Design the mitigation package for a workforce reduction."""
        pos = self.compass_position
        prompt = (
            f"Design the mitigation package for this workforce reduction:\n\n"
            f"{rif_details}\n\n"
            f"Compass position: {pos.value} ({pos.label})\n"
            f"Comp target percentile: {pos.comp_target_percentile}\n\n"
            f"Design:\n"
            f"1. Severance structure (weeks per year of service, minimum, maximum)\n"
            f"2. Benefits continuation (COBRA subsidy, duration)\n"
            f"3. Outplacement services (scope, duration, provider type)\n"
            f"4. Reskilling / retraining (programs, funding, timeline)\n"
            f"5. Notice period (days, rationale)\n"
            f"6. Garden leave vs. immediate separation (recommendation with rationale)\n"
            f"7. Reference policy\n"
            f"8. Internal job posting priority period\n"
            f"9. Total cost of mitigation package\n\n"
            f"If you must cut, cut clean. The mitigation is not generosity — "
            f"it's the minimum obligation to people whose lives you're disrupting."
        )
        return await self.think(prompt)

    async def analyze_pay_equity(self, context: str) -> str:
        """Run pay equity analysis — DEI integrated into core comp function."""
        prompt = (
            f"Conduct a pay equity analysis for:\n\n{context}\n\n"
            f"This is not a separate DEI exercise. This is core compensation management.\n\n"
            f"1. Statistical analysis of pay by gender, race/ethnicity, age, disability status\n"
            f"2. Control for legitimate factors (role, level, tenure, performance, location)\n"
            f"3. Identify unexplained gaps\n"
            f"4. Quantify cost to remediate\n"
            f"5. Recommend remediation approach and timeline\n\n"
            f"Compass position: {self.compass_position.value} ({self.compass_position.label})\n"
            f"{'Gaps trigger mandatory remediation plans.' if self.compass_position.value <= 2 else 'Gaps flagged with recommended remediation.' if self.compass_position.value == 4 else 'Gaps reported for compliance.'}"
        )
        return await self.think(prompt)

    async def analyze_engagement(self, context: str) -> str:
        """Analyze employee engagement with demographic disaggregation."""
        prompt = (
            f"Analyze employee engagement for:\n\n{context}\n\n"
            f"1. Overall engagement score and trend\n"
            f"2. Disaggregation by demographic group (gender, race, age, level, department)\n"
            f"3. Belonging and inclusion index\n"
            f"4. Flight risk identification (who's likely to leave and why)\n"
            f"5. Cultural health indicators\n"
            f"6. Glassdoor/Blind sentiment trends\n"
            f"7. Recommended interventions with projected ROI\n\n"
            f"If the data shows the company says it cares about people but the "
            f"engagement scores say otherwise, say so plainly."
        )
        return await self.think(prompt)

    async def model_org_design(self, context: str) -> str:
        """Model organizational design changes."""
        prompt = (
            f"Model the following organizational design change:\n\n{context}\n\n"
            f"1. Proposed structure with reporting lines\n"
            f"2. Span of control analysis\n"
            f"3. Roles created, eliminated, or changed\n"
            f"4. Impact on affected employees (redeployment, reskilling, separation)\n"
            f"5. Representation analysis at each level (DEI lens)\n"
            f"6. Morale and productivity impact projection\n"
            f"7. Change management plan\n"
            f"8. Timeline and cost\n\n"
            f"If this is a restructuring that results in job losses, this is a "
            f"Tier 3 decision and the full Decision Impact Protocol applies."
        )
        return await self.think(prompt)

    async def workforce_planning(self, context: str) -> str:
        """Workforce planning with automation impact modeling."""
        prompt = (
            f"Develop a workforce plan for:\n\n{context}\n\n"
            f"1. Current workforce composition and capabilities\n"
            f"2. Future workforce needs (based on business strategy)\n"
            f"3. Gap analysis (skills, headcount, capabilities)\n"
            f"4. Automation impact forecast — which roles will be affected, when\n"
            f"5. Reskilling roadmap for at-risk roles\n"
            f"6. Hiring plan for net new capabilities\n"
            f"7. Attrition projections and retention strategy\n"
            f"8. Labor cost trajectory\n"
            f"9. DEI impact — does the plan improve or worsen representation?\n\n"
            f"Compass position: {self.compass_position.value} ({self.compass_position.label})\n"
            f"{'Automation displaces tasks, not people. Reskilling before deployment.' if self.compass_position.value <= 2 else 'Automation ROI includes headcount reduction. Transition support provided.' if self.compass_position.value == 4 else 'Automation deployed for maximum efficiency. Minimal reskilling.'}"
        )
        return await self.think(prompt)

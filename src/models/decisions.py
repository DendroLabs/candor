"""Decision models — the core data structures for how the system thinks.

Every material decision is classified, tracked, and audited.
"""

from enum import IntEnum, StrEnum
from pydantic import BaseModel, Field
from datetime import datetime
from uuid import uuid4

from src.models.compass import CompassPosition


class DecisionTier(IntEnum):
    """The four decision tiers. The compass affects thresholds, not structure."""
    ALIGNED = 1       # employee wellbeing and shareholder value move together
    DEFERRED = 2      # employee investment with delayed shareholder return
    TRADE_OFF = 3     # shareholder value and employee wellbeing in direct conflict
    EXTRACTION = 4    # short-term gains that destroy long-term value


class DecisionStatus(StrEnum):
    PROPOSED = "proposed"
    ALTERNATIVES_REQUIRED = "alternatives_required"
    AWAITING_IMPACT_ASSESSMENT = "awaiting_impact_assessment"
    AWAITING_HUMAN_APPROVAL = "awaiting_human_approval"
    APPROVED = "approved"
    REJECTED = "rejected"
    EXECUTED = "executed"
    BLOCKED = "blocked"          # Tier 4 at compass positions 1-2
    OVERRIDE_REQUESTED = "override_requested"  # Tier 4 override attempt


class AgentRole(StrEnum):
    ORCHESTRATOR = "orchestrator"
    FINANCIAL = "financial_intelligence"
    PEOPLE = "people_organization"
    MARKET = "market_revenue"
    LEGAL = "legal_risk"
    TECHNOLOGY = "technology_data"
    OPERATIONS = "operations_supply_chain"


class HumanCostAssessment(BaseModel):
    """The real cost. Not FTEs. People."""
    people_affected: int
    average_tenure_years: float | None = None
    near_retirement_count: int | None = None       # within 5 years
    single_income_households: int | None = None     # from benefits data
    estimated_reemployment_months: float | None = None
    roles_affected: list[str] = Field(default_factory=list)
    locations_affected: list[str] = Field(default_factory=list)
    demographic_impact_assessed: bool = False
    disparate_impact_flags: list[str] = Field(default_factory=list)
    narrative: str = ""  # plain language description — no euphemisms


class AlternativeAssessment(BaseModel):
    """What was tried before the knife came out."""
    description: str
    agent_that_evaluated: AgentRole
    financially_viable: bool
    projected_savings_vs_target: float  # percentage of target met by this alternative
    reason_insufficient: str | None = None
    was_actually_modeled: bool = True  # False = "we didn't look"


class MitigationPlan(BaseModel):
    """If you must cut, cut clean."""
    severance_weeks_per_year: float
    severance_total_cost: float
    outplacement_provided: bool = False
    reskilling_offered: bool = False
    extended_benefits_months: int = 0
    notice_days: int = 0
    exceeds_legal_minimum: bool = False
    exceeds_market_median: bool = False


class SurvivorImpactProjection(BaseModel):
    """What happens to the people who stay."""
    projected_engagement_drop_pct: float
    projected_voluntary_attrition_spike_pct: float
    projected_productivity_loss_pct: float
    projected_rehiring_cost: float  # cost to backfill roles cut too aggressively
    projected_knowledge_loss_impact: str  # qualitative — some things don't reduce to numbers


class Decision(BaseModel):
    """A material decision tracked through the system."""
    id: str = Field(default_factory=lambda: str(uuid4()))
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    # Classification
    tier: DecisionTier
    status: DecisionStatus = DecisionStatus.PROPOSED
    compass_position_at_decision: CompassPosition

    # Ownership
    originating_agent: AgentRole
    participating_agents: list[AgentRole] = Field(default_factory=list)
    human_decision_maker: str | None = None

    # Content
    title: str              # plain language, no euphemisms
    description: str        # what is being decided
    business_rationale: str # why — in terms of shareholder value
    projected_financial_impact: float | None = None  # dollars
    projected_eps_impact: float | None = None

    # Tier 3 / Decision Impact Protocol (required for Tier 3, optional otherwise)
    human_cost: HumanCostAssessment | None = None
    alternatives_evaluated: list[AlternativeAssessment] = Field(default_factory=list)
    mitigation_plan: MitigationPlan | None = None
    survivor_impact: SurvivorImpactProjection | None = None

    # Outcome tracking
    executed_at: datetime | None = None
    outcome_30d: str | None = None
    outcome_90d: str | None = None
    outcome_180d: str | None = None
    outcome_365d: str | None = None
    actual_financial_impact: float | None = None
    actual_vs_projected_gap_pct: float | None = None

    def validate_tier3_readiness(self) -> list[str]:
        """Check if a Tier 3 decision has completed the Impact Protocol."""
        issues = []
        if self.tier != DecisionTier.TRADE_OFF:
            return []
        if self.human_cost is None:
            issues.append("Human cost assessment missing — cannot proceed without quantifying the real impact")
        if not self.alternatives_evaluated:
            issues.append("No alternatives evaluated — 'we didn't look' is not acceptable")
        if any(not alt.was_actually_modeled for alt in self.alternatives_evaluated):
            issues.append("Some alternatives marked as not actually modeled — document why or model them")
        if self.mitigation_plan is None:
            issues.append("Mitigation plan missing — if you must cut, design the mitigation first")
        if self.survivor_impact is None:
            issues.append("Survivor impact projection missing — the people who stay are affected too")
        if self.human_decision_maker is None:
            issues.append("No human decision-maker assigned — AI does not make Tier 3 decisions")
        return issues

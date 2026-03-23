"""Simulator data models."""

from dataclasses import dataclass, field
from enum import StrEnum


class DecisionCategory(StrEnum):
    WORKFORCE = "workforce"          # Layoffs, hiring freezes, restructuring
    COMPENSATION = "compensation"    # Pay, benefits, equity
    CONDITIONS = "conditions"        # Working conditions, safety, work-life balance
    COMMUNICATION = "communication"  # How decisions are framed and delivered
    INVESTMENT = "investment"        # Training, reskilling, development, growth


# How much each category matters in the overall score.
# Workforce decisions carry the most weight because that's where
# the profit-vs-people tension is most visible and consequential.
CATEGORY_WEIGHTS: dict[DecisionCategory, float] = {
    DecisionCategory.WORKFORCE: 0.30,
    DecisionCategory.COMPENSATION: 0.25,
    DecisionCategory.CONDITIONS: 0.20,
    DecisionCategory.COMMUNICATION: 0.15,
    DecisionCategory.INVESTMENT: 0.10,
}


@dataclass
class Decision:
    """A single documented corporate decision.

    profit_orientation: 0–100 scale.
        0  = maximally people-oriented
        50 = balanced
        100 = maximally profit-oriented

    All decisions should be based on publicly documented events.
    The `context` field explains the scoring rationale.
    """
    year: int
    category: DecisionCategory
    title: str
    description: str
    profit_orientation: int  # 0–100
    context: str  # why this score — sourcing / rationale

    def __post_init__(self):
        if not 0 <= self.profit_orientation <= 100:
            raise ValueError(f"profit_orientation must be 0–100, got {self.profit_orientation}")


@dataclass
class CompanyProfile:
    """A company and its documented decisions."""
    name: str
    ticker: str
    sector: str
    decisions: list[Decision] = field(default_factory=list)
    period: str = ""  # e.g. "2018–2024"


@dataclass
class CategoryScore:
    """Score for a single decision category."""
    category: DecisionCategory
    profit_orientation: float  # 0–100 average
    decision_count: int
    weight: float


@dataclass
class RevealedScore:
    """The full revealed compass result for a company."""
    company: str
    ticker: str
    overall_profit_orientation: float  # 0–100
    category_scores: list[CategoryScore]
    compass_position: int | None  # 1, 2, 4, 5, or None if dead zone
    compass_label: str
    total_decisions: int
    period: str

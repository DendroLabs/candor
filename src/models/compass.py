"""Priority Compass — the system's moral configuration.

Five positions. No middle. The center is empty on purpose.
Position X does not exist because balance is a thing people claim,
not a thing that exists in decision-making.
"""

from enum import IntEnum
from pydantic import BaseModel, Field
from datetime import datetime


class CompassPosition(IntEnum):
    """The five selectable compass positions.

    Values 1-2 are people-leaning. Values 4-5 are profit-leaning.
    There is no 3. That's the point.
    """
    PEOPLE_PRIMARY = 1    # 67% people / 33% profit
    PEOPLE_LEANING = 2    # 58% people / 42% profit
    # 3 does not exist — the dead zone
    PROFIT_LEANING = 4    # 58% profit / 42% people
    PROFIT_PRIMARY = 5    # 67% profit / 33% people

    @property
    def people_weight(self) -> float:
        return {1: 0.67, 2: 0.58, 4: 0.42, 5: 0.33}[self.value]

    @property
    def profit_weight(self) -> float:
        return {1: 0.33, 2: 0.42, 4: 0.58, 5: 0.67}[self.value]

    @property
    def label(self) -> str:
        return {
            1: "People Primary",
            2: "People Leaning",
            4: "Profit Leaning",
            5: "Profit Primary",
        }[self.value]

    @property
    def npv_horizon_years(self) -> tuple[int, int]:
        """Min/max years for employee-investment NPV modeling."""
        return {1: (5, 10), 2: (3, 5), 4: (1, 3), 5: (1, 2)}[self.value]

    @property
    def discount_rate_range(self) -> tuple[float, float]:
        """Min/max discount rates for employee-investment NPV."""
        return {
            1: (0.06, 0.08),
            2: (0.07, 0.09),
            4: (0.10, 0.12),
            5: (0.11, 0.14),
        }[self.value]

    @property
    def comp_target_percentile(self) -> tuple[int, int]:
        """Min/max compensation market percentile targets."""
        return {1: (65, 80), 2: (55, 70), 4: (45, 55), 5: (35, 50)}[self.value]

    @property
    def alternative_exhaustion_depth(self) -> str:
        """How deeply alternatives must be explored before Tier 3 proceeds."""
        return {
            1: "exhaustive",   # every viable alternative fully modeled
            2: "thorough",     # major alternatives modeled with financials
            4: "standard",     # alternatives evaluated, strong primary case lowers bar
            5: "cursory",      # alternatives documented, not deeply modeled
        }[self.value]

    @property
    def tier4_behavior(self) -> str:
        """How Tier 4 (extraction) decisions are handled."""
        return {
            1: "hard_block",          # cannot proceed, period
            2: "block_with_override", # blocked, but board can override with audit
            4: "flag_with_warning",   # flagged, human can proceed, logged
            5: "flag_with_warning",   # flagged, human can proceed, logged
        }[self.value]


class CompassChange(BaseModel):
    """Immutable record of a compass setting change."""
    previous_position: CompassPosition | None
    new_position: CompassPosition
    changed_at: datetime = Field(default_factory=datetime.utcnow)
    authorized_by: str  # who authorized this change
    reason: str
    board_resolution_ref: str | None = None  # reference to board resolution


class RevealedCompass(BaseModel):
    """The compass position implied by actual decisions over a period."""
    period_start: datetime
    period_end: datetime
    stated_position: CompassPosition
    revealed_position: float  # continuous 1.0-5.0, no rounding to hide the truth
    decision_count: int
    tier3_decisions: int
    gap: float  # difference between stated and revealed
    gap_significant: bool  # True if gap > 0.5 positions

    @property
    def gap_direction(self) -> str:
        if abs(self.gap) < 0.5:
            return "aligned"
        if self.revealed_position > self.stated_position:
            return "more_profit_than_stated"
        return "more_people_than_stated"

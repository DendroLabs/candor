"""Priority Compass — runtime implementation.

The compass is set once and applies globally. It cannot be different
internally vs externally. It cannot be hidden. Changing it is logged
and requires board-level authorization.
"""

import json
from datetime import datetime
from pathlib import Path

from src.models.compass import CompassPosition, CompassChange, RevealedCompass
from src.models.decisions import Decision, DecisionTier


class PriorityCompass:
    """The system's moral configuration.

    This is the setting that changes everything. Before any agent makes
    any decision, the system needs to know one thing: when profits and
    people conflict, which way does this organization lean?
    """

    def __init__(self, config_path: Path):
        self._config_path = config_path
        self._position: CompassPosition | None = None
        self._change_log: list[CompassChange] = []
        self._load()

    def _load(self):
        if self._config_path.exists():
            data = json.loads(self._config_path.read_text())
            pos_value = data.get("position")
            if pos_value is not None:
                self._position = CompassPosition(pos_value)
            self._change_log = [
                CompassChange(**c) for c in data.get("change_log", [])
            ]

    def _save(self):
        data = {
            "position": self._position.value if self._position else None,
            "change_log": [c.model_dump(mode="json") for c in self._change_log],
        }
        self._config_path.parent.mkdir(parents=True, exist_ok=True)
        self._config_path.write_text(json.dumps(data, indent=2, default=str))

    @property
    def position(self) -> CompassPosition:
        if self._position is None:
            raise CompassNotSetError(
                "The Priority Compass has not been set. "
                "This is the first decision the board must make. "
                "No agent can operate until the compass is configured."
            )
        return self._position

    @property
    def is_set(self) -> bool:
        return self._position is not None

    @property
    def is_people_leaning(self) -> bool:
        return self.position.value <= 2

    @property
    def is_profit_leaning(self) -> bool:
        return self.position.value >= 4

    @property
    def change_history(self) -> list[CompassChange]:
        return list(self._change_log)

    def set_position(
        self,
        position: CompassPosition,
        authorized_by: str,
        reason: str,
        board_resolution_ref: str | None = None,
    ) -> CompassChange:
        """Set or change the compass position.

        This is logged permanently. The log cannot be deleted.
        """
        if position.value == 3:
            raise ValueError(
                "Position 3 does not exist. The center is empty on purpose. "
                "Nobody is 50-50. Pick a side."
            )

        change = CompassChange(
            previous_position=self._position,
            new_position=position,
            authorized_by=authorized_by,
            reason=reason,
            board_resolution_ref=board_resolution_ref,
        )

        self._position = position
        self._change_log.append(change)
        self._save()
        return change

    def calculate_revealed_position(
        self, decisions: list[Decision], period_start: datetime, period_end: datetime
    ) -> RevealedCompass:
        """Calculate what compass position the actual decisions imply.

        This is the self-honesty mechanism. It answers:
        'Are we who we say we are?'

        If your stated position is 2 but your revealed position is 4,
        the system flags the gap. You are either lying to yourself or
        lying to your employees.
        """
        relevant = [
            d for d in decisions
            if d.executed_at
            and period_start <= d.executed_at <= period_end
        ]

        if not relevant:
            return RevealedCompass(
                period_start=period_start,
                period_end=period_end,
                stated_position=self.position,
                revealed_position=float(self.position.value),
                decision_count=0,
                tier3_decisions=0,
                gap=0.0,
                gap_significant=False,
            )

        # Score each decision on the people-profit spectrum
        # Higher score = more profit-oriented
        scores = []
        for d in relevant:
            score = self._score_decision(d)
            if score is not None:
                scores.append(score)

        if not scores:
            revealed = float(self.position.value)
        else:
            revealed = sum(scores) / len(scores)

        tier3_count = sum(1 for d in relevant if d.tier == DecisionTier.TRADE_OFF)
        gap = revealed - float(self.position.value)

        return RevealedCompass(
            period_start=period_start,
            period_end=period_end,
            stated_position=self.position,
            revealed_position=round(revealed, 2),
            decision_count=len(relevant),
            tier3_decisions=tier3_count,
            gap=round(gap, 2),
            gap_significant=abs(gap) > 0.5,
        )

    def _score_decision(self, decision: Decision) -> float | None:
        """Score a decision on the 1-5 people-profit spectrum.

        This is necessarily imperfect. But imperfect measurement
        of real behavior beats precise measurement of nothing.
        """
        if decision.tier == DecisionTier.ALIGNED:
            # Tier 1 decisions don't reveal compass — they're good for both
            return None

        if decision.tier == DecisionTier.EXTRACTION:
            # If a Tier 4 was executed, that's a strong profit signal
            return 5.0

        if decision.tier == DecisionTier.DEFERRED:
            # Tier 2 investments that were approved lean people
            if decision.status == "approved" or decision.status == "executed":
                return 2.0
            # Tier 2 investments that were rejected lean profit
            return 4.5

        # Tier 3 — the revealing tier
        if decision.tier == DecisionTier.TRADE_OFF:
            score = 3.0  # base (but remember, 3 doesn't exist on the compass)

            # Mitigation quality shifts the score
            if decision.mitigation_plan:
                mp = decision.mitigation_plan
                if mp.exceeds_market_median:
                    score -= 0.5  # more generous = more people-leaning
                if mp.reskilling_offered:
                    score -= 0.3
                if mp.outplacement_provided:
                    score -= 0.2
                if not mp.exceeds_legal_minimum:
                    score += 0.5  # bare minimum = profit-leaning

            # Alternative exhaustion shifts the score
            if decision.alternatives_evaluated:
                modeled = sum(1 for a in decision.alternatives_evaluated if a.was_actually_modeled)
                if modeled >= 4:
                    score -= 0.3  # thorough search = people-leaning
                elif modeled == 0:
                    score += 0.5  # didn't look = profit-leaning

            return max(1.0, min(5.0, score))

        return None

    def get_status_report(self) -> str:
        """Human-readable compass status."""
        if not self.is_set:
            return "COMPASS NOT SET — No agent can operate until the board configures the Priority Compass."

        pos = self.position
        lines = [
            f"Priority Compass: Position {pos.value} — {pos.label}",
            f"  People weight: {pos.people_weight:.0%}",
            f"  Profit weight: {pos.profit_weight:.0%}",
            f"  NPV horizon: {pos.npv_horizon_years[0]}-{pos.npv_horizon_years[1]} years",
            f"  Discount rate: {pos.discount_rate_range[0]:.0%}-{pos.discount_rate_range[1]:.0%}",
            f"  Comp target: {pos.comp_target_percentile[0]}th-{pos.comp_target_percentile[1]}th percentile",
            f"  Alternative depth: {pos.alternative_exhaustion_depth}",
            f"  Tier 4 behavior: {pos.tier4_behavior}",
            f"  Changes recorded: {len(self._change_log)}",
        ]
        return "\n".join(lines)


class CompassNotSetError(Exception):
    """Raised when agents try to operate without a compass.

    The compass must be set first. It is the first decision.
    Everything else follows from it.
    """
    pass

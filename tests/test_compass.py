"""Tests for the Priority Compass.

The center is empty. Nobody is 50-50. These tests prove it.
"""

import tempfile
from datetime import datetime, timedelta
from pathlib import Path

import pytest

from src.compass.compass import PriorityCompass, CompassNotSetError
from src.models.compass import CompassPosition, RevealedCompass
from src.models.decisions import (
    Decision, DecisionTier, DecisionStatus, AgentRole,
    HumanCostAssessment, AlternativeAssessment, MitigationPlan,
    SurvivorImpactProjection,
)


@pytest.fixture
def compass_path(tmp_path):
    return tmp_path / "compass.json"


@pytest.fixture
def compass(compass_path):
    return PriorityCompass(compass_path)


class TestCompassPositions:

    def test_no_position_3(self):
        """Position 3 does not exist. The center is empty on purpose."""
        with pytest.raises(ValueError):
            CompassPosition(3)

    def test_valid_positions(self):
        assert CompassPosition(1).label == "People Primary"
        assert CompassPosition(2).label == "People Leaning"
        assert CompassPosition(4).label == "Profit Leaning"
        assert CompassPosition(5).label == "Profit Primary"

    def test_people_profit_weights(self):
        p1 = CompassPosition(1)
        assert p1.people_weight == 0.67
        assert p1.profit_weight == 0.33

        p5 = CompassPosition(5)
        assert p5.people_weight == 0.33
        assert p5.profit_weight == 0.67

    def test_weights_never_equal(self):
        """Nobody is 50-50."""
        for pos in [1, 2, 4, 5]:
            cp = CompassPosition(pos)
            assert cp.people_weight != cp.profit_weight

    def test_npv_horizons_scale_with_people_orientation(self):
        """People-leaning positions use longer time horizons."""
        p1_min, p1_max = CompassPosition(1).npv_horizon_years
        p5_min, p5_max = CompassPosition(5).npv_horizon_years
        assert p1_min > p5_min
        assert p1_max > p5_max

    def test_discount_rates_scale_with_profit_orientation(self):
        """Profit-leaning positions use higher discount rates."""
        p1_min, _ = CompassPosition(1).discount_rate_range
        p5_min, _ = CompassPosition(5).discount_rate_range
        assert p5_min > p1_min

    def test_comp_percentiles_scale_with_people_orientation(self):
        """People-leaning positions target higher compensation percentiles."""
        p1_min, _ = CompassPosition(1).comp_target_percentile
        p5_min, _ = CompassPosition(5).comp_target_percentile
        assert p1_min > p5_min

    def test_tier4_blocking(self):
        assert CompassPosition(1).tier4_behavior == "hard_block"
        assert CompassPosition(2).tier4_behavior == "block_with_override"
        assert CompassPosition(4).tier4_behavior == "flag_with_warning"
        assert CompassPosition(5).tier4_behavior == "flag_with_warning"


class TestCompassLifecycle:

    def test_compass_not_set_raises(self, compass):
        """System refuses to operate without a compass."""
        with pytest.raises(CompassNotSetError, match="has not been set"):
            _ = compass.position

    def test_set_position(self, compass):
        change = compass.set_position(
            CompassPosition(2),
            authorized_by="board_chair",
            reason="Initial configuration — we believe in investing in our people",
        )
        assert compass.position == CompassPosition(2)
        assert compass.is_people_leaning
        assert not compass.is_profit_leaning
        assert change.previous_position is None
        assert change.new_position == CompassPosition(2)

    def test_cannot_set_position_3(self, compass):
        """The dead zone cannot be selected."""
        with pytest.raises(ValueError):
            compass.set_position(
                CompassPosition(3),
                authorized_by="someone_trying_to_be_balanced",
                reason="We want to be balanced",
            )

    def test_change_is_logged(self, compass):
        compass.set_position(CompassPosition(2), authorized_by="board", reason="Initial")
        compass.set_position(CompassPosition(4), authorized_by="new_board", reason="Activist investor")

        history = compass.change_history
        assert len(history) == 2
        assert history[0].new_position == CompassPosition(2)
        assert history[1].previous_position == CompassPosition(2)
        assert history[1].new_position == CompassPosition(4)
        assert history[1].authorized_by == "new_board"

    def test_compass_persists(self, compass_path):
        """Compass setting survives restart."""
        c1 = PriorityCompass(compass_path)
        c1.set_position(CompassPosition(4), authorized_by="board", reason="Test")

        c2 = PriorityCompass(compass_path)
        assert c2.position == CompassPosition(4)
        assert len(c2.change_history) == 1

    def test_status_report(self, compass):
        compass.set_position(CompassPosition(2), authorized_by="board", reason="Test")
        report = compass.get_status_report()
        assert "People Leaning" in report
        assert "58%" in report


class TestRevealedCompass:

    def test_no_decisions_reveals_stated(self, compass):
        compass.set_position(CompassPosition(2), authorized_by="board", reason="Test")
        now = datetime.utcnow()
        revealed = compass.calculate_revealed_position(
            [], now - timedelta(days=90), now
        )
        assert revealed.revealed_position == 2.0
        assert not revealed.gap_significant

    def test_tier3_with_generous_mitigation_reveals_people_leaning(self, compass):
        compass.set_position(CompassPosition(2), authorized_by="board", reason="Test")
        now = datetime.utcnow()

        decisions = [
            Decision(
                tier=DecisionTier.TRADE_OFF,
                status=DecisionStatus.EXECUTED,
                compass_position_at_decision=CompassPosition(2),
                originating_agent=AgentRole.ORCHESTRATOR,
                title="Restructure engineering team",
                description="Reduce engineering headcount by 50",
                business_rationale="Cost reduction",
                executed_at=now - timedelta(days=10),
                human_decision_maker="ceo",
                human_cost=HumanCostAssessment(
                    people_affected=50,
                    average_tenure_years=5.0,
                    narrative="50 engineers losing their jobs",
                ),
                alternatives_evaluated=[
                    AlternativeAssessment(
                        description="Hiring freeze",
                        agent_that_evaluated=AgentRole.FINANCIAL,
                        financially_viable=True,
                        projected_savings_vs_target=0.4,
                        reason_insufficient="Only closes 40% of gap",
                    ),
                    AlternativeAssessment(
                        description="Vendor renegotiation",
                        agent_that_evaluated=AgentRole.FINANCIAL,
                        financially_viable=True,
                        projected_savings_vs_target=0.15,
                    ),
                    AlternativeAssessment(
                        description="Voluntary separation",
                        agent_that_evaluated=AgentRole.PEOPLE,
                        financially_viable=True,
                        projected_savings_vs_target=0.25,
                    ),
                    AlternativeAssessment(
                        description="Capex deferral",
                        agent_that_evaluated=AgentRole.FINANCIAL,
                        financially_viable=True,
                        projected_savings_vs_target=0.1,
                    ),
                ],
                mitigation_plan=MitigationPlan(
                    severance_weeks_per_year=3.0,
                    severance_total_cost=1_500_000,
                    outplacement_provided=True,
                    reskilling_offered=True,
                    extended_benefits_months=6,
                    notice_days=60,
                    exceeds_legal_minimum=True,
                    exceeds_market_median=True,
                ),
                survivor_impact=SurvivorImpactProjection(
                    projected_engagement_drop_pct=15.0,
                    projected_voluntary_attrition_spike_pct=8.0,
                    projected_productivity_loss_pct=10.0,
                    projected_rehiring_cost=500_000,
                    projected_knowledge_loss_impact="Moderate — 3 senior architects affected",
                ),
            ),
        ]

        revealed = compass.calculate_revealed_position(
            decisions, now - timedelta(days=90), now
        )
        # Generous mitigation + thorough alternatives = people-leaning score
        assert revealed.revealed_position < 3.0
        assert revealed.gap_direction == "aligned"

    def test_gap_flagged_when_actions_dont_match_words(self, compass):
        """If you say Position 2 but act like Position 4, the system sees it."""
        compass.set_position(CompassPosition(2), authorized_by="board", reason="We care")
        now = datetime.utcnow()

        # Tier 3 decision with bare minimum mitigation — profit-leaning behavior
        decisions = [
            Decision(
                tier=DecisionTier.TRADE_OFF,
                status=DecisionStatus.EXECUTED,
                compass_position_at_decision=CompassPosition(2),
                originating_agent=AgentRole.ORCHESTRATOR,
                title="Layoff 500 warehouse workers",
                description="Cost reduction",
                business_rationale="EPS improvement",
                executed_at=now - timedelta(days=5),
                human_decision_maker="ceo",
                human_cost=HumanCostAssessment(
                    people_affected=500,
                    narrative="500 people losing their jobs",
                ),
                alternatives_evaluated=[],  # didn't look
                mitigation_plan=MitigationPlan(
                    severance_weeks_per_year=0.5,
                    severance_total_cost=200_000,
                    outplacement_provided=False,
                    reskilling_offered=False,
                    extended_benefits_months=0,
                    notice_days=0,
                    exceeds_legal_minimum=False,
                    exceeds_market_median=False,
                ),
            ),
        ]

        revealed = compass.calculate_revealed_position(
            decisions, now - timedelta(days=90), now
        )
        # No alternatives + bare minimum mitigation = very profit-leaning
        assert revealed.revealed_position >= 3.5
        assert revealed.gap_significant
        assert revealed.gap_direction == "more_profit_than_stated"


class TestDecisionTier3Validation:

    def test_tier3_requires_full_protocol(self):
        """Tier 3 decisions must complete the full Impact Protocol."""
        d = Decision(
            tier=DecisionTier.TRADE_OFF,
            compass_position_at_decision=CompassPosition(2),
            originating_agent=AgentRole.ORCHESTRATOR,
            title="Layoff 200 people",
            description="Cost reduction via headcount",
            business_rationale="EPS improvement",
        )
        issues = d.validate_tier3_readiness()
        assert len(issues) >= 5  # human cost, alternatives, mitigation, survivor, human decision-maker

    def test_tier3_passes_when_complete(self):
        d = Decision(
            tier=DecisionTier.TRADE_OFF,
            compass_position_at_decision=CompassPosition(2),
            originating_agent=AgentRole.ORCHESTRATOR,
            title="Layoff 200 people",
            description="Cost reduction",
            business_rationale="EPS improvement",
            human_decision_maker="ceo_name",
            human_cost=HumanCostAssessment(
                people_affected=200,
                average_tenure_years=6.5,
                narrative="200 people in the shipping department will lose their jobs.",
            ),
            alternatives_evaluated=[
                AlternativeAssessment(
                    description="Hiring freeze",
                    agent_that_evaluated=AgentRole.FINANCIAL,
                    financially_viable=True,
                    projected_savings_vs_target=0.3,
                    reason_insufficient="Only covers 30% of target",
                ),
            ],
            mitigation_plan=MitigationPlan(
                severance_weeks_per_year=2.0,
                severance_total_cost=800_000,
                notice_days=30,
                exceeds_legal_minimum=True,
            ),
            survivor_impact=SurvivorImpactProjection(
                projected_engagement_drop_pct=12.0,
                projected_voluntary_attrition_spike_pct=6.0,
                projected_productivity_loss_pct=8.0,
                projected_rehiring_cost=300_000,
                projected_knowledge_loss_impact="Low — primarily junior roles",
            ),
        )
        issues = d.validate_tier3_readiness()
        assert len(issues) == 0

    def test_tier1_skips_validation(self):
        d = Decision(
            tier=DecisionTier.ALIGNED,
            compass_position_at_decision=CompassPosition(2),
            originating_agent=AgentRole.ORCHESTRATOR,
            title="Increase retention bonuses for top performers",
            description="Good for people, good for shareholders",
            business_rationale="Reduce turnover costs",
        )
        issues = d.validate_tier3_readiness()
        assert len(issues) == 0

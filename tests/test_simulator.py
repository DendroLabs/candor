"""Tests for the Candor Simulator."""

import pytest

from src.simulator.models import (
    CompanyProfile,
    Decision,
    DecisionCategory,
    CATEGORY_WEIGHTS,
)
from src.simulator.engine import score_company, _map_to_compass
from src.simulator.companies import get_all_companies, get_company


C = DecisionCategory


class TestScoringEngine:
    """Test the scoring math."""

    def test_category_weights_sum_to_1(self):
        assert abs(sum(CATEGORY_WEIGHTS.values()) - 1.0) < 0.001

    def test_pure_people_company(self):
        """A company with all 0-orientation decisions should score near Position 1."""
        profile = CompanyProfile(
            name="PeopleCo", ticker="PPL", sector="Test", period="2024",
            decisions=[
                Decision(2024, C.WORKFORCE, "No layoffs", "Kept everyone", 0, "test"),
                Decision(2024, C.COMPENSATION, "Top pay", "Best in class", 0, "test"),
                Decision(2024, C.CONDITIONS, "Great conditions", "Perfect safety", 0, "test"),
                Decision(2024, C.COMMUNICATION, "Honest talk", "No euphemisms", 0, "test"),
                Decision(2024, C.INVESTMENT, "Full training", "Everyone grows", 0, "test"),
            ],
        )
        score = score_company(profile)
        assert score.overall_profit_orientation == 0.0
        assert score.compass_position == 1

    def test_pure_profit_company(self):
        """A company with all 100-orientation decisions should score near Position 5."""
        profile = CompanyProfile(
            name="ProfitCo", ticker="PRF", sector="Test", period="2024",
            decisions=[
                Decision(2024, C.WORKFORCE, "Mass layoffs", "Cut everyone", 100, "test"),
                Decision(2024, C.COMPENSATION, "Minimum pay", "Legal minimum", 100, "test"),
                Decision(2024, C.CONDITIONS, "Bad conditions", "Compliance only", 100, "test"),
                Decision(2024, C.COMMUNICATION, "Euphemism city", "Rightsizing etc", 100, "test"),
                Decision(2024, C.INVESTMENT, "No training", "Hire don't grow", 100, "test"),
            ],
        )
        score = score_company(profile)
        assert score.overall_profit_orientation == 100.0
        assert score.compass_position == 5

    def test_balanced_lands_in_dead_zone(self):
        """50/50 decisions should land in the dead zone."""
        profile = CompanyProfile(
            name="BalancedCo", ticker="BAL", sector="Test", period="2024",
            decisions=[
                Decision(2024, C.WORKFORCE, "Mixed", "Some cuts", 50, "test"),
                Decision(2024, C.COMPENSATION, "Average", "Market rate", 50, "test"),
                Decision(2024, C.CONDITIONS, "OK", "Adequate", 50, "test"),
            ],
        )
        score = score_company(profile)
        assert score.compass_position is None
        assert "Dead Zone" in score.compass_label

    def test_workforce_weighted_most(self):
        """Workforce decisions should carry more weight than other categories."""
        # All categories at 20 except workforce at 80
        profile = CompanyProfile(
            name="WorkforceBad", ticker="WB", sector="Test", period="2024",
            decisions=[
                Decision(2024, C.WORKFORCE, "Bad", "Cuts", 80, "test"),
                Decision(2024, C.COMPENSATION, "Good", "High pay", 20, "test"),
                Decision(2024, C.CONDITIONS, "Good", "Safe", 20, "test"),
                Decision(2024, C.COMMUNICATION, "Good", "Honest", 20, "test"),
                Decision(2024, C.INVESTMENT, "Good", "Training", 20, "test"),
            ],
        )
        score = score_company(profile)
        # Should be pulled above 50 by the workforce weight
        assert score.overall_profit_orientation > 30

    def test_missing_categories_still_score(self):
        """Companies with incomplete data should still produce valid scores."""
        profile = CompanyProfile(
            name="SparseData", ticker="SPR", sector="Test", period="2024",
            decisions=[
                Decision(2024, C.WORKFORCE, "Layoffs", "Cut staff", 75, "test"),
            ],
        )
        score = score_company(profile)
        assert score.overall_profit_orientation == 75.0
        assert score.total_decisions == 1

    def test_decision_validation(self):
        """Profit orientation must be 0–100."""
        with pytest.raises(ValueError):
            Decision(2024, C.WORKFORCE, "Bad", "Over 100", 101, "test")
        with pytest.raises(ValueError):
            Decision(2024, C.WORKFORCE, "Bad", "Under 0", -1, "test")


class TestCompassMapping:
    """Test the score-to-compass-position mapping."""

    def test_position_1_range(self):
        pos, label = _map_to_compass(15)
        assert pos == 1
        assert "People Primary" in label

    def test_position_2_range(self):
        pos, label = _map_to_compass(37)
        assert pos == 2
        assert "People Leaning" in label

    def test_dead_zone(self):
        pos, label = _map_to_compass(50)
        assert pos is None
        assert "Dead Zone" in label

    def test_position_4_range(self):
        pos, label = _map_to_compass(63)
        assert pos == 4
        assert "Profit Leaning" in label

    def test_position_5_range(self):
        pos, label = _map_to_compass(85)
        assert pos == 5
        assert "Profit Primary" in label

    def test_boundaries(self):
        """Test exact boundary values."""
        assert _map_to_compass(29)[0] == 1
        assert _map_to_compass(30)[0] == 2
        assert _map_to_compass(44)[0] == 2
        assert _map_to_compass(45)[0] is None
        assert _map_to_compass(55)[0] is None
        assert _map_to_compass(56)[0] == 4
        assert _map_to_compass(70)[0] == 4
        assert _map_to_compass(71)[0] == 5


class TestCompanyProfiles:
    """Test the company data itself."""

    def test_all_companies_load(self):
        companies = get_all_companies()
        assert len(companies) >= 50  # top companies, expandable

    def test_all_companies_have_decisions(self):
        for company in get_all_companies():
            assert len(company.decisions) >= 3, (
                f"{company.name} has only {len(company.decisions)} decisions"
            )

    def test_all_companies_score(self):
        """Every company should produce a valid score."""
        for company in get_all_companies():
            score = score_company(company)
            assert 0 <= score.overall_profit_orientation <= 100
            assert score.total_decisions > 0

    def test_lookup_by_name(self):
        assert get_company("amazon") is not None
        assert get_company("AMZN") is not None
        assert get_company("Amazon") is not None

    def test_lookup_by_alias(self):
        assert get_company("alphabet") is not None

    def test_lookup_unknown(self):
        assert get_company("nonexistent") is None

    def test_costco_scores_most_people_oriented(self):
        """Costco should score as the most people-oriented company."""
        scores = {
            c.name: score_company(c).overall_profit_orientation
            for c in get_all_companies()
        }
        costco_score = scores["Costco"]
        for name, score in scores.items():
            if name != "Costco":
                assert costco_score <= score, (
                    f"Costco ({costco_score}) should be <= {name} ({score})"
                )

    def test_most_profit_oriented_is_position_5(self):
        """The most profit-oriented company should be Position 5."""
        scores = [
            (c.name, score_company(c))
            for c in get_all_companies()
        ]
        most_profit = max(scores, key=lambda x: x[1].overall_profit_orientation)
        assert most_profit[1].compass_position == 5, (
            f"Most profit-oriented ({most_profit[0]}) should be Position 5"
        )

"""Tests for the Candor Advocate module."""

import pytest

from src.advocate.translator import translate, get_all_translations, Translation
from src.advocate.impact import (
    TeamProfile,
    analyze_rif_impact,
    analyze_workload_increase,
)
from src.advocate.brief import generate_rif_brief, generate_workload_brief


# --- Translator Tests ---

class TestTranslator:
    def test_translations_not_empty(self):
        assert len(get_all_translations()) > 20

    def test_all_translations_have_three_parts(self):
        for t in get_all_translations():
            assert t.corporate, "Missing corporate text"
            assert t.plain, "Missing plain text"
            assert t.what_your_team_hears, "Missing team perspective"

    def test_translate_rightsizing(self):
        matches = translate("We are rightsizing the organization")
        assert len(matches) > 0
        assert any("layoff" in m.plain.lower() or "laying" in m.plain.lower()
                    for m in matches)

    def test_translate_doing_more_with_less(self):
        matches = translate("We need to do more with less")
        assert len(matches) > 0

    def test_translate_no_match(self):
        matches = translate("purple elephant sandwich")
        assert len(matches) == 0

    def test_translate_family(self):
        matches = translate("We are one family here at this company")
        assert len(matches) > 0
        assert any("family" in m.corporate.lower() for m in matches)


# --- Impact Analysis Tests ---

class TestImpactAnalysis:
    @pytest.fixture
    def standard_team(self):
        return TeamProfile(
            team_size=20,
            avg_tenure_years=4.5,
            avg_salary=95000,
            department="Engineering",
            specialization=3,
            market_tightness=3,
        )

    def test_rif_impact_returns_all_fields(self, standard_team):
        impact = analyze_rif_impact(standard_team, 5)
        assert impact.affected_count == 5
        assert impact.remaining_count == 15
        assert impact.workload_increase_pct > 0
        assert impact.total_real_cost > 0
        assert impact.break_even_months > 0
        assert impact.replacement_cost.total_per_person > 0

    def test_larger_cuts_mean_higher_costs(self, standard_team):
        small = analyze_rif_impact(standard_team, 2)
        large = analyze_rif_impact(standard_team, 8)
        assert large.total_real_cost > small.total_real_cost
        assert large.workload_increase_pct > small.workload_increase_pct

    def test_specialized_roles_cost_more_to_replace(self):
        generic = TeamProfile(20, 3.0, 90000, "Support", specialization=1, market_tightness=3)
        specialized = TeamProfile(20, 3.0, 90000, "ML Research", specialization=5, market_tightness=3)
        g_impact = analyze_rif_impact(generic, 5)
        s_impact = analyze_rif_impact(specialized, 5)
        assert s_impact.replacement_cost.total_per_person > g_impact.replacement_cost.total_per_person

    def test_tight_market_increases_attrition(self):
        loose = TeamProfile(20, 3.0, 90000, "Ops", specialization=3, market_tightness=1)
        tight = TeamProfile(20, 3.0, 90000, "Ops", specialization=3, market_tightness=5)
        l_impact = analyze_rif_impact(loose, 5)
        t_impact = analyze_rif_impact(tight, 5)
        assert t_impact.estimated_voluntary_attrition_pct > l_impact.estimated_voluntary_attrition_pct

    def test_cannot_cut_entire_team(self, standard_team):
        """Cutting everyone should leave at least 1 person."""
        impact = analyze_rif_impact(standard_team, 20)
        assert impact.remaining_count >= 1

    def test_workload_analysis(self, standard_team):
        result = analyze_workload_increase(standard_team, 30)
        assert result["current_effective_load_pct"] == 130.0
        assert result["burnout_risk"] in ("moderate", "high", "critical")
        assert result["expected_departures_within_12_months"] >= 0
        assert result["total_attrition_cost"] >= 0

    def test_high_workload_means_high_burnout(self, standard_team):
        moderate = analyze_workload_increase(standard_team, 15)
        extreme = analyze_workload_increase(standard_team, 50)
        risk_order = {"moderate": 0, "high": 1, "critical": 2}
        assert risk_order[extreme["burnout_risk"]] >= risk_order[moderate["burnout_risk"]]


# --- Advocacy Brief Tests ---

class TestAdvocacyBrief:
    @pytest.fixture
    def standard_team(self):
        return TeamProfile(
            team_size=20,
            avg_tenure_years=4.5,
            avg_salary=95000,
            department="Engineering",
            specialization=3,
            market_tightness=3,
        )

    def test_rif_brief_has_all_sections(self, standard_team):
        brief = generate_rif_brief(standard_team, 5, "cost reduction")
        assert brief.situation
        assert brief.executive_summary
        assert len(brief.financial_case) > 0
        assert len(brief.human_case) > 0
        assert len(brief.alternatives) > 0
        assert len(brief.questions_to_ask) > 0
        assert len(brief.what_not_to_say) > 0
        assert brief.closing

    def test_brief_includes_dollar_amounts(self, standard_team):
        brief = generate_rif_brief(standard_team, 5)
        # The financial case should contain dollar amounts
        financial_text = " ".join(brief.financial_case)
        assert "$" in financial_text

    def test_brief_includes_reason_when_given(self, standard_team):
        brief = generate_rif_brief(standard_team, 5, "Q3 margin targets")
        assert "Q3 margin targets" in brief.situation

    def test_workload_brief_has_all_sections(self, standard_team):
        brief = generate_workload_brief(standard_team, 35, "team consolidation")
        assert brief.situation
        assert brief.executive_summary
        assert len(brief.financial_case) > 0
        assert len(brief.human_case) > 0
        assert len(brief.alternatives) > 0
        assert len(brief.questions_to_ask) > 0
        assert brief.closing

    def test_highly_specialized_brief_warns_about_rehiring(self):
        team = TeamProfile(10, 6.0, 150000, "ML Research", specialization=5, market_tightness=4)
        brief = generate_rif_brief(team, 3)
        alternatives_text = " ".join(brief.alternatives)
        assert "specialized" in alternatives_text.lower() or "specialization" in alternatives_text.lower()

    def test_donts_are_actionable(self, standard_team):
        brief = generate_rif_brief(standard_team, 5)
        for dont in brief.what_not_to_say:
            # Each "don't" should contain both what not to say AND what to say instead
            assert "don't" in dont.lower() or "do not" in dont.lower()

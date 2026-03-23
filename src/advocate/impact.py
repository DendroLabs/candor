"""Team Impact Analyzer.

When a decision comes down from above, this module helps managers
understand what it actually means for their team — in numbers
that are hard to ignore.
"""

from dataclasses import dataclass


@dataclass
class TeamProfile:
    """Describe your team so the model can estimate impact."""
    team_size: int
    avg_tenure_years: float
    avg_salary: float
    department: str
    # How specialized is the work? 1=generic, 5=highly specialized
    specialization: int = 3
    # How tight is the job market for these roles? 1=loose, 5=very tight
    market_tightness: int = 3


@dataclass
class ReplacementCost:
    """What it actually costs to replace someone — not what HR says."""
    recruiting_cost: float          # agency fees, job boards, recruiter time
    interview_cost: float           # manager/team time spent interviewing
    onboarding_cost: float          # training, setup, reduced productivity
    ramp_time_months: float         # months to full productivity
    productivity_loss_during_ramp: float  # dollar value of reduced output
    total_per_person: float
    knowledge_loss_risk: str        # qualitative: low, medium, high, critical


@dataclass
class TeamImpact:
    """The full impact picture for a manager's team."""
    # What happens to the people who leave
    affected_count: int
    avg_months_to_reemployment: float
    estimated_income_loss_per_person: float

    # What happens to the people who stay
    remaining_count: int
    workload_increase_pct: float
    estimated_voluntary_attrition_pct: float  # people who quit because of this
    additional_losses_from_attrition: int
    morale_impact: str  # qualitative assessment

    # What it costs the company (the part executives listen to)
    replacement_cost: ReplacementCost
    total_replacement_cost: float  # if you had to rehire everyone you lost
    institutional_knowledge_risk: str
    estimated_productivity_drop_pct: float
    recovery_time_months: int

    # The number the manager should bring to the meeting
    total_real_cost: float  # replacement + productivity loss + attrition cost
    break_even_months: int  # how long until savings exceed total real cost


def analyze_rif_impact(team: TeamProfile, positions_cut: int) -> TeamImpact:
    """Model the real impact of cutting N positions from a team.

    This is the analysis the manager needs to bring to the table.
    It speaks the language executives understand: dollars, timelines, risk.
    """
    if positions_cut >= team.team_size:
        positions_cut = team.team_size - 1  # can't cut everyone

    remaining = team.team_size - positions_cut

    # --- Replacement costs ---
    # Industry data: replacement costs range from 50% to 200% of annual salary
    # depending on specialization. We use a model based on role complexity.
    specialization_multiplier = {1: 0.5, 2: 0.75, 3: 1.0, 4: 1.5, 5: 2.0}
    base_replacement_pct = specialization_multiplier.get(team.specialization, 1.0)

    recruiting = team.avg_salary * 0.15 * base_replacement_pct
    interview_cost = team.avg_salary * 0.05  # team time
    onboarding = team.avg_salary * 0.10 * base_replacement_pct

    # Ramp time scales with specialization and tenure
    ramp_months = 3 + (team.specialization * 1.5) + min(team.avg_tenure_years * 0.5, 3)
    ramp_productivity_loss = (team.avg_salary / 12) * ramp_months * 0.4

    total_per_person = recruiting + interview_cost + onboarding + ramp_productivity_loss

    knowledge_risk = _knowledge_risk(team.avg_tenure_years, team.specialization)

    replacement = ReplacementCost(
        recruiting_cost=round(recruiting),
        interview_cost=round(interview_cost),
        onboarding_cost=round(onboarding),
        ramp_time_months=round(ramp_months, 1),
        productivity_loss_during_ramp=round(ramp_productivity_loss),
        total_per_person=round(total_per_person),
        knowledge_loss_risk=knowledge_risk,
    )

    # --- Survivor impact ---
    workload_increase = (positions_cut / remaining) * 100 if remaining > 0 else 100

    # Attrition model: baseline 10%, increases with workload and market tightness
    base_attrition = 0.10
    workload_factor = min(workload_increase / 100 * 0.15, 0.20)  # up to 20% additional
    market_factor = team.market_tightness * 0.03  # tight markets = more options
    voluntary_attrition = base_attrition + workload_factor + market_factor
    additional_losses = round(remaining * voluntary_attrition)

    # Productivity drop: immediate shock + sustained workload effect
    productivity_drop = min(15 + (workload_increase * 0.3), 40)
    recovery_months = int(6 + positions_cut * 1.5)

    # --- Reemployment for affected workers ---
    # Market tightness inversely affects reemployment time
    base_months = 4.0
    market_adjustment = (6 - team.market_tightness) * 0.8  # loose market = longer search
    tenure_adjustment = min(team.avg_tenure_years * 0.2, 2.0)  # longer tenure = harder pivot
    months_to_reemploy = base_months + market_adjustment + tenure_adjustment

    income_loss = team.avg_salary * (months_to_reemploy / 12)

    # --- Total real cost ---
    # What the company actually pays: replacement of attrition + productivity loss
    attrition_replacement = additional_losses * total_per_person
    productivity_cost = (
        team.avg_salary * remaining * (productivity_drop / 100) * (recovery_months / 12)
    )
    salary_savings = positions_cut * team.avg_salary
    total_real_cost = (
        attrition_replacement + productivity_cost
    )
    # Break-even: when do salary savings exceed the real costs?
    monthly_savings = salary_savings / 12
    break_even = int(total_real_cost / monthly_savings) if monthly_savings > 0 else 99

    morale = _morale_assessment(workload_increase, team.avg_tenure_years)

    return TeamImpact(
        affected_count=positions_cut,
        avg_months_to_reemployment=round(months_to_reemploy, 1),
        estimated_income_loss_per_person=round(income_loss),
        remaining_count=remaining,
        workload_increase_pct=round(workload_increase, 1),
        estimated_voluntary_attrition_pct=round(voluntary_attrition * 100, 1),
        additional_losses_from_attrition=additional_losses,
        morale_impact=morale,
        replacement_cost=replacement,
        total_replacement_cost=round(total_per_person * (positions_cut + additional_losses)),
        institutional_knowledge_risk=knowledge_risk,
        estimated_productivity_drop_pct=round(productivity_drop, 1),
        recovery_time_months=recovery_months,
        total_real_cost=round(total_real_cost),
        break_even_months=break_even,
    )


def analyze_workload_increase(team: TeamProfile, additional_work_pct: float) -> dict:
    """Model the impact of increased workload without additional headcount.

    The 'do more with less' analysis.
    """
    # Burnout risk increases with sustained overwork
    burnout_threshold = 120  # % of normal capacity
    current_load = 100 + additional_work_pct

    if current_load <= burnout_threshold:
        burnout_risk = "moderate"
        attrition_bump = 0.05
        quality_impact = "minor — some corners cut, most work maintained"
    elif current_load <= 140:
        burnout_risk = "high"
        attrition_bump = 0.15
        quality_impact = "significant — errors increase, proactive work stops"
    else:
        burnout_risk = "critical"
        attrition_bump = 0.25
        quality_impact = "severe — reactive mode only, quality standards slip"

    voluntary_attrition = 0.10 + attrition_bump + (team.market_tightness * 0.03)
    expected_departures = round(team.team_size * voluntary_attrition)
    replacement_cost_each = team.avg_salary * (0.5 + team.specialization * 0.3)

    return {
        "current_effective_load_pct": round(current_load, 1),
        "burnout_risk": burnout_risk,
        "quality_impact": quality_impact,
        "estimated_voluntary_attrition_pct": round(voluntary_attrition * 100, 1),
        "expected_departures_within_12_months": expected_departures,
        "replacement_cost_per_departure": round(replacement_cost_each),
        "total_attrition_cost": round(expected_departures * replacement_cost_each),
        "recommendation": _workload_recommendation(current_load, team),
    }


def _knowledge_risk(avg_tenure: float, specialization: int) -> str:
    score = avg_tenure * 2 + specialization * 3
    if score >= 20:
        return "critical — years of institutional knowledge at risk"
    elif score >= 14:
        return "high — significant domain expertise would be lost"
    elif score >= 8:
        return "medium — replaceable but with meaningful ramp time"
    return "low — roles can be backfilled without major knowledge loss"


def _morale_assessment(workload_increase_pct: float, avg_tenure: float) -> str:
    if workload_increase_pct > 40:
        return (
            "severe — survivors are doing 1.4x their job with the same pay, "
            "watching colleagues leave. Long-tenured employees feel betrayed. "
            "Expect departures from your best people first — they have the most options"
        )
    elif workload_increase_pct > 25:
        return (
            "significant — the team knows they're absorbing eliminated roles. "
            "Goodwill from tenure and loyalty is being spent. "
            "If a second round of cuts comes, expect a wave of resignations"
        )
    elif workload_increase_pct > 10:
        return (
            "moderate — manageable if temporary and acknowledged honestly. "
            "If leadership frames this as 'an opportunity to grow,' "
            "expect eye-rolling and disengagement"
        )
    return "contained — small enough to absorb if handled with honesty"


def _workload_recommendation(load_pct: float, team: TeamProfile) -> str:
    if load_pct <= 115:
        return "Sustainable short-term. Monitor for chronic overwork within 6 months."
    elif load_pct <= 130:
        return (
            f"Unsustainable beyond 3-6 months. With a market tightness of "
            f"{team.market_tightness}/5, your best people will find alternatives. "
            f"Advocate for backfill or scope reduction now — before you lose "
            f"the people you can't afford to replace."
        )
    else:
        return (
            f"Critical. Your team is operating at {load_pct:.0f}% capacity. "
            f"Quality is already declining. Departures are coming. "
            f"The cost of replacing burned-out employees who quit will exceed "
            f"the savings from not hiring. Bring this number to your skip-level."
        )

"""Advocacy Brief Generator.

The tool managers actually need: talking points for going to bat for
their team, written in the language executives respond to.

Executives don't respond to "my team is stressed." They respond to
"replacing these three people will cost $450K and take 9 months to
reach full productivity." This module generates the second version.
"""

from dataclasses import dataclass

from .impact import TeamProfile, TeamImpact, analyze_rif_impact


@dataclass
class AdvocacyBrief:
    """A ready-to-use document for the manager walking into the meeting."""
    situation: str
    executive_summary: str  # 2-3 sentences, in money language
    financial_case: list[str]  # bullet points, all dollars and timelines
    human_case: list[str]  # bullet points, what happens to real people
    alternatives: list[str]  # what to propose instead
    questions_to_ask: list[str]  # questions that make executives uncomfortable
    what_not_to_say: list[str]  # things that get you dismissed in the room
    closing: str


def generate_rif_brief(
    team: TeamProfile,
    positions_cut: int,
    stated_reason: str = "",
) -> AdvocacyBrief:
    """Generate an advocacy brief for a manager facing team cuts.

    This is the document you bring to the meeting where they're
    deciding how many of your people to let go.
    """
    impact = analyze_rif_impact(team, positions_cut)

    situation = (
        f"Proposed reduction of {positions_cut} positions from a team of "
        f"{team.team_size} in {team.department}. "
        f"Average tenure: {team.avg_tenure_years} years. "
        f"Average salary: ${team.avg_salary:,.0f}."
    )
    if stated_reason:
        situation += f" Stated reason: {stated_reason}."

    annual_savings = positions_cut * team.avg_salary
    executive_summary = (
        f"The proposed cut saves ${annual_savings:,.0f}/year in direct salary costs. "
        f"However, the total real cost — voluntary attrition of survivors, "
        f"productivity loss during recovery, and replacement costs if positions "
        f"need to be backfilled — is estimated at ${impact.total_real_cost:,.0f}. "
        f"Break-even is {impact.break_even_months} months out, assuming no "
        f"additional attrition beyond what's modeled."
    )

    financial_case = [
        f"Direct salary savings: ${annual_savings:,.0f}/year",
        f"Replacement cost per person (if backfilled later): "
        f"${impact.replacement_cost.total_per_person:,.0f}",
        f"Expected voluntary attrition from survivors: "
        f"{impact.additional_losses_from_attrition} people "
        f"({impact.estimated_voluntary_attrition_pct:.0f}% of remaining team)",
        f"Total replacement cost (cuts + attrition): "
        f"${impact.total_replacement_cost:,.0f}",
        f"Productivity drop: {impact.estimated_productivity_drop_pct:.0f}% "
        f"for approximately {impact.recovery_time_months} months",
        f"Workload increase for survivors: {impact.workload_increase_pct:.0f}% — "
        f"this is before any additional attrition",
        f"Break-even point: {impact.break_even_months} months "
        f"(if everything goes according to plan — it rarely does)",
        f"Ramp time for replacements: {impact.replacement_cost.ramp_time_months:.0f} months "
        f"to full productivity",
        f"Institutional knowledge risk: {impact.replacement_cost.knowledge_loss_risk}",
    ]

    human_case = [
        f"{positions_cut} people lose their jobs. Average tenure with the "
        f"company: {team.avg_tenure_years} years",
        f"Estimated time to re-employment: {impact.avg_months_to_reemployment:.0f} months",
        f"Estimated income loss per affected person during job search: "
        f"${impact.estimated_income_loss_per_person:,.0f}",
        f"Morale impact on remaining team: {impact.morale_impact}",
        f"The people most likely to leave voluntarily are your strongest "
        f"performers — they have the most options",
    ]

    alternatives = _generate_alternatives(team, positions_cut, annual_savings)
    questions = _generate_questions(impact, annual_savings)
    donts = _generate_donts()

    closing = (
        f"This brief is not an argument against efficiency. It is an argument "
        f"for counting all the costs, not just the salary line. If the decision "
        f"survives the full math, then it survives. But the full math should "
        f"include the ${impact.total_real_cost:,.0f} in downstream costs that "
        f"don't show up on the headcount reduction slide."
    )

    return AdvocacyBrief(
        situation=situation,
        executive_summary=executive_summary,
        financial_case=financial_case,
        human_case=human_case,
        alternatives=alternatives,
        questions_to_ask=questions,
        what_not_to_say=donts,
        closing=closing,
    )


def generate_workload_brief(
    team: TeamProfile,
    additional_work_pct: float,
    source: str = "",
) -> AdvocacyBrief:
    """Generate a brief for the 'do more with less' situation."""
    from .impact import analyze_workload_increase
    analysis = analyze_workload_increase(team, additional_work_pct)

    situation = (
        f"Team of {team.team_size} in {team.department} absorbing "
        f"{additional_work_pct:.0f}% additional workload."
    )
    if source:
        situation += f" Source: {source}."

    attrition_cost = analysis["total_attrition_cost"]
    departures = analysis["expected_departures_within_12_months"]

    executive_summary = (
        f"Current effective load is {analysis['current_effective_load_pct']:.0f}% of capacity. "
        f"Burnout risk is {analysis['burnout_risk']}. At this pace, expect "
        f"{departures} voluntary departures within 12 months, costing "
        f"${attrition_cost:,.0f} in replacement costs alone."
    )

    financial_case = [
        f"Current effective workload: {analysis['current_effective_load_pct']:.0f}%",
        f"Expected voluntary departures in 12 months: {departures}",
        f"Replacement cost per departure: ${analysis['replacement_cost_per_departure']:,.0f}",
        f"Total projected attrition cost: ${attrition_cost:,.0f}",
        f"Quality impact: {analysis['quality_impact']}",
        f"Hiring {max(1, departures)} people now costs less than replacing "
        f"{departures} burned-out employees who quit in 6 months",
    ]

    human_case = [
        f"Burnout risk: {analysis['burnout_risk']}",
        f"Your team knows they're doing more work for the same pay",
        f"The first people to leave will be the ones with the most options — "
        f"your best performers",
        f"The people who stay aren't loyal — they're stuck. That's not a "
        f"workforce you want to build on",
    ]

    alternatives = [
        "Hire backfill for the most critical roles — even 1-2 hires reduce "
        "load significantly",
        "Formally deprioritize the lowest-value workstreams — don't just say "
        "'focus,' actually remove things from the plate",
        "Bring in contractors for the surge period — more expensive per hour, "
        "cheaper than replacing full-time employees who burn out",
        "Negotiate a 6-month timeline: if load hasn't decreased by then, "
        "headcount is approved. Get it in writing",
    ]

    questions = [
        "What is the expected duration of this increased workload?",
        "If we lose people to burnout, is backfill approved?",
        f"The attrition cost is ${attrition_cost:,.0f}. The cost of hiring "
        f"now is less. Why are we choosing the more expensive option?",
        "What workstreams are we deprioritizing to make this sustainable?",
        "Who is accountable if quality drops?",
    ]

    donts = _generate_donts()

    closing = analysis["recommendation"]

    return AdvocacyBrief(
        situation=situation,
        executive_summary=executive_summary,
        financial_case=financial_case,
        human_case=human_case,
        alternatives=alternatives,
        questions_to_ask=questions,
        what_not_to_say=donts,
        closing=closing,
    )


def _generate_alternatives(team: TeamProfile, cuts: int, annual_savings: float) -> list[str]:
    alts = [
        f"Hiring freeze: save ${annual_savings * 0.3:,.0f}–${annual_savings * 0.5:,.0f}/year "
        f"through natural attrition without the replacement costs or morale damage",
        "Voluntary separation package: let people self-select. Those who "
        "want to leave get a dignified exit. Those who stay are there by choice",
        f"Reduced hours or temporary pay adjustment: {cuts} positions at 80% time "
        f"saves 20% of salary cost while keeping institutional knowledge intact",
        "Contractor conversion: convert the most fungible roles to contract "
        "positions rather than eliminating them — easier to scale back up",
        "Revenue-side solutions: has the same level of effort been applied to "
        "growing revenue as has been applied to cutting costs?",
    ]

    if team.specialization >= 4:
        alts.append(
            f"These are highly specialized roles (specialization {team.specialization}/5). "
            f"If you cut them now and need them in 18 months, the market won't have them. "
            f"Consider redeployment before elimination"
        )

    return alts


def _generate_questions(impact: TeamImpact, annual_savings: float) -> list[str]:
    return [
        f"The salary savings are ${annual_savings:,.0f}/year. The downstream costs "
        f"are ${impact.total_real_cost:,.0f}. Has the net been calculated?",
        f"Break-even is {impact.break_even_months} months. What happens if we "
        f"need to rehire before then?",
        f"Survivor workload increases {impact.workload_increase_pct:.0f}%. "
        f"What's the plan for when they start leaving?",
        "What alternatives were modeled before reaching this recommendation? "
        "Can I see the analysis?",
        "If we proceed and the projected savings don't materialize after "
        "accounting for attrition and productivity loss, who is accountable?",
        "Has the company done this before? What were the actual realized savings "
        "versus projected? Most companies don't check.",
        f"The people we're cutting have an average tenure of "
        f"{impact.avg_months_to_reemployment:.0f} months to find new work. "
        f"What severance and support are we providing?",
        "Will the executives recommending this cut take a proportional "
        "compensation reduction? If not, why not?",
    ]


def _generate_donts() -> list[str]:
    return [
        "Don't say 'my team is stressed' — say 'attrition risk is 25% and "
        "replacement cost is $X'",
        "Don't say 'this isn't fair' — say 'the net savings are negative "
        "when you include downstream costs'",
        "Don't say 'morale is low' — say 'our top performers have the most "
        "options and the highest flight risk'",
        "Don't appeal to loyalty — appeal to the replacement cost of "
        "institutional knowledge",
        "Don't argue against efficiency — argue that this specific approach "
        "to efficiency is more expensive than the alternatives",
        "Don't get emotional in the room — bring the spreadsheet. The "
        "spreadsheet is your weapon. They built this game. Beat them at it",
    ]

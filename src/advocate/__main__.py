"""Candor Advocate — CLI entry point.

Usage:
    python -m src.advocate translate "We are rightsizing the organization"
    python -m src.advocate translations
    python -m src.advocate impact --team-size 20 --cuts 5 --salary 95000 --tenure 4.5
    python -m src.advocate brief --team-size 20 --cuts 5 --salary 95000 --tenure 4.5
    python -m src.advocate workload --team-size 12 --increase 35 --salary 85000
"""

import argparse
import sys
import textwrap

from .translator import translate, get_all_translations
from .impact import TeamProfile, analyze_rif_impact, analyze_workload_increase
from .brief import generate_rif_brief, generate_workload_brief


def main():
    parser = argparse.ArgumentParser(
        prog="candor-advocate",
        description="Tools for managers who advocate for their people.",
    )
    sub = parser.add_subparsers(dest="command")

    # --- translate ---
    p_translate = sub.add_parser("translate", help="Translate corporate speak")
    p_translate.add_argument("text", help="The corporate statement to translate")

    # --- translations ---
    sub.add_parser("translations", help="Show the full translation dictionary")

    # --- impact ---
    p_impact = sub.add_parser("impact", help="Analyze team impact of cuts")
    _add_team_args(p_impact)
    p_impact.add_argument("--cuts", type=int, required=True, help="Positions being cut")

    # --- brief ---
    p_brief = sub.add_parser("brief", help="Generate an advocacy brief for a RIF")
    _add_team_args(p_brief)
    p_brief.add_argument("--cuts", type=int, required=True, help="Positions being cut")
    p_brief.add_argument("--reason", default="", help="Stated reason for the cuts")

    # --- workload ---
    p_workload = sub.add_parser("workload", help="Analyze 'do more with less'")
    _add_team_args(p_workload)
    p_workload.add_argument("--increase", type=float, required=True,
                            help="Additional workload percentage")
    p_workload.add_argument("--source", default="", help="Source of additional work")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return

    if args.command == "translate":
        _do_translate(args.text)
    elif args.command == "translations":
        _do_translations()
    elif args.command == "impact":
        team = _build_team(args)
        _do_impact(team, args.cuts)
    elif args.command == "brief":
        team = _build_team(args)
        _do_brief(team, args.cuts, args.reason)
    elif args.command == "workload":
        team = _build_team(args)
        _do_workload(team, args.increase, args.source)


def _add_team_args(parser):
    parser.add_argument("--team-size", type=int, required=True)
    parser.add_argument("--salary", type=float, required=True, help="Average salary")
    parser.add_argument("--tenure", type=float, default=3.0, help="Average tenure in years")
    parser.add_argument("--dept", default="Engineering", help="Department name")
    parser.add_argument("--specialization", type=int, default=3,
                        help="Role specialization 1-5 (1=generic, 5=highly specialized)")
    parser.add_argument("--market", type=int, default=3,
                        help="Job market tightness 1-5 (1=loose, 5=very tight)")


def _build_team(args) -> TeamProfile:
    return TeamProfile(
        team_size=args.team_size,
        avg_tenure_years=args.tenure,
        avg_salary=args.salary,
        department=args.dept,
        specialization=args.specialization,
        market_tightness=args.market,
    )


def _do_translate(text: str):
    matches = translate(text)
    if not matches:
        print("\nNo direct matches found. Try using key phrases from the statement.")
        print("Run 'python -m src.advocate translations' to see the full dictionary.\n")
        return

    print(f"\n{'=' * 70}")
    print(f"  Input: \"{text}\"")
    print(f"{'=' * 70}")
    for m in matches[:5]:  # top 5 matches
        print(f"\n  THEY SAID:       {m.corporate}")
        print(f"  THEY MEANT:      {m.plain}")
        print(f"  YOUR TEAM HEARD: {m.what_your_team_hears}")
    print(f"\n{'=' * 70}\n")


def _do_translations():
    translations = get_all_translations()
    print(f"\n{'=' * 70}")
    print("  CANDOR ADVOCATE — Corporate Translation Dictionary")
    print(f"{'=' * 70}")
    print(f"\n  {len(translations)} translations. What they say, what they mean,")
    print("  and what your team actually hears.\n")

    for i, t in enumerate(translations, 1):
        print(f"  {i:2d}. THEY SAY:  \"{t.corporate}\"")
        print(f"      MEANING:  {t.plain}")
        print(f"      HEARD AS: {t.what_your_team_hears}")
        print()
    print(f"{'=' * 70}\n")


def _do_impact(team: TeamProfile, cuts: int):
    impact = analyze_rif_impact(team, cuts)
    w = 70

    print(f"\n{'=' * w}")
    print("  CANDOR ADVOCATE — Team Impact Analysis")
    print(f"{'=' * w}")
    print(f"\n  Team: {team.team_size} people in {team.department}")
    print(f"  Proposed cuts: {cuts}")
    print(f"  Avg salary: ${team.avg_salary:,.0f}  |  Avg tenure: {team.avg_tenure_years} years")
    print(f"\n  {'─' * (w-4)}")
    print(f"  WHAT HAPPENS TO THE PEOPLE WHO LEAVE")
    print(f"  {'─' * (w-4)}")
    print(f"  Affected: {impact.affected_count} people")
    print(f"  Estimated time to new job: {impact.avg_months_to_reemployment:.0f} months")
    print(f"  Income loss during search: ${impact.estimated_income_loss_per_person:,.0f} per person")
    print(f"\n  {'─' * (w-4)}")
    print(f"  WHAT HAPPENS TO THE PEOPLE WHO STAY")
    print(f"  {'─' * (w-4)}")
    print(f"  Remaining: {impact.remaining_count} people")
    print(f"  Workload increase: {impact.workload_increase_pct:.0f}%")
    print(f"  Expected voluntary departures: {impact.additional_losses_from_attrition} "
          f"({impact.estimated_voluntary_attrition_pct:.0f}% attrition rate)")
    print(f"  Morale: {impact.morale_impact}")
    print(f"\n  {'─' * (w-4)}")
    print(f"  WHAT IT ACTUALLY COSTS (the part they didn't model)")
    print(f"  {'─' * (w-4)}")
    savings = cuts * team.avg_salary
    print(f"  Salary savings: ${savings:,.0f}/year")
    print(f"  Replacement cost per person: ${impact.replacement_cost.total_per_person:,.0f}")
    print(f"  Total downstream cost: ${impact.total_real_cost:,.0f}")
    print(f"  Productivity drop: {impact.estimated_productivity_drop_pct:.0f}% "
          f"for {impact.recovery_time_months} months")
    print(f"  Break-even: {impact.break_even_months} months")
    print(f"  Knowledge risk: {impact.institutional_knowledge_risk}")
    print(f"\n{'=' * w}\n")


def _do_brief(team: TeamProfile, cuts: int, reason: str):
    brief = generate_rif_brief(team, cuts, reason)
    w = 70

    print(f"\n{'=' * w}")
    print("  CANDOR ADVOCATE — Advocacy Brief")
    print(f"  Bring this to the meeting.")
    print(f"{'=' * w}")

    print(f"\n  SITUATION")
    print(f"  {_wrap(brief.situation, w)}")

    print(f"\n  EXECUTIVE SUMMARY")
    print(f"  {_wrap(brief.executive_summary, w)}")

    print(f"\n  THE FINANCIAL CASE")
    for point in brief.financial_case:
        print(f"  * {_wrap(point, w)}")

    print(f"\n  THE HUMAN CASE")
    for point in brief.human_case:
        print(f"  * {_wrap(point, w)}")

    print(f"\n  ALTERNATIVES TO PROPOSE")
    for i, alt in enumerate(brief.alternatives, 1):
        print(f"  {i}. {_wrap(alt, w)}")

    print(f"\n  QUESTIONS TO ASK")
    print("  (these are designed to be uncomfortable)")
    for q in brief.questions_to_ask:
        print(f"  ? {_wrap(q, w)}")

    print(f"\n  WHAT NOT TO SAY")
    print("  (and what to say instead)")
    for d in brief.what_not_to_say:
        print(f"  x {_wrap(d, w)}")

    print(f"\n  {'─' * (w-4)}")
    print(f"  {_wrap(brief.closing, w)}")
    print(f"\n{'=' * w}\n")


def _do_workload(team: TeamProfile, increase: float, source: str):
    brief = generate_workload_brief(team, increase, source)
    w = 70

    print(f"\n{'=' * w}")
    print("  CANDOR ADVOCATE — Workload Brief")
    print(f"  For when they say 'do more with less.'")
    print(f"{'=' * w}")

    print(f"\n  SITUATION")
    print(f"  {_wrap(brief.situation, w)}")

    print(f"\n  EXECUTIVE SUMMARY")
    print(f"  {_wrap(brief.executive_summary, w)}")

    print(f"\n  THE FINANCIAL CASE")
    for point in brief.financial_case:
        print(f"  * {_wrap(point, w)}")

    print(f"\n  THE HUMAN CASE")
    for point in brief.human_case:
        print(f"  * {_wrap(point, w)}")

    print(f"\n  ALTERNATIVES TO PROPOSE")
    for i, alt in enumerate(brief.alternatives, 1):
        print(f"  {i}. {_wrap(alt, w)}")

    print(f"\n  QUESTIONS TO ASK")
    for q in brief.questions_to_ask:
        print(f"  ? {_wrap(q, w)}")

    print(f"\n  WHAT NOT TO SAY")
    for d in brief.what_not_to_say:
        print(f"  x {_wrap(d, w)}")

    print(f"\n  {'─' * (w-4)}")
    print(f"  {_wrap(brief.closing, w)}")
    print(f"\n{'=' * w}\n")


def _wrap(text: str, width: int) -> str:
    """Wrap text for display."""
    lines = textwrap.wrap(text, width=width - 4)
    return ("\n    ").join(lines)


if __name__ == "__main__":
    main()

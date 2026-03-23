"""Candor Simulator — CLI entry point.

Usage:
    python -m src.simulator                  # Compare all companies
    python -m src.simulator amazon           # Deep dive on Amazon
    python -m src.simulator amazon costco    # Compare specific companies
    python -m src.simulator --list           # List available companies
"""

import argparse
import sys

from .companies import get_all_companies, get_company
from .engine import score_company
from .display import render_single, render_comparison


def main():
    parser = argparse.ArgumentParser(
        prog="candor-simulator",
        description="Reveal where real companies land on the Priority Compass.",
    )
    parser.add_argument(
        "companies",
        nargs="*",
        help="Company name(s) or ticker(s) to analyze. Omit for all.",
    )
    parser.add_argument(
        "--list",
        action="store_true",
        help="List available companies.",
    )
    parser.add_argument(
        "--detail",
        action="store_true",
        help="Show detailed decision breakdown (default for single company).",
    )

    args = parser.parse_args()

    if args.list:
        print("\nAvailable companies:")
        for c in get_all_companies():
            print(f"  {c.ticker:<6}  {c.name:<20}  {c.sector}")
        print()
        return

    if not args.companies:
        # Show all companies in comparison view
        all_companies = get_all_companies()
        scores = [score_company(c) for c in all_companies]
        print(render_comparison(scores))
        return

    if len(args.companies) == 1 or args.detail:
        # Single company or detail mode: show full breakdown
        for name in args.companies:
            profile = get_company(name)
            if not profile:
                print(f"Unknown company: '{name}'. Use --list to see available companies.", file=sys.stderr)
                sys.exit(1)
            score = score_company(profile)
            print(render_single(score, decisions=profile.decisions))
            if len(args.companies) > 1:
                print()
    else:
        # Multiple companies: comparison view
        profiles = []
        for name in args.companies:
            profile = get_company(name)
            if not profile:
                print(f"Unknown company: '{name}'. Use --list to see available companies.", file=sys.stderr)
                sys.exit(1)
            profiles.append(profile)
        scores = [score_company(p) for p in profiles]
        print(render_comparison(scores))


if __name__ == "__main__":
    main()

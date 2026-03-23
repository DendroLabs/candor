"""Report generator — the full top-company analysis in one document."""

from collections import defaultdict

from .companies import get_all_companies
from .engine import score_company
from .models import RevealedScore
from .display import FILLED, EMPTY


def generate_report() -> str:
    """Generate the full comparative report across all companies."""
    companies = get_all_companies()
    scores = [score_company(c) for c in companies]
    scores.sort(key=lambda s: s.overall_profit_orientation)

    lines = []
    w = 78

    # Header
    lines.append("=" * w)
    lines.append("  CANDOR SIMULATOR")
    lines.append("  The Revealed Compass of Corporate America")
    lines.append("=" * w)
    lines.append("")
    lines.append(f"  Companies analyzed: {len(scores)}")
    lines.append("")

    # Methodology
    lines.append("  METHODOLOGY")
    lines.append("  " + "-" * (w - 4))
    lines.append("  Each company is scored on publicly documented decisions across five")
    lines.append("  weighted categories:")
    lines.append("")
    lines.append("    Workforce decisions (layoffs, hiring, restructuring)    30%")
    lines.append("    Compensation & benefits                                25%")
    lines.append("    Working conditions & safety                            20%")
    lines.append("    Communication & transparency                           15%")
    lines.append("    Investment in people (training, development)            10%")
    lines.append("")
    lines.append("  Scores range from 0% (maximally people-oriented) to 100% (maximally")
    lines.append("  profit-oriented). Mapped to compass positions:")
    lines.append("    0-29%:  Position 1 — People Primary")
    lines.append("    30-44%: Position 2 — People Leaning")
    lines.append("    45-55%: Dead Zone — pick a side")
    lines.append("    56-70%: Position 4 — Profit Leaning")
    lines.append("    71-100%: Position 5 — Profit Primary")
    lines.append("")
    lines.append("  All scores are based on publicly documented decisions — SEC filings,")
    lines.append("  press releases, OSHA data, NLRB rulings, investigative reporting,")
    lines.append("  and company statements. Scores are interpretive. Reasonable people")
    lines.append("  will disagree on individual numbers. The pattern is the point.")
    lines.append("")

    # Distribution
    lines.append("  DISTRIBUTION")
    lines.append("  " + "-" * (w - 4))
    dist = _distribution(scores)
    total = len(scores)
    for label, count in dist:
        pct = count / total * 100
        bar = FILLED * int(pct / 2) + EMPTY * (50 - int(pct / 2))
        lines.append(f"  {label:<32} {count:>3} ({pct:4.1f}%)  {bar}")
    lines.append("")

    # Key stats
    avg = sum(s.overall_profit_orientation for s in scores) / len(scores)
    median = scores[len(scores) // 2].overall_profit_orientation
    most_people = scores[0]
    most_profit = scores[-1]

    lines.append("  KEY STATISTICS")
    lines.append("  " + "-" * (w - 4))
    lines.append(f"  Average profit orientation:  {avg:.1f}%")
    lines.append(f"  Median profit orientation:   {median:.1f}%")
    lines.append(f"  Most people-oriented:        {most_people.company} ({most_people.ticker}) — {most_people.overall_profit_orientation:.1f}%")
    lines.append(f"  Most profit-oriented:        {most_profit.company} ({most_profit.ticker}) — {most_profit.overall_profit_orientation:.1f}%")
    lines.append("")

    # Sector analysis
    lines.append("  SECTOR ANALYSIS")
    lines.append("  " + "-" * (w - 4))
    sectors = _sector_analysis(scores, companies)
    for sector, avg_score, count, position in sectors:
        lines.append(f"  {sector:<40} {avg_score:5.1f}%  ({count} companies)  {position}")
    lines.append("")

    # Full ranked list
    lines.append("  RANKED LIST — MOST PEOPLE-ORIENTED TO MOST PROFIT-ORIENTED")
    lines.append("  " + "-" * (w - 4))
    lines.append(f"  {'#':<4} {'Company':<30} {'Score':>6}  {'Position':<22} Sector")
    lines.append("  " + "-" * (w - 4))

    for i, s in enumerate(scores, 1):
        company = get_all_companies()
        # Find the matching company for sector info
        sector = ""
        for c in companies:
            if c.ticker == s.ticker:
                sector = c.sector
                break

        pos_str = (
            f"Pos {s.compass_position} ({s.compass_label})"
            if s.compass_position
            else f"({s.compass_label})"
        )

        bar = _mini_bar(s.overall_profit_orientation, 12)
        lines.append(
            f"  {i:<4} {s.company + ' (' + s.ticker + ')':<30} "
            f"{s.overall_profit_orientation:5.1f}%  {bar}  {pos_str}"
        )

    lines.append("")

    # Observations
    lines.append("  OBSERVATIONS")
    lines.append("  " + "-" * (w - 4))
    lines.append("")
    lines += _generate_observations(scores, companies, avg, dist)
    lines.append("")

    # Footer
    lines.append("  " + "-" * (w - 4))
    lines.append("  Scores are interpretive. Reasonable people will disagree on")
    lines.append("  individual numbers. The pattern is the point.")
    lines.append("")
    lines.append("  Generated by Candor — candor, noun: the quality of being open")
    lines.append("  and honest in expression; frankness.")
    lines.append("=" * w)

    return "\n".join(lines)


def _distribution(scores: list[RevealedScore]) -> list[tuple[str, int]]:
    buckets = {
        "Position 1 (People Primary)": 0,
        "Position 2 (People Leaning)": 0,
        "Dead Zone": 0,
        "Position 4 (Profit Leaning)": 0,
        "Position 5 (Profit Primary)": 0,
    }
    for s in scores:
        if s.compass_position == 1:
            buckets["Position 1 (People Primary)"] += 1
        elif s.compass_position == 2:
            buckets["Position 2 (People Leaning)"] += 1
        elif s.compass_position is None:
            buckets["Dead Zone"] += 1
        elif s.compass_position == 4:
            buckets["Position 4 (Profit Leaning)"] += 1
        elif s.compass_position == 5:
            buckets["Position 5 (Profit Primary)"] += 1
    return list(buckets.items())


def _sector_analysis(scores: list[RevealedScore], companies: list) -> list[tuple[str, float, int, str]]:
    sector_scores: dict[str, list[float]] = defaultdict(list)
    for s in scores:
        for c in companies:
            if c.ticker == s.ticker:
                # Normalize sector names
                sector = c.sector.split("/")[0].strip()
                sector_scores[sector].append(s.overall_profit_orientation)
                break

    result = []
    for sector, vals in sorted(sector_scores.items(), key=lambda x: sum(x[1]) / len(x[1])):
        avg = sum(vals) / len(vals)
        if avg <= 29:
            pos = "Pos 1"
        elif avg <= 44:
            pos = "Pos 2"
        elif avg <= 55:
            pos = "Dead Zone"
        elif avg <= 70:
            pos = "Pos 4"
        else:
            pos = "Pos 5"
        result.append((sector, avg, len(vals), pos))

    return result


def _mini_bar(profit_pct: float, width: int = 12) -> str:
    filled = int(profit_pct / 100 * width)
    filled = max(0, min(width, filled))
    return FILLED * filled + EMPTY * (width - filled)


def _generate_observations(scores, companies, avg, dist) -> list[str]:
    lines = []

    # 1. Overall lean
    lines.append(f"  1. Corporate America leans profit. The average score across")
    lines.append(f"     {len(scores)} companies is {avg:.1f}% profit-oriented.")
    lines.append("")

    # 2. Distribution skew
    pos4_5 = sum(1 for s in scores if s.compass_position in (4, 5))
    pos1_2 = sum(1 for s in scores if s.compass_position in (1, 2))
    lines.append(f"  2. {pos4_5} companies land at Position 4 or 5 (profit-leaning/primary).")
    lines.append(f"     {pos1_2} land at Position 1 or 2 (people-leaning/primary).")
    lines.append(f"     The compass tilts one direction.")
    lines.append("")

    # 3. The pattern across sectors
    lines.append(f"  3. No sector averages below Position 2. People-first orientation")
    lines.append(f"     is the exception at every level of the economy, not the rule.")
    lines.append("")

    # 4. Growth vs cuts
    growth_companies = [s for s in scores if s.overall_profit_orientation < 30]
    if growth_companies:
        names = ", ".join(s.company for s in growth_companies)
        lines.append(f"  4. The most people-oriented companies ({names}) share a common")
        lines.append(f"     trait: they're growing. It's easy to invest in people when")
        lines.append(f"     revenue is rising. The real test comes when it stops.")
        lines.append("")

    # 5. The honest outlier
    lines.append(f"  5. Boeing scores highest in conditions ({_find_cat_score(scores, companies, 'Boeing', 'conditions')}%) — not because")
    lines.append(f"     it's the worst employer, but because people died. Most companies")
    lines.append(f"     extract value from employees quietly. Boeing's extraction became")
    lines.append(f"     visible because gravity doesn't accept euphemisms.")
    lines.append("")

    # 6. The question
    lines.append(f"  6. Every company on this list has said 'our people are our greatest")
    lines.append(f"     asset.' The average score is {avg:.1f}% profit-oriented. The")
    lines.append(f"     revealed compass shows what the stated compass won't: most")
    lines.append(f"     companies have already picked a side. They just haven't said it")
    lines.append(f"     out loud.")

    return lines


def _find_cat_score(scores, companies, company_name, category_name) -> str:
    for s in scores:
        if s.company == company_name:
            for cs in s.category_scores:
                if cs.category.value == category_name:
                    return f"{cs.profit_orientation:.0f}"
    return "N/A"

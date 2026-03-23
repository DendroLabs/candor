"""Terminal display for simulator results."""

from .models import RevealedScore, DecisionCategory


# Bar characters
FILLED = "\u2588"   # █
EMPTY = "\u2591"    # ░


def render_single(score: RevealedScore, decisions: list | None = None) -> str:
    """Render a full detailed view of one company."""
    lines = []
    w = 70

    lines.append("=" * w)
    lines.append("  CANDOR SIMULATOR — Revealed Compass Analysis")
    lines.append("=" * w)
    lines.append("")
    lines.append(f"  Company:  {score.company} ({score.ticker})")
    lines.append(f"  Period:   {score.period}")
    lines.append(f"  Analyzed: {score.total_decisions} decisions")
    lines.append("")

    # Compass visualization
    lines.append(_compass_line(score.overall_profit_orientation))
    lines.append("")

    # Result box
    people_pct = round(100 - score.overall_profit_orientation, 1)
    profit_pct = score.overall_profit_orientation
    pos_str = (
        f"Position {score.compass_position} ({score.compass_label})"
        if score.compass_position
        else score.compass_label
    )

    lines.append(f"  {profit_pct}% Profit / {people_pct}% People")
    lines.append(f"  Nearest Compass: {pos_str}")
    lines.append("")

    # Category breakdown
    lines.append("  Category Breakdown")
    lines.append("  " + "-" * (w - 4))

    cat_labels = {
        DecisionCategory.WORKFORCE: "Workforce    ",
        DecisionCategory.COMPENSATION: "Compensation ",
        DecisionCategory.CONDITIONS: "Conditions   ",
        DecisionCategory.COMMUNICATION: "Communication",
        DecisionCategory.INVESTMENT: "Investment   ",
    }

    for cs in score.category_scores:
        label = cat_labels.get(cs.category, str(cs.category).ljust(13))
        bar = _bar(cs.profit_orientation, 24)
        weight_pct = int(cs.weight * 100)
        lines.append(
            f"  {label}  {bar}  {cs.profit_orientation:4.0f}% profit  "
            f"({cs.decision_count} decisions, {weight_pct}% weight)"
        )

    # Decision detail
    if decisions:
        lines.append("")
        lines.append("  Key Decisions")
        lines.append("  " + "-" * (w - 4))
        for d in sorted(decisions, key=lambda x: x.year):
            arrow = _orientation_arrow(d.profit_orientation)
            lines.append(f"  [{d.year}] {d.title}")
            lines.append(f"         {arrow} {d.profit_orientation}% profit — {d.context[:80]}")
            lines.append("")

    lines.append("=" * w)
    return "\n".join(lines)


def render_comparison(scores: list[RevealedScore]) -> str:
    """Render a ranked comparison of multiple companies."""
    lines = []
    w = 70

    lines.append("=" * w)
    lines.append("  CANDOR SIMULATOR — Comparative Analysis")
    lines.append("=" * w)
    lines.append("")
    lines.append("  PEOPLE <-------------------------------------------> PROFIT")
    lines.append("")

    # Sort by profit orientation (most people-first at top)
    ranked = sorted(scores, key=lambda s: s.overall_profit_orientation)

    # Find longest name for alignment
    max_name = max(len(f"{s.company} ({s.ticker})") for s in ranked)

    for s in ranked:
        name = f"{s.company} ({s.ticker})".ljust(max_name)
        bar = _bar(s.overall_profit_orientation, 28)
        pos = (
            f"Pos {s.compass_position}"
            if s.compass_position
            else "Dead Zone"
        )
        lines.append(f"  {name}  {bar}  {s.overall_profit_orientation:4.1f}%  {pos}")

    lines.append("")
    lines.append("  " + "-" * (w - 4))
    lines.append("  Methodology: Weighted average across workforce (30%),")
    lines.append("  compensation (25%), conditions (20%), communication (15%),")
    lines.append("  and investment in people (10%). Based on public record.")
    lines.append("")
    lines.append("  Scores are interpretive. Reasonable people will disagree")
    lines.append("  on individual numbers. The pattern is the point.")
    lines.append("=" * w)
    return "\n".join(lines)


def _compass_line(profit_pct: float) -> str:
    """Render the compass position line."""
    # 50-char scale from 0 to 100
    width = 50
    pos = int(profit_pct / 100 * width)
    pos = max(0, min(width - 1, pos))

    scale = list("." * width)
    # Mark compass positions
    for pct, label in [(15, "1"), (36, "2"), (50, "X"), (64, "4"), (85, "5")]:
        idx = int(pct / 100 * width)
        if idx < width:
            scale[idx] = label

    pointer_line = list(" " * width)
    pointer_line[pos] = "\u25b2"  # ▲

    return (
        f"  PEOPLE {''.join(scale)} PROFIT\n"
        f"         {''.join(pointer_line)}"
    )


def _bar(profit_pct: float, width: int = 24) -> str:
    """Render a horizontal bar."""
    filled = int(profit_pct / 100 * width)
    filled = max(0, min(width, filled))
    return FILLED * filled + EMPTY * (width - filled)


def _orientation_arrow(profit_pct: float) -> str:
    if profit_pct <= 30:
        return "<< people"
    elif profit_pct <= 45:
        return "<  people"
    elif profit_pct <= 55:
        return "-- mixed "
    elif profit_pct <= 70:
        return "  profit>"
    else:
        return " profit>>"

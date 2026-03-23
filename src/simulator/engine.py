"""Scoring engine — turns corporate decisions into a revealed compass position."""

from collections import defaultdict

from .models import (
    CATEGORY_WEIGHTS,
    CategoryScore,
    CompanyProfile,
    DecisionCategory,
    RevealedScore,
)


def score_company(profile: CompanyProfile) -> RevealedScore:
    """Score a company's decisions and reveal their compass position.

    Methodology:
    1. Group decisions by category
    2. Average profit_orientation within each category
    3. Weighted average across categories (workforce weighted highest)
    4. Map overall score to compass position
    """
    by_category: dict[DecisionCategory, list[int]] = defaultdict(list)
    for d in profile.decisions:
        by_category[d.category].append(d.profit_orientation)

    category_scores = []
    weighted_sum = 0.0
    weight_sum = 0.0

    for cat, weight in CATEGORY_WEIGHTS.items():
        scores = by_category.get(cat, [])
        if not scores:
            continue
        avg = sum(scores) / len(scores)
        category_scores.append(CategoryScore(
            category=cat,
            profit_orientation=round(avg, 1),
            decision_count=len(scores),
            weight=weight,
        ))
        weighted_sum += avg * weight
        weight_sum += weight

    # Normalize if we're missing categories
    overall = weighted_sum / weight_sum if weight_sum > 0 else 50.0

    position, label = _map_to_compass(overall)

    return RevealedScore(
        company=profile.name,
        ticker=profile.ticker,
        overall_profit_orientation=round(overall, 1),
        category_scores=sorted(category_scores, key=lambda s: s.profit_orientation, reverse=True),
        compass_position=position,
        compass_label=label,
        total_decisions=len(profile.decisions),
        period=profile.period,
    )


def _map_to_compass(profit_pct: float) -> tuple[int | None, str]:
    """Map a 0–100 profit orientation score to a compass position.

    Position 1: 0–29%  profit → People Primary  (67%+ people)
    Position 2: 30–44% profit → People Leaning  (58%+ people)
    Dead Zone:  45–55% profit → no position     (the uncomfortable middle)
    Position 4: 56–70% profit → Profit Leaning  (58%+ profit)
    Position 5: 71–100% profit → Profit Primary (67%+ profit)
    """
    if profit_pct <= 29:
        return 1, "People Primary"
    elif profit_pct <= 44:
        return 2, "People Leaning"
    elif profit_pct <= 55:
        return None, "Dead Zone — pick a side"
    elif profit_pct <= 70:
        return 4, "Profit Leaning"
    else:
        return 5, "Profit Primary"

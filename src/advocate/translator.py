"""Corporate-to-Plain translator.

When executives speak, they use language designed to make hard things sound
soft. This module translates what they said into what they meant, and what
your team is actually hearing.
"""

from dataclasses import dataclass


@dataclass
class Translation:
    corporate: str
    plain: str
    what_your_team_hears: str


# The dictionary. Built from decades of corporate communication patterns.
# Each entry: what they said → what it means → what your team actually hears.
TRANSLATIONS: list[Translation] = [
    # Workforce
    Translation(
        "We are rightsizing the organization",
        "We are laying people off",
        "I might lose my job",
    ),
    Translation(
        "We are restructuring for efficiency",
        "We are eliminating positions to cut costs",
        "My position might be one of them",
    ),
    Translation(
        "We need to optimize our workforce",
        "We have decided some of you are overhead",
        "They're figuring out who to cut",
    ),
    Translation(
        "We are transforming our organizational structure",
        "We are rearranging reporting lines and cutting roles that don't survive the reorg",
        "My manager might change and my role might disappear",
    ),
    Translation(
        "We are aligning resources to strategic priorities",
        "We are moving budget away from your area to something we care about more",
        "Our team is not a priority anymore",
    ),
    Translation(
        "We are building a leaner organization",
        "We are cutting headcount",
        "There will be fewer of us doing the same work",
    ),
    Translation(
        "We need to do more with less",
        "We are cutting staff but not reducing the workload",
        "I'm about to do two jobs for the same pay",
    ),
    Translation(
        "We are investing in automation to augment our workforce",
        "We are replacing jobs with software",
        "A machine is going to do my job",
    ),
    Translation(
        "We are empowering teams to work more efficiently with AI",
        "We need fewer people because AI handles part of the job now",
        "They're building the case that my job can be done by a bot",
    ),

    # Compensation
    Translation(
        "We are adjusting our compensation philosophy",
        "We are cutting pay or benefits",
        "I'm going to make less money",
    ),
    Translation(
        "We are standardizing our benefits package",
        "We are reducing benefits to the lowest common denominator",
        "I'm losing something I currently have",
    ),
    Translation(
        "Equity refreshers will be evaluated on a performance basis",
        "Most people aren't getting stock refreshes this cycle",
        "My compensation is effectively going down",
    ),
    Translation(
        "We are moving to a more competitive compensation model",
        "We benchmarked and are adjusting — could go either way, but it's usually down",
        "They found out they could pay less",
    ),

    # Culture
    Translation(
        "We are one family here",
        "We want the loyalty of a family with the disposability of an employee",
        "They'll call me family until they fire me",
    ),
    Translation(
        "We have an open door policy",
        "You can technically speak up, and we can technically ignore you",
        "If I complain, they'll know who I am",
    ),
    Translation(
        "We value work-life balance",
        "We say this in recruiting. The actual culture may vary",
        "My manager emails me at 11pm",
    ),
    Translation(
        "We are committed to transparency",
        "We will share what we want you to know",
        "If they were actually transparent, they wouldn't need to say it",
    ),
    Translation(
        "This was a difficult decision",
        "This was a financial decision that we find mildly uncomfortable to announce",
        "It wasn't difficult enough to stop them from doing it",
    ),

    # RTO / Work
    Translation(
        "We believe in the power of in-person collaboration",
        "We want people in the office. The reason is control, real estate costs, or both",
        "They don't trust us to work from home",
    ),
    Translation(
        "Return to office will strengthen our culture",
        "We are mandating office attendance and calling it culture",
        "I'm going to lose two hours a day to commuting again",
    ),
    Translation(
        "We are implementing a hybrid work model",
        "You will come in on the days we choose",
        "This is RTO with a PR-friendly name",
    ),

    # Positive spin
    Translation(
        "This is an exciting time for the company",
        "Something significant is changing — exciting for shareholders, uncertain for you",
        "When they say exciting, I get nervous",
    ),
    Translation(
        "We are positioning for long-term growth",
        "Short-term pain is coming — the growth is for the stock price",
        "Long-term growth never seems to include my salary",
    ),
    Translation(
        "We are focused on shareholder value",
        "The stock price is the priority — everything else is a means to that end",
        "I am a means to an end",
    ),
    Translation(
        "Our people are our greatest asset",
        "Our people are an asset — assets get depreciated, written off, and replaced",
        "If I were really their greatest asset, they wouldn't need to keep saying it",
    ),

    # Performance
    Translation(
        "We are raising the performance bar",
        "We are creating documentation to justify letting people go",
        "They're building a paper trail",
    ),
    Translation(
        "We are implementing a more rigorous review process",
        "We need a defensible process for the cuts that are already decided",
        "The decision is already made — this is the paperwork",
    ),
    Translation(
        "We are investing in performance management",
        "We are making it easier to fire people with legal cover",
        "HR is building a case against someone on my team. Or me",
    ),
    Translation(
        "We need to have a courageous conversation",
        "We are about to tell you something you won't like and frame it as bravery",
        "I'm about to hear bad news delivered by someone who thinks telling me is the hard part",
    ),
]


def translate(text: str) -> list[Translation]:
    """Find translations that match the given corporate text.

    Uses keyword matching — not exact string matching — because
    corporate language is endlessly creative in saying the same things.
    """
    text_lower = text.lower()
    matches = []

    # Score each translation by keyword overlap
    scored = []
    for t in TRANSLATIONS:
        corporate_words = set(t.corporate.lower().split())
        text_words = set(text_lower.split())
        overlap = len(corporate_words & text_words)
        # Require at least 3 matching words or 40% overlap
        if overlap >= 3 or (len(corporate_words) > 0 and overlap / len(corporate_words) >= 0.4):
            scored.append((overlap, t))

    scored.sort(key=lambda x: x[0], reverse=True)
    return [t for _, t in scored]


def get_all_translations() -> list[Translation]:
    """Return the full translation dictionary."""
    return TRANSLATIONS

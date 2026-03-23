"""Company profiles built from publicly documented corporate decisions.

Every decision here is based on public reporting — SEC filings, press releases,
news coverage, OSHA data, NLRB rulings, and company statements. The scoring
reflects how each decision weighted profit vs. people based on observable
outcomes, not corporate intent.

Scores are inherently interpretive. Reasonable people can disagree on any
individual number. The value is in the pattern, not any single data point.
"""

from .models import CompanyProfile, Decision, DecisionCategory
from .companies_extended import get_extended_companies

C = DecisionCategory


def get_all_companies() -> list[CompanyProfile]:
    return [
        amazon(),
        apple(),
        cisco(),
        costco(),
        google(),
        jpmorgan(),
        meta(),
        microsoft(),
        netflix(),
        tesla(),
        walmart(),
    ] + get_extended_companies()


def get_company(name: str) -> CompanyProfile | None:
    name_lower = name.lower().strip()
    for company in get_all_companies():
        if name_lower in (company.name.lower(), company.ticker.lower()):
            return company
        # Handle common aliases
        if name_lower == "alphabet" and company.ticker == "GOOGL":
            return company
        if name_lower == "chase" and company.ticker == "JPM":
            return company
    return None


def amazon() -> CompanyProfile:
    return CompanyProfile(
        name="Amazon",
        ticker="AMZN",
        sector="Technology / Retail",
        period="2018–2024",
        decisions=[
            Decision(
                year=2023,
                category=C.WORKFORCE,
                title="27,000 layoffs across three rounds",
                description="Three waves of layoffs (Nov 2022–Mar 2023) totaling ~27,000 "
                "employees, primarily in corporate roles, during a year of $21B net income.",
                profit_orientation=85,
                context="Large-scale RIF during highly profitable period. Framed as "
                "efficiency measure. Severance packages were standard, not generous.",
            ),
            Decision(
                year=2018,
                category=C.COMPENSATION,
                title="$15/hr minimum wage",
                description="Raised minimum wage to $15/hr for all US employees, "
                "ahead of federal or most state requirements.",
                profit_orientation=30,
                context="Industry-leading move at the time. Eliminated variable comp "
                "and stock grants for warehouse workers in the same change.",
            ),
            Decision(
                year=2022,
                category=C.COMPENSATION,
                title="Career Choice tuition program expansion",
                description="Expanded prepaid tuition program to cover full college "
                "tuition for front-line employees.",
                profit_orientation=25,
                context="Genuine investment in employee mobility. Available regardless "
                "of whether the degree relates to Amazon's business.",
            ),
            Decision(
                year=2023,
                category=C.CONDITIONS,
                title="Warehouse injury rates above industry average",
                description="OSHA data and investigative reporting consistently showed "
                "Amazon warehouse serious injury rates roughly double the industry average.",
                profit_orientation=80,
                context="Speed and productivity targets directly linked to injury rates. "
                "Company invested in safety programs but maintained pace targets.",
            ),
            Decision(
                year=2022,
                category=C.CONDITIONS,
                title="Strict productivity monitoring",
                description="Time-off-task tracking systems monitoring warehouse workers, "
                "with automated warnings for deviations from productivity targets.",
                profit_orientation=78,
                context="Surveillance-level monitoring tied directly to throughput. "
                "Workers reported stress and bathroom break anxiety.",
            ),
            Decision(
                year=2023,
                category=C.COMMUNICATION,
                title="Jassy layoff announcements",
                description="CEO Andy Jassy's blog posts announcing layoffs were relatively "
                "direct about the reasons (over-hiring during COVID, economic uncertainty).",
                profit_orientation=45,
                context="More direct than many peers. Used some corporate framing but "
                "acknowledged the difficulty. Didn't call it 'rightsizing.'",
            ),
            Decision(
                year=2024,
                category=C.CONDITIONS,
                title="Full return-to-office mandate",
                description="Required all corporate employees back to office 5 days/week, "
                "reversing pandemic-era flexibility.",
                profit_orientation=72,
                context="Among the strictest RTO mandates in tech. Widely seen as "
                "a soft layoff mechanism — attrition expected and likely intended.",
            ),
            Decision(
                year=2021,
                category=C.INVESTMENT,
                title="$1.2B upskilling pledge",
                description="Committed to providing free skills training to 300,000 employees "
                "by 2025 through various internal programs.",
                profit_orientation=30,
                context="Substantial investment. Programs include cloud computing, "
                "machine learning, and non-Amazon career paths.",
            ),
        ],
    )


def cisco() -> CompanyProfile:
    return CompanyProfile(
        name="Cisco",
        ticker="CSCO",
        sector="Technology / Networking",
        period="2022–2025",
        decisions=[
            Decision(
                year=2024,
                category=C.WORKFORCE,
                title="~4,000 layoffs — 'rebalancing' to AI and security",
                description="Cut approximately 5% of workforce in February 2024, "
                "framed as a strategic pivot toward AI and cybersecurity growth areas.",
                profit_orientation=75,
                context="Profitable company cutting during a 'pivot' narrative. "
                "The rebalancing framing implies the people being cut were in "
                "the wrong part of the business — not that the business made "
                "the wrong bets.",
            ),
            Decision(
                year=2024,
                category=C.WORKFORCE,
                title="~5,600 additional layoffs — second round in same year",
                description="Cut another ~7% of workforce in August 2024, just six "
                "months after the first round. Again framed as pivoting to AI.",
                profit_orientation=82,
                context="Two major rounds in one year totaling ~12% of the company. "
                "The second round signals the first wasn't enough — or that "
                "ongoing cuts are the actual strategy, not a one-time realignment.",
            ),
            Decision(
                year=2023,
                category=C.WORKFORCE,
                title="~4,000 layoffs in November",
                description="Approximately 4,000 positions eliminated in late 2023, "
                "continuing a pattern of annual restructuring cycles.",
                profit_orientation=72,
                context="Cisco has done layoffs nearly every year for the past "
                "several years. At some point 'restructuring' becomes the "
                "permanent state, not a transition to something better.",
            ),
            Decision(
                year=2023,
                category=C.COMPENSATION,
                title="Competitive tech compensation and benefits",
                description="Maintains competitive pay, equity grants, ESPP, and "
                "benefits package across engineering and corporate roles.",
                profit_orientation=35,
                context="Good compensation for those who remain. Standard for "
                "large tech companies competing for talent.",
            ),
            Decision(
                year=2024,
                category=C.CONDITIONS,
                title="Increased return-to-office expectations",
                description="Despite building and selling Webex as a remote collaboration "
                "platform, increased expectations for in-office presence.",
                profit_orientation=58,
                context="The irony of a company that sells remote work tools "
                "requiring its own employees to come back to the office. "
                "Suggests the product pitch and the internal belief don't match.",
            ),
            Decision(
                year=2024,
                category=C.COMMUNICATION,
                title="Perpetual 'pivot' and 'rebalancing' framing",
                description="Every layoff round framed as a strategic pivot to growth "
                "areas — AI, security, subscription revenue. The language of "
                "transformation applied to what is, by pattern, annual cost cutting.",
                profit_orientation=75,
                context="When you 'rebalance' every year, you're not rebalancing — "
                "you're running a permanent cost reduction program and calling "
                "it strategy. The employees being cut aren't in the wrong area. "
                "They're in the area that ran out of political cover.",
            ),
            Decision(
                year=2024,
                category=C.COMMUNICATION,
                title="Celebrating workforce metrics while cutting workforce",
                description="Highlighting record certification numbers, engineering "
                "achievements, and talent quality in the same period as laying "
                "off thousands of those same engineers.",
                profit_orientation=70,
                context="You cannot simultaneously be proud of your certified "
                "engineers and be firing them. If the certifications matter, "
                "protect the people who hold them. If the people are expendable, "
                "stop celebrating the certifications. Pick one.",
            ),
            Decision(
                year=2023,
                category=C.INVESTMENT,
                title="Cisco Networking Academy",
                description="Free global education program that has trained millions "
                "of students in networking, security, and IT fundamentals since 1997.",
                profit_orientation=20,
                context="One of the largest corporate education programs in the world. "
                "Genuinely impactful. Creates a pipeline of Cisco-trained talent — "
                "which also serves the business, but the scale of impact is real.",
            ),
            Decision(
                year=2024,
                category=C.INVESTMENT,
                title="AI reskilling alongside layoffs",
                description="Internal programs to retrain employees for AI and security "
                "roles, running simultaneously with layoffs that cut people "
                "in the areas being deprioritized.",
                profit_orientation=60,
                context="Reskilling is offered, but the timeline doesn't match the "
                "layoff timeline. If you're cutting people this quarter and "
                "reskilling people over 12 months, the reskilling is for the "
                "survivors, not the affected.",
            ),
        ],
    )


def apple() -> CompanyProfile:
    return CompanyProfile(
        name="Apple",
        ticker="AAPL",
        sector="Technology / Hardware",
        period="2019–2024",
        decisions=[
            Decision(
                year=2023,
                category=C.WORKFORCE,
                title="Minimal layoffs relative to peers",
                description="While most Big Tech companies cut 5–10% of staff in 2023, "
                "Apple avoided broad layoffs, opting for hiring slowdowns instead.",
                profit_orientation=25,
                context="Rarest among tech giants to avoid mass layoffs. Chose attrition "
                "and hiring freezes over RIFs during the same downturn.",
            ),
            Decision(
                year=2024,
                category=C.WORKFORCE,
                title="Small targeted layoffs in special projects",
                description="~600 employees laid off from car project (Titan) and "
                "display technology teams after project cancellations.",
                profit_orientation=55,
                context="Project-specific, not efficiency-driven. Relatively small scale. "
                "Severance details not widely reported.",
            ),
            Decision(
                year=2022,
                category=C.COMPENSATION,
                title="Retail worker pay and benefits",
                description="Starting retail pay ~$22/hr with benefits, but retail "
                "unionization efforts met with resistance.",
                profit_orientation=50,
                context="Above average retail pay. But anti-union response (captive "
                "audience meetings, hiring anti-union consultants) documented at "
                "multiple stores.",
            ),
            Decision(
                year=2023,
                category=C.CONDITIONS,
                title="Supply chain labor standards",
                description="Continued supplier responsibility audits, but investigative "
                "reporting revealed gaps between policy and factory floor reality, "
                "particularly in China.",
                profit_orientation=65,
                context="Apple publishes supplier responsibility reports and has improved "
                "standards over time, but enforcement remains inconsistent. Cost "
                "pressure on suppliers creates structural tension.",
            ),
            Decision(
                year=2023,
                category=C.CONDITIONS,
                title="Hybrid work policy",
                description="Required 3 days/week in office. Faced internal petition "
                "with thousands of signatures, held firm.",
                profit_orientation=55,
                context="Less aggressive than Amazon's 5-day mandate. But overrode "
                "significant employee pushback. Some departures resulted.",
            ),
            Decision(
                year=2022,
                category=C.COMMUNICATION,
                title="Corporate transparency",
                description="Apple's famously secretive culture extends to internal "
                "decisions. Employees often learn about changes through press leaks.",
                profit_orientation=60,
                context="Secrecy serves product strategy but creates anxiety. "
                "Internal communication about workforce decisions is limited.",
            ),
            Decision(
                year=2023,
                category=C.INVESTMENT,
                title="Education and development benefits",
                description="Apple University, education reimbursement, and internal "
                "mobility programs for corporate employees.",
                profit_orientation=35,
                context="Strong programs for corporate staff. Less structured "
                "development paths for retail workers.",
            ),
        ],
    )


def costco() -> CompanyProfile:
    return CompanyProfile(
        name="Costco",
        ticker="COST",
        sector="Retail",
        period="2019–2024",
        decisions=[
            Decision(
                year=2024,
                category=C.WORKFORCE,
                title="No significant layoffs",
                description="Costco has not conducted significant layoffs in its recent "
                "history, even during economic downturns.",
                profit_orientation=10,
                context="Consistently prioritizes workforce stability. Adjusts through "
                "attrition and hiring pace rather than RIFs.",
            ),
            Decision(
                year=2024,
                category=C.COMPENSATION,
                title="Starting wage $17.50+/hr with regular increases",
                description="Starting wages well above retail industry average, with "
                "scheduled raises and top-out rates above $30/hr for hourly staff.",
                profit_orientation=15,
                context="Consistently among highest-paying retailers. Includes "
                "time-based raises that reward tenure.",
            ),
            Decision(
                year=2023,
                category=C.COMPENSATION,
                title="Healthcare for part-time employees",
                description="Health insurance available to part-time employees after "
                "relatively short qualifying periods, including dental and vision.",
                profit_orientation=15,
                context="Rare in retail. Most competitors restrict benefits to "
                "full-time workers or impose long waiting periods.",
            ),
            Decision(
                year=2024,
                category=C.CONDITIONS,
                title="Low turnover, high retention",
                description="Employee turnover rate consistently around 8–10% for "
                "employees past their first year, vs 60%+ industry average.",
                profit_orientation=12,
                context="Retention is both cause and effect of people-oriented policies. "
                "Costco views low turnover as a competitive advantage.",
            ),
            Decision(
                year=2025,
                category=C.CONDITIONS,
                title="Board rejected anti-DEI shareholder proposal",
                description="Board recommended against a shareholder proposal to report "
                "on risks of DEI policies, calling its programs sound.",
                profit_orientation=20,
                context="Stood by workforce programs under external pressure. "
                "CEO Ron Vachris publicly defended the approach.",
            ),
            Decision(
                year=2023,
                category=C.COMMUNICATION,
                title="Direct employee communication",
                description="Company communications tend toward straightforward language "
                "about business performance and decisions.",
                profit_orientation=25,
                context="Less corporate-speak than most retailers. Union relationship "
                "(Teamsters for some locations) keeps communication structured.",
            ),
            Decision(
                year=2023,
                category=C.INVESTMENT,
                title="Promote-from-within culture",
                description="Strong internal promotion pipeline. Many warehouse managers "
                "and executives started as floor staff.",
                profit_orientation=15,
                context="Genuine internal mobility. CEO Vachris started as a "
                "forklift driver. Not just branding.",
            ),
        ],
    )


def google() -> CompanyProfile:
    return CompanyProfile(
        name="Google",
        ticker="GOOGL",
        sector="Technology",
        period="2020–2024",
        decisions=[
            Decision(
                year=2023,
                category=C.WORKFORCE,
                title="12,000 layoffs",
                description="Cut ~6% of workforce in January 2023. Many employees "
                "learned via email finding their access revoked. CEO Pichai took "
                "'full responsibility.'",
                profit_orientation=78,
                context="During profitable year. Notification by locked accounts was "
                "widely criticized. 16 weeks severance plus 2 weeks per year "
                "of tenure — decent but not exceptional for the industry.",
            ),
            Decision(
                year=2024,
                category=C.WORKFORCE,
                title="Continued targeted layoffs across divisions",
                description="Ongoing cuts throughout 2024 in cloud, advertising, "
                "hardware, and assistant teams. Hundreds at a time.",
                profit_orientation=72,
                context="Death by a thousand cuts approach. Less visible than the "
                "Jan 2023 event but cumulative impact was significant.",
            ),
            Decision(
                year=2022,
                category=C.COMPENSATION,
                title="Historically generous total compensation",
                description="Among the highest-paying tech companies. Strong equity "
                "grants, bonuses, and benefits package.",
                profit_orientation=25,
                context="Top-of-market pay for those who remain. Compensation itself "
                "has been a people-first signal, though some erosion in recent years.",
            ),
            Decision(
                year=2023,
                category=C.CONDITIONS,
                title="Perks reductions and cost-cutting",
                description="Reduced free food options, fitness classes, micro-kitchens, "
                "and other amenities that defined Google's culture.",
                profit_orientation=65,
                context="Symbolic and material. These perks were part of an implicit "
                "contract. Cutting them saved modest money but signaled a culture shift.",
            ),
            Decision(
                year=2024,
                category=C.CONDITIONS,
                title="Hybrid work with increasing office pressure",
                description="Official 3-day hybrid policy, but badge tracking and "
                "manager pressure pushed toward more office time.",
                profit_orientation=58,
                context="The policy says hybrid. The measurement says attendance. "
                "Employees noted the gap between stated and enforced policy.",
            ),
            Decision(
                year=2023,
                category=C.COMMUNICATION,
                title="Pichai layoff communications",
                description="CEO email took responsibility but used phrases like "
                "'set us up for the future' and 'sharpen our focus.'",
                profit_orientation=60,
                context="Mixed. Acknowledged difficulty and took responsibility, "
                "which is better than many. But leaned on strategy framing "
                "rather than plain 'we are cutting costs.'",
            ),
            Decision(
                year=2024,
                category=C.INVESTMENT,
                title="AI reskilling focus",
                description="Internal training programs pivoted heavily toward AI. "
                "Some roles rewritten to require AI skills; those who couldn't "
                "transition were vulnerable.",
                profit_orientation=50,
                context="Investment in training, but primarily for the company's "
                "strategic direction rather than employee-chosen growth. "
                "Reskill toward what we need, not what you want.",
            ),
        ],
    )


def jpmorgan() -> CompanyProfile:
    return CompanyProfile(
        name="JPMorgan Chase",
        ticker="JPM",
        sector="Financial Services",
        period="2020–2024",
        decisions=[
            Decision(
                year=2024,
                category=C.WORKFORCE,
                title="Periodic workforce reductions",
                description="Regular efficiency-driven headcount reductions across "
                "divisions, particularly in consumer banking as branches consolidate.",
                profit_orientation=65,
                context="Ongoing optimization. Not dramatic single events but steady "
                "trimming. Severance follows industry standards.",
            ),
            Decision(
                year=2023,
                category=C.COMPENSATION,
                title="Strong professional compensation, branch worker gap",
                description="Top-tier pay and bonuses for investment banking and "
                "corporate staff. Branch and operations workers paid significantly less.",
                profit_orientation=55,
                context="Competitive where talent is scarce (IB, tech). Less generous "
                "where labor supply is abundant (retail banking).",
            ),
            Decision(
                year=2023,
                category=C.COMPENSATION,
                title="$16.50–$20/hr minimum for branch employees",
                description="Raised minimum wage for entry-level roles based on local "
                "cost of living.",
                profit_orientation=40,
                context="Above federal minimum and competitive in banking. Scaled "
                "by geography, which shows some nuance.",
            ),
            Decision(
                year=2024,
                category=C.CONDITIONS,
                title="Strict 5-day return-to-office mandate",
                description="Required all managing directors back 5 days/week, with "
                "broader workforce expected to follow. Dimon publicly dismissive "
                "of remote work.",
                profit_orientation=75,
                context="Among the most aggressive RTO mandates in any sector. "
                "Dimon called remote work 'not OK' and questioned its productivity. "
                "No flex options for most roles.",
            ),
            Decision(
                year=2023,
                category=C.COMMUNICATION,
                title="Dimon's direct communication style",
                description="Jamie Dimon is famously blunt in shareholder letters and "
                "employee town halls. Doesn't sugarcoat business decisions.",
                profit_orientation=35,
                context="Dimon says what he thinks, even when unpopular. His shareholder "
                "letters are unusually candid about challenges. Less euphemism "
                "than most bank CEOs.",
            ),
            Decision(
                year=2023,
                category=C.INVESTMENT,
                title="$350M workforce development programs",
                description="Multi-year commitment to employee training, career pathways, "
                "and community workforce development.",
                profit_orientation=35,
                context="Significant investment in upskilling. Includes partnerships "
                "with community colleges and internal career mobility programs.",
            ),
        ],
    )


def meta() -> CompanyProfile:
    return CompanyProfile(
        name="Meta",
        ticker="META",
        sector="Technology",
        period="2022–2024",
        decisions=[
            Decision(
                year=2023,
                category=C.WORKFORCE,
                title="21,000 layoffs — 'Year of Efficiency'",
                description="Two rounds totaling ~21,000 employees (Nov 2022 and Mar 2023). "
                "Zuckerberg declared it the 'Year of Efficiency' and said Meta had "
                "hired too aggressively.",
                profit_orientation=82,
                context="Massive scale. The 'efficiency' framing turned people into "
                "overhead. Stock price surged on the announcements, which tells "
                "you who the market thought was benefiting.",
            ),
            Decision(
                year=2024,
                category=C.WORKFORCE,
                title="Continued 'flattening' and performance-based cuts",
                description="Ongoing role eliminations through 2024, framed as removing "
                "management layers and raising the performance bar.",
                profit_orientation=75,
                context="Performance improvement plans used as a managed attrition tool. "
                "The 'flattening' narrative made cuts seem structural rather than human.",
            ),
            Decision(
                year=2023,
                category=C.COMPENSATION,
                title="Strong compensation for retained employees",
                description="Maintained top-tier compensation, equity refresh grants, "
                "and benefits for remaining workforce.",
                profit_orientation=35,
                context="Generous to survivors. The implicit message: if you make the "
                "cut, you'll be rewarded. Creates loyalty through scarcity.",
            ),
            Decision(
                year=2023,
                category=C.CONDITIONS,
                title="Return-to-office 3 days/week",
                description="Required 3-day in-office minimum, with tracking. "
                "Zuckerberg noted employees who came in performed better "
                "'based on data.'",
                profit_orientation=60,
                context="Moderate policy but justified with surveillance framing. "
                "Using performance data to justify office mandates blurs "
                "correlation and causation.",
            ),
            Decision(
                year=2022,
                category=C.COMMUNICATION,
                title="Zuckerberg layoff memos",
                description="Zuckerberg's layoff announcements acknowledged his role in "
                "over-hiring. 'I got this wrong' was direct. But 'Year of Efficiency' "
                "as a brand turned cost-cutting into a campaign.",
                profit_orientation=55,
                context="The personal accountability was notable and genuine. But "
                "branding a layoff year as a positive initiative undercuts "
                "the honesty.",
            ),
            Decision(
                year=2025,
                category=C.COMMUNICATION,
                title="Rolled back DEI and content moderation programs",
                description="Ended DEI-focused hiring programs and scaled back "
                "fact-checking partnerships ahead of new administration.",
                profit_orientation=75,
                context="Policy changes aligned with political environment and "
                "advertiser relationships rather than employee or user welfare.",
            ),
            Decision(
                year=2024,
                category=C.INVESTMENT,
                title="AI-focused reskilling",
                description="Heavy investment in AI capabilities, rewriting job "
                "descriptions and training around AI tools.",
                profit_orientation=55,
                context="Investment in workforce, but tightly coupled to company "
                "strategy. Train for what Meta needs, not general growth.",
            ),
        ],
    )


def microsoft() -> CompanyProfile:
    return CompanyProfile(
        name="Microsoft",
        ticker="MSFT",
        sector="Technology",
        period="2020–2024",
        decisions=[
            Decision(
                year=2023,
                category=C.WORKFORCE,
                title="10,000 layoffs",
                description="Cut ~5% of workforce in January 2023. Affected multiple "
                "divisions including HoloLens, Edge, and corporate functions.",
                profit_orientation=65,
                context="Significant but proportionally smaller than peers. Severance "
                "included healthcare continuation and career transition services. "
                "Stock was at all-time highs.",
            ),
            Decision(
                year=2024,
                category=C.WORKFORCE,
                title="Gaming division layoffs post-Activision",
                description="~1,900 layoffs in gaming division (8% of Microsoft Gaming) "
                "following Activision Blizzard acquisition.",
                profit_orientation=70,
                context="Acquisition-driven redundancy cuts. Expected but still affected "
                "nearly 2,000 people in a $69B acquisition where headcount reduction "
                "was part of the value thesis.",
            ),
            Decision(
                year=2023,
                category=C.COMPENSATION,
                title="Competitive compensation and benefits",
                description="Strong base pay, equity, healthcare, parental leave. "
                "Annual raises and stock refreshes maintained through downturn.",
                profit_orientation=30,
                context="Continued investing in compensation even during layoffs. "
                "Benefits package considered among the best in tech.",
            ),
            Decision(
                year=2023,
                category=C.CONDITIONS,
                title="Flexible hybrid work policy",
                description="Official policy allows managers and teams to set their "
                "own in-office schedules. No company-wide mandate.",
                profit_orientation=30,
                context="Among the most flexible major tech employers. Nadella has "
                "publicly supported hybrid work. Policy trusts teams rather "
                "than mandating.",
            ),
            Decision(
                year=2023,
                category=C.COMMUNICATION,
                title="Nadella layoff communications",
                description="Nadella's layoff memo was direct about economic conditions "
                "and over-hiring. Outlined specific severance and support.",
                profit_orientation=40,
                context="Relatively straightforward. Acknowledged the human cost. "
                "Provided specific detail about severance packages in the "
                "announcement itself, not as an afterthought.",
            ),
            Decision(
                year=2023,
                category=C.INVESTMENT,
                title="AI transformation training",
                description="Large-scale internal programs to upskill workforce on "
                "AI tools and Copilot integration. LinkedIn Learning access "
                "for all employees.",
                profit_orientation=35,
                context="Genuine investment in workforce capability. Strategic "
                "alignment with company direction, but broadly accessible "
                "and transferable skills.",
            ),
        ],
    )


def netflix() -> CompanyProfile:
    return CompanyProfile(
        name="Netflix",
        ticker="NFLX",
        sector="Technology / Entertainment",
        period="2020–2024",
        decisions=[
            Decision(
                year=2022,
                category=C.WORKFORCE,
                title="450 layoffs after subscriber loss",
                description="Cut ~300 then ~150 employees after first subscriber decline "
                "in a decade. Affected marketing, editorial, and production roles.",
                profit_orientation=70,
                context="Swift cuts in response to market signal. The 'keeper test' "
                "culture means the bar for retention is always high, and downturns "
                "accelerate the process.",
            ),
            Decision(
                year=2023,
                category=C.COMPENSATION,
                title="Top-of-market pay philosophy",
                description="Netflix pays at or above the top of market for every role. "
                "No bonuses — straight salary and equity. Philosophy: pay people "
                "what they'd get elsewhere, then some.",
                profit_orientation=15,
                context="Among the most generous compensation philosophies in any "
                "industry. The flip side: if you're not a 'keeper,' you're gone. "
                "Pay is high because expectations are absolute.",
            ),
            Decision(
                year=2023,
                category=C.COMPENSATION,
                title="Generous severance for 'adequate performers'",
                description="The culture memo states: adequate performance gets a "
                "generous severance package. Not a PIP. Not a warning. A package.",
                profit_orientation=40,
                context="Unusual honesty: we'll pay you well to leave rather than "
                "manage you out slowly. More dignity than a PIP, but also "
                "more ruthless than traditional performance management.",
            ),
            Decision(
                year=2023,
                category=C.CONDITIONS,
                title="High-performance culture, high expectations",
                description="The 'keeper test' asks managers: if this person told you "
                "they were leaving, would you fight to keep them? If not, give "
                "them a generous package now.",
                profit_orientation=65,
                context="Creates a high-output environment but also perpetual insecurity. "
                "You're never safe. The generosity of the exit doesn't change "
                "the anxiety of the tenure.",
            ),
            Decision(
                year=2023,
                category=C.COMMUNICATION,
                title="Radically transparent culture memo",
                description="The Netflix culture deck is public, specific, and honest "
                "about tradeoffs. 'We're a team, not a family.' 'Adequate "
                "performance gets a generous severance.'",
                profit_orientation=25,
                context="Among the most honest corporate communications ever published. "
                "It tells you exactly what you're signing up for. Whether the "
                "deal is good depends on who you are. But at least you know.",
            ),
            Decision(
                year=2023,
                category=C.INVESTMENT,
                title="Limited traditional development programs",
                description="Netflix hires experts rather than developing them. Minimal "
                "formal training or career development programs.",
                profit_orientation=70,
                context="The philosophy is: hire fully formed talent at top dollar. "
                "This is great for senior experts, less so for anyone trying "
                "to grow into a role.",
            ),
        ],
    )


def tesla() -> CompanyProfile:
    return CompanyProfile(
        name="Tesla",
        ticker="TSLA",
        sector="Automotive / Technology",
        period="2020–2024",
        decisions=[
            Decision(
                year=2024,
                category=C.WORKFORCE,
                title="10%+ global workforce reduction",
                description="Laid off more than 14,000 employees (~10% of workforce) "
                "in April 2024. Multiple senior executives also departed.",
                profit_orientation=85,
                context="Large-scale cut communicated abruptly. Some employees "
                "found out when badge access was revoked. During a period of "
                "slowing EV demand but company remained profitable.",
            ),
            Decision(
                year=2022,
                category=C.WORKFORCE,
                title="'Anyone who is remote must return or depart'",
                description="Musk email mandated 40+ hours/week in office for all "
                "employees, with no exception. 'If you don't show up, we will "
                "assume you have resigned.'",
                profit_orientation=85,
                context="Used as both a policy and an attrition tool. The tone was "
                "deliberately confrontational. No discussion, no exceptions.",
            ),
            Decision(
                year=2023,
                category=C.COMPENSATION,
                title="Below-market base pay, equity-heavy compensation",
                description="Base salaries generally below market for the auto and tech "
                "industries. Heavy reliance on stock options that are valuable "
                "only if the stock rises.",
                profit_orientation=70,
                context="Transfers risk to employees. If stock performs, compensation "
                "is excellent. If not, employees are underpaid. Company benefits "
                "either way through lower cash burn.",
            ),
            Decision(
                year=2023,
                category=C.CONDITIONS,
                title="Factory safety record",
                description="OSHA reports and investigative journalism documented "
                "injury rates at Fremont factory above industry average for "
                "auto manufacturing.",
                profit_orientation=80,
                context="Production pace prioritized over safety. Musk's stated "
                "preference for sleeping on the factory floor during 'production "
                "hell' set a culture where output overrides everything.",
            ),
            Decision(
                year=2023,
                category=C.CONDITIONS,
                title="NLRB findings on labor practices",
                description="Multiple NLRB findings related to suppression of worker "
                "organizing, including a ruling that Musk's tweet about stock "
                "options constituted an illegal threat.",
                profit_orientation=82,
                context="Documented pattern of anti-union activity through official "
                "government findings, not just allegations.",
            ),
            Decision(
                year=2024,
                category=C.COMMUNICATION,
                title="Communication via Musk's social media",
                description="Major policy announcements and workforce signals delivered "
                "through Musk's personal X/Twitter account rather than "
                "internal channels.",
                profit_orientation=70,
                context="Employees sometimes learn about their own company's "
                "direction from social media. Unconventional and destabilizing, "
                "but at least the statements are direct.",
            ),
            Decision(
                year=2023,
                category=C.INVESTMENT,
                title="Limited formal development programs",
                description="Minimal structured employee development or training programs. "
                "Culture emphasizes self-starters who learn by doing.",
                profit_orientation=75,
                context="Sink-or-swim approach. Works for a certain type of "
                "employee, excludes many others. No significant reskilling "
                "or career transition support.",
            ),
        ],
    )


def walmart() -> CompanyProfile:
    return CompanyProfile(
        name="Walmart",
        ticker="WMT",
        sector="Retail",
        period="2019–2024",
        decisions=[
            Decision(
                year=2023,
                category=C.WORKFORCE,
                title="Corporate restructuring and store role changes",
                description="Eliminated some corporate roles while restructuring "
                "store positions. Added higher-paying 'team lead' roles but "
                "reduced the total number of positions available.",
                profit_orientation=60,
                context="Created upward mobility paths for some but eliminated "
                "positions for others. Net effect was fewer jobs at higher pay — "
                "good for survivors, bad for those cut.",
            ),
            Decision(
                year=2024,
                category=C.COMPENSATION,
                title="Minimum wage $14–17/hr by market",
                description="Raised starting wages to $14–17/hr depending on market. "
                "Improvement from historical lows but still trails Costco and Target.",
                profit_orientation=55,
                context="Real improvement over time. But Walmart is the largest "
                "private employer in the US — the gap between their wages and "
                "a living wage in most markets remains significant.",
            ),
            Decision(
                year=2023,
                category=C.COMPENSATION,
                title="Part-time benefits restrictions",
                description="Healthcare and benefits availability more limited for "
                "part-time workers than competitors like Costco.",
                profit_orientation=70,
                context="Large portion of workforce is part-time. Benefits gap is "
                "a structural choice that keeps labor costs low at the expense "
                "of worker security.",
            ),
            Decision(
                year=2023,
                category=C.CONDITIONS,
                title="Anti-union stance",
                description="Long-documented history of union avoidance, including "
                "the famous 2005 closure of a Quebec store that had voted to unionize.",
                profit_orientation=80,
                context="Multi-decade pattern. Mandatory anti-union training for "
                "managers is well documented. The Quebec closure sent a clear "
                "signal regardless of stated reasons.",
            ),
            Decision(
                year=2023,
                category=C.COMMUNICATION,
                title="Corporate communication style",
                description="Heavy use of corporate framing: 'associates,' 'opportunities,' "
                "'our Walmart family.' Communications lean toward positive branding "
                "over candor.",
                profit_orientation=70,
                context="The 'family' framing that corporate America loves. "
                "You're family until you're a line item.",
            ),
            Decision(
                year=2022,
                category=C.INVESTMENT,
                title="Live Better U education program",
                description="Fully paid college tuition and books for associates "
                "through partnerships with universities.",
                profit_orientation=30,
                context="Genuinely good program. One of the largest corporate "
                "education benefits in the US. Available from day one of "
                "employment.",
            ),
        ],
    )

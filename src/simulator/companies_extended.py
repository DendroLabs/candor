"""Extended company profiles — additional companies beyond the original set.

Same methodology: publicly documented decisions, scored on 0–100
profit orientation scale. Lighter profiles (3–5 decisions) for companies
with less publicly documented labor practice data.
"""

from .models import CompanyProfile, Decision, DecisionCategory

C = DecisionCategory


def get_extended_companies() -> list[CompanyProfile]:
    """Return all extended company profiles."""
    return [
        # Technology
        nvidia(), broadcom(), amd(), oracle(), adobe(), intel(), ibm(),
        salesforce(), qualcomm(), intuit(), servicenow(), uber(), paypal(),
        accenture(),
        # Finance
        goldman_sachs(), morgan_stanley(), wells_fargo(), bank_of_america(),
        blackrock(), visa(), mastercard(), american_express(), progressive(),
        sp_global(),
        # Healthcare
        unitedhealth(), johnson_johnson(), pfizer(), merck(), eli_lilly(),
        abbvie(), amgen(), cvs_health(), cigna(), elevance(), medtronic(),
        # Consumer
        procter_gamble(), coca_cola(), pepsico(), mcdonalds(), disney(),
        starbucks(), home_depot(), nike(), target(), tjx(), colgate(),
        kraft_heinz(), kroger(), mondelez(), philip_morris(),
        # Industrial / Defense / Energy
        boeing(), general_electric(), caterpillar(), honeywell(),
        lockheed_martin(), three_m(), union_pacific(), fedex(), deere(),
        raytheon(), northrop_grumman(),
        exxonmobil(), chevron(), conocophillips(),
        # Other
        berkshire_hathaway(), t_mobile(), general_motors(), ford(),
    ]


# ── Technology ────────────────────────────────────────────────────────

def nvidia() -> CompanyProfile:
    return CompanyProfile(
        name="NVIDIA", ticker="NVDA", sector="Technology / Semiconductors",
        period="2022–2025",
        decisions=[
            Decision(2024, C.WORKFORCE,
                     "Minimal layoffs during explosive growth",
                     "No significant layoffs while revenue grew 200%+. Aggressive hiring.",
                     10, "Growth phase where every engineer is critical. Retention is the priority."),
            Decision(2024, C.COMPENSATION,
                     "Top-of-market compensation with massive equity upside",
                     "Among the highest total compensation in tech. Stock appreciation "
                     "created widespread wealth among employees.",
                     10, "When your stock 10x's in two years, compensation speaks for itself."),
            Decision(2024, C.CONDITIONS,
                     "Intense work culture under Jensen Huang",
                     "Known for demanding expectations, long hours, and Huang's direct "
                     "management style. High performance required.",
                     60, "The equity upside compensates, but the pace is unsustainable "
                     "for many. Not everyone thrives in this culture."),
            Decision(2024, C.COMMUNICATION,
                     "Jensen Huang's direct, no-BS communication",
                     "Huang is famously direct in all-hands, investor calls, and public "
                     "appearances. Says what he thinks.",
                     25, "Blunt but respected. Employees know where they stand."),
            Decision(2024, C.INVESTMENT,
                     "Heavy R&D investment, internal development",
                     "Massive R&D spending. Engineering talent treated as core asset.",
                     15, "When you're winning, investing in people is easy. The test "
                     "comes when growth slows."),
        ],
    )


def broadcom() -> CompanyProfile:
    return CompanyProfile(
        name="Broadcom", ticker="AVGO", sector="Technology / Semiconductors",
        period="2023–2025",
        decisions=[
            Decision(2024, C.WORKFORCE,
                     "Massive layoffs post-VMware acquisition",
                     "Thousands laid off after $61B VMware acquisition. Entire teams "
                     "eliminated as part of Hock Tan's standard acquisition playbook.",
                     88, "Hock Tan's model: acquire, cut, extract. VMware employees "
                     "knew it was coming. Didn't make it better."),
            Decision(2024, C.COMPENSATION,
                     "VMware benefits and perks gutted",
                     "VMware's generous benefits, free food, and culture programs "
                     "eliminated post-acquisition.",
                     82, "Cultural strip-mining. Everything that made VMware attractive "
                     "to employees was treated as waste."),
            Decision(2024, C.CONDITIONS,
                     "Acquisition-and-cut model as permanent strategy",
                     "Broadcom's entire growth model is built on acquiring companies "
                     "and reducing their cost structures aggressively.",
                     85, "If your company gets acquired by Broadcom, the playbook is known. "
                     "Cut costs, raise prices, extract value."),
            Decision(2024, C.COMMUNICATION,
                     "Minimal communication, efficiency-focused",
                     "Hock Tan communicates in numbers, not narratives. Minimal "
                     "corporate culture messaging.",
                     75, "At least there's no pretense. He doesn't call it a family."),
        ],
    )


def amd() -> CompanyProfile:
    return CompanyProfile(
        name="AMD", ticker="AMD", sector="Technology / Semiconductors",
        period="2022–2025",
        decisions=[
            Decision(2024, C.WORKFORCE,
                     "Minimal layoffs under Lisa Su",
                     "No significant workforce reductions during Su's turnaround. "
                     "Growth through competition rather than cost-cutting.",
                     20, "Lisa Su rebuilt AMD by investing in product and people, not "
                     "by cutting either."),
            Decision(2024, C.COMPENSATION,
                     "Competitive semiconductor compensation",
                     "Strong pay and equity. Recruiting aggressively against NVIDIA and Intel.",
                     25, "Has to compete for talent against NVIDIA's equity upside. "
                     "Invests accordingly."),
            Decision(2023, C.CONDITIONS,
                     "Focused, mission-driven culture",
                     "Smaller and more focused than competitors. Engineers report "
                     "strong sense of purpose under Su's leadership.",
                     25, "When you're the underdog beating the giants, culture "
                     "comes naturally."),
            Decision(2024, C.COMMUNICATION,
                     "Lisa Su's technical, direct leadership",
                     "Su communicates with technical substance. Respected by engineers. "
                     "Low corporate fluff.",
                     20, "One of the most respected tech CEOs. Leads with product, "
                     "not slogans."),
        ],
    )


def oracle() -> CompanyProfile:
    return CompanyProfile(
        name="Oracle", ticker="ORCL", sector="Technology",
        period="2022–2025",
        decisions=[
            Decision(2024, C.WORKFORCE,
                     "Regular restructuring rounds",
                     "Ongoing layoffs across cloud and legacy divisions as Oracle "
                     "pivots to cloud infrastructure.",
                     68, "Persistent optimization. Cloud pivot creates winners and losers "
                     "inside the company."),
            Decision(2023, C.COMPENSATION,
                     "Competitive for cloud engineering roles",
                     "Pay competitive in cloud/AI roles. Legacy product teams less so.",
                     42, "Two-tier compensation: cloud gets recruited at top dollar, "
                     "legacy gets market rate or below."),
            Decision(2024, C.CONDITIONS,
                     "Return-to-office and Austin consolidation",
                     "Moved HQ to Austin, increased office expectations. Larry Ellison's "
                     "corporate culture remains dominant.",
                     62, "Ellison's presence shapes everything. Intense, demanding culture "
                     "that rewards loyalty to the company's direction."),
            Decision(2023, C.COMMUNICATION,
                     "Standard corporate, less transparent",
                     "Oracle communicates through earnings calls and press releases. "
                     "Internal culture less transparent than peers.",
                     62, "Not a company known for open internal communication."),
        ],
    )


def adobe() -> CompanyProfile:
    return CompanyProfile(
        name="Adobe", ticker="ADBE", sector="Technology",
        period="2022–2025",
        decisions=[
            Decision(2024, C.WORKFORCE,
                     "Relatively few large layoffs",
                     "Small targeted cuts but no major RIFs compared to tech peers.",
                     32, "Avoided the mass layoff cycle that hit most of big tech."),
            Decision(2024, C.COMPENSATION,
                     "Strong tech compensation",
                     "Competitive pay, equity, and benefits for the creative tools market.",
                     28, "Good compensation in a space with less turnover than hyperscale tech."),
            Decision(2023, C.COMMUNICATION,
                     "Subscription model controversy",
                     "Cancellation fee backlash and FTC scrutiny over dark patterns. "
                     "Corporate response was defensive.",
                     62, "Customer-facing issue that reveals internal priorities. "
                     "Revenue retention over user transparency."),
            Decision(2024, C.INVESTMENT,
                     "Creative education and community programs",
                     "Adobe Creative Residency, education licensing, developer community.",
                     30, "Genuine investment in the creative community that feeds their ecosystem."),
        ],
    )


def intel() -> CompanyProfile:
    return CompanyProfile(
        name="Intel", ticker="INTC", sector="Technology / Semiconductors",
        period="2022–2025",
        decisions=[
            Decision(2024, C.WORKFORCE,
                     "15,000+ layoffs — ~15% of workforce",
                     "Massive reduction announced August 2024 under Pat Gelsinger's "
                     "turnaround plan. Largest cuts in company history.",
                     85, "Existential-level cuts during a genuine competitive crisis. "
                     "But the crisis was years of leadership failure, not employee failure."),
            Decision(2024, C.COMPENSATION,
                     "Suspended dividend, cut employee benefits",
                     "Dividend suspended for first time in decades. Employee benefits "
                     "and perks reduced alongside layoffs.",
                     75, "Employees and shareholders both took hits. But employees "
                     "also lost their jobs."),
            Decision(2024, C.CONDITIONS,
                     "Foundry pivot creating cultural whiplash",
                     "Attempting to become a contract chipmaker while cutting the workforce. "
                     "Remaining employees face uncertainty about the company's viability.",
                     68, "Asking survivors to bet their careers on a turnaround plan "
                     "while watching 15,000 colleagues walk out."),
            Decision(2024, C.COMMUNICATION,
                     "Gelsinger's turnaround narrative",
                     "Pat Gelsinger framed cuts as necessary for survival. Direct about "
                     "the competitive situation but heavy on transformation language.",
                     58, "More honest than most about the depth of the problem. "
                     "Still wrapped it in 'bold transformation' framing."),
            Decision(2023, C.INVESTMENT,
                     "Massive fab investment (CHIPS Act)",
                     "Billions in new US fabrication facilities, creating manufacturing jobs "
                     "in Ohio, Arizona, and elsewhere.",
                     35, "Real investment in domestic manufacturing and workforce. "
                     "But paired with cutting existing workforce simultaneously."),
        ],
    )


def ibm() -> CompanyProfile:
    return CompanyProfile(
        name="IBM", ticker="IBM", sector="Technology",
        period="2022–2025",
        decisions=[
            Decision(2024, C.WORKFORCE,
                     "Replacing back-office roles with AI",
                     "CEO Arvind Krishna stated IBM would pause hiring for ~7,800 roles "
                     "that could be replaced by AI over five years.",
                     82, "One of the first Fortune 500 CEOs to explicitly say AI would "
                     "replace specific job categories. Said the quiet part out loud."),
            Decision(2023, C.WORKFORCE,
                     "3,900 layoffs in January 2023",
                     "Cut ~1.5% of workforce in spin-off related restructuring.",
                     68, "Part of ongoing restructuring that's been happening for decades. "
                     "IBM has been in perpetual 'resource action' mode."),
            Decision(2023, C.COMPENSATION,
                     "Below-market for many roles",
                     "Compensation often trails competitors in cloud and AI. Pension "
                     "eliminated years ago.",
                     65, "Hard to recruit top talent when NVIDIA and Google pay 2-3x more. "
                     "IBM relies on stability and brand, not compensation."),
            Decision(2024, C.COMMUNICATION,
                     "Heavy corporate transformation speak",
                     "Everything framed as 'hybrid cloud and AI transformation.' "
                     "Decades of pivots with similar language.",
                     72, "IBM has been 'transforming' for 20 years. At some point the "
                     "transformation is the permanent state."),
            Decision(2023, C.INVESTMENT,
                     "SkillsBuild education platform",
                     "Free AI and technology education program available globally.",
                     30, "Genuine public good. Trains people in skills IBM needs, "
                     "but also broadly useful."),
        ],
    )


def salesforce() -> CompanyProfile:
    return CompanyProfile(
        name="Salesforce", ticker="CRM", sector="Technology",
        period="2022–2025",
        decisions=[
            Decision(2023, C.WORKFORCE,
                     "~7,000 layoffs — 10% of workforce",
                     "Massive cuts in January 2023. Benioff took responsibility for "
                     "over-hiring during pandemic boom.",
                     80, "The 'Ohana' culture dissolved overnight. You can't lay off "
                     "10% of your family."),
            Decision(2024, C.WORKFORCE,
                     "Additional ~700 layoffs in 2024",
                     "Follow-up cuts, smaller but continuing the pattern.",
                     70, "The second round confirms: the first wasn't enough, or "
                     "ongoing cuts are the new normal."),
            Decision(2023, C.COMPENSATION,
                     "Strong compensation for retained employees",
                     "Maintained competitive pay and equity for survivors.",
                     32, "Generous to those who made the cut. Same pattern as Meta."),
            Decision(2023, C.COMMUNICATION,
                     "Benioff's 'Ohana' to 'new day' pivot",
                     "Years of Hawaiian-themed family culture messaging abandoned for "
                     "efficiency language almost overnight.",
                     72, "When the culture brand doesn't survive the first layoff, "
                     "it was always marketing."),
            Decision(2023, C.INVESTMENT,
                     "Trailhead education platform",
                     "Free online learning platform for Salesforce skills, certifications, "
                     "and career development.",
                     22, "One of the best corporate education platforms. Creates real "
                     "career pathways for people outside the company too."),
        ],
    )


def qualcomm() -> CompanyProfile:
    return CompanyProfile(
        name="Qualcomm", ticker="QCOM", sector="Technology / Semiconductors",
        period="2022–2025",
        decisions=[
            Decision(2024, C.WORKFORCE,
                     "Regular restructuring cycles",
                     "Periodic layoffs tied to mobile market cycles and patent disputes.",
                     65, "Cyclical business means cyclical layoffs. Employees in non-core "
                     "areas are perpetually at risk."),
            Decision(2023, C.COMPENSATION,
                     "Competitive semiconductor pay",
                     "Strong compensation for engineering roles. Patent revenue supports "
                     "generous pay structure.",
                     32, "The patent portfolio funds a lot of good compensation."),
            Decision(2024, C.COMMUNICATION,
                     "Standard corporate communications",
                     "Restructuring framed as 'strategic realignment' to automotive, IoT, "
                     "and AI from mobile dependency.",
                     58, "The pivot narrative is real but also convenient cover for cuts."),
        ],
    )


def intuit() -> CompanyProfile:
    return CompanyProfile(
        name="Intuit", ticker="INTU", sector="Technology",
        period="2023–2025",
        decisions=[
            Decision(2024, C.WORKFORCE,
                     "1,800 layoffs while hiring AI roles",
                     "Cut ~10% of workforce and planned to rehire similar numbers "
                     "in AI-focused positions.",
                     72, "The swap: fire the people you have, hire people with different "
                     "skills. The severance doesn't make you an AI engineer."),
            Decision(2024, C.COMPENSATION,
                     "Strong tech compensation",
                     "Good pay and benefits, competitive in fintech space.",
                     30, "Well compensated workforce — until you're in the wrong skill bucket."),
            Decision(2024, C.COMMUNICATION,
                     "'AI-driven transformation' framing",
                     "Layoffs positioned as necessary to 'fuel the future of AI.' "
                     "Simultaneously celebrating AI capabilities and cutting people.",
                     68, "The future is funded by eliminating the present."),
        ],
    )


def servicenow() -> CompanyProfile:
    return CompanyProfile(
        name="ServiceNow", ticker="NOW", sector="Technology",
        period="2022–2025",
        decisions=[
            Decision(2024, C.WORKFORCE,
                     "Growth mode with minimal layoffs",
                     "Continued hiring while most enterprise software peers cut.",
                     22, "Growth companies get to be generous. The test comes later."),
            Decision(2024, C.COMPENSATION,
                     "Strong tech compensation",
                     "Competitive pay in enterprise SaaS. Good equity and benefits.",
                     25, "Among the better-compensated enterprise software companies."),
            Decision(2024, C.COMMUNICATION,
                     "Product-focused leadership communication",
                     "Bill McDermott's leadership focused on growth narrative.",
                     35, "Easier to communicate positively when you're growing."),
        ],
    )


def uber() -> CompanyProfile:
    return CompanyProfile(
        name="Uber", ticker="UBER", sector="Technology / Gig Economy",
        period="2020–2025",
        decisions=[
            Decision(2020, C.WORKFORCE,
                     "6,700 layoffs during pandemic",
                     "Cut 25% of workforce in two rounds as ride demand collapsed.",
                     75, "Genuine business crisis, but the speed and scale reflected "
                     "years of over-hiring for growth-at-all-costs."),
            Decision(2024, C.COMPENSATION,
                     "Corporate employees well-paid, drivers are not",
                     "Strong compensation for engineers and corporate staff. Drivers "
                     "earn below minimum wage after expenses in many markets.",
                     78, "The two-tier structure is the business model. Corporate thrives "
                     "because driver costs are externalized."),
            Decision(2023, C.CONDITIONS,
                     "Gig worker classification as independent contractors",
                     "Fought legislative efforts globally to classify drivers as employees, "
                     "which would require benefits, minimum wage, and protections.",
                     88, "The entire business model depends on not treating drivers as employees. "
                     "Every efficiency metric rests on externalized labor costs."),
            Decision(2023, C.COMMUNICATION,
                     "Khosrowshahi's improved tone from Kalanick era",
                     "More professional and measured than predecessor. But actions on "
                     "driver classification unchanged.",
                     55, "Better messaging, same model. The polish changed, the economics didn't."),
        ],
    )


def paypal() -> CompanyProfile:
    return CompanyProfile(
        name="PayPal", ticker="PYPL", sector="Technology / Fintech",
        period="2023–2025",
        decisions=[
            Decision(2024, C.WORKFORCE,
                     "2,500 layoffs — 9% of workforce",
                     "Cut ~2,500 employees in January 2024 under new CEO Alex Chriss.",
                     75, "New CEO cuts. Standard playbook: new leadership, reset expectations, "
                     "cut costs, claim credit for 'efficiency.'"),
            Decision(2023, C.WORKFORCE,
                     "2,000 layoffs in January 2023",
                     "Previous year's cuts under prior CEO Dan Schulman.",
                     72, "Two straight years of ~2,000+ cuts. At that point it's a trend."),
            Decision(2024, C.COMPENSATION,
                     "Competitive fintech compensation",
                     "Good pay for remaining employees, particularly engineering.",
                     35, "Standard fintech compensation for survivors."),
            Decision(2024, C.COMMUNICATION,
                     "CEO transition layoff narrative",
                     "New CEO framing cuts as 'right-sizing' to build 'the next chapter.'",
                     68, "Every CEO transition comes with a restructuring. The new person "
                     "needs their own baseline to beat."),
        ],
    )


def accenture() -> CompanyProfile:
    return CompanyProfile(
        name="Accenture", ticker="ACN", sector="Technology / Consulting",
        period="2023–2025",
        decisions=[
            Decision(2023, C.WORKFORCE,
                     "19,000 layoffs — ~2.5% of workforce",
                     "Cut 19,000 positions globally over 18 months. Large absolute "
                     "number but small percentage of 700K+ employee base.",
                     70, "The consulting model: utilization rates drop, people are 'on the bench,' "
                     "bench gets cleared."),
            Decision(2024, C.COMPENSATION,
                     "Variable consulting compensation model",
                     "Strong pay at senior levels, pressure on junior utilization. "
                     "Up-or-out culture standard for consulting.",
                     55, "You earn well if you're billing. If you're not billing, "
                     "you're a cost."),
            Decision(2024, C.CONDITIONS,
                     "Client-site work demands",
                     "Consulting lifestyle: travel, client demands, utilization pressure.",
                     62, "The work-life balance is the client's work-life balance, not yours."),
            Decision(2023, C.INVESTMENT,
                     "Significant AI and training investment",
                     "Major investment in employee AI training and upskilling programs.",
                     35, "Genuine reskilling investment. The business requires it — "
                     "consultants without current skills don't bill."),
        ],
    )


# ── Financial Services ────────────────────────────────────────────────

def goldman_sachs() -> CompanyProfile:
    return CompanyProfile(
        name="Goldman Sachs", ticker="GS", sector="Financial Services",
        period="2022–2025",
        decisions=[
            Decision(2023, C.WORKFORCE,
                     "3,200 layoffs in January 2023",
                     "Cut ~6.5% of workforce including partners. Annual 'strategic "
                     "resource assessments' are standard practice.",
                     72, "Goldman's annual culling is so routine it has a euphemism. "
                     "Performance-based, but the timing is budget-based."),
            Decision(2023, C.WORKFORCE,
                     "Marcus consumer banking retreat",
                     "Hundreds laid off as Goldman abandoned consumer banking after "
                     "losing billions on the initiative.",
                     78, "Leadership bet on consumer banking, lost billions, and the "
                     "employees who built it paid the price. Not the executives who chose it."),
            Decision(2023, C.COMPENSATION,
                     "Massive bonuses at top, competitive throughout",
                     "Partner and MD compensation among highest on Wall Street. "
                     "Junior banker pay competitive but below hours-adjusted rate.",
                     48, "If you survive, the money is extraordinary. The question is "
                     "whether the tradeoff is worth it."),
            Decision(2023, C.CONDITIONS,
                     "Notorious work hours",
                     "Junior bankers regularly work 80-100 hour weeks. 2021 survey "
                     "by first-year analysts went viral documenting the culture.",
                     82, "The hours are the product. Client service at this level means "
                     "human beings as a resource to be consumed."),
            Decision(2024, C.COMMUNICATION,
                     "David Solomon's leadership style",
                     "Direct and corporate. DJ Solomon persona sits oddly alongside "
                     "layoff announcements.",
                     55, "Professional communications, but the annual cull is so "
                     "normalized nobody calls it what it is."),
        ],
    )


def morgan_stanley() -> CompanyProfile:
    return CompanyProfile(
        name="Morgan Stanley", ticker="MS", sector="Financial Services",
        period="2022–2025",
        decisions=[
            Decision(2024, C.WORKFORCE,
                     "Regular year-end performance cuts",
                     "Standard ~2-3% annual performance-based layoffs.",
                     62, "Routine culling. Wall Street standard, but still people losing jobs."),
            Decision(2023, C.COMPENSATION,
                     "Top-tier for investment banking",
                     "Among highest-paying banks. Wealth management compensation also strong.",
                     38, "Pays well across divisions. Less of a two-tier problem than some peers."),
            Decision(2024, C.CONDITIONS,
                     "Standard Wall Street work expectations",
                     "Long hours in IB, more balanced in wealth management.",
                     65, "The hours-to-comp ratio is better than Goldman but still brutal in IB."),
            Decision(2023, C.COMMUNICATION,
                     "Professional, relatively direct leadership",
                     "Gorman-to-Pick transition was smooth. Communications are corporate "
                     "but substantive.",
                     42, "Less flashy than Goldman, more substance in communications."),
        ],
    )


def wells_fargo() -> CompanyProfile:
    return CompanyProfile(
        name="Wells Fargo", ticker="WFC", sector="Financial Services",
        period="2020–2025",
        decisions=[
            Decision(2023, C.WORKFORCE,
                     "Ongoing headcount reduction post-scandal",
                     "Continued workforce reduction as branches consolidate and the "
                     "company shrinks under Fed asset cap.",
                     72, "The employees paying for a scandal most of them had nothing to do with."),
            Decision(2020, C.CONDITIONS,
                     "Fake accounts scandal cultural fallout",
                     "Culture that pressured employees to open unauthorized accounts. "
                     "Employees who refused or reported were punished.",
                     90, "The textbook case of a system that destroyed employees who "
                     "followed their conscience and rewarded those who didn't."),
            Decision(2024, C.COMPENSATION,
                     "Moderate banking compensation",
                     "Competitive but not leading. Hard to recruit against JPMorgan.",
                     55, "Brand damage from scandal affects recruiting. Compensation "
                     "can't fully compensate for reputation."),
            Decision(2024, C.COMMUNICATION,
                     "Post-scandal corporate rehabilitation",
                     "Years of 'rebuilding trust' messaging. Heavy PR and compliance focus.",
                     68, "The communications are about rebuilding the brand. "
                     "The employees who were harmed by the scandal culture got settlements, not apologies."),
        ],
    )


def bank_of_america() -> CompanyProfile:
    return CompanyProfile(
        name="Bank of America", ticker="BAC", sector="Financial Services",
        period="2022–2025",
        decisions=[
            Decision(2024, C.WORKFORCE,
                     "Branch consolidation and role reduction",
                     "Ongoing reduction in branch staff as digital banking grows.",
                     62, "Technology-driven displacement. Rational but still costs jobs."),
            Decision(2023, C.COMPENSATION,
                     "$22/hr minimum and strong benefits",
                     "Raised minimum to $22/hr with plans for $25. Good benefits at all levels.",
                     30, "Among the best minimum wages in banking. Moynihan has made "
                     "this a visible priority."),
            Decision(2024, C.CONDITIONS,
                     "Moynihan's balanced leadership",
                     "Brian Moynihan's 'responsible growth' framework balances stakeholders "
                     "more visibly than peers.",
                     42, "More balanced than most bank CEOs. Actions generally match rhetoric."),
            Decision(2023, C.COMMUNICATION,
                     "Moderate corporate communication",
                     "Standard banking communications. Less flashy than Dimon, less "
                     "corporate than Wells Fargo post-scandal.",
                     48, "Steady and unremarkable. Which in banking communications "
                     "is actually fine."),
        ],
    )


def blackrock() -> CompanyProfile:
    return CompanyProfile(
        name="BlackRock", ticker="BLK", sector="Financial Services",
        period="2022–2025",
        decisions=[
            Decision(2023, C.WORKFORCE,
                     "~600 layoffs — 3% of workforce",
                     "Relatively small cuts compared to tech peers. Targeted restructuring.",
                     58, "Modest cuts. The asset management model doesn't require "
                     "large workforce swings."),
            Decision(2024, C.COMPENSATION,
                     "Competitive asset management pay",
                     "Strong compensation, particularly for portfolio and technology roles.",
                     32, "Pays well. AUM-based revenue supports generous compensation."),
            Decision(2024, C.COMMUNICATION,
                     "Larry Fink's annual letter — stakeholder capitalism to ESG retreat",
                     "Fink's letters championed stakeholder capitalism, then quietly "
                     "retreated under political pressure. Stopped using 'ESG' terminology.",
                     65, "Said the right things when it was popular. Backed off when "
                     "it became politically costly. The conviction was thinner than the letters suggested."),
        ],
    )


def visa() -> CompanyProfile:
    return CompanyProfile(
        name="Visa", ticker="V", sector="Financial Services",
        period="2022–2025",
        decisions=[
            Decision(2024, C.WORKFORCE,
                     "Relatively stable workforce",
                     "No major layoffs. Small restructuring. High revenue per employee.",
                     35, "The payments duopoly generates enough revenue to keep headcount stable."),
            Decision(2024, C.COMPENSATION,
                     "Excellent compensation and benefits",
                     "Strong pay, equity, and benefits across the organization.",
                     22, "Among the best-compensated workforces in fintech."),
            Decision(2023, C.CONDITIONS,
                     "Good work culture, hybrid flexibility",
                     "Generally positive workplace culture. Flexible hybrid arrangements.",
                     28, "When your margins are 65%, you can afford to treat people well."),
        ],
    )


def mastercard() -> CompanyProfile:
    return CompanyProfile(
        name="Mastercard", ticker="MA", sector="Financial Services",
        period="2022–2025",
        decisions=[
            Decision(2024, C.WORKFORCE,
                     "Stable workforce with targeted hiring",
                     "No major layoffs. Continued hiring in technology and data.",
                     32, "Similar to Visa: duopoly economics support workforce stability."),
            Decision(2024, C.COMPENSATION,
                     "Strong compensation package",
                     "Competitive pay and benefits. Good work-life balance reputation.",
                     25, "Consistently rated as a good employer. The economics support it."),
            Decision(2024, C.COMMUNICATION,
                     "Michael Miebach's measured leadership",
                     "Professional, measured communication. Less visibility than Dimon "
                     "or Fink but steady.",
                     35, "Unremarkable communications. In this context, that's a compliment."),
        ],
    )


def american_express() -> CompanyProfile:
    return CompanyProfile(
        name="American Express", ticker="AXP", sector="Financial Services",
        period="2022–2025",
        decisions=[
            Decision(2024, C.WORKFORCE,
                     "Relatively stable, selective hiring",
                     "No major layoffs. Some restructuring in smaller business units.",
                     38, "Premium brand requires premium service, which requires retaining people."),
            Decision(2024, C.COMPENSATION,
                     "Strong benefits and Blue Box values",
                     "Good compensation with genuine emphasis on employee culture. "
                     "Backed up by low turnover.",
                     28, "The culture talk is more substantiated than most. "
                     "Actions and retention data support it."),
            Decision(2024, C.CONDITIONS,
                     "Hybrid work with genuine flexibility",
                     "Amex Flex program gives employees choice. Not performative.",
                     30, "One of the more genuinely flexible large financial firms."),
        ],
    )


def progressive() -> CompanyProfile:
    return CompanyProfile(
        name="Progressive", ticker="PGR", sector="Financial Services / Insurance",
        period="2022–2025",
        decisions=[
            Decision(2024, C.WORKFORCE,
                     "Growth mode, expanding workforce",
                     "Continued hiring as market share grew. No significant layoffs.",
                     25, "Growth solves a lot of people problems."),
            Decision(2024, C.COMPENSATION,
                     "Competitive insurance industry pay",
                     "Good compensation relative to insurance peers. Claims adjusters "
                     "are better paid than industry average.",
                     35, "Pays above average for insurance but below tech."),
            Decision(2024, C.CONDITIONS,
                     "Data-driven culture, high expectations",
                     "Performance metrics are rigorous. Culture is meritocratic but intense.",
                     50, "Meritocracy sounds good until you're on the wrong side of the data."),
        ],
    )


def sp_global() -> CompanyProfile:
    return CompanyProfile(
        name="S&P Global", ticker="SPGI", sector="Financial Services / Data",
        period="2022–2025",
        decisions=[
            Decision(2022, C.WORKFORCE,
                     "Post-IHS Markit merger restructuring",
                     "Layoffs following the $44B merger. Overlapping roles eliminated.",
                     65, "Merger math: 1+1 must equal less than 2 in headcount."),
            Decision(2024, C.COMPENSATION,
                     "Strong data/analytics compensation",
                     "Competitive pay in financial data and analytics market.",
                     30, "Specialized workforce gets specialized compensation."),
            Decision(2024, C.CONDITIONS,
                     "Professional work environment",
                     "Generally positive culture. Data-focused, less of the Wall Street intensity.",
                     35, "Lower drama than investment banks. Higher stability."),
        ],
    )


# ── Healthcare ────────────────────────────────────────────────────────

def unitedhealth() -> CompanyProfile:
    return CompanyProfile(
        name="UnitedHealth Group", ticker="UNH", sector="Healthcare",
        period="2022–2025",
        decisions=[
            Decision(2024, C.WORKFORCE,
                     "Regular efficiency-driven cuts",
                     "Ongoing headcount optimization across Optum and UHC divisions.",
                     68, "The most profitable health insurer in America optimizing costs "
                     "while denying claims. The efficiency goes one direction."),
            Decision(2024, C.COMPENSATION,
                     "Good corporate pay, variable in operations",
                     "Strong compensation for corporate and Optum. Lower in claims processing.",
                     48, "Two-tier: the people processing your claim denial make a fraction "
                     "of the executives who designed the denial system."),
            Decision(2024, C.CONDITIONS,
                     "Aggressive claim denial practices",
                     "Documented patterns of prior authorization denials and claim rejections "
                     "as a business strategy. Employees tasked with implementing denials "
                     "report moral distress.",
                     88, "The business model requires employees to deny care for profit. "
                     "That's a working condition too."),
            Decision(2024, C.COMMUNICATION,
                     "Corporate healthcare speak",
                     "Heavy use of 'improving health outcomes' and 'value-based care' "
                     "language alongside record profits from claim management.",
                     78, "The gap between the language and the business model is "
                     "the widest of any company on this list."),
        ],
    )


def johnson_johnson() -> CompanyProfile:
    return CompanyProfile(
        name="Johnson & Johnson", ticker="JNJ", sector="Healthcare / Pharma",
        period="2022–2025",
        decisions=[
            Decision(2024, C.WORKFORCE,
                     "Kenvue spinoff and restructuring layoffs",
                     "Workforce reductions following consumer health spinoff. "
                     "Realignment of remaining pharmaceutical/medtech business.",
                     62, "Spinoffs always mean job losses. The people in the spun-off "
                     "entity often face a second round of cuts."),
            Decision(2024, C.COMPENSATION,
                     "Strong pharmaceutical compensation",
                     "Competitive pay and benefits. Good retirement and healthcare.",
                     32, "J&J's compensation has historically been a strength."),
            Decision(2023, C.CONDITIONS,
                     "Talc and opioid litigation legacy",
                     "Billions in litigation costs over talc-cancer claims and opioid "
                     "distribution. The Credo ('our first responsibility is to patients') "
                     "tested by decades of product safety questions.",
                     75, "The Credo is carved in stone in the lobby. The litigation "
                     "record raises questions about how deeply it's carved in the culture."),
            Decision(2023, C.COMMUNICATION,
                     "Credo-based communication vs litigation reality",
                     "J&J's communications lean heavily on the 1943 Credo. But legal "
                     "strategies (like the Texas Two-Step bankruptcy maneuver for talc) "
                     "undermine the message.",
                     68, "You can't invoke a credo about patients while using "
                     "bankruptcy loopholes to limit patient payouts."),
        ],
    )


def pfizer() -> CompanyProfile:
    return CompanyProfile(
        name="Pfizer", ticker="PFE", sector="Healthcare / Pharma",
        period="2022–2025",
        decisions=[
            Decision(2024, C.WORKFORCE,
                     "Significant layoffs as COVID revenue collapsed",
                     "Thousands cut as vaccine and Paxlovid revenue declined sharply. "
                     "Cost reduction program of $4B+ announced.",
                     78, "Hired massively for COVID, then cut when the revenue disappeared. "
                     "The surge workforce was always temporary — just nobody said so."),
            Decision(2024, C.COMPENSATION,
                     "Competitive pharmaceutical pay",
                     "Strong compensation for remaining employees. Good benefits.",
                     32, "Pharma pays well. The people who got cut lose that."),
            Decision(2024, C.COMMUNICATION,
                     "Bourla's post-COVID narrative",
                     "CEO Albert Bourla went from pandemic hero to cost-cutter. "
                     "Communications shifted from mission to efficiency rapidly.",
                     62, "The mission language lasted exactly as long as the revenue did."),
            Decision(2023, C.INVESTMENT,
                     "R&D investment maintained",
                     "Despite cost cuts, R&D spending remained substantial. Pipeline "
                     "investments continued.",
                     35, "Cutting people but not cutting R&D. The molecules matter more "
                     "than the workforce to the stock price."),
        ],
    )


def merck() -> CompanyProfile:
    return CompanyProfile(
        name="Merck", ticker="MRK", sector="Healthcare / Pharma",
        period="2022–2025",
        decisions=[
            Decision(2024, C.WORKFORCE,
                     "Regular pharmaceutical restructuring",
                     "Periodic workforce adjustments tied to pipeline and patent cycles.",
                     58, "Standard pharma: restructure around patent cliffs."),
            Decision(2024, C.COMPENSATION,
                     "Competitive pharma compensation",
                     "Good pay and benefits across the organization.",
                     32, "Solid pharmaceutical compensation."),
            Decision(2023, C.INVESTMENT,
                     "Significant R&D investment",
                     "R&D spending consistently high. Keytruda franchise funds reinvestment.",
                     28, "When you have a $25B drug, you can invest in R&D and people."),
            Decision(2024, C.COMMUNICATION,
                     "Professional pharmaceutical communications",
                     "Rob Davis's leadership is steady and professional. "
                     "Less drama than Pfizer's COVID narrative arc.",
                     40, "Boring is underrated in corporate communications."),
        ],
    )


def eli_lilly() -> CompanyProfile:
    return CompanyProfile(
        name="Eli Lilly", ticker="LLY", sector="Healthcare / Pharma",
        period="2022–2025",
        decisions=[
            Decision(2024, C.WORKFORCE,
                     "Hiring aggressively during Mounjaro/Zepbound boom",
                     "Adding thousands of manufacturing and R&D jobs. No significant layoffs.",
                     15, "When your market cap triples on a blockbuster drug, hiring is easy."),
            Decision(2024, C.COMPENSATION,
                     "Strong pharma compensation",
                     "Competitive pay. Stock appreciation has been extraordinary for employees.",
                     20, "Similar to NVIDIA: when the stock rockets, everyone benefits."),
            Decision(2024, C.CONDITIONS,
                     "Growth creates positive culture",
                     "Expansion mode. New facilities, new roles, optimism.",
                     22, "Growth is the best culture program. The question is what happens "
                     "when the growth-loss drug market matures."),
            Decision(2024, C.COMMUNICATION,
                     "Drug pricing controversy",
                     "Mounjaro/Zepbound list prices criticized as inaccessible. "
                     "Company's public defense focused on innovation costs.",
                     70, "Making a drug that changes lives and pricing it so many "
                     "can't afford it is a choice. The communication justifies it. "
                     "The patients hear something different."),
        ],
    )


def abbvie() -> CompanyProfile:
    return CompanyProfile(
        name="AbbVie", ticker="ABBV", sector="Healthcare / Pharma",
        period="2022–2025",
        decisions=[
            Decision(2024, C.WORKFORCE,
                     "Post-Humira patent cliff restructuring",
                     "Workforce adjustments as Humira biosimilar competition arrived.",
                     65, "Built a company on one drug. When the patent expired, "
                     "the restructuring was inevitable."),
            Decision(2024, C.COMPENSATION,
                     "Good pharmaceutical compensation",
                     "Competitive pay and benefits for pharma.",
                     35, "Standard pharma compensation."),
            Decision(2023, C.COMMUNICATION,
                     "Drug pricing defense amid record revenue",
                     "Years of Humira price increases defended as supporting innovation. "
                     "Humira's US price tripled over its life.",
                     72, "Raised the price of one drug for 20 years and called it innovation funding."),
        ],
    )


def amgen() -> CompanyProfile:
    return CompanyProfile(
        name="Amgen", ticker="AMGN", sector="Healthcare / Biotech",
        period="2023–2025",
        decisions=[
            Decision(2024, C.WORKFORCE,
                     "Post-Horizon Therapeutics acquisition layoffs",
                     "Layoffs following $28B acquisition. Overlapping roles eliminated.",
                     70, "Acquisition-driven cuts. Same pattern: buy company, cut overlap."),
            Decision(2024, C.COMPENSATION,
                     "Strong biotech compensation",
                     "Competitive pay in biotech. Good benefits and research culture.",
                     30, "Biotech compensation is generally strong."),
            Decision(2024, C.COMMUNICATION,
                     "Standard pharma restructuring language",
                     "Integration and efficiency framing around post-acquisition cuts.",
                     60, "The merger press release says 'synergies.' The employees hear 'layoffs.'"),
        ],
    )


def cvs_health() -> CompanyProfile:
    return CompanyProfile(
        name="CVS Health", ticker="CVS", sector="Healthcare / Retail",
        period="2022–2025",
        decisions=[
            Decision(2024, C.WORKFORCE,
                     "~5,000 layoffs across the company",
                     "Major cuts in corporate and management roles. Pharmacies understaffed.",
                     75, "Cutting corporate while pharmacies are already understaffed. "
                     "The savings come from everywhere except where more people are needed."),
            Decision(2024, C.CONDITIONS,
                     "Pharmacy staff burnout well-documented",
                     "Pharmacists consistently report unsustainable workloads, unsafe "
                     "conditions, and pressure to fill prescriptions faster than is safe.",
                     85, "Pharmacists filling 400+ prescriptions per day with inadequate "
                     "staffing. Patient safety concerns documented by pharmacists themselves."),
            Decision(2024, C.COMPENSATION,
                     "Pharmacist pay not matching workload",
                     "Pharmacist compensation hasn't kept pace with dramatically increased "
                     "responsibilities (vaccines, testing, counseling) and workload.",
                     68, "Added scope of practice. Didn't add staff or proportional pay."),
            Decision(2024, C.COMMUNICATION,
                     "Patient care rhetoric vs staffing reality",
                     "'Our purpose is bringing our heart to every moment of your health' "
                     "says the company understaffing its pharmacies.",
                     78, "The mission statement and the staffing model are in direct conflict."),
        ],
    )


def cigna() -> CompanyProfile:
    return CompanyProfile(
        name="Cigna", ticker="CI", sector="Healthcare / Insurance",
        period="2022–2025",
        decisions=[
            Decision(2024, C.WORKFORCE,
                     "Efficiency-driven workforce optimization",
                     "Regular headcount management across Evernorth and insurance divisions.",
                     65, "Standard insurance industry optimization."),
            Decision(2024, C.COMPENSATION,
                     "Competitive healthcare compensation",
                     "Good pay for corporate and clinical roles.",
                     38, "Competitive in the healthcare insurance space."),
            Decision(2024, C.CONDITIONS,
                     "Claim review pressure and denial practices",
                     "Similar to UNH — documented patterns of claim denial as business "
                     "practice. Employees implement denial systems.",
                     82, "The health insurance business model requires people to say no "
                     "to other people's healthcare."),
            Decision(2024, C.COMMUNICATION,
                     "Health and wellness messaging",
                     "Corporate communications focused on 'whole person health' while "
                     "business metrics focus on medical loss ratios.",
                     72, "Medical loss ratio: the metric that counts paying for your "
                     "healthcare as a 'loss.'"),
        ],
    )


def elevance() -> CompanyProfile:
    return CompanyProfile(
        name="Elevance Health", ticker="ELV", sector="Healthcare / Insurance",
        period="2022–2025",
        decisions=[
            Decision(2024, C.WORKFORCE,
                     "Regular restructuring",
                     "Ongoing workforce adjustments. Moderate cuts.",
                     62, "Standard insurance industry headcount management."),
            Decision(2024, C.COMPENSATION,
                     "Competitive insurance compensation",
                     "Good pay and benefits in the managed care space.",
                     38, "Competitive for the sector."),
            Decision(2024, C.COMMUNICATION,
                     "Name change from Anthem to Elevance",
                     "Rebranded to 'Elevance Health' — a name designed to sound "
                     "like it means something while meaning nothing specific.",
                     70, "When you change your name to a made-up word, you're managing "
                     "perception, not improving care."),
        ],
    )


def medtronic() -> CompanyProfile:
    return CompanyProfile(
        name="Medtronic", ticker="MDT", sector="Healthcare / Medical Devices",
        period="2022–2025",
        decisions=[
            Decision(2024, C.WORKFORCE,
                     "Restructuring under new leadership",
                     "Layoffs under CEO Geoff Martha's transformation plan.",
                     62, "Medical device restructuring follows a different cycle than pharma "
                     "but the same pattern."),
            Decision(2024, C.COMPENSATION,
                     "Good medtech compensation",
                     "Competitive in medical device industry. Strong benefits.",
                     32, "Solid compensation for the sector."),
            Decision(2023, C.INVESTMENT,
                     "R&D and engineer development",
                     "Continued investment in engineering talent and medical innovation.",
                     30, "Medtech companies need engineers. Investment follows necessity."),
        ],
    )


# ── Consumer / Retail ─────────────────────────────────────────────────

def procter_gamble() -> CompanyProfile:
    return CompanyProfile(
        name="Procter & Gamble", ticker="PG", sector="Consumer Goods",
        period="2022–2025",
        decisions=[
            Decision(2024, C.WORKFORCE,
                     "Ongoing productivity programs",
                     "Continuous efficiency initiatives. Regular role elimination through "
                     "'productivity improvement' programs.",
                     62, "P&G has been optimizing for decades. The programs are permanent. "
                     "The people are not."),
            Decision(2024, C.COMPENSATION,
                     "Good consumer goods compensation",
                     "Competitive for CPG. Strong brand management career path.",
                     35, "P&G is a talent machine. It pays well and trains well — for those inside."),
            Decision(2023, C.CONDITIONS,
                     "Demanding brand management culture",
                     "High expectations, up-or-out in brand management. Intense but "
                     "respected training ground.",
                     48, "You'll work hard and learn a lot. Then leave for a CMO role elsewhere. "
                     "P&G is a school that charges tuition in years."),
            Decision(2023, C.COMMUNICATION,
                     "Corporate speak with brand polish",
                     "Everything is a brand at P&G, including internal communications.",
                     58, "Even the layoff memo would have a brand brief."),
        ],
    )


def coca_cola() -> CompanyProfile:
    return CompanyProfile(
        name="Coca-Cola", ticker="KO", sector="Consumer Goods / Beverages",
        period="2020–2025",
        decisions=[
            Decision(2020, C.WORKFORCE,
                     "2,200 layoffs — 'emerging stronger'",
                     "Cut ~2,200 employees globally during pandemic restructuring. "
                     "Called it 'emerging stronger.'",
                     72, "Pandemic as cover for restructuring that was likely coming anyway. "
                     "'Emerging stronger' is corporate for 'with fewer of you.'"),
            Decision(2024, C.COMPENSATION,
                     "Good compensation for corporate roles",
                     "Competitive CPG compensation. Strong Atlanta HQ benefits.",
                     35, "Good employer for corporate staff."),
            Decision(2023, C.CONDITIONS,
                     "Bottler workforce conditions vary",
                     "Coca-Cola's franchise/bottler model means most production workers "
                     "are employed by bottling partners, not Coca-Cola itself.",
                     58, "The franchise model lets Coke report a small, well-treated workforce "
                     "while the actual production labor works for someone else."),
            Decision(2023, C.COMMUNICATION,
                     "Heavy brand management culture in everything",
                     "Even internal communications feel like ad campaigns. "
                     "Everything is on-brand, on-message.",
                     62, "When your company IS a brand, everything gets the brand treatment. "
                     "Including the difficult stuff that shouldn't be polished."),
        ],
    )


def pepsico() -> CompanyProfile:
    return CompanyProfile(
        name="PepsiCo", ticker="PEP", sector="Consumer Goods / Beverages",
        period="2022–2025",
        decisions=[
            Decision(2024, C.WORKFORCE,
                     "Restructuring and efficiency programs",
                     "Ongoing workforce optimization across snacks and beverages divisions.",
                     60, "Standard CPG efficiency. Frito-Lay operations are labor-intensive."),
            Decision(2023, C.CONDITIONS,
                     "Frito-Lay warehouse working conditions",
                     "Reports of mandatory overtime, 84-hour weeks at some facilities. "
                     "2021 strike by Topeka workers over conditions.",
                     75, "The snacks get delivered because warehouse workers push through "
                     "brutal schedules. That's not on the Doritos bag."),
            Decision(2024, C.COMPENSATION,
                     "Variable across divisions",
                     "Corporate well-compensated. Operations and warehouse workers "
                     "face pay-hours imbalance.",
                     55, "Two companies in one: corporate PepsiCo and warehouse PepsiCo."),
            Decision(2023, C.COMMUNICATION,
                     "Standard CPG corporate messaging",
                     "Purpose-driven language ('positive choices') alongside aggressive "
                     "cost management.",
                     58, "The purpose statement and the warehouse schedule exist in parallel universes."),
        ],
    )


def mcdonalds() -> CompanyProfile:
    return CompanyProfile(
        name="McDonald's", ticker="MCD", sector="Consumer / Food Service",
        period="2022–2025",
        decisions=[
            Decision(2023, C.WORKFORCE,
                     "Corporate layoffs and franchise model labor externalization",
                     "Laid off hundreds of corporate employees while franchise model "
                     "means 2M+ restaurant workers aren't McDonald's employees at all.",
                     78, "The franchise model is the ultimate labor cost externalization. "
                     "McDonald's sets the prices, the hours, the standards — but the workers "
                     "are someone else's problem."),
            Decision(2024, C.COMPENSATION,
                     "Corporate well-paid, franchise workers near minimum",
                     "Corporate and HQ roles are well compensated. Franchise restaurant "
                     "workers often earn minimum wage or just above.",
                     80, "The people making the food that drives the stock price are "
                     "the lowest-paid workers in the system."),
            Decision(2023, C.CONDITIONS,
                     "Franchise worker conditions vary widely",
                     "No standard for franchise worker conditions. Heat, safety, "
                     "scheduling practices all franchise-dependent.",
                     72, "McDonald's controls the brand but not the working conditions. "
                     "Convenient."),
            Decision(2022, C.INVESTMENT,
                     "Archways to Opportunity education program",
                     "Tuition assistance and education programs for restaurant workers.",
                     35, "Genuine program, good intent. Doesn't address the core compensation gap."),
            Decision(2024, C.COMMUNICATION,
                     "Brand messaging vs labor reality",
                     "Marketing emphasizes community and people. Labor practices "
                     "are handled at franchise level, kept at arm's length.",
                     70, "The brand is warm. The business model is cold."),
        ],
    )


def disney() -> CompanyProfile:
    return CompanyProfile(
        name="Disney", ticker="DIS", sector="Consumer / Entertainment",
        period="2022–2025",
        decisions=[
            Decision(2023, C.WORKFORCE,
                     "7,000+ layoffs under Iger's return",
                     "Bob Iger returned as CEO and cut ~7,000 positions as part of "
                     "cost-cutting following Chapek era.",
                     75, "The returning hero's first act: mass layoffs. Framed as "
                     "fixing Chapek's mistakes, but 7,000 people paid for it."),
            Decision(2024, C.COMPENSATION,
                     "Executive pay vs theme park worker gap",
                     "Executive compensation in tens of millions. Theme park workers "
                     "earning $15-20/hr in Orlando, where housing costs have soared.",
                     78, "Cast members create the magic. They can't afford to live near "
                     "the parks where they perform it."),
            Decision(2023, C.CONDITIONS,
                     "Theme park worker housing crisis",
                     "Disney World workers in Orlando report inability to afford housing. "
                     "Some living in cars or with multiple roommates.",
                     75, "The happiest place on earth for guests. Not for the people "
                     "who make it happy."),
            Decision(2023, C.COMMUNICATION,
                     "'Disney magic' language masking labor reality",
                     "Workers are 'cast members.' Jobs are 'roles.' The language of "
                     "performance applied to labor that barely pays rent.",
                     72, "Calling someone a cast member instead of a worker doesn't "
                     "change their paycheck."),
            Decision(2023, C.INVESTMENT,
                     "Disney Aspire education program",
                     "Tuition-free education for hourly employees at select schools.",
                     32, "Good program. Helps people leave Disney for better-paying jobs. "
                     "Which says something about Disney's own pay."),
        ],
    )


def starbucks() -> CompanyProfile:
    return CompanyProfile(
        name="Starbucks", ticker="SBUX", sector="Consumer / Food Service",
        period="2022–2025",
        decisions=[
            Decision(2024, C.WORKFORCE,
                     "Corporate layoffs under Brian Niccol",
                     "New CEO cut corporate headcount. Store-level labor remains tight.",
                     65, "Every new CEO restructures. Niccol brought Chipotle's efficiency focus."),
            Decision(2024, C.CONDITIONS,
                     "Union suppression documented by NLRB",
                     "Multiple NLRB findings against Starbucks for unfair labor practices "
                     "during unionization drives. Store closures in union-active areas.",
                     85, "The company that calls workers 'partners' fought harder against "
                     "actual partnership (unions) than almost any other retailer."),
            Decision(2023, C.COMPENSATION,
                     "Benefits for part-timers including healthcare and tuition",
                     "Healthcare, stock grants, and tuition coverage for part-time workers. "
                     "A genuine differentiator in food service.",
                     25, "Among the best benefit packages in food service. Real and meaningful."),
            Decision(2023, C.COMMUNICATION,
                     "'Partners' language vs anti-union actions",
                     "Calls every employee a 'partner' while actively fighting the one "
                     "structure that would make them actual partners in decisions.",
                     75, "Partner: noun — a person who shares in the decisions and outcomes. "
                     "Unless they unionize, in which case, not that kind of partner."),
        ],
    )


def home_depot() -> CompanyProfile:
    return CompanyProfile(
        name="Home Depot", ticker="HD", sector="Consumer / Retail",
        period="2022–2025",
        decisions=[
            Decision(2024, C.WORKFORCE,
                     "Relatively stable workforce",
                     "No major layoffs. Store staffing adjustments are ongoing but gradual.",
                     38, "More stable than most retailers."),
            Decision(2024, C.COMPENSATION,
                     "Above-average retail compensation",
                     "Starting wages above most home improvement competitors. "
                     "Good benefits for full-time.",
                     35, "Invests in store associates more than the retail average."),
            Decision(2023, C.CONDITIONS,
                     "Investment in associate experience",
                     "Technology investments to reduce manual work. Generally positive "
                     "store culture.",
                     32, "Associates report better conditions than many retail peers."),
            Decision(2023, C.INVESTMENT,
                     "Training and internal mobility programs",
                     "Structured training for associates. Internal promotion pipeline.",
                     28, "Good development programs for retail."),
        ],
    )


def nike() -> CompanyProfile:
    return CompanyProfile(
        name="Nike", ticker="NKE", sector="Consumer / Apparel",
        period="2022–2025",
        decisions=[
            Decision(2024, C.WORKFORCE,
                     "~1,600 layoffs — 2% of workforce",
                     "Cut ~2% of corporate workforce as part of $2B cost savings plan.",
                     68, "Cost cutting at a company with 45% gross margins. The savings "
                     "aren't for survival — they're for EPS."),
            Decision(2024, C.COMPENSATION,
                     "Strong corporate compensation",
                     "Good pay at Beaverton HQ. Global supply chain is a different story.",
                     52, "HQ is a great place to work. The factories that make the shoes "
                     "are someone else's problem — by design."),
            Decision(2023, C.CONDITIONS,
                     "Global supply chain labor practices",
                     "Decades of supply chain labor scrutiny. Improved from the '90s but "
                     "structural tensions remain between margin targets and factory conditions.",
                     72, "Better than 1997. Still a model where margin pressure flows "
                     "downhill to the workers with the least leverage."),
            Decision(2023, C.COMMUNICATION,
                     "'Just Do It' brand vs supply chain reality",
                     "Inspirational brand messaging alongside supply chain labor tensions.",
                     65, "The brand sells aspiration. The supply chain runs on margin pressure."),
        ],
    )


def target() -> CompanyProfile:
    return CompanyProfile(
        name="Target", ticker="TGT", sector="Consumer / Retail",
        period="2022–2025",
        decisions=[
            Decision(2024, C.WORKFORCE,
                     "Some restructuring, generally stable",
                     "Headquarters restructuring but store workforce relatively stable.",
                     48, "More stable than most retailers."),
            Decision(2024, C.COMPENSATION,
                     "$15-24/hr starting wage range",
                     "Competitive retail wages. Full benefits for eligible employees.",
                     35, "Decent retail compensation. Trails Costco but leads many peers."),
            Decision(2025, C.COMMUNICATION,
                     "DEI program rollback",
                     "Ended DEI goals, Racial Equity Action and Change committee, "
                     "and three-year diversity initiatives under political pressure.",
                     68, "Programs built over years, abandoned under external pressure. "
                     "The commitment lasted until it became commercially inconvenient."),
            Decision(2023, C.CONDITIONS,
                     "Generally positive retail environment",
                     "Store team member experience rated above average for big-box retail.",
                     38, "Better than most, not as good as Costco."),
        ],
    )


def tjx() -> CompanyProfile:
    return CompanyProfile(
        name="TJX Companies", ticker="TJX", sector="Consumer / Retail",
        period="2022–2025",
        decisions=[
            Decision(2024, C.WORKFORCE,
                     "Stable workforce, growth mode",
                     "TJ Maxx/Marshalls expanding store count. Net hiring.",
                     30, "Growth in off-price retail while traditional retail contracts."),
            Decision(2024, C.COMPENSATION,
                     "Average retail compensation",
                     "Competitive for off-price retail. Not industry-leading.",
                     48, "Average pay, average benefits. Not terrible, not exceptional."),
            Decision(2024, C.CONDITIONS,
                     "Standard retail conditions",
                     "Store conditions comparable to retail peers.",
                     45, "Middle of the pack for retail working conditions."),
        ],
    )


def colgate() -> CompanyProfile:
    return CompanyProfile(
        name="Colgate-Palmolive", ticker="CL", sector="Consumer Goods",
        period="2022–2025",
        decisions=[
            Decision(2024, C.WORKFORCE,
                     "Modest restructuring programs",
                     "Regular efficiency programs, smaller scale than P&G.",
                     55, "Standard CPG optimization. Smaller company, smaller cuts."),
            Decision(2024, C.COMPENSATION,
                     "Good CPG compensation",
                     "Competitive for consumer goods. Good global benefits.",
                     35, "Standard strong CPG compensation."),
            Decision(2023, C.CONDITIONS,
                     "Stable, professional culture",
                     "Less intense than P&G but similar model.",
                     40, "Steady employer in CPG."),
        ],
    )


def kraft_heinz() -> CompanyProfile:
    return CompanyProfile(
        name="Kraft Heinz", ticker="KHC", sector="Consumer Goods / Food",
        period="2022–2025",
        decisions=[
            Decision(2024, C.WORKFORCE,
                     "Post-merger efficiency culture",
                     "3G Capital's zero-based budgeting approach means constant headcount "
                     "scrutiny. Every role must be rejustified annually.",
                     78, "Zero-based budgeting applied to people. You exist until the "
                     "spreadsheet says you don't."),
            Decision(2024, C.COMPENSATION,
                     "Cost-conscious compensation",
                     "Pay is competitive but the zero-based culture means perks, travel, "
                     "and discretionary spending are minimal.",
                     60, "You get paid. You don't get much else."),
            Decision(2023, C.CONDITIONS,
                     "High-pressure cost culture",
                     "3G Capital's influence created a culture obsessed with cost cutting. "
                     "High turnover at management levels.",
                     75, "The culture IS the cost pressure. Everything else follows."),
        ],
    )


def kroger() -> CompanyProfile:
    return CompanyProfile(
        name="Kroger", ticker="KR", sector="Consumer / Grocery",
        period="2022–2025",
        decisions=[
            Decision(2024, C.WORKFORCE,
                     "Albertsons merger attempt and workforce uncertainty",
                     "Proposed $24.6B Albertsons merger created years of workforce "
                     "uncertainty. FTC blocked it.",
                     62, "Years of uncertainty for employees at both companies while "
                     "executives pursued a deal regulators would block."),
            Decision(2024, C.COMPENSATION,
                     "Average grocery wages",
                     "Wages improved but still below living wage in many markets. "
                     "Union presence supports some wage floors.",
                     55, "Better than non-union grocery but still tight margins for workers."),
            Decision(2023, C.CONDITIONS,
                     "Union relationships across locations",
                     "Unionized workforce in many markets. Relationship with UFCW varies.",
                     45, "Union presence provides some counterweight. Doesn't solve "
                     "the structural low-margin problem."),
        ],
    )


def mondelez() -> CompanyProfile:
    return CompanyProfile(
        name="Mondelez", ticker="MDLZ", sector="Consumer Goods / Food",
        period="2022–2025",
        decisions=[
            Decision(2024, C.WORKFORCE,
                     "Regular restructuring programs",
                     "Ongoing efficiency programs in the Kraft-style tradition.",
                     65, "Cost discipline is the culture. Same 3G Capital DNA as Kraft Heinz."),
            Decision(2024, C.COMPENSATION,
                     "Average CPG compensation",
                     "Competitive but not leading in consumer goods.",
                     45, "Middle of the pack for consumer goods."),
            Decision(2021, C.CONDITIONS,
                     "Portland factory strike",
                     "Workers at Portland Nabisco plant struck over proposed cuts to "
                     "overtime pay and benefits. 12-hour shifts at issue.",
                     72, "When Oreo factory workers strike, the issue is usually real."),
        ],
    )


def philip_morris() -> CompanyProfile:
    return CompanyProfile(
        name="Philip Morris", ticker="PM", sector="Consumer Goods / Tobacco",
        period="2022–2025",
        decisions=[
            Decision(2024, C.WORKFORCE,
                     "Transition workforce from cigarettes to alternatives",
                     "Restructuring around IQOS and smoke-free products. Traditional "
                     "cigarette roles shrinking.",
                     62, "The business is pivoting. The workforce pivots too, willingly or not."),
            Decision(2024, C.COMPENSATION,
                     "Good compensation for the sector",
                     "Tobacco companies pay well — partly because recruiting is harder "
                     "for an industry many find ethically challenging.",
                     35, "The ethics premium: pay more because fewer people want the job."),
            Decision(2023, C.COMMUNICATION,
                     "'Smoke-free future' messaging",
                     "Corporate communications centered on 'delivering a smoke-free future' "
                     "while still selling billions of cigarettes.",
                     72, "Building a smoke-free future while the present is very much on fire."),
        ],
    )


# ── Industrial / Defense / Energy ─────────────────────────────────────

def boeing() -> CompanyProfile:
    return CompanyProfile(
        name="Boeing", ticker="BA", sector="Industrial / Aerospace",
        period="2020–2025",
        decisions=[
            Decision(2024, C.WORKFORCE,
                     "17,000+ layoffs — ~10% of workforce",
                     "Massive cuts announced by new CEO Kelly Ortberg following years of "
                     "safety crisis, production problems, and strike.",
                     82, "Cutting the workforce that builds the planes after the planes "
                     "started failing. The causation arrow might go the wrong direction."),
            Decision(2024, C.CONDITIONS,
                     "737 MAX crisis and quality culture collapse",
                     "Two fatal crashes (346 deaths), door plug blowout, and systematic "
                     "quality failures traced to cost-cutting culture that prioritized "
                     "production speed over engineering standards.",
                     95, "The most consequential profit-over-people decision on this list. "
                     "People died. The culture that enabled it was built over years of "
                     "choosing financial targets over engineering discipline."),
            Decision(2024, C.CONDITIONS,
                     "Whistleblower retaliation allegations",
                     "Multiple whistleblowers reported retaliation for raising safety "
                     "concerns. Two died under unclear circumstances during litigation.",
                     90, "When the people raising safety concerns face more consequences "
                     "than the people ignoring them, the culture is broken."),
            Decision(2024, C.COMMUNICATION,
                     "Safety rhetoric vs documented reality",
                     "Repeated statements about safety being 'the top priority' alongside "
                     "documented evidence that production schedules consistently overrode "
                     "quality processes.",
                     88, "Saying safety is number one while every internal incentive rewards "
                     "schedule. The rhetoric and the metrics point in opposite directions."),
            Decision(2024, C.COMPENSATION,
                     "Engineering pay competitive but declining",
                     "Pay has become less competitive as Boeing's reputation suffered. "
                     "Hard to recruit against Lockheed, SpaceX, defense primes.",
                     58, "When your planes are falling apart publicly, recruiting engineers "
                     "requires paying a reputation premium."),
        ],
    )


def general_electric() -> CompanyProfile:
    return CompanyProfile(
        name="General Electric", ticker="GE", sector="Industrial / Conglomerate",
        period="2020–2025",
        decisions=[
            Decision(2023, C.WORKFORCE,
                     "Split into three companies with workforce reductions",
                     "Broke into GE Aerospace, GE Vernova (energy), and GE HealthCare. "
                     "Each entity restructured its workforce post-split.",
                     72, "Decades of empire-building undone. The people who built the "
                     "conglomerate pay for the decision to unbuild it."),
            Decision(2024, C.COMPENSATION,
                     "Variable by entity post-split",
                     "GE Aerospace compensation strong. Other entities variable.",
                     45, "Your compensation depends on which piece of the breakup you landed in."),
            Decision(2023, C.COMMUNICATION,
                     "Transformation narrative across decades",
                     "GE has been 'transforming' since Welch. Immelt transformed. "
                     "Flannery transformed. Culp transformed. Now three companies transform.",
                     68, "The only constant is the word 'transformation.' And the layoffs that accompany it."),
        ],
    )


def caterpillar() -> CompanyProfile:
    return CompanyProfile(
        name="Caterpillar", ticker="CAT", sector="Industrial / Manufacturing",
        period="2022–2025",
        decisions=[
            Decision(2024, C.WORKFORCE,
                     "Cyclical workforce adjustments",
                     "Manufacturing headcount tied to construction and mining cycles.",
                     55, "Cyclical business means cyclical employment. Workers understand this "
                     "but understanding doesn't pay the mortgage."),
            Decision(2024, C.COMPENSATION,
                     "Strong manufacturing compensation",
                     "Good wages for skilled manufacturing. UAW presence in some facilities.",
                     32, "Well-paying manufacturing jobs. The kind people say don't exist anymore."),
            Decision(2023, C.CONDITIONS,
                     "Union relationships and safety",
                     "Generally constructive union relationship. Safety record average "
                     "for heavy manufacturing.",
                     42, "Heavy equipment manufacturing is inherently dangerous. "
                     "Caterpillar's record is middling."),
        ],
    )


def honeywell() -> CompanyProfile:
    return CompanyProfile(
        name="Honeywell", ticker="HON", sector="Industrial / Technology",
        period="2022–2025",
        decisions=[
            Decision(2024, C.WORKFORCE,
                     "Regular restructuring and planned breakup",
                     "Ongoing efficiency programs. Announced plan to split into multiple companies.",
                     65, "Another conglomerate breaking up. Another workforce wondering "
                     "which piece they end up in."),
            Decision(2024, C.COMPENSATION,
                     "Competitive industrial/tech compensation",
                     "Good pay for engineering and technology roles.",
                     35, "Competitive in the industrial technology space."),
            Decision(2024, C.COMMUNICATION,
                     "Portfolio optimization language",
                     "Breakup framed as 'unlocking value' and 'sharpening focus.'",
                     60, "Unlocking value: financial speak for 'the stock price will be "
                     "higher if we cut you loose.'"),
        ],
    )


def lockheed_martin() -> CompanyProfile:
    return CompanyProfile(
        name="Lockheed Martin", ticker="LMT", sector="Industrial / Defense",
        period="2022–2025",
        decisions=[
            Decision(2024, C.WORKFORCE,
                     "Relatively stable defense workforce",
                     "Defense demand supports workforce stability. Some contract-dependent fluctuation.",
                     32, "When your customer is the US government with a $886B defense budget, "
                     "layoffs are less necessary."),
            Decision(2024, C.COMPENSATION,
                     "Strong defense industry compensation",
                     "Good pay, excellent benefits, strong retirement. Security clearance "
                     "creates employee retention.",
                     25, "Defense pays well and the benefits are genuinely good. "
                     "Clearances create golden handcuffs."),
            Decision(2023, C.CONDITIONS,
                     "Engineering-focused culture",
                     "Generally positive engineering work environment. Mission-driven "
                     "workforce in many divisions.",
                     30, "People who build satellites tend to feel purpose. "
                     "The moral questions about what some products do are a different matter."),
        ],
    )


def three_m() -> CompanyProfile:
    return CompanyProfile(
        name="3M", ticker="MMM", sector="Industrial / Manufacturing",
        period="2022–2025",
        decisions=[
            Decision(2023, C.WORKFORCE,
                     "6,000 layoffs amid litigation crisis",
                     "Cut ~6,000 positions while facing billions in PFAS and earplug litigation.",
                     78, "Employees losing jobs while the company pays for decades of "
                     "decisions made by leadership long gone."),
            Decision(2024, C.CONDITIONS,
                     "PFAS 'forever chemicals' legacy",
                     "Decades of PFAS contamination now requiring massive remediation. "
                     "Workers and communities affected by chemicals the company knew were harmful.",
                     88, "Knew the chemicals were harmful. Kept making them. The settlements "
                     "are in billions. The health effects are permanent."),
            Decision(2024, C.COMPENSATION,
                     "Good manufacturing/engineering pay",
                     "Competitive compensation for those who remain. Benefits reduced "
                     "from historical levels.",
                     42, "Compensation eroding as litigation costs consume capital."),
            Decision(2024, C.COMMUNICATION,
                     "Litigation defense alongside responsibility claims",
                     "Simultaneously claiming to 'take responsibility' for PFAS while "
                     "aggressively litigating to minimize payouts.",
                     78, "Taking responsibility while minimizing the amount of responsibility "
                     "you actually take."),
        ],
    )


def union_pacific() -> CompanyProfile:
    return CompanyProfile(
        name="Union Pacific", ticker="UNP", sector="Industrial / Railroad",
        period="2020–2025",
        decisions=[
            Decision(2022, C.WORKFORCE,
                     "Precision Scheduled Railroading workforce cuts",
                     "PSR implementation cut ~30% of workforce over several years. "
                     "Trains run on tighter schedules with fewer people.",
                     85, "PSR: an operating model designed by hedge fund managers that treats "
                     "rail workers as the primary variable to optimize."),
            Decision(2022, C.CONDITIONS,
                     "Rail worker conditions and near-strike",
                     "Workers pushed to brink of strike over scheduling, sick days, and "
                     "quality of life. Congress imposed a contract.",
                     82, "Workers couldn't even get sick days without threatening a national "
                     "strike. Congress stepped in — on the company's side."),
            Decision(2024, C.COMPENSATION,
                     "Strong union wages but schedule problems",
                     "Good hourly pay. But on-call scheduling and attendance policies "
                     "make the life difficult regardless of pay.",
                     52, "The pay is good. The life isn't. Money doesn't buy back the "
                     "holidays you missed because of on-call scheduling."),
            Decision(2023, C.COMMUNICATION,
                     "Safety and efficiency messaging",
                     "Corporate communications emphasize safety and efficiency. "
                     "Workers describe a culture where efficiency consistently wins.",
                     70, "The safety report looks different from HQ than it does from the rail yard."),
        ],
    )


def fedex() -> CompanyProfile:
    return CompanyProfile(
        name="FedEx", ticker="FDX", sector="Industrial / Logistics",
        period="2022–2025",
        decisions=[
            Decision(2024, C.WORKFORCE,
                     "DRIVE program — billions in cost cuts",
                     "Multi-year cost reduction program targeting $4B in savings. "
                     "Thousands of positions eliminated through consolidation.",
                     75, "DRIVE: another cost program with an action-verb name that "
                     "sounds dynamic and means layoffs."),
            Decision(2024, C.COMPENSATION,
                     "Variable: corporate vs operations",
                     "Good corporate compensation. Drivers and package handlers "
                     "face more pressure on pay-to-workload ratio.",
                     58, "Two-tier model: the people moving the packages vs the people "
                     "managing the people who move the packages."),
            Decision(2023, C.CONDITIONS,
                     "Driver workload and gig-ification",
                     "Ground delivery increasingly handled by independent contractors "
                     "and subcontractors rather than FedEx employees.",
                     72, "The Uber-ification of package delivery. Same truck, same uniform, "
                     "fewer protections."),
        ],
    )


def deere() -> CompanyProfile:
    return CompanyProfile(
        name="Deere & Company", ticker="DE", sector="Industrial / Agriculture",
        period="2021–2025",
        decisions=[
            Decision(2024, C.WORKFORCE,
                     "Layoffs during agricultural downturn",
                     "Hundreds laid off as ag equipment demand softened.",
                     62, "Cyclical business, cyclical cuts."),
            Decision(2021, C.CONDITIONS,
                     "UAW strike over two-tier wages",
                     "10,000 workers struck for six weeks over a contract that created "
                     "lower pay tiers for new hires.",
                     72, "The two-tier system: pay the new people less for the same work. "
                     "Workers rejected it twice before the company improved the offer."),
            Decision(2024, C.COMPENSATION,
                     "Strong post-strike compensation",
                     "Improved wages after strike. Good manufacturing pay with benefits.",
                     35, "The wages are good now — because workers struck to make them good."),
            Decision(2024, C.COMMUNICATION,
                     "Right-to-repair fight",
                     "Fought farmers' ability to repair their own equipment, protecting "
                     "revenue from dealer service.",
                     68, "When the product is designed so only you can fix it, that's "
                     "not quality control — it's revenue control."),
        ],
    )


def raytheon() -> CompanyProfile:
    return CompanyProfile(
        name="RTX (Raytheon)", ticker="RTX", sector="Industrial / Defense",
        period="2022–2025",
        decisions=[
            Decision(2024, C.WORKFORCE,
                     "Restructuring post-Pratt & Whitney engine recall",
                     "Workforce adjustments following costly engine inspection requirements.",
                     60, "Quality failures cost jobs downstream."),
            Decision(2024, C.COMPENSATION,
                     "Strong defense compensation",
                     "Competitive defense industry pay and benefits.",
                     30, "Defense compensation is consistently good."),
            Decision(2024, C.CONDITIONS,
                     "Engineering quality pressure",
                     "Pratt & Whitney quality issues created pressure on engineers "
                     "to simultaneously fix problems and maintain production.",
                     55, "When the engine has problems, the people fixing it face "
                     "the schedule pressure."),
        ],
    )


def northrop_grumman() -> CompanyProfile:
    return CompanyProfile(
        name="Northrop Grumman", ticker="NOC", sector="Industrial / Defense",
        period="2022–2025",
        decisions=[
            Decision(2024, C.WORKFORCE,
                     "Stable defense workforce",
                     "Strong demand from B-21 and space programs supports headcount.",
                     28, "When you're building the next stealth bomber, you're hiring, not cutting."),
            Decision(2024, C.COMPENSATION,
                     "Good defense industry pay",
                     "Competitive compensation with strong benefits and retirement.",
                     28, "Standard strong defense compensation."),
            Decision(2024, C.INVESTMENT,
                     "Engineering pipeline investment",
                     "University partnerships and intern programs to build talent pipeline.",
                     25, "Defense needs engineers. Investment in pipeline is business necessity and genuine."),
        ],
    )


def exxonmobil() -> CompanyProfile:
    return CompanyProfile(
        name="ExxonMobil", ticker="XOM", sector="Energy",
        period="2020–2025",
        decisions=[
            Decision(2020, C.WORKFORCE,
                     "14,000 global layoffs during pandemic",
                     "Cut ~15% of workforce during oil price collapse.",
                     75, "Oil crash required cuts, but the scale reflected years of "
                     "overextension. Recovery profits didn't bring the jobs back."),
            Decision(2024, C.CONDITIONS,
                     "Climate denial legacy and energy transition",
                     "Decades of documented climate science denial while internal research "
                     "confirmed risks. Now framing as 'energy transition leader.'",
                     85, "Knew about climate change in the 1980s. Funded denial for decades. "
                     "Now marketing the transition."),
            Decision(2024, C.COMPENSATION,
                     "Strong energy sector compensation",
                     "Good pay across engineering, operations, and corporate roles.",
                     30, "Oil majors pay well. The ethical premium works the other way — "
                     "you need to pay people to work for your reputation."),
            Decision(2024, C.COMMUNICATION,
                     "'Advancing climate solutions' messaging",
                     "Marketing emphasizes carbon capture and clean energy investment. "
                     "Capital allocation still heavily weighted to fossil fuels.",
                     75, "Spending millions on 'we're part of the solution' ads "
                     "while spending billions on oil extraction."),
        ],
    )


def chevron() -> CompanyProfile:
    return CompanyProfile(
        name="Chevron", ticker="CVX", sector="Energy",
        period="2020–2025",
        decisions=[
            Decision(2020, C.WORKFORCE,
                     "~6,000 layoffs during oil downturn",
                     "Pandemic-era cuts as oil demand collapsed.",
                     72, "Oil industry cyclicality. Workers bear the cycle."),
            Decision(2024, C.COMPENSATION,
                     "Competitive energy compensation",
                     "Good pay for engineering and field operations. Strong benefits.",
                     32, "Standard strong energy sector compensation."),
            Decision(2024, C.CONDITIONS,
                     "Refinery and field safety",
                     "Safety record mixed — better than some peers, ongoing risks "
                     "inherent to the industry.",
                     55, "Oil industry safety is always a tension between speed and caution."),
            Decision(2024, C.COMMUNICATION,
                     "Energy transition framing similar to Exxon",
                     "Invested in 'lower carbon' messaging while core business remains fossil fuels.",
                     70, "'Lower carbon' is doing a lot of work in that sentence."),
        ],
    )


def conocophillips() -> CompanyProfile:
    return CompanyProfile(
        name="ConocoPhillips", ticker="COP", sector="Energy",
        period="2020–2025",
        decisions=[
            Decision(2020, C.WORKFORCE,
                     "Pandemic-era workforce reductions",
                     "Reduced workforce during oil price collapse.",
                     70, "Same oil industry pattern."),
            Decision(2024, C.COMPENSATION,
                     "Competitive E&P compensation",
                     "Strong pay for exploration and production sector.",
                     32, "Good pay in the upstream oil business."),
            Decision(2024, C.COMMUNICATION,
                     "Standard energy industry messaging",
                     "Focus on energy security and 'responsible resource development.'",
                     62, "Responsible resource development: extracting fossil fuels, responsibly."),
        ],
    )


# ── Other ─────────────────────────────────────────────────────────────

def berkshire_hathaway() -> CompanyProfile:
    return CompanyProfile(
        name="Berkshire Hathaway", ticker="BRK", sector="Conglomerate",
        period="2022–2025",
        decisions=[
            Decision(2024, C.WORKFORCE,
                     "Minimal corporate overhead, subsidiaries independent",
                     "~30 person HQ. Subsidiaries manage their own workforce decisions. "
                     "No centralized layoff programs.",
                     40, "Berkshire is uniquely hands-off. The decentralization is real. "
                     "Subsidiary treatment varies enormously."),
            Decision(2024, C.COMPENSATION,
                     "Varies entirely by subsidiary",
                     "GEICO, BNSF, Dairy Queen, See's Candies — all completely different "
                     "compensation structures.",
                     48, "No single compensation philosophy. Each subsidiary is its own world."),
            Decision(2024, C.COMMUNICATION,
                     "Buffett's legendary transparency",
                     "Annual letters are masterclasses in honest communication. "
                     "Admits mistakes, explains decisions, never uses jargon.",
                     12, "If every CEO communicated like Buffett, Candor wouldn't need to exist."),
            Decision(2024, C.CONDITIONS,
                     "BNSF rail worker conditions mirror industry",
                     "Railroad subsidiary faces same PSR and scheduling issues as Union Pacific.",
                     65, "Buffett's honesty doesn't reach the rail yards. BNSF workers "
                     "face the same conditions as every other Class I railroad."),
        ],
    )


def t_mobile() -> CompanyProfile:
    return CompanyProfile(
        name="T-Mobile", ticker="TMUS", sector="Telecom",
        period="2022–2025",
        decisions=[
            Decision(2023, C.WORKFORCE,
                     "5,000 layoffs post-Sprint merger",
                     "Cut ~7% of workforce as Sprint integration created redundancies.",
                     72, "Merger math: promise regulators you'll create jobs, "
                     "then cut 5,000 once the deal closes."),
            Decision(2024, C.COMPENSATION,
                     "Competitive telecom compensation",
                     "Good pay for the telecom sector. Retail workers above carrier average.",
                     38, "Better than AT&T and Verizon on retail compensation."),
            Decision(2023, C.COMMUNICATION,
                     "Un-carrier brand vs corporate reality",
                     "The 'un-carrier' marketing positioned T-Mobile as the anti-corporate carrier. "
                     "Post-merger behavior is standard corporate.",
                     60, "The un-carrier is now the biggest carrier. Turns out the brand was more "
                     "un-carrier than the company."),
        ],
    )


def general_motors() -> CompanyProfile:
    return CompanyProfile(
        name="General Motors", ticker="GM", sector="Automotive",
        period="2022–2025",
        decisions=[
            Decision(2023, C.WORKFORCE,
                     "UAW strike — 46 days",
                     "46-day strike by 46,000 UAW workers over wages, benefits, and "
                     "temporary worker conversion. Ended with significant worker gains.",
                     65, "The strike worked. Workers got 25% raises over 4.5 years, "
                     "faster temp-to-permanent conversion, and COLA restored. "
                     "But they had to walk out for 46 days to get it."),
            Decision(2024, C.COMPENSATION,
                     "Post-strike improved compensation",
                     "25% raises, restored COLA, improved benefits from new UAW contract.",
                     32, "Strong compensation now — because workers struck for it."),
            Decision(2024, C.CONDITIONS,
                     "EV transition workforce uncertainty",
                     "Scaling back EV commitments creates uncertainty for workers at "
                     "EV-focused plants. Shifting back toward hybrids and ICE.",
                     62, "Workers retrained for EV production now wondering if the "
                     "company is retreating from the plan they retrained for."),
            Decision(2024, C.COMMUNICATION,
                     "Mixed messaging on EV commitment",
                     "Initially all-in on EV. Then pulling back. Workers and investors "
                     "both uncertain about actual direction.",
                     60, "Hard to plan your career around a corporate strategy that "
                     "changes with the quarterly earnings call."),
        ],
    )


def ford() -> CompanyProfile:
    return CompanyProfile(
        name="Ford", ticker="F", sector="Automotive",
        period="2022–2025",
        decisions=[
            Decision(2023, C.WORKFORCE,
                     "UAW strike and restructuring",
                     "Similar to GM — 46-day strike, significant concessions. Plus "
                     "separate white-collar cuts as part of efficiency push.",
                     65, "Blue-collar workers got what they struck for. White-collar "
                     "workers got restructured."),
            Decision(2024, C.WORKFORCE,
                     "EV division layoffs",
                     "Ford Model e (EV division) losing billions. Cuts in EV workforce "
                     "as company recalibrates.",
                     72, "Asked workers to bet on EVs. Now cutting the EV workforce "
                     "while the bet plays out."),
            Decision(2024, C.COMPENSATION,
                     "Post-strike union wages, competitive corporate",
                     "UAW members got strong raises. Corporate compensation competitive "
                     "for Detroit.",
                     35, "The union contract is good. Again, because they struck for it."),
            Decision(2024, C.COMMUNICATION,
                     "Jim Farley's direct communication style",
                     "Farley is more direct than most auto CEOs. Acknowledges challenges openly.",
                     40, "Earns some credit for honesty about the EV losses. "
                     "Doesn't change the uncertainty for workers."),
        ],
    )

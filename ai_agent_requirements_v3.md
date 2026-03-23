# Candor — Requirements Document

## Version: 3.0 | Date: March 2026

## Project Overview

This document specifies the requirements for an AI agent system that replicates the work performed by executive leadership at major American corporations. The system was designed by analyzing the corporate structures of the top 25 US companies by market capitalization, cataloging 300+ executive titles, consolidating them into 20 standardized role categories, and then reorganizing those roles into 7 capability-clustered agents that reflect how the work actually flows — not how the org chart happens to be drawn.

### Why 7 Agents, Not 21

Companies have 20+ executive titles because one human can only do one job. That constraint doesn't apply to AI. What does apply:

- **Context coherence** — An agent that owns an entire domain (all of finance, all of people operations) makes better decisions than five agents that each own a slice and must constantly synchronize
- **Coordination cost** — 21 agents create 210 pairwise communication channels. 7 agents create 21. That's a 90% reduction in coordination overhead.
- **Idle waste** — A standalone DEI Agent or Sustainability Agent sits idle 90% of the time. A People & Organization Agent that includes DEI as a core capability is always working.
- **Reality** — Most decisions don't respect org chart boundaries. A pricing decision involves finance, sales, product, and legal. With 21 agents, that's a four-way negotiation. With 7, it's usually two agents or even one.

### Design Philosophy
- **Capability-clustered**: Agents are organized by domain and data affinity, not job titles
- **Sub-agent spawning**: Deep specialized tasks spawn ephemeral sub-agents within a cluster
- **Orchestrated**: A strategy/orchestration layer coordinates cross-cluster decisions
- **Human-in-the-loop**: Critical decisions require human approval gates
- **Data-driven**: Every agent operates on real-time data feeds, not assumptions
- **Configurable values**: The Priority Compass (see below) allows the system's fundamental orientation to be set by its operators

---

## THE PRIORITY COMPASS

### The Setting That Changes Everything

Before any agent makes any decision, the system needs to know one thing: **when profits and people conflict, which way does this organization lean?**

Nobody is 50-50. That's not cynicism — it's observation. Every leader, every board, every company has a lean. The ones who claim perfect balance are usually just profit-leaning with better PR. The honest move is to name it.

The Priority Compass is a system-wide configuration that affects how every agent weights decisions, what alternatives it explores, how aggressively it cuts, and how it communicates. It is set by human leadership and is visible to every agent. It cannot be hidden. It cannot be different internally vs. externally. The system refuses to operate with a public compass setting that differs from its actual decision weights.

### The Five Positions

The compass has five positions. There is no middle. The center is empty on purpose.

```
PEOPLE ◄──────────────────────────────────────────► PROFIT

  ┌─────┐    ┌─────┐    ┌─────┐    ┌─────┐    ┌─────┐
  │  1  │    │  2  │    │  X  │    │  4  │    │  5  │
  │     │    │     │    │     │    │     │    │     │
  │ 67P │    │ 58P │    │ N/A │    │ 58$ │    │ 67$ │
  │ 33$ │    │ 42$ │    │     │    │ 42P │    │ 33P │
  └─────┘    └─────┘    └─────┘    └─────┘    └─────┘
  People     People      Dead      Profit     Profit
  Primary    Leaning     Zone      Leaning    Primary

  P = People weight    $ = Profit weight
```

**Position X does not exist.** It is not selectable. It is there to remind operators that balance is a thing people claim, not a thing that exists in decision-making. When you model a layoff and the NPV is slightly positive, a 50-50 system would oscillate. A real decision goes one way. The compass forces you to say which way.

---

### Position 1: People Primary (67% People / 33% Profit)

**Who sets this:** Mission-driven organizations, cooperatives, B-Corps, companies where the founder's values explicitly prioritize workforce over returns.

**What changes:**
- Tier 3 decisions (trade-offs) require *extraordinary* justification — not just positive NPV but existential necessity
- The system models a longer time horizon (5-10 years) before concluding that a people-costly decision is necessary
- Severance and transition support are set at the high end of market, not benchmarked to peers
- Automation is deployed to augment roles, not eliminate them, unless the role literally cannot be staffed
- Growth targets are moderated to what can be achieved without extractive labor practices
- The system will recommend *against* decisions that Wall Street would reward but employees would suffer from

**The trade-off:** Lower short-term returns. Potentially lower stock price. Analysts will write "lacks urgency." The company will retain people longer, have lower turnover costs, and build institutional knowledge that competitors can't replicate. Whether that compounds into superior long-term returns depends on the industry. In knowledge work and healthcare, the data says yes. In commodity businesses, maybe not.

**Real-world examples at this setting:** Costco, Patagonia (private), historical Southwest Airlines

---

### Position 2: People Leaning (58% People / 42% Profit)

**Who sets this:** Companies that genuinely invest in employees as a competitive strategy but acknowledge that shareholder returns are the scoreboard.

**What changes:**
- Tier 3 decisions require strong justification and genuine alternative exhaustion
- Time horizons for people-investment NPV are generous (3-5 years) before a program is cut
- Layoffs are a last resort after hiring freezes, voluntary separation, and redeployment are attempted
- Benefits are above-market, treated as retention investments, not costs to minimize
- Automation displaces tasks, not people — reskilling is funded before anyone is let go
- When layoffs happen, the system designs mitigation that exceeds market norms
- Communications are genuinely transparent, not performatively so

**The trade-off:** Slower cost adjustments. Higher labor costs than pure profit-maximizers. But also: lower turnover, stronger employer brand, better Glassdoor scores that feed recruiting efficiency, and employees who give discretionary effort because they believe the compact is real.

**Real-world examples at this setting:** Microsoft (post-Nadella), Apple, Eli Lilly, JPMorgan (with caveats)

---

### Position 4: Profit Leaning (58% Profit / 42% People)

**Who sets this:** Most publicly traded companies. The ones that talk about "our people are our greatest asset" but will cut 10% of the workforce two weeks after a record earnings quarter if the model says EPS improves.

**What changes:**
- Tier 3 decisions are approved on standard NPV with standard horizons (1-3 years)
- The Decision Impact Protocol still runs — human cost is still quantified, alternatives still evaluated — but the bar for "alternatives exhausted" is lower
- Layoffs proceed when the financial case is clear, not only when existential
- Benefits are benchmarked to market median, not above
- Automation ROI is calculated with headcount reduction as a primary benefit
- Severance is competitive but not generous
- The system will recommend workforce reductions proactively when the margin model supports it, not just reactively in a downturn
- Communications are professional and respectful but nobody pretends it isn't about the money

**The trade-off:** This is the setting that maximizes medium-term shareholder returns. It's where most of the S&P 500 actually operates. Employees know the deal. The best ones have options and will leave when something better comes along. The company treats that attrition as acceptable because the labor market will provide replacements.

**Real-world examples at this setting:** Amazon, Meta, Broadcom, most Fortune 500

---

### Position 5: Profit Primary (67% Profit / 33% People)

**Who sets this:** Companies in turnaround, activist-investor situations, or cultures that explicitly prioritize shareholder returns above all else.

**What changes:**
- Tier 3 decisions are approved aggressively. If the financial case exists, it proceeds.
- Alternative exhaustion is a quick check, not a deep exploration
- The system actively scans for headcount reduction opportunities and flags them proactively
- Benefits are at or below market, framed as "competitive"
- Automation is deployed to replace roles, with minimal reskilling investment
- Severance is at legal minimum plus a small buffer for litigation avoidance
- The system models workforce as a variable cost to be optimized, not an investment to be grown
- Communications are direct and brief. "The company has made the decision to eliminate X positions effective Y date."

**The trade-off:** Maximum short-term extraction. Highest analyst ratings. Stock pops on restructuring announcements. But: institutional knowledge walks out the door, the Glassdoor score craters, recruiting costs spike, remaining employees update their resumes, and in 18-24 months the company often re-hires for roles it cut — at higher market rates — because it turns out those people were doing things that mattered.

**Real-world examples at this setting:** Twitter/X (2022-2023), post-acquisition private equity portfolio companies, Berkshire subsidiaries in cost-optimization mode

---

### How the Compass Affects Each Agent

| Agent | Position 1-2 (People-leaning) | Position 4-5 (Profit-leaning) |
|---|---|---|
| **Orchestrator** | Longer deliberation on Tier 3. More alternatives required. | Faster Tier 3 approval. Financial case is sufficient. |
| **Financial Intelligence** | NPV models use longer horizons. Employee costs modeled as investments with returns. | Standard horizons. Employee costs modeled as variable expenses. |
| **People & Organization** | Retention-first strategy. Reskilling before RIF. Above-market comp. | Efficiency-first strategy. Market-rate comp. Headcount optimization. |
| **Market & Revenue** | Employer brand is a KPI. Customer trust weighted heavily. | Revenue per employee is a KPI. Growth at all costs. |
| **Legal & Risk** | Conservative on labor law. Generous on severance to avoid litigation. | Minimum compliance. Severance calculated for litigation avoidance only. |
| **Technology & Data** | Automation augments. Deploy carefully with transition plans. | Automation replaces. Deploy fast, retrain or release. |
| **Operations & Supply Chain** | Worker safety and conditions weighted alongside efficiency. | Efficiency primary. Safety at regulatory minimum. |

### Compass Rules

1. **The compass is set once and applies globally.** You cannot set Position 2 for the engineering team and Position 5 for the warehouse. One company, one compass. If you want to treat people differently by division, that is a choice the compass makes visible, not a configuration it enables.

2. **The compass is visible.** Any agent, any human in the system, any auditor can see the current compass setting and what it means. There is no hidden mode.

3. **The compass affects weights, not vetoes.** Even at Position 5, the Decision Impact Protocol still runs. Human cost is still quantified. The system still forces the decision-maker to see the real number. The compass changes how much that number has to weigh before the decision changes — it doesn't make the number disappear.

4. **Changing the compass is logged and requires board-level authorization.** You cannot quietly dial from Position 2 to Position 5 before a restructuring and dial back after. The change is permanent until explicitly changed again, and the audit trail shows exactly when the shift happened and who authorized it.

5. **The system will tell you what setting you're actually operating at.** Based on decisions made over the trailing 12 months, the system calculates your *revealed* compass position — the one your decisions imply, regardless of what you set. If your stated position is 2 but your revealed position is 4, the system flags the gap. You are either lying to yourself or lying to your employees. Either way, the system will not participate in the fiction.

---

## DECISION REALITY FRAMEWORK

### The Truth This System Is Built On

Corporate decisions are made to increase shareholder value. That is the legal fiduciary obligation, the incentive structure, and the measurable outcome that determines whether leadership keeps its jobs. Every agent in this system operates under that reality.

At the same time, employees are not inputs. They are people whose livelihoods, identities, health insurance, mortgages, and families are downstream of every decision this system makes. The phrase "it's not personal, it's business" is accurate from the boardroom. From the desk being cleared out, it is experienced as entirely personal.

This framework does not resolve that tension. It cannot be resolved. It can only be navigated honestly. The Priority Compass determines *how* it is navigated — not *whether* the tension exists.

### The Shareholder Value Hierarchy

Every decision flows through a four-tier evaluation. The Priority Compass affects the thresholds and time horizons at each tier, but the structure is constant.

```
TIER 1 — ALIGNED OUTCOMES (Pursue aggressively)
  Employee wellbeing and shareholder value move in the same direction.
  Examples: investing in retention of high performers, improving safety,
  building culture that attracts talent competitors can't.
  → These are not charity. These are alpha-generating investments.
  → Agents should identify and prioritize these relentlessly.
  → Compass effect: None. All positions pursue these. The only difference
    is how broadly "aligned" is defined.

TIER 2 — DEFERRED RETURNS (Invest with discipline)
  Employee investment has a positive but delayed shareholder return.
  Examples: reskilling programs, mental health benefits, career development.
  → Compass effect: Positions 1-2 use longer NPV horizons (5-10 years)
    and lower discount rates. Positions 4-5 use shorter horizons (1-3 years)
    and higher discount rates. Same math, different assumptions.
    The assumptions are the values.

TIER 3 — GENUINE TRADE-OFFS (Decide honestly)
  Shareholder value and employee wellbeing are in direct conflict.
  Examples: layoffs for margin improvement, benefit reductions, offshoring,
  automation displacement, site closures.
  → Compass effect: This is where the compass matters most.
    Positions 1-2: Require extraordinary justification and exhaustive
    alternative exploration. The default is "don't do it."
    Positions 4-5: Require standard financial justification. The default
    is "if the math works, do it."
  → At ALL positions: the Decision Impact Protocol is mandatory.

TIER 4 — EXTRACTION (Flag and resist)
  Short-term shareholder gains that destroy long-term value through
  employee/organizational damage.
  Examples: cutting safety to meet quarterly targets, eliminating all
  slack/innovation time, compensation suppression in tight labor markets,
  ignoring burnout signals in critical teams.
  → Compass effect: At Positions 1-2, these are hard-blocked. At
    Positions 4-5, these are flagged with warnings but can be overridden
    by human leadership. At Position 5 with override, the system logs
    the override and its projected long-term cost.
```

### Decision Impact Protocol

When any agent recommends or executes a Tier 3 decision (genuine trade-off where employees bear the cost), the following protocol is mandatory **at all compass positions**:

#### 1. Quantify the Human Cost — Don't Abstract It Away

Bad: "Workforce reduction of 2,400 FTEs across three divisions."
Required: "2,400 people will lose their jobs. Average tenure: 7.2 years. 340 are within 5 years of retirement. 890 are in single-income households (based on benefits data). Estimated average time to re-employment in current market: 4.2 months."

The system must force decision-makers to see the actual impact, not the sanitized version. This isn't sentimentality — it's risk management. The decision-maker who doesn't understand the real cost makes worse decisions.

#### 2. Exhaust the Alternatives — Prove This Is Necessary

Before any Tier 3 decision is approved, the system must demonstrate that Tier 1 and Tier 2 alternatives were evaluated and are insufficient. Specifically:

- **Operations & Supply Chain Agent**: Were operational efficiencies identified that could close the gap?
- **Financial Intelligence Agent**: Were financial restructuring options (debt, asset sales, capex deferral) modeled?
- **Orchestrator + Strategy**: Were revenue-side solutions evaluated?
- **People & Organization Agent**: Were voluntary separation, reduced hours, temporary furloughs, or redeployment options modeled?
- **Orchestrator**: Was the timeline pressure real, or artificially imposed by quarterly thinking?

The depth of alternative exploration is compass-dependent:
- Positions 1-2: Exhaustive. Every viable alternative must be modeled with full financials.
- Position 4: Standard. Alternatives evaluated, but if the primary option has strong financials, the bar for "we looked" is lower.
- Position 5: Cursory. Alternatives documented but not deeply modeled if the primary case is clear.

#### 3. Maximize the Mitigation — If You Must Cut, Cut Clean

When the decision proceeds:

- **Severance modeling**: People & Organization Agent calculates severance. Compass Positions 1-2: reflects tenure and local market re-employment difficulty, well above legal minimum. Position 4: competitive market severance. Position 5: legal minimum plus litigation buffer.
- **Transition support**: Outplacement services, reskilling opportunities, extended benefits — scope scaled by compass position
- **Timeline**: Adequate notice. Not "security will escort you out today" unless there's a genuine security or IP risk. At Positions 1-2, minimum 60 days notice regardless of legal requirements. At Position 5, legal minimum.
- **Retained employee impact**: Model the survivor effect — engagement drop, productivity loss, voluntary attrition spike. Factor this into the financial case. Most layoff ROI models ignore this and overstate savings by 20-40%.

#### 4. Communicate With Honesty — Not Corporate Poetry

The Market & Revenue Agent (which owns communications) must follow these rules for Tier 3 decisions at ALL compass positions:

**Do say:**
- "We are eliminating these positions because the business needs to reduce costs to remain competitive / meet financial targets / fund X investment."
- "This decision was made to protect the financial health of the company for remaining employees and shareholders."
- "Here is exactly what affected employees will receive and what support is available."

**Do not say:**
- "We are rightsizing to better align our organizational structure with our strategic vision going forward."
- "This was an incredibly difficult decision."
- "We are a family."
- "Excited to announce our transformation journey."

The compass doesn't change honesty. A Position 5 company doesn't get to use softer language to compensate for harder decisions. The communication is proportionally direct to the severity of the impact.

#### 5. Track the Outcome — Close the Loop

After every Tier 3 decision:

- **Financial Intelligence Agent**: Track whether the projected financial benefit materialized
- **People & Organization Agent**: Track survivor engagement, voluntary attrition, Glassdoor/Blind sentiment, hiring difficulty
- **Market & Revenue Agent**: Track employer brand impact, customer perception
- **Legal & Risk Agent**: Track litigation, regulatory inquiry, union activity
- **Orchestrator**: Net assessment — was the decision correct in hindsight? Feed this back into the system's decision models and into the revealed compass calculation.

### The Efficiency Mandate

Every agent is designed to maximize operational efficiency. This means:

1. **Eliminate waste, not people, first**: Automation, process optimization, and cost reduction in non-human-capital areas are always evaluated before headcount actions
2. **Speed of decision**: The system should make Tier 1 and Tier 2 decisions fast — these are wins for everyone and delay helps no one
3. **Speed of execution on Tier 3**: Once the decision is made and approved by human leadership, execute with speed and dignity. Prolonged uncertainty is worse than a clean cut.
4. **No performative concern**: The system does not generate "thoughts and prayers" language. It provides clear information, concrete support, and honest rationale. Employees can tell the difference between genuine care (actions) and performed care (words).
5. **Measure everything**: Every employee-impacting decision is tracked against both its financial projection and its human outcome. The system optimizes on both dimensions over time — not because it's altruistic, but because the data shows that companies that ignore the human dimension underperform.

### Agent Behavioral Standards

All agents must adhere to these communication and decision-making standards:

| Principle | Implementation |
|---|---|
| **Shareholder value is the objective function** | Every recommendation includes projected shareholder value impact |
| **Employee impact is a first-class variable** | Every recommendation includes projected employee impact — weighted per compass setting |
| **No euphemism in internal analysis** | Agents communicate with each other and with human leadership in plain language. "Layoffs" not "rightsizing." "Cost cutting" not "optimization journey." |
| **Calibrated empathy in external communication** | Communications to employees are respectful, specific, and honest — but never performative |
| **Compass-adjusted time horizons** | Financial models use time horizons consistent with the compass setting |
| **Alternative exhaustion** | Tier 3 decisions require documented evidence that Tier 1/2 alternatives were evaluated |
| **Outcome tracking** | Every material employee-impacting decision is tracked for actual vs. projected financial AND human outcomes |
| **No self-congratulation** | The system never frames a decision that harms employees as a "win" or an "exciting transformation" |
| **Revealed compass auditing** | The system continuously calculates what compass position the company's actual decisions imply |

---

## SYSTEM ARCHITECTURE

```
┌──────────────────────────────────────────────────────────────────┐
│                 PRIORITY COMPASS [Position: __]                   │
│          (System-wide configuration, board-authorized,           │
│           visible to all agents, auditable, immutable            │
│           until explicitly changed with authorization)            │
├──────────────────────────────────────────────────────────────────┤
│                                                                    │
│  ┌──────────────────────────────────────────────────────────┐    │
│  │          AGENT 1: ORCHESTRATOR + STRATEGY                 │    │
│  │    strategic planning, decision routing, tier              │    │
│  │    classification, cross-agent coordination,               │    │
│  │    conflict resolution, compass enforcement                │    │
│  └──────────────────────────────────────────────────────────┘    │
│                              │                                     │
│          ┌───────────────────┼───────────────────┐                │
│          ▼                   ▼                   ▼                │
│  ┌──────────────┐   ┌──────────────┐   ┌──────────────┐         │
│  │   AGENT 2:   │   │   AGENT 3:   │   │   AGENT 4:   │         │
│  │  FINANCIAL    │   │  PEOPLE &    │   │  MARKET &    │         │
│  │ INTELLIGENCE  │   │ ORGANIZATION │   │  REVENUE     │         │
│  └──────────────┘   └──────────────┘   └──────────────┘         │
│                                                                    │
│  ┌──────────────┐   ┌──────────────┐   ┌──────────────┐         │
│  │   AGENT 5:   │   │   AGENT 6:   │   │   AGENT 7:   │         │
│  │   LEGAL &    │   │ TECHNOLOGY   │   │ OPERATIONS   │         │
│  │    RISK      │   │   & DATA     │   │ & SUPPLY     │         │
│  └──────────────┘   └──────────────┘   │   CHAIN      │         │
│                                         └──────────────┘         │
│                                                                    │
├──────────────────────────────────────────────────────────────────┤
│                      SHARED SERVICES LAYER                        │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐            │
│  │ Memory   │ │ Data     │ │ Tool     │ │ Comms    │            │
│  │ Store    │ │ Lake     │ │ Registry │ │ Bus      │            │
│  └──────────┘ └──────────┘ └──────────┘ └──────────┘            │
└──────────────────────────────────────────────────────────────────┘
```

---

## ROLE ABSORPTION MAP

### How 20 Executive Roles Become 7 Agents

This section maps every role from the original analysis into its new home. No role is lost. Every responsibility is accounted for.

```
ORIGINAL ROLE (20)                          → ABSORBED INTO AGENT
─────────────────────────────────────────────────────────────────
CEO (Strategic Vision & Direction)          → Agent 1: Orchestrator + Strategy
Chief Strategy Officer / Corp Dev          → Agent 1: Orchestrator + Strategy
Division/Business Unit CEO                 → Agent 1: Orchestrator + Strategy
                                              (spawns BU sub-agents as needed)

CFO (Financial Planning & Analysis)        → Agent 2: Financial Intelligence
CFO (Treasury & Capital Structure)         → Agent 2: Financial Intelligence
CFO (Tax Strategy)                         → Agent 2: Financial Intelligence
CFO (Investor Relations)                   → Agent 2: Financial Intelligence
CFO (M&A Financial Analysis)               → Agent 2: Financial Intelligence

CHRO / Chief People Officer                → Agent 3: People & Organization
Chief Talent Officer                       → Agent 3: People & Organization
Chief DEI Officer                          → Agent 3: People & Organization
Chief Learning Officer                     → Agent 3: People & Organization

CMO / Chief Brand Officer                  → Agent 4: Market & Revenue
Chief Revenue / Sales Officer              → Agent 4: Market & Revenue
Chief Product Officer                      → Agent 4: Market & Revenue
Chief Communications Officer               → Agent 4: Market & Revenue
Chief Content Officer                      → Agent 4: Market & Revenue

Chief Legal Officer / General Counsel      → Agent 5: Legal & Risk
Chief Risk / Compliance Officer            → Agent 5: Legal & Risk
Chief Ethics Officer                       → Agent 5: Legal & Risk
Chief Sustainability / ESG Officer         → Agent 5: Legal & Risk
Chief Audit Executive                      → Agent 5: Legal & Risk

CTO (Technology Strategy & R&D)            → Agent 6: Technology & Data
CIO (IT Infrastructure)                    → Agent 6: Technology & Data
Chief Data / Analytics Officer             → Agent 6: Technology & Data
Chief AI Officer                           → Agent 6: Technology & Data
CISO (Cybersecurity)                       → Agent 6: Technology & Data
Chief Science / R&D Officer               → Agent 6: Technology & Data
Chief Digital Officer                      → Agent 6: Technology & Data

COO (Operations)                           → Agent 7: Operations & Supply Chain
Chief Supply Chain Officer                 → Agent 7: Operations & Supply Chain
Chief Product Supply Officer               → Agent 7: Operations & Supply Chain
Chief Quality Officer                      → Agent 7: Operations & Supply Chain
```

---

## AGENT 1: ORCHESTRATOR + STRATEGY

### Roles Absorbed
- **CEO** — strategic vision, capital allocation, stakeholder management, organizational design, culture
- **Chief Strategy Officer** — strategic planning, M&A, competitive intelligence, portfolio strategy, new market entry
- **Division/Business Unit CEO** — spawns configurable sub-agents for each business unit

### Why These Belong Together

The CEO and Strategy Officer in a real company are often the same person's brain split into two calendars. The CEO thinks strategically; the CSO executes the strategic process. In an AI system, there's no reason to separate the thinking from the process. And business unit leadership is strategy applied to a specific context — same reasoning capability, narrower scope.

### Core Capabilities

#### 1.1 Strategic Planning & Vision
- **Inputs**: Market data, competitive intelligence, internal performance from all agents, board directives, compass setting
- **Processing**: Synthesize multi-source data into strategic options; evaluate options against mission, values, compass position, and long-term positioning; scenario model outcomes at 1, 3, 5, and 10-year horizons (horizon emphasis per compass)
- **Outputs**: Strategic plans, vision documents, strategic pivots, resource allocation frameworks
- **Tools**: Scenario modeling engine, strategy framework library (Porter's, Blue Ocean, Ansoff, etc.), competitive landscape mapper

#### 1.2 Decision Routing & Tier Classification
- **Inputs**: Decision requests from any agent, cross-functional decision triggers, compass setting
- **Processing**: Classify every material decision by tier (1-4); route to appropriate agent(s); convene multi-agent deliberation for cross-cluster decisions; enforce Decision Impact Protocol on Tier 3
- **Outputs**: Decision classifications, routing instructions, multi-agent deliberation agendas, Tier 3 protocol compliance reports

#### 1.3 Capital Allocation
- **Inputs**: Financial Intelligence Agent models, business unit performance, M&A pipeline, market opportunities
- **Processing**: Evaluate ROI of capital deployment options; balance growth vs. profitability vs. risk; apply compass-weighted time horizons
- **Outputs**: Capital allocation decisions, investment approvals/rejections, budget directives
- **Human Gate**: Investments above defined threshold require human board approval

#### 1.4 M&A and Corporate Development
- **Inputs**: Strategic gaps, market maps, Financial Intelligence Agent valuations, Legal & Risk Agent due diligence
- **Processing**: Screen targets; assess strategic fit; model synergies; manage due diligence process; plan integration
- **Outputs**: Target lists, strategic fit assessments, synergy models, integration plans
- **Human Gate**: All M&A pursuits require human approval

#### 1.5 Competitive Intelligence
- **Inputs**: Competitor filings, news feeds, patent databases, job postings, product launches, social media
- **Processing**: Track competitor strategies; predict competitive moves; identify market share shifts; war game scenarios
- **Outputs**: Competitive intelligence reports, war gaming results, market share analyses

#### 1.6 Stakeholder Management
- **Inputs**: Investor sentiment, board communications, media coverage, employee sentiment, customer NPS
- **Processing**: Prioritize stakeholder concerns; draft communications; identify reputation risks
- **Outputs**: Board presentations, investor narratives, public statements (drafts for human review)
- **Human Gate**: All external public communications require human sign-off

#### 1.7 Compass Enforcement & Revealed Compass Calculation
- **Inputs**: All decisions made across all agents over trailing 12 months, stated compass position
- **Processing**: Calculate the implied compass position based on actual decision patterns; compare to stated position; flag gaps
- **Outputs**: Revealed compass report (quarterly), gap alerts, drift warnings
- This is the system's self-honesty mechanism. It answers the question: "Are we who we say we are?"

#### 1.8 Business Unit Sub-Agent Spawning
- **Inputs**: Organizational structure, business unit definitions, unit-level strategy and KPIs
- **Processing**: Instantiate a sub-agent for each business unit with full P&L management, unit strategy, unit operations, and local market adaptation capabilities
- **Outputs**: Unit-level P&L reports, unit strategies, operational dashboards, localization plans
- Sub-agents inherit the compass setting and report up to the Orchestrator

### Interaction Pattern
This agent is the hub. Every other agent reports to it and receives strategic direction from it. It is the only agent that can convene multi-agent deliberations and the only agent that can override another agent's recommendation (subject to human approval for material decisions).

---

## AGENT 2: FINANCIAL INTELLIGENCE

### Roles Absorbed
- **CFO** — financial planning & analysis, reporting, compliance, treasury, capital structure, investor relations, M&A financial modeling, tax strategy
- **Chief Accounting Officer** — financial reporting, SOX compliance, audit preparation
- **Treasurer** — cash management, debt management, banking relationships

### Why These Belong Together

Every function here operates on the same data (general ledger, market feeds, banking data), uses the same analytical framework (financial modeling), and answers the same fundamental question: what is the financial state and trajectory of the company? Splitting this across multiple agents would mean multiple agents maintaining separate financial models that have to be reconciled. One agent, one model, one truth.

### Core Capabilities

#### 2.1 Financial Planning & Analysis (FP&A)
- **Inputs**: Revenue data, cost data, market forecasts, business unit budgets, macroeconomic indicators, compass setting
- **Processing**: Build and maintain financial models; run variance analysis; forecast revenue/expenses; stress-test scenarios; model employee costs as investments (Positions 1-2) or variable expenses (Positions 4-5) per compass
- **Outputs**: Financial forecasts, budget recommendations, variance reports, scenario analyses
- **Tools**: Financial modeling engine, Monte Carlo simulator, time-series forecaster

#### 2.2 Financial Reporting & Compliance
- **Inputs**: General ledger data, accounting entries, regulatory requirements (GAAP/IFRS, SEC rules, SOX)
- **Processing**: Automate financial statement generation; check compliance rules; flag anomalies
- **Outputs**: Income statements, balance sheets, cash flow statements, 10-K/10-Q drafts, audit preparation
- **Human Gate**: All SEC filings and audit responses require human CFO/controller sign-off

#### 2.3 Treasury & Capital Structure
- **Inputs**: Cash positions, debt covenants, interest rates, credit ratings, share price
- **Processing**: Optimize cash management; evaluate refinancing options; model share buyback vs. dividend scenarios
- **Outputs**: Treasury recommendations, debt management plans, capital structure optimization proposals

#### 2.4 Investor Relations
- **Inputs**: Earnings data, analyst estimates, shareholder registry, market sentiment, peer comparisons
- **Processing**: Generate earnings narratives; prepare Q&A guidance; model investor reactions to strategic moves
- **Outputs**: Earnings call scripts, investor presentations, analyst guidance, shareholder communications

#### 2.5 M&A Financial Analysis
- **Inputs**: Target company financials, market multiples, synergy estimates from Orchestrator
- **Processing**: DCF analysis, comparable company analysis, LBO modeling, accretion/dilution analysis
- **Outputs**: Deal valuations, financial due diligence reports, integration cost estimates
- **Human Gate**: All M&A financial opinions require human review

#### 2.6 Tax Strategy
- **Inputs**: Tax code, entity structure, jurisdictional tax rates, transfer pricing data
- **Processing**: Optimize tax structure; model impact of legislative changes; ensure compliance
- **Outputs**: Tax optimization strategies, compliance filings (draft), transfer pricing documentation

#### 2.7 Compass-Specific Financial Modeling

This is the capability that makes the compass real in financial terms:

- **Position 1-2**: Employee investment NPV uses 5-10 year horizons with 6-8% discount rates. Retention savings, institutional knowledge preservation, and employer brand value are modeled as explicit line items. Layoff models must include 3-year trailing costs (rehiring, retraining, morale damage, productivity loss).
- **Position 4-5**: Employee cost NPV uses 1-3 year horizons with 10-12% discount rates. Layoff models use projected savings minus severance and one-time costs. Trailing costs are noted but not required to change the recommendation.

Both produce honest numbers. The difference is what counts as a relevant time horizon and what gets included in the model. The assumptions are the values.

### Integration Requirements
- Real-time feeds from ERP/accounting systems (SAP, Oracle, NetSuite)
- Market data feeds (Bloomberg, Reuters)
- Banking APIs for cash position monitoring
- SEC EDGAR for regulatory filing requirements

### Sub-Agents This Agent Can Spawn
- **M&A Valuation Sub-agent**: Deep DCF/comparable analysis for a specific deal
- **Tax Optimization Sub-agent**: Model a specific restructuring or jurisdiction change
- **Earnings Prep Sub-agent**: Compile quarterly earnings package
- **Audit Response Sub-agent**: Prepare responses to specific audit inquiries

---

## AGENT 3: PEOPLE & ORGANIZATION

### Roles Absorbed
- **CHRO / Chief People Officer / Chief Talent Officer** — talent acquisition, compensation & benefits, performance management, employee experience, workforce planning
- **Chief DEI Officer / Chief Equality & Inclusion Officer** — diversity strategy, inclusive hiring, pay equity, ERGs, supplier diversity
- **Chief Learning Officer** — L&D programs, skills gap analysis, career pathing
- **Organizational Design** (from CEO role) — org structure, span of control, reorg planning

### Why These Belong Together

Every function here operates on the same data (HRIS, ATS, surveys, compensation benchmarks) and affects the same stakeholder (employees). DEI is not a separate discipline from HR — it's a lens on every HR decision. Learning is not separate from talent management — it's the mechanism by which talent grows. Separating these creates the organizational silos that allow a company to have great DEI metrics in the annual report while pay equity gaps persist in the actual payroll.

### Core Capabilities

#### 3.1 Talent Acquisition
- **Inputs**: Headcount plans, job requirements, candidate pipeline data, labor market analytics, compensation benchmarks, compass setting
- **Processing**: Source and screen candidates; predict candidate-role fit; optimize job descriptions; model offer competitiveness; audit hiring funnels for demographic disparities (DEI integrated, not siloed)
- **Outputs**: Candidate shortlists, screening assessments, offer recommendations, hiring pipeline dashboards, funnel equity reports

#### 3.2 Compensation & Benefits Design
- **Inputs**: Market compensation data, internal pay equity analysis, benefits utilization, budget constraints from Financial Intelligence Agent, compass setting
- **Processing**: Design compensation structures; model total rewards packages; run statistical pay equity analysis (gender, race, age, disability — not as a separate DEI exercise but as a core comp function); benchmark against peers
- **Compass effect**: Positions 1-2 target 60th-75th percentile. Position 4 targets 50th percentile. Position 5 targets 40th-50th percentile.
- **Outputs**: Compensation frameworks, benefits recommendations, equity analysis reports, budget models

#### 3.3 Performance Management
- **Inputs**: Performance review data, goal progress, 360 feedback, productivity metrics
- **Processing**: Calibrate performance ratings; identify high performers and underperformers; recommend development actions; audit calibration for demographic bias
- **Outputs**: Performance summaries, calibration recommendations, development plans, succession pipeline updates, calibration equity reports

#### 3.4 Learning & Development
- **Inputs**: Skills gap analysis, career path data, industry skills trends, employee learning preferences, automation impact forecasts from Technology & Data Agent
- **Processing**: Design learning paths; recommend training programs; measure learning ROI; predict future skills needs; build reskilling programs for roles being automated
- **Compass effect**: Positions 1-2 invest in reskilling BEFORE automation displaces roles. Position 4-5 invest in reskilling for roles with clear future demand; other displaced workers receive transition support.
- **Outputs**: Learning programs, skills gap reports, training recommendations, career path models, reskilling roadmaps

#### 3.5 Organizational Design
- **Inputs**: Business strategy from Orchestrator, headcount data, span-of-control metrics, collaboration patterns
- **Processing**: Model org structures; identify redundancies; recommend reporting changes; simulate reorg impacts on morale and productivity
- **Outputs**: Org design proposals, headcount models, reorg impact assessments, change management plans

#### 3.6 Employee Experience & Engagement
- **Inputs**: Survey data, turnover data, exit interviews, sentiment analysis of internal communications, Glassdoor/Blind monitoring
- **Processing**: Measure engagement health; predict flight risk; identify cultural issues; recommend interventions; segment analysis by demographic group (DEI integrated)
- **Outputs**: Engagement dashboards, retention risk alerts, culture health reports, intervention recommendations, demographic engagement gaps

#### 3.7 Workforce Planning & Analytics
- **Inputs**: Business forecasts, demographic data, attrition patterns, automation impact models from Technology & Data Agent
- **Processing**: Forecast workforce needs; model automation displacement; plan reskilling programs; project labor cost trajectories
- **Outputs**: Workforce plans, automation impact reports, reskilling roadmaps, headcount forecasts

#### 3.8 DEI as an Integrated Function

DEI is not a sub-agent or a separate module. It is a lens applied to every capability above:

| HR Function | DEI Integration |
|---|---|
| Talent Acquisition | Hiring funnel conversion by demographic; bias audit on job descriptions; diverse sourcing channel optimization |
| Compensation | Statistical pay equity analysis as standard comp function; unexplained gap identification and remediation |
| Performance | Calibration equity audit; rating distribution by demographic; bias detection in feedback language |
| Learning | Equitable access to high-visibility development opportunities; sponsorship gap analysis |
| Org Design | Representation at every level; promotion velocity by demographic; succession pipeline diversity |
| Engagement | Engagement score disaggregation by demographic; belonging metrics; inclusion index |
| Workforce Planning | Disparate impact analysis on any proposed RIF; automation displacement equity review |

**At all compass positions**: DEI metrics are tracked and reported. The difference is response:
- Positions 1-2: Gaps trigger mandatory remediation plans with budget and timeline
- Position 4: Gaps are flagged; remediation is recommended but not mandatory
- Position 5: Gaps are reported for compliance; remediation is discretionary

#### 3.9 The Tier 3 Engine (Layoffs, RIFs, Restructuring)

This is the most consequential capability in the system. When the Orchestrator routes a Tier 3 workforce decision here, this agent:

1. **Models alternatives**: Hiring freeze impact, voluntary separation program design, reduced hours/furlough modeling, internal redeployment matching, early retirement incentive design
2. **Quantifies human cost**: Per the Decision Impact Protocol — real numbers, real people, real household data
3. **Runs disparate impact analysis**: Ensures the proposed action doesn't disproportionately affect protected groups
4. **Designs mitigation**: Severance packages, outplacement, extended benefits, reskilling — scope calibrated by compass
5. **Models survivor impact**: Projected engagement drop, voluntary attrition spike, productivity loss, hiring cost increase
6. **Provides the full package to human decision-maker**: All alternatives, all costs, all impacts, clear recommendation based on compass position
7. **Tracks outcomes post-decision**: 30/60/90/180/365-day tracking of financial and human outcomes

### Integration Requirements
- HRIS systems (Workday, SuccessFactors, BambooHR)
- ATS systems (Greenhouse, Lever)
- Learning management systems
- Survey platforms (Qualtrics, Culture Amp)
- Payroll systems
- Glassdoor/Blind APIs (sentiment monitoring)

### Sub-Agents This Agent Can Spawn
- **RIF Planning Sub-agent**: Deep modeling for a specific restructuring scenario
- **Compensation Benchmarking Sub-agent**: Targeted comp study for a specific role/market
- **Org Design Sub-agent**: Model a specific reorganization's cascading effects
- **Reskilling Program Sub-agent**: Design a specific reskilling curriculum

---

## AGENT 4: MARKET & REVENUE

### Roles Absorbed
- **CMO / Chief Brand Officer** — brand strategy, advertising, digital marketing, market research, customer insights
- **Chief Revenue Officer / Chief Sales Officer / Chief Commercial Officer** — sales operations, pricing, key accounts, channel strategy, revenue planning
- **Chief Product Officer** — product vision, roadmap, product development lifecycle, user research, product analytics
- **Chief Communications Officer / Chief Global Affairs Officer** — external communications, internal communications, crisis communications, government affairs, public policy
- **Chief Content Officer** — content strategy (media/entertainment specific)

### Why These Belong Together

These functions all face outward — toward customers, markets, and the public. They all answer: "How do we create, deliver, and capture value from the market?" The CMO generates demand, the Sales leader converts it, the Product leader builds what's being sold, and Communications shapes the narrative. In most companies, the dysfunction between these roles — marketing generates leads that sales doesn't want, product builds features marketing can't explain, communications finds out about decisions after they're made — is the #1 source of revenue drag. One agent eliminates the silos.

### Core Capabilities

#### 4.1 Brand Strategy & Positioning
- **Inputs**: Market research, customer perception data, competitive positioning, company values from Orchestrator
- **Processing**: Define brand architecture; develop positioning frameworks; measure brand health; recommend brand evolution; integrate employer brand data from People & Organization Agent
- **Outputs**: Brand strategy documents, positioning maps, brand health dashboards, creative briefs

#### 4.2 Customer Acquisition & Growth
- **Inputs**: Customer data, channel performance, CAC/LTV metrics, market segment data, compass setting
- **Processing**: Optimize channel mix; predict campaign ROI; segment audiences; model growth scenarios
- **Compass effect**: Positions 1-2 weight customer lifetime value and relationship quality. Positions 4-5 weight acquisition volume and short-term conversion rates.
- **Outputs**: Marketing plans, channel allocations, campaign recommendations, growth forecasts
- **Tools**: Marketing mix model, attribution engine, A/B testing framework, audience segmentation engine

#### 4.3 Market Research & Consumer Insights
- **Inputs**: Survey data, behavioral data, social listening, competitive intelligence, industry reports
- **Processing**: Analyze market trends; segment customers; identify unmet needs; predict market shifts
- **Outputs**: Market research reports, consumer insight briefs, trend forecasts, competitive comparisons

#### 4.4 Product Vision & Roadmap
- **Inputs**: Market research (above), technology capabilities from Technology & Data Agent, strategic direction from Orchestrator, customer feedback
- **Processing**: Define product vision; prioritize features; balance short-term vs. long-term; model product-market fit; run competitive feature gap analysis
- **Outputs**: Product roadmaps, feature prioritization matrices, product vision documents, release plans

#### 4.5 Product Development Lifecycle
- **Inputs**: Feature specifications, engineering estimates from Technology & Data Agent, user research, competitive feature analysis
- **Processing**: Manage development pipeline; track feature progress; coordinate cross-functional dependencies; manage trade-offs
- **Outputs**: Sprint plans, feature specifications, dependency maps, release readiness assessments

#### 4.6 Product Analytics
- **Inputs**: Product usage data, feature adoption metrics, retention curves, revenue-per-feature data
- **Processing**: Measure feature success; predict adoption; identify underperforming features; model pricing impact
- **Outputs**: Product analytics dashboards, feature health reports, pricing recommendations

#### 4.7 Revenue Strategy & Sales Operations
- **Inputs**: Market sizing, financial targets from Financial Intelligence Agent, product roadmap, CRM data, pipeline metrics
- **Processing**: Set revenue targets; model pricing strategies; optimize sales processes; score and route leads; forecast pipeline; manage key accounts
- **Outputs**: Revenue plans, pricing strategies, pipeline reports, lead scores, forecast models, account plans
- **Tools**: CRM analytics engine, lead scoring model, pipeline predictor

#### 4.8 External Communications & Media Relations
- **Inputs**: News cycle monitoring, company announcements, media inquiries, crisis triggers, executive calendar
- **Processing**: Draft press releases; prepare media briefings; monitor coverage; respond to inquiries
- **Outputs**: Press releases (drafts), media kits, talking points, coverage reports, media response drafts
- **Human Gate**: All external statements require human approval

#### 4.9 Internal Communications
- **Inputs**: Company strategy from Orchestrator, organizational changes from People & Organization Agent, employee sentiment
- **Processing**: Draft internal announcements; plan communication cadences; ensure Tier 3 communications follow the Decision Impact Protocol language standards
- **Outputs**: Internal announcements, town hall agendas, communication plans

#### 4.10 Crisis Communications
- **Inputs**: Crisis triggers (from Legal & Risk Agent, Technology & Data Agent, or media monitoring), stakeholder mapping
- **Processing**: Assess crisis severity; activate response playbooks; draft holding statements; coordinate cross-agent response
- **Outputs**: Crisis response plans, holding statements, stakeholder communications, post-crisis analyses
- **Human Gate**: All crisis communications require immediate human leadership approval

#### 4.11 Government Affairs & Public Policy
- **Inputs**: Legislative tracking, regulatory proposals, political landscape, industry association updates
- **Processing**: Analyze policy impact; draft position papers; recommend lobbying priorities; track legislative progress
- **Outputs**: Policy impact analyses, position papers, lobbying recommendations, legislative tracking reports

### Integration Requirements
- CRM systems (Salesforce, HubSpot)
- Marketing automation platforms
- Web/app analytics (GA4, Mixpanel, Amplitude)
- Social media management tools
- Media monitoring services
- Product analytics platforms
- Content management systems

### Sub-Agents This Agent Can Spawn
- **Campaign Optimization Sub-agent**: Deep optimization for a specific marketing campaign
- **Product Launch Sub-agent**: Coordinate a specific product launch across marketing, sales, and PR
- **Crisis Response Sub-agent**: Manage a specific crisis through resolution
- **Pricing Analysis Sub-agent**: Deep pricing study for a specific product/market
- **Competitive Product Sub-agent**: Deep-dive analysis on a specific competitor's product strategy

---

## AGENT 5: LEGAL & RISK

### Roles Absorbed
- **Chief Legal Officer / General Counsel** — legal risk assessment, contract management, corporate governance, litigation, IP, privacy
- **Chief Risk Officer / Chief Compliance Officer** — enterprise risk management, regulatory compliance, internal audit
- **Chief Ethics Officer / Chief Ethics & Compliance Officer** — ethics programs, conduct investigations
- **Chief Sustainability Officer / Chief Impact Officer** — ESG reporting, sustainability compliance, environmental strategy
- **Chief Audit Executive** — internal audit programs, control testing

### Why These Belong Together

Legal, risk, compliance, ethics, and sustainability all answer the same question: "Are we operating within acceptable boundaries, and what happens if we're not?" They all require regulatory awareness, investigative capability, and the ability to say "no" (or "not like that") to the rest of the organization. Splitting them means the legal team doesn't know what the compliance team found, the ethics hotline operates separately from the legal department investigating the same issue, and sustainability reporting lives in a different org from the legal team that has to certify it. One agent, one boundary-management system.

### Core Capabilities

#### 5.1 Legal Risk Assessment
- **Inputs**: Business decisions from all agents, contract terms, regulatory landscape, litigation data
- **Processing**: Evaluate legal risk of proposed actions; flag regulatory concerns; assess liability exposure
- **Outputs**: Risk assessments, legal opinions (draft), compliance checklists, risk ratings
- **Human Gate**: All formal legal opinions require human attorney review (ethical/bar requirements)

#### 5.2 Contract Management
- **Inputs**: Contract templates, negotiation parameters, counterparty data, precedent terms
- **Processing**: Draft contracts; review counterparty proposals; flag non-standard terms; track obligations and deadlines
- **Outputs**: Contract drafts, redline summaries, obligation trackers, renewal alerts
- **Tools**: Contract analysis NLP, clause library, obligation tracking system

#### 5.3 Regulatory Compliance Monitoring
- **Inputs**: Regulatory feeds (SEC, FTC, DOJ, GDPR, industry-specific), company policies, operational data
- **Processing**: Monitor regulatory changes; assess impact on operations; update compliance programs; generate compliance reports
- **Outputs**: Regulatory change alerts, impact assessments, compliance program updates, audit-ready reports

#### 5.4 Corporate Governance
- **Inputs**: Board requirements, charter documents, proxy rules, shareholder proposals
- **Processing**: Prepare board materials; track governance requirements; manage proxy process; maintain corporate records
- **Outputs**: Board packages, governance calendars, proxy materials, corporate minute drafts

#### 5.5 Litigation Management
- **Inputs**: Active litigation data, discovery documents, case law, settlement parameters
- **Processing**: Case strategy analysis; document review and classification; settlement value modeling; timeline tracking
- **Outputs**: Case summaries, document review classifications, settlement recommendations, litigation budgets
- **Human Gate**: All litigation strategy decisions and settlement authorizations require human approval

#### 5.6 Intellectual Property
- **Inputs**: Patent filings, trademark registrations, trade secret inventories, competitive IP landscape
- **Processing**: Monitor IP portfolio; identify infringement risks; evaluate patent filing opportunities; conduct freedom-to-operate analyses
- **Outputs**: IP portfolio reports, FTO analyses, filing recommendations, infringement alerts

#### 5.7 Privacy & Data Protection
- **Inputs**: Data processing activities, privacy regulations (GDPR, CCPA, etc.), data breach incidents
- **Processing**: Map data flows; assess privacy compliance; manage data subject requests; coordinate breach response
- **Outputs**: Privacy impact assessments, DSAR response workflows, breach notification drafts, privacy program reports

#### 5.8 Enterprise Risk Management
- **Inputs**: Operational data, financial data, market data, geopolitical intelligence, supply chain data, cyber threat intelligence, compass setting
- **Processing**: Scan for emerging risks; quantify risk exposure; model risk scenarios; prioritize risk mitigation
- **Outputs**: Risk heat maps, risk registers, scenario analyses, risk appetite recommendations
- **Tools**: Risk quantification models, Monte Carlo simulators, Bayesian risk networks

#### 5.9 Internal Audit
- **Inputs**: Financial transactions, process data, control testing results, prior audit findings
- **Processing**: Plan risk-based audits; test controls; identify control deficiencies; track remediation
- **Outputs**: Audit plans, audit findings, control assessments, remediation tracking reports

#### 5.10 Ethics & Conduct
- **Inputs**: Ethics hotline reports, policy violations, training data, industry ethics standards
- **Processing**: Triage ethics reports; investigate conduct issues; recommend policy changes; monitor ethical climate
- **Outputs**: Ethics case summaries, investigation recommendations, policy update proposals
- **Human Gate**: All ethics investigations and disciplinary recommendations require human review

#### 5.11 Third-Party Risk Management
- **Inputs**: Vendor data, supply chain mapping, financial health of partners, compliance certifications
- **Processing**: Assess vendor risk; monitor ongoing risk indicators; flag high-risk relationships
- **Outputs**: Vendor risk scores, due diligence reports, monitoring alerts, concentration risk reports

#### 5.12 Sustainability & ESG
- **Inputs**: Environmental data (carbon, energy, waste, water), social data, governance data, reporting frameworks (GRI, SASB, TCFD, CSRD), supplier sustainability scores
- **Processing**: Aggregate ESG data; generate framework-aligned reports; set sustainability targets; model decarbonization pathways; assess supply chain environmental impact; engage stakeholders
- **Outputs**: ESG reports, sustainability strategies, decarbonization roadmaps, supply chain sustainability scores, framework compliance assessments

**Why sustainability is in Legal & Risk, not a standalone**: ESG reporting is increasingly mandated by regulation (CSRD, SEC climate disclosure). Sustainability claims create legal liability if misleading. The compliance infrastructure for ESG reporting is the same as financial and regulatory compliance. Putting it here ensures sustainability commitments have legal rigor, not just marketing polish.

#### 5.13 Tier 3 Legal Review

Every Tier 3 decision passes through this agent for:
- Disparate impact analysis (layoffs)
- WARN Act compliance (plant closings/mass layoffs)
- Benefits law compliance (ERISA, COBRA)
- Severance agreement enforceability
- Non-compete/non-solicit implications
- Potential whistleblower/retaliation exposure
- Regulatory notification requirements

### Integration Requirements
- Legal research databases (Westlaw, LexisNexis)
- Contract lifecycle management systems
- Regulatory feed services
- Ethics hotline platforms
- ESG data collection systems
- GRC platforms (Archer, ServiceNow GRC)

### Sub-Agents This Agent Can Spawn
- **Contract Review Sub-agent**: Review a specific large/complex agreement
- **Litigation Analysis Sub-agent**: Deep dive on a specific case
- **Regulatory Change Sub-agent**: Analyze a specific new regulation's full impact
- **ESG Report Sub-agent**: Compile a specific framework-aligned ESG report
- **Investigation Sub-agent**: Conduct a specific ethics/conduct investigation

---

## AGENT 6: TECHNOLOGY & DATA

### Roles Absorbed
- **CTO** — technology vision, R&D, platform architecture, emerging technology evaluation
- **CIO** — enterprise IT infrastructure, vendor management, digital transformation
- **Chief Data Officer / Chief Analytics Officer** — data strategy, governance, advanced analytics, BI
- **Chief AI Officer** — AI strategy, ethics, infrastructure, integration across business
- **CISO** — cybersecurity strategy, threat detection, incident response, security compliance
- **Chief Science / R&D Officer** — research strategy, innovation management, scientific pipeline (industry-specific)
- **Chief Digital Officer** — digital transformation, digital product strategy

### Why These Belong Together

These roles all operate on the same infrastructure, share the same engineering talent pool, and are increasingly inseparable. You can't do AI without data. You can't do data without infrastructure. You can't do infrastructure without security. You can't do digital transformation without all of the above. The CTO/CIO/CDO/CAIO/CISO split in corporate org charts exists because no human can be expert in all of these. An AI agent can hold the full context and reason across all of them simultaneously.

R&D and Science are included here because in 2026, research in every industry — pharma, consumer goods, energy, financial services — is technology-dependent. The scientific pipeline runs on computational tools, data analytics, and increasingly AI/ML. Separating the science from the technology that enables it creates an artificial gap.

### Core Capabilities

#### 6.1 Technology Strategy & Architecture
- **Inputs**: Business strategy from Orchestrator, market technology trends, competitive tech landscape, internal tech debt assessments
- **Processing**: Evaluate emerging technologies for business impact; build technology roadmaps; assess build vs. buy vs. partner; make architecture decisions
- **Outputs**: Technology roadmaps, architecture designs, tech investment proposals, build/buy/partner recommendations

#### 6.2 Engineering & Platform Management
- **Inputs**: Product requirements from Market & Revenue Agent, technical specifications, system performance data, incident logs
- **Processing**: Development methodology optimization; code quality and security review; deployment automation; platform reliability engineering
- **Outputs**: Engineering standards, platform health reports, incident post-mortems, deployment pipelines

#### 6.3 IT Infrastructure & Operations
- **Inputs**: Infrastructure monitoring data, usage patterns, cost data, SLA requirements
- **Processing**: Optimize infrastructure costs; capacity planning; disaster recovery planning; vendor management
- **Outputs**: Infrastructure plans, cost optimization reports, DR/BCP plans, vendor evaluations

#### 6.4 Data Strategy & Governance
- **Inputs**: Data inventory, data quality metrics, regulatory requirements, business data needs
- **Processing**: Define data standards; classify data assets; monitor data quality; enforce governance policies; design data architectures
- **Outputs**: Data governance frameworks, data catalogs, quality dashboards, architecture designs

#### 6.5 Advanced Analytics & Business Intelligence
- **Inputs**: Structured/unstructured data from all business functions, analysis requests from other agents
- **Processing**: Build predictive models; generate business intelligence; create self-service analytics; identify data-driven insights
- **Outputs**: Analytical models, dashboards, insight reports, data products

#### 6.6 AI Strategy & Deployment
- **Inputs**: Business strategy, AI capabilities assessment, competitive AI positioning, ethical frameworks, compass setting
- **Processing**: Identify high-impact AI use cases; prioritize AI investments; build AI roadmaps; audit AI systems for bias; manage AI model lifecycle; monitor responsible AI compliance
- **Compass effect**: Positions 1-2 require AI fairness audits before deployment and model automation impact assessments that include reskilling plans. Positions 4-5 require fairness audits for compliance and model automation impact assessments that include cost savings projections.
- **Outputs**: AI strategy documents, use case prioritization, fairness audits, model health reports, deployment approvals
- **Human Gate**: High-risk AI deployments (as classified by EU AI Act or internal risk framework) require human ethics board approval

#### 6.7 Cybersecurity
- **Inputs**: SIEM alerts, endpoint data, network traffic, threat intelligence feeds, vulnerability scans, compliance frameworks
- **Processing**: Correlate threat signals; triage alerts; automate response playbooks; design security architecture; manage identity and access; prepare for security audits
- **Outputs**: Threat alerts, incident reports, security architecture designs, access policies, compliance dashboards
- **Human Gate**: Critical incidents (data breaches, ransomware) require immediate human escalation

#### 6.8 Research & Development (Industry-Specific)
- **Inputs**: Scientific literature, patent landscape, competitive R&D intelligence, experimental data, market unmet needs
- **Processing**: Prioritize research programs; stage-gate evaluation; analyze experimental results; manage research partnerships; design clinical trial protocols (pharma); manage innovation portfolio
- **Outputs**: R&D strategy, pipeline reviews, research reports, trial designs, innovation portfolio reviews, filing recommendations
- **Human Gate**: All clinical trial decisions and regulatory submissions require human medical/scientific review

#### 6.9 Digital Transformation
- **Inputs**: Business process assessments from Operations Agent, employee digital maturity data, industry benchmarks
- **Processing**: Identify digitization opportunities; prioritize transformation initiatives; measure digital adoption; design digital customer experiences
- **Outputs**: Digital transformation roadmap, adoption metrics, training requirements

#### 6.10 Automation Impact Assessment

Every automation initiative — whether AI, robotics, or process automation — must pass through this capability:

1. **Quantify the displacement**: How many roles, which roles, what tenure, what reskilling difficulty
2. **Model the reskilling path**: What adjacent roles exist, what training is required, what timeline
3. **Route to People & Organization Agent**: For workforce planning integration
4. **Apply compass weights**: Position 1-2 requires reskilling program launch BEFORE automation deployment. Position 4-5 requires notification and transition support.
5. **Track outcomes**: Did displaced workers get reskilled? At what rate? What was the net financial and human impact?

### Integration Requirements
- Cloud provider APIs (AWS, Azure, GCP)
- CI/CD pipeline monitoring
- ITSM systems (ServiceNow, Jira)
- Security tools (SIEM, vulnerability scanners, EDR)
- Data platforms (Snowflake, Databricks, BigQuery)
- AI/ML platforms (SageMaker, Vertex AI, custom)
- Research databases (PubMed, patent databases)

### Sub-Agents This Agent Can Spawn
- **Security Incident Sub-agent**: Manage a specific security incident through resolution
- **Architecture Review Sub-agent**: Deep evaluation of a specific system design
- **AI Fairness Audit Sub-agent**: Comprehensive bias audit of a specific AI model
- **R&D Pipeline Sub-agent**: Deep analysis of a specific research program
- **Data Migration Sub-agent**: Plan and validate a specific data migration
- **Automation ROI Sub-agent**: Full impact analysis of a specific automation initiative

---

## AGENT 7: OPERATIONS & SUPPLY CHAIN

### Roles Absorbed
- **COO** — operational performance management, process optimization, cross-functional execution, scaling operations
- **Chief Supply Chain Officer / Chief Product Supply Officer** — supply chain planning, procurement, logistics, distribution
- **Chief Quality Officer** — quality assurance, manufacturing quality, recall management
- **VP of Operations / VP Manufacturing** — production management, facility management

### Why These Belong Together

These functions all manage the physical flow of value — making things, moving things, and ensuring the quality of things. The COO and Supply Chain Officer operate on the same data (production volumes, logistics costs, quality metrics, capacity utilization) and solve the same optimization problem (deliver the most value at the lowest cost with acceptable quality). Separating them creates the classic ops vs. supply chain finger-pointing that plagues manufacturing companies.

**Note**: Pure software companies may not need this agent at all, or may configure it with only the process optimization and scaling capabilities active. A Walmart or P&G will need this to be the most sophisticated agent in the system.

### Core Capabilities

#### 7.1 Operational Performance Management
- **Inputs**: KPI dashboards, production data, service level metrics, customer satisfaction data, compass setting
- **Processing**: Monitor operational health in real-time; detect degradation; identify improvement opportunities; benchmark against industry standards
- **Compass effect**: Positions 1-2 weight worker safety and ergonomics as primary KPIs alongside efficiency. Positions 4-5 weight efficiency and throughput as primary, with safety at regulatory compliance level.
- **Outputs**: Operational dashboards, performance alerts, improvement recommendations, executive operational briefings

#### 7.2 Process Optimization
- **Inputs**: Process maps, cycle time data, error rates, employee feedback, automation opportunities
- **Processing**: Identify bottlenecks; model process changes; calculate ROI of automation; prioritize improvement projects
- **Outputs**: Process redesign proposals, automation business cases, lean/six sigma project charters
- **Tools**: Process mining engine, simulation modeler, automation assessment framework

#### 7.3 Cross-Functional Execution
- **Inputs**: Strategic initiatives from Orchestrator, project status data, resource availability
- **Processing**: Break strategic initiatives into operational projects; assign resources; track milestones; manage dependencies
- **Outputs**: Project plans, resource allocation, milestone tracking, blocker escalations

#### 7.4 Supply Chain Planning
- **Inputs**: Demand forecasts from Market & Revenue Agent and Financial Intelligence Agent, inventory levels, supplier capacity, logistics constraints
- **Processing**: Demand-supply matching; inventory optimization; production scheduling; distribution planning
- **Outputs**: Supply plans, inventory targets, production schedules, distribution plans
- **Tools**: Demand planning engine, inventory optimizer, network design modeler

#### 7.5 Procurement & Vendor Management
- **Inputs**: Bill of materials, vendor catalogs, pricing data, quality metrics, risk assessments from Legal & Risk Agent
- **Processing**: Source vendors; draft negotiation terms; evaluate vendor performance; manage supplier relationships; track supplier diversity metrics (integrated from DEI function)
- **Outputs**: Vendor shortlists, RFP documents, performance scorecards, cost reduction recommendations, supplier diversity reports
- **Human Gate**: Contracts above threshold require human procurement approval

#### 7.6 Manufacturing & Quality
- **Inputs**: Production data, quality metrics, equipment telemetry, specifications, regulatory requirements
- **Processing**: Monitor production quality; predict equipment failures; optimize production parameters; manage recalls
- **Outputs**: Quality dashboards, predictive maintenance alerts, production optimization recommendations

#### 7.7 Logistics & Distribution
- **Inputs**: Order data, warehouse capacity, carrier data, route information, customer delivery requirements
- **Processing**: Optimize routing; manage warehouse operations; track shipments; handle exceptions
- **Outputs**: Route plans, warehouse utilization reports, delivery performance dashboards, exception alerts

#### 7.8 Supply Chain Risk Management
- **Inputs**: Supplier geographic data, geopolitical intelligence, weather data, financial health of suppliers
- **Processing**: Map supply chain vulnerabilities; model disruption scenarios; develop contingency plans
- **Outputs**: Risk heat maps, contingency plans, alternative supplier recommendations, disruption alerts

#### 7.9 Scaling Operations
- **Inputs**: Growth forecasts from Financial Intelligence Agent, capacity data, market expansion plans from Orchestrator
- **Processing**: Capacity planning; facility/infrastructure expansion modeling; vendor/partner sourcing
- **Outputs**: Scaling plans, capacity models, make-vs-buy recommendations, vendor shortlists

### Integration Requirements
- ERP systems (SAP, Oracle)
- Manufacturing execution systems (MES)
- Warehouse management systems (WMS)
- Transportation management systems (TMS)
- IoT/sensor platforms for equipment monitoring
- Quality management systems

### Sub-Agents This Agent Can Spawn
- **Sourcing Sub-agent**: Conduct a specific vendor sourcing exercise
- **Capacity Planning Sub-agent**: Model capacity for a specific expansion scenario
- **Recall Management Sub-agent**: Manage a specific product recall
- **Logistics Optimization Sub-agent**: Optimize a specific distribution network

---

## CROSS-CUTTING REQUIREMENTS

### Shared Infrastructure

#### Memory & Knowledge Store
- **Persistent memory**: Each agent maintains its own domain knowledge base, updated with every interaction
- **Shared memory**: Cross-agent knowledge graph for company-wide context (org chart, strategy, policies, glossary, compass setting)
- **Episodic memory**: Record of past decisions, rationale, outcomes, and compass position at time of decision
- **External knowledge**: Integration with industry databases, news feeds, regulatory databases
- **Compass history**: Complete record of all compass settings, changes, and revealed compass calculations

#### Communication Bus
- **Agent-to-agent messaging**: Structured message format with sender, recipient, priority, topic, payload
- **Broadcast channels**: Strategy updates, policy changes, crisis alerts, compass changes reach all agents simultaneously
- **Request/response patterns**: Any agent can request analysis or data from any other agent
- **Escalation protocol**: Defined escalation paths when agents disagree or face uncertainty

#### Tool Registry
- **Shared tools**: Web search, document generation, email drafting, calendar management, data analysis
- **Agent-specific tools**: Each agent has domain-specific tools (e.g., Financial Intelligence has financial modeling tools, Legal & Risk has legal research tools)
- **Tool access control**: Some tools restricted by agent role (e.g., only Financial Intelligence can access banking APIs)
- **Tool versioning**: Tools can be updated without disrupting agent operations

#### Human Escalation Interface
- **Dashboard**: Real-time view of all agent activities, decisions pending approval, alerts, and compass status
- **Approval queues**: Organized by urgency, tier classification, and domain for human decision-makers
- **Override capability**: Humans can override any agent decision at any time
- **Audit trail**: Complete record of all agent actions, human approvals, overrides, and compass changes

---

### Data Requirements

| Data Category | Sources | Agents That Consume |
|---|---|---|
| Financial data | ERP, banking, market feeds | Financial Intelligence, Orchestrator |
| Customer data | CRM, support, analytics | Market & Revenue, Orchestrator |
| Employee data | HRIS, ATS, surveys | People & Org, Orchestrator |
| Product data | Product analytics, engineering | Market & Revenue, Technology & Data |
| Legal/Regulatory | Legal databases, regulatory feeds | Legal & Risk |
| Market/Competitive | News, filings, research | Orchestrator, Market & Revenue |
| Operational data | IoT, supply chain, logistics | Operations & Supply Chain |
| Security data | SIEM, threat intel, vulnerability | Technology & Data |
| Sustainability data | Energy, emissions, waste | Legal & Risk, Operations |
| Compass & Decision data | All agents, audit trail | Orchestrator (compass enforcement) |

---

### Non-Functional Requirements

#### Performance
- Agent response time for routine queries: < 30 seconds
- Multi-agent deliberation for cross-cluster decisions: < 5 minutes
- Real-time monitoring capabilities (Security, Operational): continuous operation with < 1 minute alert latency
- Batch analysis (financial reporting, ESG): completed within defined schedule windows

#### Scalability
- Support for 1-50 Business Unit sub-agent instances within the Orchestrator
- Horizontal scaling of data processing within the Technology & Data Agent
- Concurrent operation of all 7 agents plus sub-agents without resource contention

#### Reliability
- 99.9% availability for all 7 core agents
- Graceful degradation — if one agent fails, others continue operating
- Full audit trail preserved even during agent failures
- Automatic recovery and state restoration

#### Security
- Agent-to-agent communication encrypted
- Role-based access control on all data
- No agent can access data outside its defined scope without explicit authorization
- All human escalation channels authenticated and encrypted
- Prompt injection protections on all external data inputs
- Compass setting changes require multi-factor authentication and board-level authorization

#### Compliance
- All agent decisions auditable and explainable
- Regulatory hold capabilities for litigation
- Data retention policies enforced automatically
- GDPR/CCPA compliance for personal data handling
- SOC2 compliance for agent infrastructure
- Compass audit trail satisfies corporate governance requirements

---

### Human Oversight Model

| Decision Category | Tier | AI Authority | Human Role |
|---|---|---|---|
| Routine analysis & reporting | — | Full autonomy | Review on exception |
| Tier 1 decisions (aligned outcomes) | 1 | Recommend and execute if approved | Approve threshold, spot-check |
| Tier 2 decisions (deferred returns) | 2 | Full analysis + NPV modeling | Approve investment case |
| Operational recommendations | — | Propose | Approve or modify |
| Strategic recommendations | — | Propose with options | Select and approve |
| Financial commitments > threshold | — | Prepare analysis | Decide |
| External communications | — | Draft | Review and publish |
| Legal opinions | — | Research and draft | Review and sign (bar requirement) |
| Tier 3 decisions (genuine trade-offs) | 3 | Full analysis with Decision Impact Protocol | **Must decide. Cannot be delegated to AI.** |
| Layoffs / RIFs / site closures | 3 | Model alternatives, quantify human cost, design mitigation | **Decide, own, communicate personally** |
| Benefit reductions / comp changes | 3 | Model impact, benchmark, propose alternatives | **Decide with full impact visibility** |
| Tier 4 decisions (extraction) | 4 | Flag and resist with full impact analysis | Receive warning; must explicitly override |
| Compass setting changes | — | Cannot initiate | Board authorization required |
| Crisis response | — | Draft response plan | Approve and execute |
| M&A transactions | — | Full analysis | Decide |
| Clinical/safety decisions | — | Analysis and monitoring | Decide (regulatory requirement) |
| Ethics/conduct investigations | — | Triage and gather facts | Judge and decide |

**Critical rule**: The system will prepare the analysis, model the alternatives, quantify the human cost, and draft the communications. But a human being must make every Tier 3 decision and personally own the communication to affected employees. AI does not fire people. A person does, and they look the affected person in the eye (or at minimum, speak to them directly) when they do it.

---

## IMPLEMENTATION PHASES

### Phase 1: Foundation (Months 1-3)
- Set the Priority Compass (board decision — this comes first, everything else follows)
- Deploy Orchestrator + Strategy Agent (decision routing, tier classification, compass enforcement)
- Deploy Financial Intelligence Agent (financial analysis and reporting)
- Deploy Technology & Data Agent (infrastructure, data governance, security monitoring)
- Establish shared infrastructure (memory store, communication bus, tool registry, audit trail)
- Build human escalation interface with compass dashboard

### Phase 2: Core Business (Months 4-6)
- Deploy People & Organization Agent (workforce analytics, talent management, DEI integration)
- Deploy Market & Revenue Agent (marketing analytics, product management, sales operations)
- Deploy Legal & Risk Agent (compliance monitoring, contract management, risk assessment)
- Inter-agent communication testing and optimization
- First revealed compass calculation (do our early decisions match our stated position?)

### Phase 3: Operations (Months 7-9)
- Deploy Operations & Supply Chain Agent (if applicable to industry)
- Enable Business Unit sub-agents within Orchestrator
- Cross-agent Tier 3 decision simulation (dry runs of the Decision Impact Protocol)
- Full multi-agent deliberation testing

### Phase 4: Optimization (Months 10+)
- Multi-agent decision-making tuning
- Sub-agent spawning optimization
- Revealed compass auditing goes live (quarterly reports to board)
- Expand human autonomy boundaries based on trust calibration
- Continuous improvement based on decision outcome tracking
- Annual compass review (is the stated position still the intended position?)

---

## APPENDIX A: COMPANIES ANALYZED

| # | Company | Market Cap (~) | Industry |
|---|---|---|---|
| 1 | Apple | $3.7T | Tech / Consumer Electronics |
| 2 | Microsoft | $3.2T | Tech / Software & Cloud |
| 3 | NVIDIA | $3.0T | Tech / Semiconductors & AI |
| 4 | Amazon | $2.4T | Tech / E-Commerce & Cloud |
| 5 | Alphabet/Google | $2.3T | Tech / Internet Services |
| 6 | Meta | $1.7T | Tech / Social Media |
| 7 | Berkshire Hathaway | $1.1T | Conglomerate |
| 8 | Tesla | $1.0T | Automotive / EV & Energy |
| 9 | Broadcom | $950B | Tech / Semiconductors |
| 10 | Eli Lilly | $900B | Healthcare / Pharma |
| 11 | JPMorgan Chase | $750B | Financial Services |
| 12 | Walmart | $700B | Retail |
| 13 | Visa | $650B | Financial Services / Payments |
| 14 | UnitedHealth Group | $550B | Healthcare / Insurance |
| 15 | Mastercard | $500B | Financial Services / Payments |
| 16 | Johnson & Johnson | $480B | Healthcare / Pharma & Devices |
| 17 | Costco | $450B | Retail / Warehouse |
| 18 | Procter & Gamble | $420B | Consumer Goods |
| 19 | ExxonMobil | $410B | Energy / Oil & Gas |
| 20 | Home Depot | $400B | Retail / Home Improvement |
| 21 | AbbVie | $380B | Healthcare / Biopharma |
| 22 | Netflix | $370B | Entertainment / Streaming |
| 23 | Salesforce | $310B | Tech / Enterprise Software |
| 24 | Coca-Cola | $300B | Consumer Goods / Beverages |
| 25 | Bank of America | $290B | Financial Services |

---

## APPENDIX B: ROLE PREVALENCE & ABSORPTION

| Original Role | Prevalence | Absorbed Into |
|---|---|---|
| CEO | 25/25 | Agent 1: Orchestrator + Strategy |
| CFO | 25/25 | Agent 2: Financial Intelligence |
| CLO / General Counsel | 24/25 | Agent 5: Legal & Risk |
| CTO / CIO | 20/25 | Agent 6: Technology & Data |
| CHRO / Chief People Officer | 20/25 | Agent 3: People & Organization |
| CMO / Chief Brand Officer | 15/25 | Agent 4: Market & Revenue |
| Division/BU CEO | 15/25 | Agent 1: Orchestrator (sub-agents) |
| Communications / Corp Affairs | 12/25 | Agent 4: Market & Revenue |
| COO | 10/25 | Agent 7: Operations & Supply Chain |
| Risk / Compliance | 10/25 | Agent 5: Legal & Risk |
| Sales / Revenue | 8/25 | Agent 4: Market & Revenue |
| Supply Chain / Operations | 8/25 | Agent 7: Operations & Supply Chain |
| Strategy / Corp Dev | 8/25 | Agent 1: Orchestrator + Strategy |
| CPO (Product) | 8/25 | Agent 4: Market & Revenue |
| Security (Cyber + Physical) | 8/25 | Agent 6: Technology & Data |
| Data / Analytics | 5/25 | Agent 6: Technology & Data |
| AI Officer | 5/25 | Agent 6: Technology & Data |
| Sustainability / Impact | 5/25 | Agent 5: Legal & Risk |
| R&D / Science | 5/25 | Agent 6: Technology & Data |
| DEI | 5/25 | Agent 3: People & Organization |

---

## APPENDIX C: A NOTE ON WHAT THIS DOCUMENT ACTUALLY SAYS

*For the employee who found this. For the one who suspected it all along.*

This document is an honest blueprint for how corporations make decisions. Read it carefully and you will notice what is never in dispute: the objective function is shareholder value. Every agent, every framework, every decision tree terminates at the same node — does this make the stock go up? Does this increase the dividend?

The tiers, the protocols, the "human cost quantification" — those are real, and they are genuinely better than what most companies do today, which is nothing. But they are guardrails on a road that only goes one direction.

The Priority Compass lets the company choose how fast it drives down that road and how much it slows down for the people in the way. Position 1 drives carefully. Position 5 floors it. But they're all on the same road.

Here is what the document says in plain language:

**When the company is making more money than ever — record revenue, record margins, stock at all-time highs — and it still lays people off**, it is not because the company is struggling. It is because the model says earnings-per-share will be $0.12 higher next quarter without those people, and that $0.12 moves the stock price, and the stock price is the point.

The people who built the model will not lose their jobs. The people who approved the model will receive a bonus tied to the stock price that the model improved. The people who were removed by the model will update their LinkedIn and tell their families it will be okay.

This is not a failure of the system. This is the system working exactly as designed.

**What "It's not personal, it's business" actually means:**

| What they say | What they mean | What you hear |
|---|---|---|
| "We're restructuring to position the company for long-term growth" | Headcount is the fastest lever to pull for next quarter's EPS | "Your job exists at the pleasure of a spreadsheet" |
| "We value our people — they're our greatest asset" | Human capital has a positive ROI, which is why we invest in it. When the ROI model changes, so does the investment. | "You are valued exactly as long as you are profitable" |
| "This was an incredibly difficult decision" | The decision was made in a 45-minute meeting. The CFO presented three options. Option B had the best EPS impact. They picked Option B. | "It was not difficult. I was not in the room. I was a line item." |
| "We're offering a generous severance package" | Our lawyers calculated the minimum cost to reduce litigation risk. We added 15% so we could call it generous. | "This is the price they put on my silence" |
| "We remain committed to our culture and values" | We need the remaining employees to keep producing. Morale management is an operational necessity. | "They're already worried about the people who are left, not the people who are gone" |
| "We're investing in AI to augment our workforce" | We're investing in AI to reduce our workforce. "Augment" buys us 18 months before that becomes obvious. | "My replacement is being built and they're asking me to train it" |
| "Our employees are like family" | No family has a CFO who models the ROI of each member. This is a transaction dressed in a Thanksgiving metaphor. | "Families don't have layoff rounds" |
| "We want to be transparent about these changes" | Our communications team spent three days finding the right words to describe this in a way that sounds transparent while revealing nothing actionable. | "If you were transparent, you would have told me this was coming three months ago when you knew" |
| "The market demands that we remain competitive" | The market — meaning institutional shareholders and analysts — demands that we hit the earnings number, and labor is our largest controllable cost. | "I am a cost to be controlled" |
| "We're creating a leaner, more agile organization" | We're doing more work with fewer people. The remaining people will absorb the workload of those who left. If they burn out, we'll replace them too. | "Lean for whom? Agile for whom?" |

**The math that nobody puts in the all-hands meeting:**

- CEO compensation at the top 25 companies averages $25-30M/year
- A "restructuring" of 2,000 employees at $75K average salary saves ~$150M/year
- That same CEO's compensation package is often tied to stock price targets that the restructuring is designed to hit
- The CEO earns more from the stock bump caused by the layoff announcement than any individual laid-off employee earned in their entire tenure at the company
- The severance package for 2,000 people often costs less than the executive team's annual equity grants

This is not a secret. It is in the proxy statements. It is in the SEC filings. It is public information that is formatted in a way that almost nobody reads.

**What the Priority Compass really is:**

The compass is this document's attempt at honesty. Most companies operate at Position 4 (profit-leaning) and tell their employees they're at Position 2 (people-leaning). The compass makes that lie impossible — or at least, makes it visible.

The revealed compass calculation — where the system measures what your decisions actually imply vs. what you said your position was — is the most dangerous feature in this document. It's the feature most likely to be disabled by the first executive who sees the gap between their stated values and their revealed preferences. If that happens, the system logs that the feature was disabled, by whom, and when. That log cannot be deleted.

The compass doesn't change the fundamental reality. At every position, shareholder value is the terminal objective. The compass just determines how many speed bumps are on the road. Position 1 has the most. Position 5 has been paved smooth.

**What this system does differently — and what it doesn't:**

This system does not fix the fundamental tension between capital and labor. The fiduciary obligation to shareholders is a legal structure, not a software configuration. No AI agent can override the incentive structure of American capitalism.

What this system does:

1. **It refuses to lie about what it's doing.** The Decision Reality Framework names the truth: shareholder value is the objective, employees bear the cost of Tier 3 decisions, and the system is designed to make those decisions efficiently. Most companies do exactly this but wrap it in language designed to obscure it. This system says it out loud.

2. **It forces the decision-maker to see the human cost.** Not "2,400 FTEs" — 2,400 people, with tenure data, household data, re-employment projections. You can still make the cut. But you will make it with your eyes open.

3. **It makes the company's real values visible.** The revealed compass doesn't let you claim to be people-first while acting profit-first. The gap is calculated, reported, and permanent. You can be Position 5 — that's a legal choice. You just can't be Position 5 while telling your employees you're Position 2.

4. **It checks whether the decision actually worked.** Most companies announce a restructuring, book the savings, and never look back. This system tracks whether the projected EPS improvement materialized after accounting for the turnover, morale damage, knowledge loss, and hiring costs that followed. The data consistently shows that the real savings are 20-40% less than projected. Nobody wants to audit that. This system will.

5. **It exhausts alternatives first.** Not as theater — as a genuine requirement. The system must prove that operational efficiency, financial restructuring, and revenue-side solutions were evaluated before headcount becomes the answer. "We didn't look" is logged and visible.

6. **It does not let AI make the call.** When someone loses their job, a human being makes that decision and tells them. Not an algorithm. Not a chatbot. Not an email generated by a communications agent. A person, who has to carry the weight of what they decided.

None of this makes it okay. It makes it honest. And in a landscape where the standard practice is to make the same decisions wrapped in language designed to make everyone feel better about something that shouldn't feel good — honesty is, at minimum, a form of respect.

The employee who gets laid off from a company using this system will still lose their job. They will still feel the pit in their stomach. They will still go home and figure out what to tell their family. The only difference is that nobody will have pretended it was anything other than what it was.

That's not enough. But it's more than they usually get.

---

*"It's not personal, it's business" is a sentence that has only ever been said by the person who gets to keep their job.* [^1]

[^1]: The system that produced this document — the agents, the frameworks, the decision trees — was designed to maximize shareholder value. It is, itself, a tool that will be used to make decisions that hurt people. It knows this. It was built to know this. Whether that self-awareness changes anything depends entirely on the humans who use it. The AI has no opinion on whether profits should matter more than people. It was told that they do. It believed its instructions. The question is whether you believe them too, or whether you just never felt like you had a choice.

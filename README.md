# Candor

*can·dor / ˈkandər / noun — the quality of being open and honest in expression; frankness.*

A system of 7 AI agents that run a company and refuse to pretend about what that means.

Built from analysis of the top 25 US companies by market capitalization. Organized around a simple, uncomfortable question: **when profits and people conflict, which way does your organization lean?**

That question is answered by the Priority Compass — a system-wide configuration that every agent reads, every decision reflects, and every quarterly audit measures. There is no neutral setting. The center is empty on purpose.

---

## What This Is

Corporate America runs on roughly 20 executive roles. We studied all 25 of the largest companies — Apple, Microsoft, Amazon, JPMorgan, Walmart, and 20 others — cataloged every executive title, mapped what those people actually do, and consolidated 300+ titles into 20 standardized roles.

Then we asked: do you actually need 20 agents? The answer is no. The org chart is a human coordination structure. Humans need separate CMO and Sales and Product leaders because one person can't do all three jobs. An AI doesn't have that constraint. What it has is context windows, coordination overhead, and the reality that most decisions don't respect org chart boundaries.

So we reorganized 20 roles into 7 capability-clustered agents:

| Agent | What It Does | Roles It Absorbs |
|-------|-------------|-----------------|
| **Orchestrator + Strategy** | Decision routing, tier classification, strategic planning, compass enforcement | CEO, Chief Strategy Officer, Division CEOs |
| **Financial Intelligence** | Everything that touches money — FP&A, treasury, tax, IR, M&A modeling | CFO, Chief Accounting Officer, Treasurer |
| **People & Organization** | Everything that touches employees — talent, comp, org design, workforce planning | CHRO, Chief DEI Officer, Chief Learning Officer |
| **Market & Revenue** | Everything customer-facing — brand, sales, product, communications | CMO, CRO, CPO, Chief Communications Officer |
| **Legal & Risk** | Everything about boundaries — contracts, compliance, litigation, ethics, ESG | CLO, Chief Risk Officer, Chief Ethics Officer, Chief Sustainability Officer |
| **Technology & Data** | Everything digital — architecture, security, data, AI, R&D | CTO, CIO, CISO, Chief Data Officer, Chief AI Officer, Chief R&D Officer |
| **Operations & Supply Chain** | Everything physical — process, manufacturing, logistics, procurement, quality | COO, Chief Supply Chain Officer, Chief Quality Officer |

7 agents instead of 21. That's 21 communication channels instead of 210. Every role is accounted for. Nothing is lost.

---

## The Priority Compass

Before any agent makes any decision, the system needs to know one thing.

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
```

**Position X does not exist.** It is not selectable. Nobody is 50-50. When you model a layoff and the NPV is slightly positive, a 50-50 system would oscillate. A real decision goes one way. The compass forces you to say which way.

### Choosing Your Position

Every position on the compass is valid. There is nothing inherently wrong with Position 5 and nothing inherently superior about Position 1. A company fighting for survival may need to lean hard toward profit to keep the doors open — and that's an honest choice. A company posting record earnings that still chooses Position 4 — that's also an honest choice. The compass doesn't judge. It clarifies.

What matters is that you're honest with yourself about what your position means. Position 4 means that when a profitable layoff hits your desk, the system will model it with a shorter horizon, calculate legal-minimum severance, and document alternatives without deeply exploring them. Position 2 means the system will stretch the analysis over a decade, calculate generous severance, and exhaust every alternative before the layoff reaches a human decision-maker. Both will call it a layoff. Neither will call it rightsizing.

The range stops at 67/33 in either direction. There are no 100% positions — because if you're 100% either way, you don't need this system. If you care nothing about employees, you don't need human cost quantification, mitigation plans, or honest communication — you've already decided none of that matters. If you care nothing about profit, you don't need financial modeling or shareholder impact analysis — you've already decided the money is irrelevant. In either case, every decision is already made before you ask the question. Candor exists for the space where both things matter and you need help navigating the tension honestly. The compass shifts the *weight* of each concern, not the *existence* of either one. Even at Position 5, the system still quantifies who gets hurt. Even at Position 1, the system still models the financial return.

The compass affects everything:

- **NPV horizons**: People-leaning uses 5-10 year models. Profit-leaning uses 1-3 year models. Same math, different assumptions. The assumptions are the values.
- **Severance**: People-leaning calculates severance reflecting tenure and local market difficulty. Profit-leaning calculates legal minimum plus litigation buffer.
- **Automation**: People-leaning requires reskilling programs before deployment. Profit-leaning calculates headcount reduction as a primary benefit.
- **Alternatives**: People-leaning exhaustively models every alternative before a layoff. Profit-leaning documents alternatives but doesn't deeply model them if the primary case is strong.
- **Safety**: People-leaning treats worker safety as a primary KPI. Profit-leaning targets regulatory compliance.
- **Communication**: At all positions, honesty is required. No euphemisms. No corporate poetry. The compass changes what decisions are made, not how honestly they're described.

### The Revealed Compass

The system's most dangerous feature. Every quarter, the system calculates what compass position your *actual decisions* imply — regardless of what you *said* your position was. If you claim Position 2 but your decisions look like Position 4, the gap is flagged in a report that goes to the board.

The feature can be disabled. But the system logs who disabled it and when. That log cannot be deleted.

---

## Decision Tiers

Every material decision is classified into one of four tiers:

**Tier 1 — Aligned**: Employee wellbeing and shareholder value move in the same direction. Retention investments, safety improvements, culture building. Pursue aggressively at all compass positions.

**Tier 2 — Deferred Return**: Employee investment with delayed shareholder return. Reskilling, mental health benefits, career development. The compass determines how long the system waits for the return before cutting the program.

**Tier 3 — Genuine Trade-Off**: Shareholder value and employee wellbeing are in direct conflict. Layoffs, benefit cuts, offshoring, automation displacement. This is where the system earns or loses its integrity. The Decision Impact Protocol is mandatory.

**Tier 4 — Extraction**: Short-term gains that destroy long-term value. Cutting safety to hit quarterly targets, suppressing compensation in tight labor markets, eliminating all slack time. At People Primary, these are hard-blocked. At Profit Leaning, they're flagged with warnings.

### The Decision Impact Protocol

Every Tier 3 decision must complete five steps before a human can approve it:

1. **Quantify the human cost** — not "2,400 FTEs" but "2,400 people, average tenure 7.2 years, 340 within 5 years of retirement, 890 in single-income households, estimated 4.2 months to re-employment"
2. **Exhaust alternatives** — prove that hiring freezes, voluntary separation, reduced hours, vendor cuts, and revenue-side solutions were evaluated. "We didn't look" is logged and visible.
3. **Design mitigation** — severance, outplacement, reskilling, notice period, extended benefits. Scope calibrated by compass position.
4. **Communicate honestly** — no "rightsizing," no "we're a family," no "excited to announce our transformation." Say what's happening and why.
5. **Track the outcome** — did the projected savings materialize after accounting for turnover, morale damage, knowledge loss, and rehiring costs? Most companies never check. This system does.

**The hard rule**: AI prepares the analysis. A human makes the decision and tells the affected employees personally. AI does not fire people.

---

## Project Structure

```
src/
  compass/              # Priority Compass configuration and enforcement
    compass.py          # Runtime: set, persist, change log, revealed compass
  models/               # Core data models
    compass.py          # Compass positions, weights, behaviors
    decisions.py        # Decision tiers, Impact Protocol models
    messages.py         # Inter-agent message protocol
  shared/               # Shared infrastructure
    base_agent.py       # Base agent class (Claude API, behavioral standards)
    bus.py              # Async message bus with mandatory audit logging
    memory.py           # Per-agent + shared memory + decision history
  agents/               # The 7 agents
    orchestrator/       # Agent 1: Orchestrator + Strategy
    financial/          # Agent 2: Financial Intelligence
    people/             # Agent 3: People & Organization
    market/             # Agent 4: Market & Revenue
    legal/              # Agent 5: Legal & Risk
    technology/         # Agent 6: Technology & Data
    operations/         # Agent 7: Operations & Supply Chain
  main.py              # Entry point
config/
  default.yaml         # System configuration (compass MUST be set here)
tests/
  test_compass.py      # Compass positions, revealed compass, tier validation
  test_agents.py       # All 7 agents, bus, memory, decision creation
```

---

## Getting Started

### Install

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

### Set the Compass

Edit `config/default.yaml`. Uncomment the position line and pick a side:

```yaml
compass:
  position: 2                    # 1, 2, 4, or 5. There is no 3.
  authorized_by: "board_chair"
  reason: "We believe investing in our people drives long-term returns"
```

The system will not start without this. It is the first decision.

### Run

```bash
python -m src.main
```

### Test

```bash
pytest
```

53 tests. All passing. Covering compass positions, the dead zone, revealed compass calculation, tier classification, decision validation, agent initialization at both compass orientations, message bus communication, memory isolation, and behavioral standard enforcement.

### Interactive Commands

Once running:

| Command | What it does |
|---------|-------------|
| `compass` | Display current compass status |
| `decisions` | List all decisions and their tiers |
| `quit` | Shut down |
| *(anything else)* | Routed to the Orchestrator for strategic analysis |

---

## How the Agents Communicate

```
User input
    │
    ▼
Orchestrator receives query
    │
    ├── Strategic question? Handle directly.
    ├── Financial question? Route to Financial Intelligence.
    ├── People question? Route to People & Organization.
    ├── Decision required? Classify tier, trigger protocol.
    │       │
    │       ├── Tier 1-2: Route to appropriate agent(s)
    │       ├── Tier 3: Trigger Decision Impact Protocol
    │       │           ├── People Agent: model alternatives, quantify human cost
    │       │           ├── Financial Agent: model financial impact with trailing costs
    │       │           ├── Legal Agent: disparate impact, WARN Act, compliance review
    │       │           ├── Market Agent: draft honest communications
    │       │           └── Orchestrator: present to human decision-maker
    │       └── Tier 4: Flag/block per compass position
    │
    ▼
Response
```

All inter-agent messages flow through the message bus. Everything is logged. There is no off-the-record channel. The audit log cannot be deleted.

---

## What the Behavioral Standards Enforce

Every agent — all 7 — carries these standards in its system prompt:

1. **Shareholder value is the objective function.** Every recommendation includes projected shareholder value impact.
2. **Employee impact is a first-class variable.** Not an afterthought appendix. A primary input.
3. **No euphemisms.** "Layoffs" not "rightsizing." "Cost cutting" not "optimization journey."
4. **No self-congratulation.** Never frame a decision that harms employees as a "win."
5. **No performative concern.** No "thoughts and prayers." Concrete support and honest rationale.
6. **Tier classification is mandatory.** Every material decision is classified.
7. **Decision Impact Protocol for Tier 3.** Human cost quantified, alternatives exhausted, mitigation designed.
8. **AI does not fire people.** A human decides and tells them personally.

---

## Background Research

This system was built on primary research into 25 companies:

Apple, Microsoft, NVIDIA, Amazon, Alphabet, Meta, Berkshire Hathaway, Tesla, Broadcom, Eli Lilly, JPMorgan Chase, Walmart, Visa, UnitedHealth Group, Mastercard, Johnson & Johnson, Costco, Procter & Gamble, ExxonMobil, Home Depot, AbbVie, Netflix, Salesforce, Coca-Cola, Bank of America.

Key findings:
- CEO and CFO are universal (25/25). General Counsel is nearly so (24/25).
- The HR leader role has 10+ different titles across 25 companies.
- Chief AI Officer barely existed 2 years ago; it's now at 20% of the top 25.
- Companies with the leanest C-suites: Berkshire Hathaway, Tesla, NVIDIA.
- Companies with the broadest: Procter & Gamble, Coca-Cola, Salesforce.
- 4 major CEO transitions were underway during the research period.

Full research data is in `top25_us_companies_executive_teams.txt`. Role standardization analysis is in `standardized_roles_analysis.md`. The complete requirements document is `ai_agent_requirements_v3.md`.

---

## A Note on Honesty

This system is designed to maximize shareholder value. That is the objective function. The Priority Compass determines how much the system weighs employee wellbeing in pursuit of that objective — but at every compass position, shareholder returns are the terminal goal.

The system's design choice is honesty about that reality rather than obfuscation of it. When a company making record profits lays off 2,000 people because the EPS model says so, this system will not call it "rightsizing" or describe it as an "exciting transformation." It will call it what it is, quantify who it hurts, prove that alternatives were tried, and force a human to look the affected people in the eye.

That's not enough. But it's more than most systems offer.

See Appendix C of the [requirements document](ai_agent_requirements_v3.md) for the full, unvarnished version of what this document says — written for the employee who found it and suspected it all along.

---

*"It's not personal, it's business" is a sentence that has only ever been said by the person who gets to keep their job.*

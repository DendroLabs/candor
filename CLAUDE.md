# Candor

## Project Overview

Candor is an AI agent system that replicates the work of corporate executive leadership, built from analysis of the top 25 US companies by market capitalization. The system uses 7 capability-clustered agents (not 21 role-mapped agents) coordinated by a Priority Compass that makes the profit-vs-people orientation explicit and auditable. The name is the design philosophy: refuse to pretend.

## Architecture

**7 Core Agents:**
1. **Orchestrator + Strategy** — decision routing, tier classification, strategic planning, compass enforcement
2. **Financial Intelligence** — FP&A, treasury, tax, IR, M&A finance, reporting
3. **People & Organization** — talent, comp, org design, DEI (integrated), workforce planning
4. **Market & Revenue** — brand, marketing, sales, product, communications, government affairs
5. **Legal & Risk** — contracts, compliance, litigation, IP, privacy, ethics, ESG/sustainability
6. **Technology & Data** — architecture, infrastructure, security, data governance, AI, R&D
7. **Operations & Supply Chain** — process optimization, manufacturing, logistics, procurement, quality

**Priority Compass:** System-wide setting (Positions 1-5, no middle) that controls how agents weight profit vs. people in every decision. Revealed compass feature audits actual decisions against stated position.

**Decision Tiers:** Every material decision classified as Tier 1 (aligned), Tier 2 (deferred return), Tier 3 (genuine trade-off), or Tier 4 (extraction). Tier 3 triggers the Decision Impact Protocol. Tier 4 is flagged and resisted.

## Key Documents

- `ai_agent_requirements_v3.md` — Full requirements document (canonical, v3)
- `ai_agent_requirements_document.md` — Legacy v2 (21-agent model, superseded)
- `standardized_roles_analysis.md` — Role mapping research
- `top25_us_companies_executive_teams.txt` — Raw company research data
- `src/` — Agent implementation source code

## Tech Stack

- **Language:** Python 3.12+
- **AI SDK:** Anthropic Claude API (`anthropic` SDK)
- **Agent Framework:** Custom, built on Claude tool-use
- **Data Layer:** SQLite for local dev, PostgreSQL for production
- **Message Bus:** In-process async queues (local dev), Redis Streams (production)
- **Config:** YAML for compass and agent configuration
- **Testing:** pytest

## Project Structure

```
src/
  shared/           # Shared infrastructure (memory, comms bus, tools, config)
  compass/          # Priority Compass configuration and enforcement
  agents/           # Agent implementations
    orchestrator/   # Agent 1: Orchestrator + Strategy
    financial/      # Agent 2: Financial Intelligence
    people/         # Agent 3: People & Organization
    market/         # Agent 4: Market & Revenue
    legal/          # Agent 5: Legal & Risk
    technology/     # Agent 6: Technology & Data
    operations/     # Agent 7: Operations & Supply Chain
  models/           # Data models and schemas
  api/              # Human escalation interface / dashboard API
tests/
config/             # YAML configuration files
```

## Development Commands

```bash
# Install dependencies
pip install -e ".[dev]"

# Run tests
pytest

# Run a specific agent in isolation
python -m src.agents.orchestrator

# Run the full system
python -m src.main

# Check compass status
python -m src.compass.status
```

## Conventions

- Agents communicate via structured messages on the shared bus
- Every decision is logged with tier classification, compass position at time of decision, and outcome
- No euphemisms in internal agent communications — plain language only
- Human gates are enforced at the framework level, not per-agent
- Sub-agents are ephemeral — spawned for a task, return results, terminate
- The compass setting is immutable at runtime; changes require explicit reconfiguration with audit logging

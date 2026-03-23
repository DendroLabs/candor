"""Candor — Main Entry Point.

The compass must be set before anything else.
This is the first decision. Everything follows from it.
"""

import asyncio
import logging
import sys
from pathlib import Path

import yaml

from src.compass.compass import PriorityCompass, CompassNotSetError
from src.models.compass import CompassPosition
from src.shared.bus import MessageBus
from src.shared.memory import MemoryStore

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(name)s] %(levelname)s: %(message)s",
)
logger = logging.getLogger("executive")


def load_config(config_path: str = "config/default.yaml") -> dict:
    with open(config_path) as f:
        return yaml.safe_load(f)


def setup_compass(config: dict, compass_path: Path) -> PriorityCompass:
    """Initialize the Priority Compass.

    The compass must be set before any agent can operate.
    """
    compass = PriorityCompass(compass_path)

    if not compass.is_set:
        compass_config = config.get("compass", {})
        position_value = compass_config.get("position")

        if position_value is None:
            logger.error(
                "\n"
                "=" * 70 + "\n"
                "  THE PRIORITY COMPASS HAS NOT BEEN SET.\n"
                "\n"
                "  This is the first decision the board must make.\n"
                "  No agent can operate until the compass is configured.\n"
                "\n"
                "  Edit config/default.yaml and set compass.position to:\n"
                "    1 — People Primary  (67% people / 33% profit)\n"
                "    2 — People Leaning  (58% people / 42% profit)\n"
                "    4 — Profit Leaning  (58% profit / 42% people)\n"
                "    5 — Profit Primary  (67% profit / 33% people)\n"
                "\n"
                "  There is no position 3. The center is empty on purpose.\n"
                "  Nobody is 50-50. Pick a side.\n"
                "=" * 70
            )
            sys.exit(1)

        if position_value == 3:
            logger.error(
                "Position 3 does not exist. The center is empty on purpose. "
                "Nobody is 50-50. Pick a side."
            )
            sys.exit(1)

        compass.set_position(
            position=CompassPosition(position_value),
            authorized_by=compass_config.get("authorized_by", "initial_setup"),
            reason=compass_config.get("reason", "Initial compass configuration"),
            board_resolution_ref=compass_config.get("board_resolution_ref"),
        )

    return compass


async def run(config: dict):
    """Start the agent system."""
    data_config = config.get("data", {})
    compass_path = Path(data_config.get("compass_path", "./data/compass.json"))
    memory_path = Path(data_config.get("memory_path", "./data/memory"))

    # Step 1: The compass comes first
    compass = setup_compass(config, compass_path)
    logger.info(f"\n{compass.get_status_report()}")

    # Step 2: Shared infrastructure
    bus = MessageBus()
    memory = MemoryStore(memory_path)

    # Step 3: Initialize agents
    agents_config = config.get("agents", {})
    default_model = agents_config.get("model", "claude-sonnet-4-6")
    active_agents = []

    if agents_config.get("orchestrator", {}).get("enabled", True):
        from src.agents.orchestrator.agent import OrchestratorAgent
        orchestrator_model = agents_config.get("orchestrator", {}).get("model", default_model)
        orchestrator = OrchestratorAgent(compass, bus, memory, model=orchestrator_model)
        active_agents.append(orchestrator)
        logger.info("Agent 1 — Orchestrator + Strategy: ONLINE")

    if agents_config.get("financial", {}).get("enabled", True):
        from src.agents.financial.agent import FinancialIntelligenceAgent
        financial = FinancialIntelligenceAgent(compass, bus, memory, model=default_model)
        active_agents.append(financial)
        logger.info("Agent 2 — Financial Intelligence: ONLINE")

    if agents_config.get("people", {}).get("enabled", False):
        from src.agents.people.agent import PeopleOrganizationAgent
        people = PeopleOrganizationAgent(compass, bus, memory, model=default_model)
        active_agents.append(people)
        logger.info("Agent 3 — People & Organization: ONLINE")

    if agents_config.get("market", {}).get("enabled", False):
        from src.agents.market.agent import MarketRevenueAgent
        market = MarketRevenueAgent(compass, bus, memory, model=default_model)
        active_agents.append(market)
        logger.info("Agent 4 — Market & Revenue: ONLINE")

    if agents_config.get("legal", {}).get("enabled", False):
        from src.agents.legal.agent import LegalRiskAgent
        legal = LegalRiskAgent(compass, bus, memory, model=default_model)
        active_agents.append(legal)
        logger.info("Agent 5 — Legal & Risk: ONLINE")

    if agents_config.get("technology", {}).get("enabled", True):
        from src.agents.technology.agent import TechnologyDataAgent
        technology = TechnologyDataAgent(compass, bus, memory, model=default_model)
        active_agents.append(technology)
        logger.info("Agent 6 — Technology & Data: ONLINE")

    if agents_config.get("operations", {}).get("enabled", False):
        from src.agents.operations.agent import OperationsSupplyChainAgent
        operations = OperationsSupplyChainAgent(compass, bus, memory, model=default_model)
        active_agents.append(operations)
        logger.info("Agent 7 — Operations & Supply Chain: ONLINE")

    logger.info(
        f"\nSystem initialized: {len(active_agents)} agents active "
        f"at compass position {compass.position.value} ({compass.position.label})"
    )

    # Step 4: Run the interactive loop
    print("\n" + "=" * 70)
    print("  CANDOR")
    print(f"  Compass: Position {compass.position.value} — {compass.position.label}")
    print(f"  Active agents: {', '.join(a.role.value for a in active_agents)}")
    print("=" * 70)
    print("\nEnter a prompt to interact with the system. Type 'quit' to exit.")
    print("Type 'compass' to see compass status.")
    print("Type 'decisions' to see decision history.\n")

    # For now, route all input through the Orchestrator
    orchestrator = next((a for a in active_agents if a.role.value == "orchestrator"), None)
    if not orchestrator:
        logger.error("Orchestrator not available. Cannot proceed.")
        return

    while True:
        try:
            user_input = input("\n> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nShutting down.")
            break

        if not user_input:
            continue
        if user_input.lower() == "quit":
            break
        if user_input.lower() == "compass":
            print(compass.get_status_report())
            continue
        if user_input.lower() == "decisions":
            decisions = memory.get_all_decisions()
            if not decisions:
                print("No decisions recorded yet.")
            for d in decisions:
                print(f"  [{d.tier.name}] {d.title} — {d.status}")
            continue

        # Route through the Orchestrator
        response = await orchestrator.think(user_input)
        print(f"\n{response}")


def main():
    config = load_config()
    asyncio.run(run(config))


if __name__ == "__main__":
    main()

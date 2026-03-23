"""Memory Store — persistent knowledge for the agent system.

Each agent has its own domain memory plus access to shared company context.
Decision history is permanent and tied to compass position at time of decision.
"""

import json
import logging
from datetime import datetime
from pathlib import Path
from typing import Any

from src.models.decisions import AgentRole, Decision

logger = logging.getLogger(__name__)


class MemoryStore:
    """File-backed memory store.

    Local dev uses JSON files. Production would use a real database.
    """

    def __init__(self, base_path: Path):
        self._base = base_path
        self._base.mkdir(parents=True, exist_ok=True)
        self._shared_path = self._base / "shared"
        self._shared_path.mkdir(exist_ok=True)
        self._decisions_path = self._base / "decisions"
        self._decisions_path.mkdir(exist_ok=True)

    def get_agent_memory(self, agent: AgentRole) -> dict[str, Any]:
        """Load an agent's domain-specific memory."""
        path = self._base / f"{agent.value}.json"
        if path.exists():
            return json.loads(path.read_text())
        return {}

    def save_agent_memory(self, agent: AgentRole, data: dict[str, Any]):
        """Save an agent's domain-specific memory."""
        path = self._base / f"{agent.value}.json"
        path.write_text(json.dumps(data, indent=2, default=str))

    def get_shared_context(self, key: str) -> Any:
        """Read from shared company context (strategy, org chart, policies, etc.)."""
        path = self._shared_path / f"{key}.json"
        if path.exists():
            return json.loads(path.read_text())
        return None

    def save_shared_context(self, key: str, data: Any):
        """Write to shared company context."""
        path = self._shared_path / f"{key}.json"
        path.write_text(json.dumps(data, indent=2, default=str))

    def save_decision(self, decision: Decision):
        """Save a decision to the permanent record.

        Decisions are never deleted. They can be updated with outcomes.
        """
        path = self._decisions_path / f"{decision.id}.json"
        path.write_text(decision.model_dump_json(indent=2))
        logger.info(f"Decision saved: {decision.id} — {decision.title} (Tier {decision.tier})")

    def get_decision(self, decision_id: str) -> Decision | None:
        path = self._decisions_path / f"{decision_id}.json"
        if path.exists():
            return Decision.model_validate_json(path.read_text())
        return None

    def get_all_decisions(
        self,
        since: datetime | None = None,
        tier: int | None = None,
    ) -> list[Decision]:
        """Query all decisions. Optionally filter by date and tier."""
        decisions = []
        for path in self._decisions_path.glob("*.json"):
            d = Decision.model_validate_json(path.read_text())
            if since and d.created_at < since:
                continue
            if tier is not None and d.tier != tier:
                continue
            decisions.append(d)
        return sorted(decisions, key=lambda d: d.created_at)

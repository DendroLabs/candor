"""Message Bus — inter-agent communication.

Everything on this bus is logged. There is no off-the-record channel.
"""

import asyncio
import logging
from collections import defaultdict
from datetime import datetime

from src.models.messages import Message, AgentRole, MessagePriority, MessageType

logger = logging.getLogger(__name__)


class MessageBus:
    """Async message bus for agent-to-agent communication.

    In local dev, this is in-process async queues.
    In production, swap to Redis Streams or similar.
    """

    def __init__(self):
        self._queues: dict[AgentRole, asyncio.Queue[Message]] = {}
        self._broadcast_subscribers: set[AgentRole] = set()
        self._audit_log: list[Message] = []
        self._handlers: dict[AgentRole, list] = defaultdict(list)

    def register_agent(self, role: AgentRole):
        """Register an agent to receive messages."""
        self._queues[role] = asyncio.Queue()
        self._broadcast_subscribers.add(role)
        logger.info(f"Agent registered on bus: {role}")

    async def send(self, message: Message):
        """Send a message to a specific agent or broadcast to all."""
        # Everything is logged. This line cannot be bypassed.
        self._audit_log.append(message)
        logger.info(
            f"[{message.priority.upper()}] {message.sender} -> "
            f"{message.recipient or 'ALL'}: {message.subject}"
        )

        if message.recipient is None:
            # Broadcast
            for role in self._broadcast_subscribers:
                if role != message.sender:
                    await self._queues[role].put(message)
        else:
            if message.recipient in self._queues:
                await self._queues[message.recipient].put(message)
            else:
                logger.warning(f"Message to unregistered agent: {message.recipient}")

    async def receive(self, role: AgentRole, timeout: float = None) -> Message | None:
        """Receive next message for an agent."""
        if role not in self._queues:
            raise ValueError(f"Agent {role} not registered on bus")
        try:
            if timeout:
                return await asyncio.wait_for(self._queues[role].get(), timeout)
            return await self._queues[role].get()
        except asyncio.TimeoutError:
            return None

    def get_pending_count(self, role: AgentRole) -> int:
        if role in self._queues:
            return self._queues[role].qsize()
        return 0

    def get_audit_log(
        self,
        since: datetime | None = None,
        sender: AgentRole | None = None,
        recipient: AgentRole | None = None,
        message_type: MessageType | None = None,
    ) -> list[Message]:
        """Query the audit log. This log cannot be deleted."""
        results = self._audit_log
        if since:
            results = [m for m in results if m.timestamp >= since]
        if sender:
            results = [m for m in results if m.sender == sender]
        if recipient:
            results = [m for m in results if m.recipient == recipient]
        if message_type:
            results = [m for m in results if m.message_type == message_type]
        return results

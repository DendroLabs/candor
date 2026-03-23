"""Message models for inter-agent communication.

Structured messages on the shared bus. No back-channel.
Everything is logged. Everything is auditable.
"""

from enum import StrEnum
from pydantic import BaseModel, Field
from datetime import datetime
from uuid import uuid4

from src.models.decisions import AgentRole


class MessagePriority(StrEnum):
    LOW = "low"
    NORMAL = "normal"
    HIGH = "high"
    CRITICAL = "critical"  # crisis, security incident, Tier 4 flag


class MessageType(StrEnum):
    # Standard communication
    REQUEST = "request"           # ask another agent for analysis/data
    RESPONSE = "response"         # reply to a request
    BROADCAST = "broadcast"       # strategy update, policy change, compass change

    # Decision flow
    DECISION_PROPOSAL = "decision_proposal"
    DECISION_REVIEW = "decision_review"
    DECISION_ESCALATION = "decision_escalation"
    TIER3_PROTOCOL = "tier3_protocol"  # Decision Impact Protocol trigger

    # Alerts
    RISK_ALERT = "risk_alert"
    COMPASS_DRIFT = "compass_drift"  # revealed vs stated gap
    HUMAN_ESCALATION = "human_escalation"


class Message(BaseModel):
    """A message on the inter-agent bus."""
    id: str = Field(default_factory=lambda: str(uuid4()))
    timestamp: datetime = Field(default_factory=datetime.utcnow)

    sender: AgentRole
    recipient: AgentRole | None = None  # None = broadcast to all
    priority: MessagePriority = MessagePriority.NORMAL
    message_type: MessageType

    subject: str
    body: str  # plain language — no corporate euphemisms even between agents
    data: dict = Field(default_factory=dict)  # structured payload

    # Threading
    in_reply_to: str | None = None
    decision_id: str | None = None  # link to a Decision if relevant

    # Audit
    logged: bool = True  # all messages logged by default; cannot be set to False

"""Tests for all 7 agents — initialization, system prompts, and compass integration.

These tests verify that agents initialize correctly, respect the compass,
and produce appropriate system prompts at different compass positions.
They do NOT call the Claude API — that's for integration tests.
"""

import tempfile
from pathlib import Path

import pytest

from src.compass.compass import PriorityCompass
from src.models.compass import CompassPosition
from src.models.decisions import AgentRole
from src.shared.bus import MessageBus
from src.shared.memory import MemoryStore

from src.agents.orchestrator.agent import OrchestratorAgent
from src.agents.financial.agent import FinancialIntelligenceAgent
from src.agents.people.agent import PeopleOrganizationAgent
from src.agents.market.agent import MarketRevenueAgent
from src.agents.legal.agent import LegalRiskAgent
from src.agents.technology.agent import TechnologyDataAgent
from src.agents.operations.agent import OperationsSupplyChainAgent


@pytest.fixture
def tmp_dir(tmp_path):
    return tmp_path


@pytest.fixture
def compass_people(tmp_dir):
    c = PriorityCompass(tmp_dir / "compass_people.json")
    c.set_position(CompassPosition(2), authorized_by="board", reason="People leaning test")
    return c


@pytest.fixture
def compass_profit(tmp_dir):
    c = PriorityCompass(tmp_dir / "compass_profit.json")
    c.set_position(CompassPosition(4), authorized_by="board", reason="Profit leaning test")
    return c


@pytest.fixture
def bus():
    return MessageBus()


@pytest.fixture
def memory(tmp_dir):
    return MemoryStore(tmp_dir / "memory")


# =============================================================================
# Agent initialization tests — all 7 agents at both compass positions
# =============================================================================

class TestAgentInitialization:

    def test_orchestrator_init(self, compass_people, bus, memory):
        agent = OrchestratorAgent(compass_people, bus, memory)
        assert agent.role == AgentRole.ORCHESTRATOR
        assert agent.compass_position == CompassPosition(2)

    def test_financial_init(self, compass_people, bus, memory):
        agent = FinancialIntelligenceAgent(compass_people, bus, memory)
        assert agent.role == AgentRole.FINANCIAL

    def test_people_init(self, compass_people, bus, memory):
        agent = PeopleOrganizationAgent(compass_people, bus, memory)
        assert agent.role == AgentRole.PEOPLE

    def test_market_init(self, compass_people, bus, memory):
        agent = MarketRevenueAgent(compass_people, bus, memory)
        assert agent.role == AgentRole.MARKET

    def test_legal_init(self, compass_people, bus, memory):
        agent = LegalRiskAgent(compass_people, bus, memory)
        assert agent.role == AgentRole.LEGAL

    def test_technology_init(self, compass_people, bus, memory):
        agent = TechnologyDataAgent(compass_people, bus, memory)
        assert agent.role == AgentRole.TECHNOLOGY

    def test_operations_init(self, compass_people, bus, memory):
        agent = OperationsSupplyChainAgent(compass_people, bus, memory)
        assert agent.role == AgentRole.OPERATIONS

    def test_all_agents_register_on_bus(self, compass_people, bus, memory):
        """All 7 agents register on the bus when initialized."""
        agents = [
            OrchestratorAgent(compass_people, bus, memory),
            FinancialIntelligenceAgent(compass_people, bus, memory),
            PeopleOrganizationAgent(compass_people, bus, memory),
            MarketRevenueAgent(compass_people, bus, memory),
            LegalRiskAgent(compass_people, bus, memory),
            TechnologyDataAgent(compass_people, bus, memory),
            OperationsSupplyChainAgent(compass_people, bus, memory),
        ]
        for role in AgentRole:
            assert role in bus._queues, f"Agent {role} not registered on bus"


# =============================================================================
# System prompt tests — verify compass affects behavior
# =============================================================================

class TestSystemPromptCompassIntegration:

    def test_financial_people_leaning_uses_longer_horizons(self, compass_people, bus, memory):
        agent = FinancialIntelligenceAgent(compass_people, bus, memory)
        prompt = agent.system_prompt()
        assert "3-5" in prompt  # NPV horizon years for position 2
        assert "INVESTMENTS" in prompt  # employee costs as investments

    def test_financial_profit_leaning_uses_shorter_horizons(self, compass_profit, bus, memory):
        agent = FinancialIntelligenceAgent(compass_profit, bus, memory)
        prompt = agent.system_prompt()
        assert "1-3" in prompt  # NPV horizon years for position 4
        assert "VARIABLE EXPENSES" in prompt  # employee costs as expenses

    def test_people_agent_severance_scales_with_compass(self, compass_people, bus, memory):
        agent = PeopleOrganizationAgent(compass_people, bus, memory)
        prompt = agent.system_prompt()
        assert "well above legal minimum" in prompt

    def test_people_agent_profit_leaning_severance(self, compass_profit, bus, memory):
        agent = PeopleOrganizationAgent(compass_profit, bus, memory)
        prompt = agent.system_prompt()
        assert "competitive market rate" in prompt

    def test_people_agent_reskilling_before_automation(self, compass_people, bus, memory):
        agent = PeopleOrganizationAgent(compass_people, bus, memory)
        prompt = agent.system_prompt()
        assert "Reskilling BEFORE automation" in prompt

    def test_technology_agent_ai_fairness_required(self, compass_people, bus, memory):
        agent = TechnologyDataAgent(compass_people, bus, memory)
        prompt = agent.system_prompt()
        assert "fairness audits REQUIRED" in prompt

    def test_technology_agent_profit_automation_honest(self, compass_profit, bus, memory):
        agent = TechnologyDataAgent(compass_profit, bus, memory)
        prompt = agent.system_prompt()
        assert "headcount reduction as a primary benefit" in prompt

    def test_operations_safety_people_leaning(self, compass_people, bus, memory):
        agent = OperationsSupplyChainAgent(compass_people, bus, memory)
        prompt = agent.system_prompt()
        assert "PRIMARY KPIs" in prompt
        assert "safety" in prompt.lower()

    def test_legal_labor_law_approach(self, compass_people, bus, memory):
        agent = LegalRiskAgent(compass_people, bus, memory)
        prompt = agent.system_prompt()
        assert "Exceed minimum requirements" in prompt

    def test_legal_profit_leaning_compliance(self, compass_profit, bus, memory):
        agent = LegalRiskAgent(compass_profit, bus, memory)
        prompt = agent.system_prompt()
        assert "Full compliance" in prompt

    def test_market_agent_communication_standards(self, compass_people, bus, memory):
        agent = MarketRevenueAgent(compass_people, bus, memory)
        prompt = agent.system_prompt()
        # Verify the anti-euphemism rules are in every market agent
        assert "rightsizing" in prompt
        assert "We are a family" in prompt
        assert "DO NOT SAY" in prompt

    def test_market_agent_revenue_approach(self, compass_people, bus, memory):
        agent = MarketRevenueAgent(compass_people, bus, memory)
        prompt = agent.system_prompt()
        assert "Customer LTV" in prompt

    def test_market_agent_profit_revenue_approach(self, compass_profit, bus, memory):
        agent = MarketRevenueAgent(compass_profit, bus, memory)
        prompt = agent.system_prompt()
        assert "Revenue per employee" in prompt


# =============================================================================
# Behavioral standards — verify base agent standards apply to all agents
# =============================================================================

class TestBehavioralStandards:

    def _build_full_prompt(self, agent):
        """Build the full system prompt including behavioral standards."""
        return agent._build_system_prompt()

    def test_all_agents_carry_behavioral_standards(self, compass_people, bus, memory):
        agents = [
            OrchestratorAgent(compass_people, bus, memory),
            FinancialIntelligenceAgent(compass_people, bus, memory),
            PeopleOrganizationAgent(compass_people, bus, memory),
            MarketRevenueAgent(compass_people, bus, memory),
            LegalRiskAgent(compass_people, bus, memory),
            TechnologyDataAgent(compass_people, bus, memory),
            OperationsSupplyChainAgent(compass_people, bus, memory),
        ]
        for agent in agents:
            full_prompt = self._build_full_prompt(agent)
            assert "SHAREHOLDER VALUE IS THE OBJECTIVE FUNCTION" in full_prompt, \
                f"{agent.role} missing shareholder standard"
            assert "EMPLOYEE IMPACT IS A FIRST-CLASS VARIABLE" in full_prompt, \
                f"{agent.role} missing employee impact standard"
            assert "NO EUPHEMISMS" in full_prompt, \
                f"{agent.role} missing no-euphemism standard"
            assert "AI DOES NOT FIRE PEOPLE" in full_prompt, \
                f"{agent.role} missing AI-doesn't-fire standard"

    def test_all_agents_include_compass_status(self, compass_people, bus, memory):
        agents = [
            OrchestratorAgent(compass_people, bus, memory),
            FinancialIntelligenceAgent(compass_people, bus, memory),
            PeopleOrganizationAgent(compass_people, bus, memory),
            MarketRevenueAgent(compass_people, bus, memory),
            LegalRiskAgent(compass_people, bus, memory),
            TechnologyDataAgent(compass_people, bus, memory),
            OperationsSupplyChainAgent(compass_people, bus, memory),
        ]
        for agent in agents:
            full_prompt = self._build_full_prompt(agent)
            assert "People Leaning" in full_prompt, \
                f"{agent.role} missing compass status"


# =============================================================================
# Message bus tests
# =============================================================================

class TestMessageBus:

    @pytest.mark.asyncio
    async def test_agent_can_send_and_receive(self, compass_people, bus, memory):
        sender = FinancialIntelligenceAgent(compass_people, bus, memory)
        receiver = OrchestratorAgent(compass_people, bus, memory)

        await sender.send_message(
            recipient=AgentRole.ORCHESTRATOR,
            subject="Q4 earnings analysis complete",
            body="Revenue up 12%, but trailing costs from Q2 layoff not yet reflected.",
        )

        msg = await receiver.receive_message(timeout=1.0)
        assert msg is not None
        assert msg.subject == "Q4 earnings analysis complete"
        assert msg.sender == AgentRole.FINANCIAL

    @pytest.mark.asyncio
    async def test_broadcast_reaches_all_agents(self, compass_people, bus, memory):
        orchestrator = OrchestratorAgent(compass_people, bus, memory)
        financial = FinancialIntelligenceAgent(compass_people, bus, memory)
        people = PeopleOrganizationAgent(compass_people, bus, memory)

        await orchestrator.send_message(
            recipient=None,  # broadcast
            subject="Strategic priority shift",
            body="Board has approved pivot to AI-first product strategy.",
        )

        msg_fin = await financial.receive_message(timeout=1.0)
        msg_ppl = await people.receive_message(timeout=1.0)

        assert msg_fin is not None
        assert msg_ppl is not None
        assert msg_fin.subject == "Strategic priority shift"

    @pytest.mark.asyncio
    async def test_audit_log_captures_all_messages(self, compass_people, bus, memory):
        agent = FinancialIntelligenceAgent(compass_people, bus, memory)
        OrchestratorAgent(compass_people, bus, memory)  # register receiver

        await agent.send_message(
            recipient=AgentRole.ORCHESTRATOR,
            subject="Test message",
            body="This is logged.",
        )

        log = bus.get_audit_log()
        assert len(log) == 1
        assert log[0].subject == "Test message"


# =============================================================================
# Memory tests
# =============================================================================

class TestMemory:

    def test_agent_memory_round_trip(self, compass_people, bus, memory):
        agent = FinancialIntelligenceAgent(compass_people, bus, memory)
        agent.save_memory("q4_forecast", {"revenue": 5_000_000, "eps": 2.35})

        result = agent.recall_memory("q4_forecast")
        assert result["revenue"] == 5_000_000
        assert result["eps"] == 2.35

    def test_agent_memory_isolated(self, compass_people, bus, memory):
        """Each agent's memory is separate."""
        fin = FinancialIntelligenceAgent(compass_people, bus, memory)
        ppl = PeopleOrganizationAgent(compass_people, bus, memory)

        fin.save_memory("secret", "financial_data")
        assert ppl.recall_memory("secret") is None

    def test_decision_persistence(self, compass_people, bus, memory):
        from src.models.decisions import DecisionTier
        agent = OrchestratorAgent(compass_people, bus, memory)

        decision = agent.create_decision(
            title="Expand into European market",
            description="Open London and Berlin offices",
            business_rationale="TAM expansion by $2B",
            tier=DecisionTier.ALIGNED,
            projected_financial_impact=50_000_000,
        )

        retrieved = memory.get_decision(decision.id)
        assert retrieved is not None
        assert retrieved.title == "Expand into European market"
        assert retrieved.compass_position_at_decision == CompassPosition(2)


# =============================================================================
# Decision creation and tier handling
# =============================================================================

class TestDecisionCreation:

    def test_tier1_decision_is_proposed(self, compass_people, bus, memory):
        from src.models.decisions import DecisionTier, DecisionStatus
        agent = OrchestratorAgent(compass_people, bus, memory)
        d = agent.create_decision(
            title="Increase retention bonuses",
            description="Top performer retention program",
            business_rationale="Reduce $3M annual turnover cost",
            tier=DecisionTier.ALIGNED,
        )
        assert d.status == DecisionStatus.PROPOSED

    def test_tier3_decision_requires_alternatives(self, compass_people, bus, memory):
        from src.models.decisions import DecisionTier, DecisionStatus
        agent = OrchestratorAgent(compass_people, bus, memory)
        d = agent.create_decision(
            title="Lay off 200 warehouse workers",
            description="Cost reduction via headcount",
            business_rationale="EPS improvement by $0.08",
            tier=DecisionTier.TRADE_OFF,
        )
        assert d.status == DecisionStatus.ALTERNATIVES_REQUIRED

    def test_tier4_blocked_at_people_primary(self, tmp_dir, bus, memory):
        from src.models.decisions import DecisionTier, DecisionStatus
        compass = PriorityCompass(tmp_dir / "compass_p1.json")
        compass.set_position(CompassPosition(1), authorized_by="board", reason="Test")
        agent = OrchestratorAgent(compass, bus, memory)
        d = agent.create_decision(
            title="Cut safety training to save $500K",
            description="Eliminate safety training budget",
            business_rationale="Q4 cost target",
            tier=DecisionTier.EXTRACTION,
        )
        assert d.status == DecisionStatus.BLOCKED

    def test_tier4_flagged_at_profit_leaning(self, compass_profit, bus, memory):
        from src.models.decisions import DecisionTier, DecisionStatus
        agent = OrchestratorAgent(compass_profit, bus, memory)
        d = agent.create_decision(
            title="Cut safety training to save $500K",
            description="Eliminate safety training budget",
            business_rationale="Q4 cost target",
            tier=DecisionTier.EXTRACTION,
        )
        # At profit-leaning, Tier 4 is flagged but not blocked
        assert d.status == DecisionStatus.AWAITING_HUMAN_APPROVAL

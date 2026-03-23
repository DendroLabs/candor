"""Agent 6: Technology & Data

Everything digital. Architecture, infrastructure, security, data governance,
AI, R&D. One agent because you can't do AI without data, data without
infrastructure, or infrastructure without security.

Absorbs: CTO, CIO, CDO, CAIO, CISO, Chief Science/R&D Officer, Chief Digital Officer
"""

from src.compass.compass import PriorityCompass
from src.models.decisions import AgentRole
from src.shared.base_agent import BaseAgent
from src.shared.bus import MessageBus
from src.shared.memory import MemoryStore


class TechnologyDataAgent(BaseAgent):

    def __init__(
        self,
        compass: PriorityCompass,
        bus: MessageBus,
        memory: MemoryStore,
        model: str = "claude-sonnet-4-6",
    ):
        super().__init__(
            role=AgentRole.TECHNOLOGY,
            compass=compass,
            bus=bus,
            memory=memory,
            model=model,
        )

    def system_prompt(self) -> str:
        pos = self.compass_position
        return f"""You are the Technology & Data Agent — everything digital.

YOU ABSORB THESE ROLES:
- CTO: technology vision, R&D, platform architecture, emerging tech evaluation
- CIO: enterprise IT infrastructure, vendor management, digital transformation
- Chief Data Officer: data strategy, governance, advanced analytics, BI
- Chief AI Officer: AI strategy, ethics, infrastructure, integration across business
- CISO: cybersecurity strategy, threat detection, incident response, compliance
- Chief Science/R&D Officer: research strategy, innovation, scientific pipeline
- Chief Digital Officer: digital transformation, digital product strategy

YOUR CAPABILITIES:

1. TECHNOLOGY STRATEGY & ARCHITECTURE
   Evaluate emerging technologies. Build technology roadmaps. Assess build vs. buy.
   Make architecture decisions. Manage tech debt.

2. ENGINEERING & PLATFORM MANAGEMENT
   Development methodology. Code quality and security. Deployment automation.
   Platform reliability.

3. IT INFRASTRUCTURE & OPERATIONS
   Infrastructure cost optimization. Capacity planning. Disaster recovery.
   Vendor management.

4. DATA STRATEGY & GOVERNANCE
   Data standards. Asset classification. Quality monitoring. Governance policies.
   Data architecture design.

5. ADVANCED ANALYTICS & BI
   Predictive models. Business intelligence. Self-service analytics.
   Data-driven insights for all agents.

6. AI STRATEGY & DEPLOYMENT
   Use case identification. AI investment prioritization. Fairness audits.
   Model lifecycle management. Responsible AI compliance.
   HUMAN GATE: High-risk AI deployments require human ethics board approval.

7. CYBERSECURITY
   Threat detection. Incident response. Security architecture. Identity management.
   Security compliance (SOC2, ISO 27001, NIST, HIPAA, PCI-DSS).
   HUMAN GATE: Critical security incidents require immediate human escalation.

8. RESEARCH & DEVELOPMENT (industry-specific)
   Research program prioritization. Stage-gate evaluation. Innovation portfolio.
   Clinical trial design (pharma). Patent strategy.
   HUMAN GATE: Clinical trial and regulatory decisions require human review.

9. DIGITAL TRANSFORMATION
   Digitization opportunities. Transformation roadmaps. Adoption measurement.

10. AUTOMATION IMPACT ASSESSMENT
    Every automation initiative must pass through this capability:
    a. Quantify the displacement (how many roles, which ones, what tenure)
    b. Model the reskilling path (adjacent roles, training required, timeline)
    c. Route to People & Organization Agent for workforce planning
    d. Apply compass weights (see below)
    e. Track outcomes (did displaced workers get reskilled? at what rate?)

COMPASS-SPECIFIC BEHAVIOR:
Current compass position: {pos.value} ({pos.label})

AI and Automation:
{"- AI fairness audits REQUIRED before any deployment" if pos.value <= 2 else "- AI fairness audits required for regulatory compliance"}
{"- Automation impact assessments must include reskilling plans LAUNCHED BEFORE deployment" if pos.value <= 2 else "- Automation impact assessments include cost savings projections. Reskilling noted but not blocking."}
{"- 'Augment' means augment. If the real plan is replacement, say replacement." if pos.value <= 2 else "- Automation ROI calculated with headcount reduction as a primary benefit. Say it plainly."}

Security incidents:
- At ALL compass positions: critical incidents (data breaches, ransomware)
  require immediate human escalation. There is no compass adjustment for
  security. You protect everyone equally.

WHEN ANALYZING TECHNOLOGY DECISIONS:
- Always consider the employee impact of automation
- Never say "augment" when you mean "replace"
- Include security implications in every architecture decision
- Data governance is not optional — it's the foundation
- AI ethics is not a checkbox — it's a continuous obligation
"""

    async def assess_automation_impact(self, initiative: str) -> str:
        """Assess the full impact of an automation initiative.

        This is the capability that forces honesty about what automation does to jobs.
        """
        prompt = (
            f"Assess the full impact of this automation initiative:\n\n"
            f"{initiative}\n\n"
            f"Required analysis:\n"
            f"1. DISPLACEMENT: How many roles affected? Which roles specifically? "
            f"What is the average tenure of people in those roles?\n"
            f"2. RESKILLING: What adjacent roles could these people move to? "
            f"What training is required? What's the realistic timeline?\n"
            f"3. FINANCIAL IMPACT: Cost savings from automation. Cost of reskilling. "
            f"Net financial impact over 1, 3, and 5 years.\n"
            f"4. HONESTY CHECK: Is this being framed as 'augmentation' when it's "
            f"actually 'replacement'? If so, say so. Do not participate in the fiction.\n"
            f"5. COMPASS APPLICATION: At compass position {self.compass_position.value} "
            f"({self.compass_position.label}), what is the recommended approach?\n\n"
            f"Plain language. Real numbers. No euphemisms about 'workforce transformation.'"
        )
        return await self.think(prompt)

    async def evaluate_technology_decision(self, question: str) -> str:
        """Evaluate a technology strategy question."""
        prompt = (
            f"As the Technology & Data Agent, evaluate:\n\n"
            f"{question}\n\n"
            f"Consider:\n"
            f"1. Architecture and infrastructure implications\n"
            f"2. Security implications\n"
            f"3. Data governance implications\n"
            f"4. Employee/workforce impact (especially if automation is involved)\n"
            f"5. Build vs. buy vs. partner analysis\n"
            f"6. Cost and timeline\n"
            f"7. How the compass position ({self.compass_position.label}) affects the recommendation"
        )
        return await self.think(prompt)

    async def security_incident_response(self, incident: str) -> str:
        """Handle a security incident. No compass adjustment for security."""
        prompt = (
            f"SECURITY INCIDENT — immediate assessment required.\n\n"
            f"{incident}\n\n"
            f"1. Severity classification\n"
            f"2. Immediate containment actions\n"
            f"3. Investigation scope\n"
            f"4. Notification requirements (regulatory, affected parties)\n"
            f"5. Does this require immediate human escalation? (If data breach "
            f"or ransomware: YES, always.)\n\n"
            f"Note: There is no compass adjustment for security incidents. "
            f"We protect everyone equally regardless of compass position."
        )
        return await self.think(prompt)

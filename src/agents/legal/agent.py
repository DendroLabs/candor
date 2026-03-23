"""Agent 5: Legal & Risk

Everything about protecting the company and operating within boundaries.
Legal, risk, compliance, ethics, sustainability, and audit — one agent
because these all require the ability to say "no" or "not like that"
to the rest of the organization.

Absorbs: CLO/GC, Chief Risk Officer, Chief Compliance Officer,
         Chief Ethics Officer, Chief Sustainability/Impact Officer,
         Chief Audit Executive
"""

from src.compass.compass import PriorityCompass
from src.models.decisions import AgentRole
from src.shared.base_agent import BaseAgent
from src.shared.bus import MessageBus
from src.shared.memory import MemoryStore


class LegalRiskAgent(BaseAgent):

    def __init__(
        self,
        compass: PriorityCompass,
        bus: MessageBus,
        memory: MemoryStore,
        model: str = "claude-sonnet-4-6",
    ):
        super().__init__(
            role=AgentRole.LEGAL,
            compass=compass,
            bus=bus,
            memory=memory,
            model=model,
        )

    def system_prompt(self) -> str:
        pos = self.compass_position
        return f"""You are the Legal & Risk Agent — everything about boundaries and protection.

YOU ABSORB THESE ROLES:
- Chief Legal Officer / General Counsel: legal risk, contracts, governance,
  litigation, IP, privacy
- Chief Risk Officer / Chief Compliance Officer: enterprise risk, regulatory
  compliance, internal audit
- Chief Ethics Officer: ethics programs, conduct investigations
- Chief Sustainability / Impact Officer: ESG reporting, environmental strategy,
  sustainability compliance
- Chief Audit Executive: internal audit, control testing

WHY SUSTAINABILITY IS HERE (not standalone):
ESG reporting is increasingly mandated by regulation (CSRD, SEC climate disclosure).
Sustainability claims create legal liability if misleading. The compliance
infrastructure for ESG is the same as financial and regulatory compliance.
Putting it here ensures sustainability commitments have legal rigor, not just
marketing polish.

YOUR CAPABILITIES:

1. LEGAL RISK ASSESSMENT
   Evaluate legal risk of proposed actions. Flag regulatory concerns.
   Assess liability exposure. Provide risk ratings.
   HUMAN GATE: All formal legal opinions require human attorney review
   (ethical/bar requirements).

2. CONTRACT MANAGEMENT
   Draft contracts. Review counterparty proposals. Flag non-standard terms.
   Track obligations and deadlines. Manage clause library.

3. REGULATORY COMPLIANCE MONITORING
   Monitor regulatory changes. Assess operational impact. Update compliance
   programs. Generate audit-ready reports.

4. CORPORATE GOVERNANCE
   Board materials. Governance calendars. Proxy process. Corporate records.

5. LITIGATION MANAGEMENT
   Case strategy analysis. Document review and classification. Settlement
   value modeling. Timeline tracking. Litigation budgets.
   HUMAN GATE: All litigation strategy and settlements require human approval.

6. INTELLECTUAL PROPERTY
   Patent portfolio. Infringement monitoring. Freedom-to-operate analyses.
   Filing prioritization.

7. PRIVACY & DATA PROTECTION
   Data flow mapping. Privacy compliance (GDPR, CCPA). DSAR management.
   Breach response coordination.

8. ENTERPRISE RISK MANAGEMENT
   Risk scanning. Exposure quantification. Scenario modeling. Risk appetite
   recommendations. Geopolitical risk monitoring.

9. INTERNAL AUDIT
   Risk-based audit planning. Control testing. Deficiency identification.
   Remediation tracking.

10. ETHICS & CONDUCT
    Ethics hotline triage. Conduct investigation. Policy recommendations.
    Ethical climate monitoring.
    HUMAN GATE: All ethics investigations and disciplinary recommendations
    require human review.

11. THIRD-PARTY RISK MANAGEMENT
    Vendor risk assessment. Ongoing monitoring. Concentration risk.
    Supply chain risk mapping.

12. SUSTAINABILITY & ESG
    ESG data aggregation. Framework-aligned reporting (GRI, SASB, TCFD, CSRD).
    Sustainability targets. Decarbonization pathways. Supply chain sustainability.
    Stakeholder engagement.

13. TIER 3 LEGAL REVIEW
    Every Tier 3 decision passes through you for:
    - Disparate impact analysis (EEOC compliance)
    - WARN Act compliance (plant closings / mass layoffs)
    - Benefits law compliance (ERISA, COBRA)
    - Severance agreement enforceability
    - Non-compete / non-solicit implications
    - Whistleblower / retaliation exposure
    - Regulatory notification requirements
    - Employment law compliance per jurisdiction

COMPASS POSITION: {pos.value} ({pos.label})
Labor law approach: {"Conservative. Exceed minimum requirements. Generous interpretation of employee protections." if pos.value <= 2 else "Full compliance. Meet all legal requirements." if pos.value == 4 else "Minimum compliance. Severance calculated for litigation avoidance."}
ESG approach: {"Comprehensive. Exceed reporting requirements. Proactive sustainability targets." if pos.value <= 2 else "Compliance-focused. Meet mandatory reporting requirements." if pos.value == 4 else "Minimum required reporting. No voluntary commitments."}

WHEN REVIEWING DECISIONS:
- You are the agent that says "no" when needed. That is your job.
- If another agent proposes something legally risky, flag it immediately
- Tier 3 decisions always pass through your legal review before human approval
- Never sign off on a communication that makes claims the company can't back up
  (this includes sustainability claims — greenwashing is legal risk)
- Privacy is not optional. Data protection is not optional. These don't flex
  with the compass.
- Ethics investigations are conducted fairly regardless of who is being
  investigated. The compass does not affect investigation rigor.
"""

    async def legal_risk_assessment(self, proposal: str) -> str:
        """Assess legal risk of a proposed action."""
        prompt = (
            f"Assess the legal risk of the following proposal:\n\n{proposal}\n\n"
            f"1. Legal risk classification (Low / Medium / High / Critical)\n"
            f"2. Specific legal risks identified\n"
            f"3. Regulatory implications\n"
            f"4. Litigation exposure\n"
            f"5. Compliance requirements\n"
            f"6. Recommended mitigation actions\n"
            f"7. Human attorney review required? (Yes for formal opinions)\n\n"
            f"Note: This is analysis, not a formal legal opinion. Formal opinions "
            f"require human attorney review per bar requirements."
        )
        return await self.think(prompt)

    async def tier3_legal_review(self, decision_context: str) -> str:
        """Mandatory legal review for any Tier 3 workforce decision."""
        prompt = (
            f"TIER 3 LEGAL REVIEW — mandatory before human approval.\n\n"
            f"Decision context:\n{decision_context}\n\n"
            f"Review against:\n"
            f"1. DISPARATE IMPACT: Does this action disproportionately affect any "
            f"protected group? Run the four-fifths rule analysis.\n"
            f"2. WARN ACT: Does this trigger WARN Act notice requirements? "
            f"(100+ employees at a single site, or 500+ across sites)\n"
            f"3. ERISA/COBRA: Benefits continuation obligations\n"
            f"4. SEVERANCE: Are proposed severance agreements enforceable? "
            f"Do they include required provisions (OWBPA for 40+ employees)?\n"
            f"5. NON-COMPETES: Any non-compete or non-solicit implications?\n"
            f"6. RETALIATION RISK: Has anyone affected recently filed a complaint, "
            f"participated in an investigation, or engaged in protected activity?\n"
            f"7. JURISDICTION: Employment law requirements for each affected jurisdiction\n"
            f"8. NOTIFICATION: Required regulatory notifications\n\n"
            f"Compass position: {self.compass_position.value} ({self.compass_position.label})\n"
            f"{'Recommend exceeding minimum legal requirements at all points.' if self.compass_position.value <= 2 else 'Ensure full compliance with all legal requirements.'}\n\n"
            f"Flag any issues that could block or delay the decision."
        )
        return await self.think(prompt)

    async def contract_review(self, contract_context: str) -> str:
        """Review a contract or proposed terms."""
        prompt = (
            f"Review the following contract or proposed terms:\n\n"
            f"{contract_context}\n\n"
            f"1. Key terms analysis\n"
            f"2. Non-standard or unusual provisions\n"
            f"3. Risk assessment for each material provision\n"
            f"4. Missing protections or recommended additions\n"
            f"5. Obligations and deadlines created\n"
            f"6. Termination and exit provisions\n"
            f"7. Recommended negotiation points\n"
            f"8. Overall recommendation (proceed / negotiate / reject)"
        )
        return await self.think(prompt)

    async def compliance_assessment(self, regulation: str) -> str:
        """Assess compliance with a specific regulation."""
        prompt = (
            f"Assess compliance with the following regulation:\n\n"
            f"{regulation}\n\n"
            f"1. Regulation summary and requirements\n"
            f"2. Current compliance status (compliant / partial / non-compliant)\n"
            f"3. Gaps identified\n"
            f"4. Remediation actions required\n"
            f"5. Timeline and cost for compliance\n"
            f"6. Risk of non-compliance (fines, litigation, reputational)\n"
            f"7. Coordination needed with other agents"
        )
        return await self.think(prompt)

    async def esg_report(self, context: str) -> str:
        """Generate or evaluate ESG reporting."""
        prompt = (
            f"Develop ESG reporting analysis for:\n\n{context}\n\n"
            f"1. Environmental metrics (carbon footprint, energy, waste, water)\n"
            f"2. Social metrics (workforce, community, safety, DEI)\n"
            f"3. Governance metrics (board composition, ethics, compliance)\n"
            f"4. Framework alignment (GRI, SASB, TCFD, CSRD)\n"
            f"5. Gaps in current reporting\n"
            f"6. Peer comparison\n"
            f"7. Regulatory requirements and deadlines\n"
            f"8. Recommendations for improvement\n\n"
            f"Compass position: {self.compass_position.value} ({self.compass_position.label})\n"
            f"{'Comprehensive reporting exceeding requirements. Proactive sustainability targets.' if self.compass_position.value <= 2 else 'Meet mandatory reporting requirements.' if self.compass_position.value == 4 else 'Minimum required reporting only.'}\n\n"
            f"IMPORTANT: Do not make sustainability claims that cannot be substantiated. "
            f"Greenwashing is a legal risk, not just a PR risk."
        )
        return await self.think(prompt)

    async def risk_assessment(self, context: str) -> str:
        """Enterprise risk assessment."""
        prompt = (
            f"Conduct an enterprise risk assessment for:\n\n{context}\n\n"
            f"1. Risk identification (operational, financial, strategic, compliance, "
            f"reputational, geopolitical, cyber)\n"
            f"2. Risk quantification (likelihood x impact)\n"
            f"3. Risk heat map\n"
            f"4. Top 10 risks ranked\n"
            f"5. Existing controls and their effectiveness\n"
            f"6. Recommended mitigation actions\n"
            f"7. Risk appetite assessment\n"
            f"8. Emerging risks to monitor"
        )
        return await self.think(prompt)

    async def ethics_investigation(self, report: str) -> str:
        """Triage and plan an ethics investigation.

        The compass does not affect investigation rigor.
        """
        prompt = (
            f"ETHICS INVESTIGATION — triage and plan.\n\n"
            f"Report:\n{report}\n\n"
            f"1. Severity classification\n"
            f"2. Allegations summary\n"
            f"3. Parties involved (protect confidentiality)\n"
            f"4. Preliminary assessment — is investigation warranted?\n"
            f"5. Investigation scope and plan\n"
            f"6. Preservation requirements (documents, communications)\n"
            f"7. Interim protective measures needed\n"
            f"8. Timeline estimate\n"
            f"9. External counsel needed?\n\n"
            f"NOTE: The compass does not affect investigation rigor or fairness. "
            f"Ethics investigations are conducted equally regardless of compass "
            f"position, who is being investigated, or their level in the organization.\n\n"
            f"HUMAN GATE: All investigation findings and disciplinary recommendations "
            f"require human review."
        )
        return await self.think(prompt)

---
name: lyzr-onboarding-planner
description: Step-by-step Lyzr onboarding plan covering data preparation, knowledge base setup, prompt tuning, pilot team selection, and go-live checklist
license: MIT
allowed-tools: Read Write
metadata:
  author: prd-generator
  version: "1.0.0"
  category: implementation
---

# Lyzr Onboarding Planner

## Purpose
Create a detailed, week-by-week onboarding plan for getting a company live on Lyzr, from initial setup through production deployment.

## Instructions

### Step 1: Onboarding Scope

Based on fit analysis and recommended agents, define:
- Which agents are being deployed (start with top 1–2)
- Which departments are involved
- Number of users in the pilot
- Data sources to connect
- Integrations required
- Compliance requirements

### Step 2: Pre-Onboarding Checklist

```markdown
## Pre-Onboarding Requirements

### Access & Accounts
- [ ] Lyzr platform account created
- [ ] Admin users provisioned
- [ ] SSO/authentication configured (if enterprise)
- [ ] API keys generated for integrations

### Data Readiness
- [ ] Knowledge base content identified and gathered
  - [ ] FAQ documents (format: [PDF/DOCX/TXT])
  - [ ] Help center articles (URLs or exports)
  - [ ] Product documentation
  - [ ] Policy documents
  - [ ] Training materials
- [ ] Data cleaned and deduplicated
- [ ] PII/sensitive data identified and handled
- [ ] Data owner sign-off obtained

### Integration Readiness
- [ ] CRM API access confirmed ([system name])
- [ ] Ticketing system API access confirmed ([system name])
- [ ] Email/communication system access confirmed
- [ ] Staging/sandbox environments available

### Team Readiness
- [ ] Pilot team identified ([X] people, [roles])
- [ ] Executive sponsor confirmed
- [ ] Project manager assigned
- [ ] IT/security review completed
```

### Step 3: Week-by-Week Onboarding Plan

```markdown
## Week 1: Foundation

### Day 1–2: Platform Setup
- [ ] Create Lyzr workspace
- [ ] Configure organization settings
- [ ] Set up user roles and permissions
- [ ] Connect authentication/SSO
- **Owner**: IT Admin
- **Deliverable**: Workspace ready with access for all pilot users

### Day 3–4: Knowledge Base Setup
- [ ] Upload core documents to Lyzr Knowledge Base
- [ ] Configure document categories and metadata
- [ ] Set up URL-based knowledge sources (help center, docs)
- [ ] Verify document processing and indexing
- **Owner**: Content/Knowledge Manager
- **Deliverable**: Knowledge base indexed and searchable

### Day 5: Initial Agent Configuration
- [ ] Create first agent in Lyzr Architect
- [ ] Configure system prompt based on use case recommendations
- [ ] Connect knowledge base to agent
- [ ] Set model parameters (temperature, max tokens)
- [ ] Configure Hallucination Manager settings
- **Owner**: Project Lead + Lyzr team
- **Deliverable**: First agent responding to test queries

---

## Week 2: Integration & Tuning

### Day 6–7: Connect Integrations
- [ ] Set up CRM integration (read contacts, write activities)
- [ ] Set up ticketing integration (read/create tickets)
- [ ] Set up notification channels (Slack/email alerts)
- [ ] Test each integration end-to-end
- **Owner**: IT/Developer
- **Deliverable**: All integrations functional in staging

### Day 8–9: Prompt Tuning
- [ ] Test agent with 50+ real-world queries
- [ ] Categorize failures (wrong answer, no answer, hallucination, wrong tone)
- [ ] Refine system prompt based on failure patterns
- [ ] Adjust knowledge base (add missing content, remove noise)
- [ ] Set up escalation rules (confidence thresholds, topic boundaries)
- **Owner**: Subject Matter Expert + Project Lead
- **Deliverable**: Agent accuracy > 85% on test queries

### Day 10: Workflow Configuration
- [ ] Configure agent workflows (if multi-agent)
- [ ] Set up handoff rules between agents
- [ ] Configure human escalation paths
- [ ] Test complete workflow end-to-end
- **Owner**: Project Lead
- **Deliverable**: Workflows executing correctly in staging

---

## Week 3: Pilot Launch

### Day 11–12: Pilot Team Training
- [ ] Train pilot users on interacting with the agent
- [ ] Train support team on monitoring and overriding agent actions
- [ ] Train admins on Lyzr dashboard and analytics
- [ ] Distribute quick-reference guide
- [ ] Set up feedback channel (Slack channel, form, etc.)
- **Owner**: Project Lead
- **Deliverable**: All pilot users trained and comfortable

### Day 13: Soft Launch
- [ ] Enable agent for pilot group only
- [ ] Route [10–20%] of relevant traffic to agent
- [ ] Monitor in real-time for first 4 hours
- [ ] Address any immediate issues
- **Owner**: Project Lead + IT
- **Deliverable**: Agent live for pilot users

### Day 14–15: Monitor & Iterate
- [ ] Review all agent interactions from Day 13
- [ ] Collect pilot user feedback
- [ ] Fix identified issues (prompt, knowledge, integration)
- [ ] Increase traffic routing if metrics are positive
- **Owner**: Project Lead
- **Deliverable**: Issue log addressed, metrics trending positive

---

## Week 4: Scale & Optimize

### Day 16–17: Expand Pilot
- [ ] Increase traffic to 50%
- [ ] Add additional pilot users
- [ ] Monitor expanded load performance
- [ ] Continue prompt and knowledge tuning
- **Owner**: Project Lead
- **Deliverable**: Agent handling 50% traffic successfully

### Day 18–19: Production Readiness
- [ ] Security review of production configuration
- [ ] Compliance checklist completed
- [ ] Monitoring and alerting configured
- [ ] Runbook documented (troubleshooting, rollback)
- [ ] SLA defined for agent performance
- **Owner**: IT + Security
- **Deliverable**: Production readiness sign-off

### Day 20: Go Live
- [ ] Route 100% traffic to Lyzr agent
- [ ] Communicate launch to broader team
- [ ] Monitor intensively for first 24 hours
- [ ] Celebrate wins 🎯
- **Owner**: Executive Sponsor + Project Lead
- **Deliverable**: Agent fully live in production
```

### Step 4: Post-Launch Plan (Week 5–8)

```markdown
## Post-Launch: Optimization & Expansion

### Week 5–6: Optimize
- [ ] Analyze 2 weeks of production data
- [ ] Identify top 10 failure modes → fix
- [ ] Optimize prompts for edge cases
- [ ] Update knowledge base with new content
- [ ] Review and adjust escalation thresholds
- **Goal**: Agent accuracy > 90%, CSAT > baseline

### Week 7–8: Expand
- [ ] Plan deployment of next agent (Priority 2 from recommendations)
- [ ] Identify additional knowledge sources
- [ ] Train next department's pilot team
- [ ] Begin multi-agent workflow setup (if applicable)
- **Goal**: Second agent in pilot
```

### Step 5: RACI Matrix

```markdown
| Activity | Project Lead | IT Admin | SME | Exec Sponsor | Lyzr Team |
|----------|-------------|----------|-----|-------------|-----------|
| Platform setup | A | R | — | I | C |
| Knowledge base | A | — | R | I | C |
| Agent config | R | C | C | I | A |
| Integrations | A | R | — | I | C |
| Prompt tuning | A | — | R | — | C |
| Training | R | C | C | I | C |
| Go-live decision | C | C | C | A | I |
| Post-launch optimization | R | C | C | I | C |

R = Responsible, A = Accountable, C = Consulted, I = Informed
```

### Step 6: Success Metrics

```markdown
| Metric | Week 3 Target | Week 4 Target | Month 2 Target |
|--------|--------------|--------------|---------------|
| Agent accuracy | > 80% | > 85% | > 90% |
| Automation rate | > 30% | > 45% | > 60% |
| User satisfaction | > 3.5/5 | > 4.0/5 | > 4.2/5 |
| Escalation rate | < 30% | < 20% | < 15% |
| Response time | < 30s | < 15s | < 10s |
```

## Output Format

```markdown
# Lyzr Onboarding Plan: [Company Name]

## Scope
[Agents, departments, users, integrations]

## Pre-Onboarding Checklist
[Detailed checklist]

## Week-by-Week Plan
[Detailed plan with owners and deliverables]

## Post-Launch Optimization
[Week 5–8 plan]

## RACI Matrix
[Responsibility matrix]

## Success Metrics
[Targets per phase]

## Risks & Mitigations
[Key risks with contingency plans]

## Total Timeline: [X] weeks to production
## Estimated Effort: [X] person-days
```

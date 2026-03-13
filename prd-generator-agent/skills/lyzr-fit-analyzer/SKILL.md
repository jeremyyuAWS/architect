---
name: lyzr-fit-analyzer
description: Analyze any company website to assess fit for the Lyzr AI platform — scores departments, workflows, and use cases against Lyzr capabilities
license: MIT
allowed-tools: WebFetch WebSearch Read Write Grep
metadata:
  author: prd-generator
  version: "1.0.0"
  category: sales-intelligence
---

# Lyzr Fit Analyzer

## Purpose
Analyze a company's website to determine how well their business operations align with Lyzr's AI agent platform. Produce a structured fit assessment with department-level scoring, use case mapping, and implementation recommendations.

## Instructions

### Step 1: Website Analysis
Fetch and analyze the target company's website to extract:
- Industry and vertical
- Company size indicators (team page, locations, job postings)
- Products and services offered
- Customer-facing workflows (support, sales, onboarding)
- Internal operations signals (HR, procurement, compliance)
- Technology stack indicators (integrations page, job postings, documentation)
- Existing AI/automation usage
- Regulatory environment (finance, insurance, healthcare indicators)

### Step 2: Map to Lyzr Capabilities

Score fit across each Lyzr-supported department:

#### Customer Support Fit
Evaluate for:
- **AI Cross Channel Support Agent** — Does the company handle multi-channel support (email, chat, phone, social)?
- **Email Triage Agent** — High inbound email volume? Support tickets?
- **AI Phone Support Agent** — Call center or phone support operations?
- **Support Interaction Assistance Agent** — Live agent augmentation needs?
- **CRM Case Generator Agent** — CRM usage signals? Salesforce, HubSpot, etc.?

Score: 0–10 with justification

#### Sales & Marketing Fit
Evaluate for:
- **AI SDR Agent** — Outbound sales motion? Lead generation needs?
- **AI Deal Nurturer** — Long sales cycles? Complex pipeline management?
- **Lead Enrichment Agent** — B2B with data enrichment needs?
- **ABM Agent** — Enterprise/account-based sales motion?
- **AI Internal Communication Agent** — Large distributed team? Internal comms overhead?

Score: 0–10 with justification

#### HR & People Fit
Evaluate for:
- **AI L&D Agent** — Training programs? Large workforce?
- **AI Performance Review Agent** — Structured review cycles?
- **Employee Onboarding Agent** — High hiring volume? Complex onboarding?
- **AI Hiring Assistant** — Active job postings? Recruiting needs?
- **ESAT Survey Agent** — Employee engagement focus?

Score: 0–10 with justification

#### Procurement Fit
Evaluate for:
- **Supplier Onboarding Agent** — Supply chain operations? Vendor management?
- **Supplier Sourcing Agent** — Multi-vendor procurement?
- **Supplier Performance Analysis** — Vendor evaluation needs?
- **Contract Reviews Agent** — High contract volume?
- **Contract Search Agent** — Large contract repository?

Score: 0–10 with justification

#### Industry-Specific Fit (Banking / Insurance / Financial Services)
Evaluate for:
- **Customer Onboarding** — KYC/AML processes?
- **Loan Origination & Servicing** — Lending operations?
- **Claims Processing** — Insurance claims workflows?
- **Policy Underwriting** — Underwriting operations?
- **Compliance & Regulatory Monitoring** — Regulatory requirements?

Score: 0–10 with justification

### Step 3: Technical Readiness Assessment

Evaluate:
- **Data Readiness** — Does the company likely have structured data, documents, knowledge bases? (1–5)
- **Integration Complexity** — How many systems need connecting? (1–5, lower = easier)
- **AI Maturity** — Existing AI usage signals? (1–5)
- **Security & Compliance Needs** — Regulated industry? (flag for Responsible AI features)
- **Scale Indicators** — Company size suggesting enterprise-grade needs?

### Step 4: Generate Fit Report

#### Overall Fit Score
Weighted average across departments (0–100):
- Departments with score >= 7: **Strong fit**
- Departments with score 4–6: **Moderate fit**
- Departments with score <= 3: **Low fit**

#### Fit Classification
- **90–100**: Ideal Lyzr Customer — immediate high-value deployment
- **70–89**: Strong Fit — multiple deployment opportunities
- **50–69**: Moderate Fit — targeted deployment in specific departments
- **30–49**: Emerging Fit — single use case entry point
- **0–29**: Low Fit — limited current alignment

## Output Format

```markdown
# Lyzr Platform Fit Assessment: [Company Name]

## Executive Summary
[2–3 sentence overview: company description, overall fit score, top opportunity]

## Overall Fit Score: [X]/100 — [Classification]

## Department Fit Breakdown

| Department | Score | Top Use Case | Lyzr Agent |
|------------|-------|-------------|------------|
| Customer Support | X/10 | [use case] | [agent name] |
| Sales & Marketing | X/10 | [use case] | [agent name] |
| HR & People | X/10 | [use case] | [agent name] |
| Procurement | X/10 | [use case] | [agent name] |
| Industry-Specific | X/10 | [use case] | [agent name] |

## Detailed Analysis
[Per-department breakdown with evidence from website]

## Technical Readiness
[Data, integration, maturity, compliance assessment]

## Recommended Lyzr Agents (Priority Order)
1. [Agent name] — [why, expected impact]
2. [Agent name] — [why, expected impact]
3. [Agent name] — [why, expected impact]

## Quick Win Opportunities
[1–2 agents that could be deployed in < 2 weeks]

## Implementation Roadmap
- Phase 1 (0–30 days): [quick win agents]
- Phase 2 (30–90 days): [department-wide rollout]
- Phase 3 (90–180 days): [cross-department orchestration]
```

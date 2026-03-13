---
name: integration-mapper
description: Analyze a company's tech stack (CRM, ERP, ticketing, HRIS) and map to Lyzr integration points with connection architecture
license: MIT
allowed-tools: Read Write WebFetch WebSearch
metadata:
  author: prd-generator
  version: "1.0.0"
  category: architecture
---

# Integration Mapper

## Purpose
Identify a company's existing tech stack from website signals and map each system to Lyzr integration points, producing a complete integration architecture.

## Instructions

### Step 1: Tech Stack Discovery

Analyze the company's website for technology signals:

| Signal Source | What to Look For |
|--------------|-----------------|
| Careers/jobs page | Tools mentioned in job descriptions (Salesforce, Jira, etc.) |
| Integrations page | Listed partners and connectors |
| Footer/badges | Technology partner logos, compliance badges |
| Documentation | API references, developer tools |
| Blog/case studies | Tool mentions in content |
| Login pages | SSO providers, authentication tools |
| Chat widgets | Support tool indicators (Intercom, Zendesk, etc.) |
| Source code hints | Script tags, tracking pixels, analytics tools |

### Step 2: Categorize Discovered Systems

Map findings to categories:

```markdown
| Category | Detected Tool | Confidence | Integration Priority |
|----------|--------------|------------|---------------------|
| CRM | Salesforce / HubSpot / Pipedrive | High/Med/Low | P0/P1/P2 |
| Ticketing | Zendesk / Freshdesk / Jira Service Mgmt | | |
| Communication | Slack / Teams / Email (SendGrid, etc.) | | |
| ERP | SAP / NetSuite / Oracle | | |
| HRIS | Workday / BambooHR / ADP | | |
| Marketing | Marketo / HubSpot / Mailchimp | | |
| Analytics | Google Analytics / Mixpanel / Amplitude | | |
| Auth/SSO | Okta / Auth0 / Azure AD | | |
| Cloud | AWS / GCP / Azure | | |
| Data/BI | Snowflake / BigQuery / Tableau / Looker | | |
| Document Mgmt | SharePoint / Google Drive / Box | | |
| Payments | Stripe / Braintree / Adyen | | |
```

### Step 3: Integration Architecture per System

For each high-priority integration:

```markdown
### [System Name] ↔ Lyzr Integration

**Integration Type**: API / Webhook / Database / File Sync
**Direction**: Lyzr reads / Lyzr writes / Bidirectional
**Protocol**: REST API / GraphQL / SOAP / SFTP

**Data Flow**:
- **Lyzr reads from [System]**: [what data — contacts, tickets, orders, etc.]
- **Lyzr writes to [System]**: [what actions — create ticket, update record, send message]

**Authentication**: OAuth 2.0 / API Key / Service Account

**Lyzr Agent Using This**:
- [Agent Name] uses this for [purpose]

**Sample Integration Flow**:
1. [Trigger event in source system]
2. [Webhook/API call to Lyzr]
3. [Lyzr agent processes]
4. [Lyzr agent writes back to system]

**Complexity**: Low / Medium / High
**Estimated Setup Time**: [X] days
```

### Step 4: Integration Architecture Diagram (Text)

```
┌─────────────────────────────────────────────────┐
│                  LYZR PLATFORM                  │
│                                                 │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐     │
│  │ Support  │  │  Sales   │  │    HR    │     │
│  │  Agent   │  │  Agent   │  │  Agent   │     │
│  └────┬─────┘  └────┬─────┘  └────┬─────┘     │
│       │              │              │           │
│  ┌────┴──────────────┴──────────────┴────┐     │
│  │         Orchestration Layer           │     │
│  └────┬──────────────┬──────────────┬────┘     │
└───────┼──────────────┼──────────────┼───────────┘
        │              │              │
   ┌────┴────┐    ┌────┴────┐   ┌────┴────┐
   │  CRM    │    │ Ticket  │   │  HRIS   │
   │(SF/Hub) │    │(ZD/FD)  │   │(WD/Bam) │
   └─────────┘    └─────────┘   └─────────┘
```

### Step 5: Integration Roadmap

```markdown
### Phase 1: Core Integrations (Week 1–2)
- [ ] [Primary CRM] — read contacts, write activities
- [ ] [Primary ticketing] — read/create tickets
- [ ] [Email/Slack] — send notifications

### Phase 2: Data Enrichment (Week 3–4)
- [ ] [Knowledge sources] — connect docs, wikis, help center
- [ ] [Analytics] — read user behavior data
- [ ] [Database] — direct data access

### Phase 3: Advanced Integrations (Week 5–8)
- [ ] [ERP/HRIS] — deeper workflow integration
- [ ] [BI tools] — reporting and dashboards
- [ ] [Custom APIs] — proprietary systems
```

## Output Format

```markdown
# Integration Map: [Company Name] ↔ Lyzr Platform

## Detected Tech Stack
[Categorized table]

## Integration Architecture
[Per-system integration specs]

## Architecture Diagram
[Text-based diagram]

## Integration Roadmap
[Phased plan]

## Prerequisites
[API access, credentials, permissions needed]

## Estimated Total Integration Effort: [X] person-days
```

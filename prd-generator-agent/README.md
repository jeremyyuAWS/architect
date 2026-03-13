# PRD Generator Agent

AI Product Manager that transforms websites, product ideas, or company descriptions into comprehensive engineering-ready Product Requirements Documents (PRDs). Orchestrates research, AI opportunity mapping, architecture design, and Lyzr agent specification to produce 3,000–6,000 word PRDs with structured JSON for Lyzr Architect and Gamma-ready slide decks for customer stories and solution pitches.

## Run

```bash
npx @open-gitagent/gitagent run -r https://github.com/<username>/prd-generator-agent
```

## What It Can Do

- **Website Research** — Analyze company websites to extract product intelligence, business models, and technology signals
- **Product Discovery** — Transform research into structured product definitions with personas, journeys, and modules
- **Competitive Analysis** — Identify competitors, gaps, and AI-driven differentiation opportunities
- **AI Opportunity Mapping** — Map workflows to AI use cases across automation, prediction, recommendation, generation, and conversation
- **System Architecture Design** — Design complete architectures with frontend, APIs, agent orchestration, and data layers
- **Lyzr Agent Design** — Define Lyzr-compatible agents with tools, knowledge sources, and workflows
- **PRD Writing** — Generate complete 3,000–6,000 word PRDs with all 14 required sections
- **PRD Review** — Validate PRDs for completeness, feasibility, clarity, and actionability
- **Architect Export** — Convert PRDs into structured JSON build plans for Lyzr Architect
- **Gamma Deck Generator** — Create Gamma-compatible slide decks for customer stories, AI solution pitches, and product demos
- **Lyzr Fit Analyzer** — Analyze any website and score its fit for the Lyzr platform across customer support, sales, HR, procurement, and industry-specific agents
- **Lyzr Use Case Recommender** — Generate detailed Lyzr agent deployment recommendations with ROI estimates, agent configs, and implementation plans
- **Lyzr Competitor Benchmarker** — Benchmark a company's AI readiness against competitors and show how Lyzr agents create competitive advantage
- **Lyzr ROI Calculator** — Financial ROI modeling with 3-year TCO comparison (build-from-scratch vs. Lyzr), payback period, FTE savings, and sensitivity analysis
- **Lyzr Migration Planner** — Plan migration from existing AI/chatbot tools to Lyzr with data migration, cutover strategy, parallel run approach, and risk mitigation
- **Industry Compliance Mapper** — Map regulations (HIPAA, SOX, GDPR, PCI-DSS, FINRA, CCPA, EU AI Act) to Lyzr Responsible AI features with gap analysis
- **Demo Script Generator** — Generate audience-tailored live demo scripts with talking points, objection handling, and preparation checklists
- **Integration Mapper** — Discover a company's tech stack from website signals and map CRM, ERP, ticketing, HRIS to Lyzr integration points
- **Executive Summary Generator** — Create 1-page C-suite executive briefs with business impact, ROI highlights, and strategic recommendations
- **Multi-Agent Workflow Designer** — Design cross-department agent orchestration workflows with triggers, handoffs, data flow, and monitoring
- **Lyzr Onboarding Planner** — Week-by-week onboarding plan covering data prep, knowledge base setup, prompt tuning, pilot launch, and go-live

## Example Usage

```
Analyze https://ulta.com
Create an AI customer service platform PRD
```

```
Analyze https://legalmatch.com
Generate AI product expansion opportunities
```

```
Generate a demo app spec for insurance underwriting
```

```
Create a customer story deck for Ulta Beauty AI platform
```

```
Analyze https://acme-insurance.com for Lyzr platform fit
```

```
Show me which Lyzr agents would work best for https://bigretailer.com
```

```
Calculate ROI for deploying Lyzr at https://acme-bank.com
```

```
Create a migration plan from Zendesk AI to Lyzr for our support team
```

```
Generate a demo script for presenting Lyzr to the CTO of a healthcare company
```

```
Create an executive brief for the CFO showing Lyzr's financial impact
```

## Structure

```
prd-generator-agent/
├── agent.yaml
├── SOUL.md
├── RULES.md
├── README.md
├── skills/
│   ├── website-research/
│   ├── product-discovery/
│   ├── competitive-analysis/
│   ├── ai-opportunity-mapping/
│   ├── system-architecture-design/
│   ├── lyzr-agent-design/
│   ├── prd-writer/
│   ├── prd-reviewer/
│   ├── architect-output-generator/
│   ├── gamma-deck-generator/
│   ├── lyzr-fit-analyzer/
│   ├── lyzr-use-case-recommender/
│   ├── lyzr-competitor-benchmarker/
│   ├── lyzr-roi-calculator/
│   ├── lyzr-migration-planner/
│   ├── industry-compliance-mapper/
│   ├── demo-script-generator/
│   ├── integration-mapper/
│   ├── executive-summary-generator/
│   ├── multi-agent-workflow-designer/
│   └── lyzr-onboarding-planner/
├── tools/
│   ├── web-analyzer.yaml
│   ├── prd-formatter.yaml
│   └── gamma-export.yaml
└── knowledge/
    ├── index.yaml
    ├── prd-template.md
    ├── lyzr-architect-reference.md
    └── lyzr-platform-capabilities.md
```

## Built with

[gitagent](https://github.com/open-gitagent/gitagent) — a git-native, framework-agnostic open standard for AI agents.

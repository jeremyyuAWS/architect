---
name: lyzr-use-case-recommender
description: Generate specific Lyzr agent deployment recommendations with ROI estimates, agent configurations, and implementation plans based on website analysis
license: MIT
allowed-tools: WebFetch WebSearch Read Write
metadata:
  author: prd-generator
  version: "1.0.0"
  category: sales-intelligence
---

# Lyzr Use Case Recommender

## Purpose
Take the output from lyzr-fit-analyzer and generate detailed, actionable Lyzr agent deployment recommendations with agent configurations, expected ROI, and step-by-step implementation plans.

## Instructions

For each recommended Lyzr agent from the fit analysis, produce a detailed deployment spec:

### Per Use Case, Generate:

#### 1. Use Case Overview
- **Agent Name**: The specific Lyzr agent (e.g., "AI Cross Channel Support Agent")
- **Department**: Customer Support / Sales / HR / Procurement / Industry-Specific
- **Problem Being Solved**: Specific pain point observed from website analysis
- **Current State**: How this is likely handled today (manual, legacy tool, etc.)
- **AI-Powered State**: How Lyzr transforms the workflow

#### 2. Agent Configuration
```yaml
agent:
  name: "[Agent Name]"
  type: "[Lyzr agent type]"
  model: "claude-sonnet-4-5-20250929"
  temperature: 0.2
  tools:
    - name: "[tool]"
      type: "knowledge_base | api_call | database"
      purpose: "[what it does]"
  knowledge_sources:
    - name: "[source]"
      type: "document | url | database"
      content: "[what data]"
  integrations:
    - "[CRM, ERP, ticketing system, etc.]"
```

#### 3. Workflow Design
Numbered steps showing how the agent operates in the customer's context:
1. Trigger event (customer email, form submission, scheduled task)
2. Agent receives input
3. Agent processes (classify, retrieve, generate, decide)
4. Agent takes action (respond, route, create record, alert)
5. Human review point (if applicable)
6. Feedback loop

#### 4. ROI Estimation
- **Time Savings**: Estimated hours/week saved
- **Cost Impact**: Reduction in manual effort (FTE equivalent)
- **Quality Impact**: Error reduction, consistency improvement
- **Speed Impact**: Response time / processing time improvement
- **Customer Impact**: CSAT, NPS, retention indicators

Use conservative estimates based on industry benchmarks:
- Email triage: 60–80% auto-classification accuracy
- Customer support: 40–60% deflection rate for L1 queries
- Document processing: 70–90% extraction accuracy
- Lead enrichment: 3–5x faster than manual research

#### 5. Implementation Plan
- **Week 1–2**: Setup — connect data sources, configure knowledge base
- **Week 3–4**: Pilot — deploy with human-in-the-loop, tune prompts
- **Week 5–8**: Scale — expand to full volume, reduce human oversight
- **Ongoing**: Monitor, retrain, optimize

#### 6. Success Metrics
- Primary KPI (e.g., ticket resolution time, lead response time)
- Secondary KPIs (2–3 supporting metrics)
- Measurement method
- Target improvement (% or absolute)

### Lyzr Platform Features to Highlight

Map each recommendation to relevant Lyzr platform capabilities:
- **Knowledge Graph as a Service** — for complex entity relationships (contracts, suppliers, org charts)
- **Hallucination Manager** — for regulated industries or customer-facing responses
- **Orchestration** — for multi-agent workflows spanning departments
- **Responsible AI** — for compliance-heavy industries (banking, insurance, healthcare)
- **LyzrGPT** — for secure internal knowledge access
- **Architect** — for rapid no-code agent building

### Competitive Positioning
For each use case, briefly note:
- How this compares to building with raw LLM APIs
- Why Lyzr's pre-built agents accelerate deployment
- Enterprise features that matter (security, compliance, audit trails)

## Output Format

```markdown
# Lyzr Deployment Recommendations: [Company Name]

## Priority 1: [Agent Name]
### Problem
[What's broken today]
### Solution
[How this Lyzr agent fixes it]
### Agent Configuration
[YAML block]
### Workflow
[Numbered steps]
### Expected ROI
| Metric | Current | With Lyzr | Improvement |
|--------|---------|-----------|-------------|
| [metric] | [value] | [value] | [%] |
### Implementation Timeline
[Week-by-week plan]
### Lyzr Features Used
[Platform capabilities leveraged]

## Priority 2: [Agent Name]
[Same structure]

## Priority 3: [Agent Name]
[Same structure]

## Total Estimated Impact
[Summary table across all recommended agents]

## Next Steps
1. Schedule Lyzr platform demo
2. Identify pilot department
3. Prepare data sources for first agent
```

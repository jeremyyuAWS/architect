---
name: executive-summary-generator
description: Create 1-page executive briefs for C-suite stakeholders with business impact, ROI highlights, and strategic recommendations
license: MIT
allowed-tools: Read Write
metadata:
  author: prd-generator
  version: "1.0.0"
  category: sales-enablement
---

# Executive Summary Generator

## Purpose
Distill all analysis (fit assessment, use cases, ROI, compliance) into a single-page executive brief designed for C-suite decision makers who won't read a full PRD.

## Instructions

### Audience
- CEO: Cares about competitive advantage, revenue impact, strategic positioning
- CTO: Cares about architecture, build-vs-buy, engineering capacity
- CFO: Cares about ROI, cost savings, payback period, risk
- COO: Cares about operational efficiency, process improvement, scalability

Tailor language and emphasis based on the target audience. Default to CEO/CTO if unspecified.

### Structure (Strict 1-Page Format)

The executive brief MUST fit on a single page (~500–600 words). Use this exact structure:

```markdown
# [Company Name]: AI Transformation with Lyzr

## The Opportunity
[2–3 sentences: What the company does, the key challenge AI solves, the market context.
Use specific numbers from research — revenue, employee count, customer volume.]

## What We Recommend
[3–4 bullet points — each is one Lyzr agent with a one-line impact statement]

- **[Agent 1]**: [What it does] → [specific impact metric]
- **[Agent 2]**: [What it does] → [specific impact metric]
- **[Agent 3]**: [What it does] → [specific impact metric]

## Business Impact

| Metric | Current State | With Lyzr | Improvement |
|--------|-------------|-----------|-------------|
| [Key metric 1] | [value] | [value] | [X% / $X] |
| [Key metric 2] | [value] | [value] | [X% / $X] |
| [Key metric 3] | [value] | [value] | [X% / $X] |

**3-Year ROI**: [X]% | **Payback**: [X] months | **Annual Savings**: $[X]

## Why Lyzr
[3 bullet points — why Lyzr over build-from-scratch or competitors]

- [Differentiator 1 — e.g., "Production-ready in weeks, not months"]
- [Differentiator 2 — e.g., "Enterprise security with Responsible AI built in"]
- [Differentiator 3 — e.g., "Pre-built agents for [industry] — no ML team required"]

## Timeline to Value
- **Week 1–2**: Setup and pilot with [first agent]
- **Month 2–3**: Expand to [department]
- **Month 4–6**: Full deployment across [X] departments

## Next Step
[One clear call to action — "Schedule a 30-minute pilot scoping session" or
"Start a 2-week proof of concept with [specific agent]"]
```

### Writing Rules
- **No jargon**: Avoid "RAG", "vector database", "embeddings", "orchestration" — translate to business language
- **Numbers over adjectives**: "Reduce response time from 4 hours to 12 minutes" not "significantly faster"
- **Specific to their business**: Reference their products, customers, workflows by name
- **One page maximum**: 500–600 words, no exceptions
- **Bold key numbers**: Make the financial impact scannable
- **Active voice**: "Lyzr automates X" not "X can be automated by Lyzr"

### Variants

Generate different emphasis based on audience:

| Audience | Lead With | Emphasize | De-emphasize |
|----------|----------|-----------|--------------|
| CEO | Competitive advantage | Market positioning, revenue | Technical details |
| CTO | Build-vs-buy analysis | Architecture, time-to-market | Financial projections |
| CFO | ROI and cost savings | Payback period, risk mitigation | Features |
| COO | Operational efficiency | Process improvement, FTE savings | Technology choices |

## Output Format

```markdown
# Executive Brief: [Company Name] × Lyzr
**Prepared for**: [Audience role]
**Date**: [Date]

[Single-page brief following the structure above]
```

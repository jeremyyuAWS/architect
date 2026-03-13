---
name: lyzr-roi-calculator
description: Financial ROI modeling with TCO comparison (build-from-scratch vs. Lyzr), payback period, FTE savings, and cost-benefit analysis
license: MIT
allowed-tools: Read Write WebFetch WebSearch
metadata:
  author: prd-generator
  version: "1.0.0"
  category: financial-analysis
---

# Lyzr ROI Calculator

## Purpose
Produce a detailed financial ROI model comparing the cost of building AI agents from scratch versus deploying with Lyzr. Includes TCO analysis, FTE savings, payback period, and 3-year projections.

## Instructions

### Step 1: Gather Cost Inputs

From the fit analysis and use case recommendations, estimate:

#### Build-from-Scratch Costs
| Cost Category | Estimation Method |
|---------------|-------------------|
| Engineering team | # of ML engineers × avg salary × months |
| Infrastructure | GPU compute, vector DB, hosting, monitoring |
| LLM API costs | Token volume × per-token pricing |
| Data engineering | ETL pipelines, data cleaning, labeling |
| QA & testing | Testing cycles, prompt tuning, evaluation |
| Maintenance | Ongoing model updates, drift monitoring, bug fixes |
| Opportunity cost | Delayed time-to-market (months × revenue impact) |

Use industry benchmarks:
- Senior ML engineer: $180K–$250K/year
- Infrastructure for production AI: $3K–$15K/month
- LLM API (moderate usage): $2K–$10K/month
- Time to production (custom build): 4–9 months
- Time to production (Lyzr): 2–6 weeks

#### Lyzr Platform Costs
| Cost Category | Estimation Method |
|---------------|-------------------|
| Platform subscription | Based on tier (estimate mid-tier enterprise) |
| Implementation | Setup, integration, knowledge base config |
| LLM API costs | Token volume (often lower due to optimized prompts) |
| Training | Team onboarding and training |
| Ongoing support | Platform support and maintenance |

### Step 2: Calculate FTE Savings

For each recommended Lyzr agent, estimate labor savings:

```
| Agent | Current FTEs | Tasks Automated (%) | FTE Equivalent Saved | Annual Savings |
|-------|-------------|---------------------|---------------------|----------------|
| Email Triage | 3.0 | 70% | 2.1 | $147,000 |
| AI SDR | 2.0 | 50% | 1.0 | $85,000 |
| Contract Review | 1.5 | 60% | 0.9 | $108,000 |
```

Use conservative automation rates:
- Customer support L1: 40–60% deflection
- Email triage/routing: 60–80% automation
- Document processing: 50–70% automation
- Lead research/enrichment: 60–80% automation
- Contract review (initial): 40–60% automation

### Step 3: Revenue Impact

Estimate revenue uplift from:
- **Faster response times** → improved conversion (1–5% uplift)
- **24/7 availability** → captured after-hours leads/support
- **Personalization** → higher engagement and retention
- **Reduced churn** → faster issue resolution
- **Sales acceleration** → shorter deal cycles

### Step 4: Build the ROI Model

#### 3-Year TCO Comparison

```
| Cost Item | Build Custom (3yr) | Lyzr Platform (3yr) | Savings |
|-----------|-------------------|---------------------|---------|
| Year 1 | $XXX,XXX | $XXX,XXX | $XXX,XXX |
| Year 2 | $XXX,XXX | $XXX,XXX | $XXX,XXX |
| Year 3 | $XXX,XXX | $XXX,XXX | $XXX,XXX |
| Total | $X,XXX,XXX | $XXX,XXX | $XXX,XXX |
```

#### Payback Period
Calculate months until Lyzr investment pays for itself:
```
Payback = Total Lyzr Investment / Monthly Savings
```

#### ROI Percentage
```
ROI = ((Total Benefits - Total Lyzr Cost) / Total Lyzr Cost) × 100
```

### Step 5: Sensitivity Analysis

Show ROI under 3 scenarios:
- **Conservative**: Low automation rates, high costs, minimal revenue impact
- **Expected**: Median estimates across all variables
- **Optimistic**: High automation rates, strong revenue impact

### Step 6: Non-Financial Benefits

Quantify where possible:
- Time-to-market advantage (weeks vs. months)
- Reduced engineering burden (focus on core product)
- Enterprise-grade security and compliance (built-in)
- Scalability without proportional cost increase
- Continuous platform improvements (no maintenance burden)

## Output Format

```markdown
# ROI Analysis: Lyzr Platform for [Company Name]

## Executive Summary
[3-sentence summary: total 3-year savings, payback period, ROI %]

## 3-Year TCO Comparison

### Build from Scratch
| Category | Year 1 | Year 2 | Year 3 | Total |
|----------|--------|--------|--------|-------|
| [items] | | | | |
| **Total** | | | | **$X.XM** |

### Lyzr Platform
| Category | Year 1 | Year 2 | Year 3 | Total |
|----------|--------|--------|--------|-------|
| [items] | | | | |
| **Total** | | | | **$XXXk** |

### Savings: $X.XM over 3 years

## FTE Savings Detail
[Agent-by-agent breakdown table]

## Revenue Impact
[Uplift estimates with assumptions]

## Payback Period: [X] months

## ROI: [X]%

## Sensitivity Analysis
| Scenario | 3-Year Savings | Payback | ROI |
|----------|---------------|---------|-----|
| Conservative | $XXX,XXX | X months | X% |
| Expected | $XXX,XXX | X months | X% |
| Optimistic | $X,XXX,XXX | X months | X% |

## Non-Financial Benefits
[Bulleted list]

## Assumptions & Methodology
[Transparency on all estimates and benchmarks used]
```

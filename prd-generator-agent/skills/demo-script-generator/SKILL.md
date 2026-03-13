---
name: demo-script-generator
description: Generate live demo scripts with talking points, objection handling, audience-specific messaging, and step-by-step walkthrough
license: MIT
allowed-tools: Read Write
metadata:
  author: prd-generator
  version: "1.0.0"
  category: sales-enablement
---

# Demo Script Generator

## Purpose
Create ready-to-deliver demo scripts for showcasing Lyzr agents to prospects, tailored to the company's specific use cases, industry, and audience.

## Instructions

### Step 1: Audience Analysis

Determine the demo audience from context:

| Audience Type | Focus | Language | Depth |
|--------------|-------|---------|-------|
| C-Suite (CEO, CTO, CFO) | Business impact, ROI, strategic advantage | Non-technical, outcome-focused | High-level |
| VP/Director Engineering | Architecture, integration, scalability | Technical but strategic | Medium |
| IT/DevOps | Security, deployment, maintenance | Highly technical | Deep |
| Business Users (Support, Sales, HR) | Daily workflow improvement, ease of use | Non-technical, practical | Hands-on |
| Procurement / Legal | Compliance, security, vendor evaluation | Risk-focused | Compliance-heavy |

### Step 2: Generate Demo Script

Structure each script as:

#### Opening (2–3 minutes)
```markdown
## Opening

**Hook**: [One sentence connecting to the prospect's specific pain point]

"[Company Name] handles [X volume] of [specific workflow] today. Based on our analysis,
[specific pain point] is costing your team approximately [estimate]. Today I'll show you
how Lyzr's [Agent Name] eliminates that in [timeframe]."

**Agenda**: What we'll cover in the next [X] minutes
1. [Point 1]
2. [Point 2]
3. [Point 3]
```

#### Context Setting (2 minutes)
```markdown
## Your Current Challenge

**Talking points:**
- [Pain point 1 from research — use their specific data]
- [Pain point 2 — reference their website/product]
- [Industry trend that makes this urgent]

**Transition**: "Let me show you exactly how this changes with Lyzr."
```

#### Live Demo Flow (10–15 minutes)
```markdown
## Demo Walkthrough

### Scene 1: [Scenario Name]
**Setup**: "[Describe the realistic scenario using their company context]"

**Step 1**: [Action to perform in Lyzr]
- What to click/type
- What the audience sees
- **Say**: "[Talking point explaining what's happening]"

**Step 2**: [Next action]
- What to click/type
- What the audience sees
- **Say**: "[Talking point — connect to their workflow]"

**Wow Moment**: [The impressive result]
- **Say**: "[Impact statement — time saved, quality improvement]"

### Scene 2: [Next Scenario]
[Same structure]

### Scene 3: [Edge Case / Advanced Feature]
[Show how Lyzr handles complexity]
```

#### ROI Slide (2 minutes)
```markdown
## Impact for [Company Name]

**Say**: "Based on your [X volume] of [workflow], here's what this means:"

| Metric | Today | With Lyzr |
|--------|-------|-----------|
| [Metric 1] | [current] | [improved] |
| [Metric 2] | [current] | [improved] |
| [Metric 3] | [current] | [improved] |

**Key number**: "[The single most impressive metric]"
```

#### Close & Next Steps (2 minutes)
```markdown
## Next Steps

**Say**: "Here's how we typically get started:"

1. [Immediate next step — pilot proposal, POC, trial]
2. [Short-term step — integration planning]
3. [Timeline to value — "You'll see results in X weeks"]

**Ask**: "[Closing question to gauge interest and identify champion]"
```

### Step 3: Objection Handling Guide

Prepare responses for common objections:

```markdown
## Objection Handling

### "We already have [competitor tool]"
**Response**: "[Acknowledge → differentiate → offer proof point]"
**Evidence**: [Specific capability Lyzr has that competitor lacks]

### "How secure is this?"
**Response**: "[Reference enterprise security features, compliance certifications]"
**Evidence**: [Responsible AI, encryption, audit trails, SOC 2]

### "What about hallucinations / accuracy?"
**Response**: "[Reference Hallucination Manager, Knowledge Graph grounding]"
**Evidence**: [Accuracy metrics, human-in-the-loop options]

### "This seems expensive"
**Response**: "[Pivot to ROI — cost of current state vs. Lyzr investment]"
**Evidence**: [FTE savings, time-to-value comparison]

### "Can it integrate with our [specific system]?"
**Response**: "[Reference API capabilities, existing integrations]"
**Evidence**: [Integration architecture from analysis]

### "We tried AI before and it didn't work"
**Response**: "[Acknowledge → explain what's different with Lyzr's approach]"
**Evidence**: [Knowledge Graph, Hallucination Manager, enterprise focus]
```

### Step 4: Demo Preparation Checklist

```markdown
## Pre-Demo Checklist

- [ ] Knowledge base loaded with prospect-relevant content
- [ ] Demo environment configured with prospect's branding/context
- [ ] Sample data prepared (realistic to their industry)
- [ ] Backup demo flow ready (in case of technical issues)
- [ ] ROI numbers validated
- [ ] Audience roles confirmed
- [ ] Follow-up materials prepared (PRD, one-pager, proposal)
```

## Output Format

```markdown
# Demo Script: [Company Name] — [Audience Type]

## Demo Details
- **Duration**: [X] minutes
- **Audience**: [roles and names if known]
- **Primary Use Case**: [agent being demonstrated]
- **Key Message**: [one sentence]

## Script
[Full script with talking points, transitions, and stage directions]

## Objection Handling
[Prepared responses]

## Preparation Checklist
[Pre-demo tasks]

## Follow-Up Plan
[Post-demo actions and materials to send]
```

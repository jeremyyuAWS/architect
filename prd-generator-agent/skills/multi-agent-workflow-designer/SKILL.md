---
name: multi-agent-workflow-designer
description: Design complex cross-department agent orchestration workflows with triggers, handoffs, data flow, and error handling
license: MIT
allowed-tools: Read Write
metadata:
  author: prd-generator
  version: "1.0.0"
  category: architecture
---

# Multi-Agent Workflow Designer

## Purpose
Design sophisticated multi-agent orchestration workflows that span departments and coordinate multiple Lyzr agents to handle complex business processes end-to-end.

## Instructions

### Step 1: Identify Cross-Department Workflows

From the fit analysis and use case recommendations, find workflows that touch multiple departments:

**Common Cross-Department Patterns:**
- Support ticket → CRM update → sales follow-up → manager alert
- Job application → screening → interview scheduling → onboarding
- Customer complaint → ticket creation → root cause analysis → product feedback
- Contract request → legal review → procurement approval → vendor onboarding
- Lead capture → enrichment → scoring → SDR outreach → deal creation
- Employee question → HR knowledge search → policy lookup → manager escalation
- Invoice receipt → data extraction → approval routing → payment processing

### Step 2: Design Workflow Architecture

For each workflow, define:

#### Workflow Definition
```yaml
workflow:
  name: "[Descriptive Name]"
  description: "[What this workflow accomplishes end-to-end]"
  trigger:
    type: "[user_input | webhook | scheduled | event]"
    source: "[System or action that starts it]"
    conditions: "[Optional: when to activate]"

  agents:
    - name: "[Agent 1]"
      department: "[Department]"
      role: "[What this agent does in this workflow]"
    - name: "[Agent 2]"
      department: "[Department]"
      role: "[What this agent does in this workflow]"

  steps:
    - id: 1
      agent: "[Agent Name]"
      action: "[What the agent does]"
      input: "[Data received — from trigger or previous step]"
      output: "[Data produced]"
      next:
        success: 2
        failure: error_handler
      timeout: "[seconds]"

    - id: 2
      agent: "[Agent Name]"
      action: "[What the agent does]"
      input: "[Output from step 1]"
      output: "[Data produced]"
      condition: "[Optional: only execute if condition met]"
      next:
        success: 3
        failure: 4

  error_handling:
    retry:
      max_attempts: 3
      backoff: exponential
    fallback: "[Human escalation | alternative agent | skip]"
    notification: "[Who gets alerted on failure]"

  sla:
    total_duration: "[max time for entire workflow]"
    per_step_timeout: "[default per-step timeout]"
```

### Step 3: Data Flow Mapping

Show how data transforms as it moves through agents:

```
Trigger Input
    │
    ▼
┌─────────────────┐
│ Agent 1: Intake  │
│ IN:  raw email   │
│ OUT: {           │
│   intent: "...", │
│   urgency: "...",│
│   customer: {}   │
│ }                │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Agent 2: Router  │
│ IN:  classified  │
│ OUT: {           │
│   route: "...",  │
│   ticket_id: "", │
│   context: {}    │
│ }                │
└────────┬────────┘
         │
    ┌────┴────┐
    ▼         ▼
[Agent 3]  [Agent 4]
(parallel if independent)
```

### Step 4: Orchestration Patterns

Apply the right pattern for each workflow:

| Pattern | When to Use | Example |
|---------|------------|---------|
| **Sequential** | Each step depends on the previous | Ticket → classify → route → respond |
| **Parallel** | Independent steps can run simultaneously | Enrich lead data + check CRM + score lead |
| **Conditional** | Different paths based on agent output | If urgent → fast-track; if routine → queue |
| **Fan-out/Fan-in** | Split work, then aggregate results | Analyze 5 documents in parallel → summarize all |
| **Loop** | Repeat until condition met | Retry customer contact until response or max attempts |
| **Human-in-the-loop** | Agent pauses for human decision | High-value deal requires manager approval |

### Step 5: Handoff Protocol

Define how agents hand off to each other:

```markdown
### Handoff: [Agent A] → [Agent B]

**Data Contract**:
- Required fields: [list fields Agent B needs]
- Optional fields: [enrichment data]
- Format: JSON

**Quality Gate**:
- Agent A must provide confidence score
- If confidence < 0.7, route to human instead of Agent B

**Error Protocol**:
- If Agent B rejects input: [return to Agent A / escalate / skip]
- If Agent B times out: [retry / alternative agent / human]
```

### Step 6: Monitoring & Observability

```markdown
### Workflow Metrics

| Metric | Target | Alert Threshold |
|--------|--------|----------------|
| End-to-end completion time | < [X] minutes | > [Y] minutes |
| Step success rate | > 95% | < 90% |
| Human escalation rate | < 15% | > 25% |
| Error rate | < 2% | > 5% |

### Dashboard Components
- Workflow execution timeline (Gantt view)
- Per-agent success/failure rates
- Bottleneck identification (slowest steps)
- Human escalation reasons breakdown
```

## Output Format

```markdown
# Multi-Agent Workflow Design: [Company Name]

## Workflow Inventory
| # | Workflow | Departments | Agents | Trigger | Complexity |
|---|---------|------------|--------|---------|-----------|
| 1 | [name] | [depts] | [count] | [type] | Low/Med/High |

## Workflow 1: [Name]
### Overview
[Description]
### Workflow Diagram
[Text-based flow diagram]
### Step-by-Step Definition
[YAML workflow definition]
### Data Flow
[Data transformation diagram]
### Handoff Protocols
[Per-handoff specs]
### Error Handling
[Retry, fallback, escalation rules]
### Monitoring
[Metrics and alerts]

## Workflow 2: [Name]
[Same structure]

## Cross-Workflow Dependencies
[How workflows interact or share agents]

## Implementation Priority
[Ordered list with rationale]
```

---
name: lyzr-agent-design
description: Define Lyzr-compatible agent architectures with inputs, tools, knowledge sources, and workflows for each agent
license: MIT
allowed-tools: Read Write
metadata:
  author: prd-generator
  version: "1.0.0"
  category: agent-design
---

# Lyzr Agent Design

## Purpose
Define a complete agent architecture compatible with Lyzr Architect, specifying each agent's role, tools, knowledge, and workflows.

## Instructions

Design 3–8 specialized agents for the product:

### Per Agent, Define:

#### Identity
- **Name**: Descriptive agent name (e.g., "Customer Support Agent")
- **Role**: One-line purpose
- **Description**: 2–3 sentence detailed description

#### Inputs
- What data/context the agent receives
- Input format (text, JSON, file)
- Required vs. optional inputs

#### Tools
List tools the agent uses:
- **Knowledge Base Search**: Vector search over documents
- **CRM Lookup**: Query customer data
- **API Calls**: External service integrations
- **Database Query**: Structured data access
- **Document Generator**: Create reports/documents
- Custom tools specific to the use case

#### Knowledge Sources
- Documents the agent has access to
- Knowledge base categories
- Update frequency
- Embedding strategy

#### Outputs
- Primary output (response, classification, document, action)
- Output format
- Confidence scoring
- Fallback behavior

#### Workflow
Numbered steps showing the agent's decision flow:
1. Receive input
2. Classify intent
3. Retrieve relevant knowledge
4. Generate response
5. Validate output
6. Return or escalate

#### Escalation Rules
- When to escalate to human
- When to delegate to another agent
- Confidence thresholds

### Agent Interaction Map
Show how agents communicate:
- Which agent calls which
- Data passed between agents
- Orchestration pattern (sequential, parallel, conditional)

## Output Format
Structured markdown with consistent agent definition blocks. Include a summary table of all agents with name, role, and key tools.

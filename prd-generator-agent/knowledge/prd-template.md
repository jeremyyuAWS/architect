# PRD Template Reference

## Required Sections (14 total)

Every generated PRD must include these sections in order:

| # | Section | Min Words | Purpose |
|---|---------|-----------|---------|
| 1 | Executive Summary | 200 | Product concept overview |
| 2 | Product Vision | 150 | Strategic direction |
| 3 | Target Users | 200 | User personas and segments |
| 4 | Problem Statement | 200 | Problems being solved |
| 5 | Proposed Solution | 300 | High-level solution concept |
| 6 | User Journeys | 400 | Step-by-step user flows |
| 7 | Core Features | 300 | Feature list with priorities |
| 8 | AI Capabilities | 300 | AI/ML features |
| 9 | System Architecture | 300 | Technical components |
| 10 | Agent Architecture | 300 | AI agent definitions |
| 11 | Data Architecture | 200 | Data sources and storage |
| 12 | APIs | 200 | Integration endpoints |
| 13 | Security | 200 | Auth, encryption, compliance |
| 14 | Responsible AI | 200 | Ethics, bias, oversight |

## Total Length Target
- Minimum: 3,000 words
- Maximum: 6,000 words
- Ideal: 4,000–5,000 words

## Agent Definition Format

```
### Agent: [Name]

**Role**: [One-line purpose]

**Description**: [2-3 sentences]

**Inputs**:
- [Input 1]: [description]
- [Input 2]: [description]

**Tools**:
- [Tool 1]: [what it does]
- [Tool 2]: [what it does]

**Outputs**:
- [Output 1]: [format and description]

**Workflow**:
1. [Step 1]
2. [Step 2]
3. [Step 3]
```

## User Journey Format

```
### Journey: [Name]

**Trigger**: [What initiates this journey]

**Steps**:
1. [Actor] [action]
2. [System/Agent] [response]
3. [Actor] [next action]
...

**AI Intervention Points**: Steps [X, Y, Z]
```

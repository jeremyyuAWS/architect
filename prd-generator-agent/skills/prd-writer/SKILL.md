---
name: prd-writer
description: Generate complete 3,000–6,000 word engineering-ready PRDs with all 14 required sections from research and design inputs
license: MIT
allowed-tools: Read Write
metadata:
  author: prd-generator
  version: "1.0.0"
  category: documentation
---

# PRD Writer

## Purpose
Compile all research, discovery, and design outputs into a comprehensive Product Requirements Document.

## Instructions

Generate a PRD with exactly these 14 sections:

### 1. Executive Summary (200–400 words)
- Product concept overview
- Key value proposition
- Target market
- Expected outcomes

### 2. Product Vision (150–300 words)
- Vision statement
- Strategic alignment
- Long-term direction

### 3. Target Users (200–400 words)
- Primary user personas (from product-discovery)
- Secondary users
- User segment priorities

### 4. Problem Statement (200–400 words)
- Core problems being solved
- Current pain points
- Cost of inaction

### 5. Proposed Solution (300–500 words)
- High-level system concept
- Key differentiators
- How AI addresses each problem

### 6. User Journeys (400–800 words)
- 2–4 detailed user journeys
- Numbered steps per journey
- AI intervention points highlighted

### 7. Core Features (300–500 words)
- Feature list organized by module
- Priority (P0, P1, P2)
- Brief description per feature

### 8. AI Capabilities (300–500 words)
- Classification capabilities
- Generation capabilities
- Recommendation capabilities
- Conversational capabilities
- Automation capabilities

### 9. System Architecture (300–500 words)
- Component overview (from system-architecture-design)
- Technology choices with justification
- Integration points

### 10. Agent Architecture (300–500 words)
- Agent summary table
- Agent descriptions (from lyzr-agent-design)
- Inter-agent communication

### 11. Data Architecture (200–400 words)
- Data sources and types
- Storage strategy
- Data flow

### 12. APIs (200–400 words)
- Key API endpoints
- Authentication
- Rate limiting

### 13. Security (200–300 words)
- Authentication and authorization
- Data encryption
- Compliance requirements
- Access control

### 14. Responsible AI (200–300 words)
- Bias mitigation strategies
- Audit logging
- Human oversight mechanisms
- Transparency measures

## Formatting Rules
- Use markdown headers (## for sections, ### for subsections)
- Use tables for comparisons and summaries
- Use numbered lists for sequential steps
- Use bullet points for feature lists
- Bold key terms on first use
- Total length: 3,000–6,000 words

## Output
A single markdown document containing the complete PRD.

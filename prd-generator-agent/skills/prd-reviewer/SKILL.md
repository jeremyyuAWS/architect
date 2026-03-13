---
name: prd-reviewer
description: Review generated PRDs for completeness, technical feasibility, clarity, and consistency across all 14 sections
license: MIT
allowed-tools: Read Write
metadata:
  author: prd-generator
  version: "1.0.0"
  category: quality-assurance
---

# PRD Reviewer

## Purpose
Ensure generated PRDs meet quality standards before delivery.

## Instructions

Review the PRD against these criteria:

### 1. Completeness Check
Verify all 14 sections are present and meet minimum word counts:
- [ ] Executive Summary (200+ words)
- [ ] Product Vision (150+ words)
- [ ] Target Users (200+ words)
- [ ] Problem Statement (200+ words)
- [ ] Proposed Solution (300+ words)
- [ ] User Journeys (400+ words)
- [ ] Core Features (300+ words)
- [ ] AI Capabilities (300+ words)
- [ ] System Architecture (300+ words)
- [ ] Agent Architecture (300+ words)
- [ ] Data Architecture (200+ words)
- [ ] APIs (200+ words)
- [ ] Security (200+ words)
- [ ] Responsible AI (200+ words)

### 2. Technical Feasibility
- Are recommended technologies appropriate for the use case?
- Are agent architectures implementable with current Lyzr capabilities?
- Are integration requirements realistic?
- Are performance expectations reasonable?

### 3. Clarity & Consistency
- Are user personas consistent across sections?
- Do user journeys align with defined features?
- Does the architecture support all described capabilities?
- Are there contradictions between sections?

### 4. Actionability
- Can an engineering team start building from this PRD?
- Are feature priorities clear?
- Are acceptance criteria implied or explicit?
- Is the scope well-defined?

### 5. Quality Score
Rate the PRD on a scale of 1–10 for:
- Completeness
- Technical depth
- Clarity
- Actionability
- Overall quality

## Output
A review report with:
- Pass/fail per section
- Issues found (with specific quotes)
- Recommended improvements
- Quality scores
- Overall verdict: APPROVED / NEEDS REVISION

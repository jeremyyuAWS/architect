---
name: ai-opportunity-mapping
description: Analyze business workflows and identify AI use cases across automation, prediction, recommendation, generation, and conversation categories
license: MIT
allowed-tools: Read Write
metadata:
  author: prd-generator
  version: "1.0.0"
  category: ai-strategy
---

# AI Opportunity Mapping

## Purpose
Systematically identify and prioritize AI opportunities across the target business.

## Instructions

Analyze all discovered workflows and map them to AI capability categories:

### Categories

#### 1. Automation
Identify repetitive, rule-based tasks that can be fully automated:
- Task description
- Current manual effort (time/frequency)
- AI approach (RPA, workflow automation, document processing)
- Expected reduction in manual effort

#### 2. Prediction
Identify decisions that benefit from predictive models:
- Decision being made
- Data inputs available
- Prediction type (classification, regression, anomaly detection)
- Business value of better predictions

#### 3. Recommendation
Identify opportunities for personalized recommendations:
- What's being recommended (products, content, actions)
- Available signals (behavior, preferences, context)
- Recommendation approach (collaborative filtering, content-based, hybrid)
- Expected impact on engagement/conversion

#### 4. Generation
Identify content or artifact creation opportunities:
- What's being generated (text, images, code, reports)
- Input context required
- Quality requirements
- Human review needs

#### 5. Conversation
Identify conversational AI opportunities:
- Use case (support, sales, onboarding, internal)
- Required knowledge sources
- Escalation criteria
- Expected resolution rate

### Prioritization Matrix

Score each opportunity on:
- **Feasibility** (1–5): Technical complexity, data availability
- **Impact** (1–5): Business value, user benefit
- **Urgency** (1–5): Competitive pressure, user demand

Rank opportunities by combined score.

## Output Format
Structured markdown with categorized opportunities and a prioritization table sorted by total score.

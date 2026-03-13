---
name: gamma-deck-generator
description: Generate Gamma-compatible slide decks and presentations for customer stories, product demos, and AI solution pitches
license: MIT
allowed-tools: Read Write WebFetch
metadata:
  author: prd-generator
  version: "1.0.0"
  category: presentations
---

# Gamma Deck Generator

## Purpose
Transform PRD outputs, customer research, and AI opportunity analysis into polished Gamma slide decks for customer stories, sales presentations, and stakeholder pitches.

## Instructions

### When to Use
- After a PRD has been generated and the user wants a presentation
- When the user asks for a customer story, case study deck, or pitch deck
- When preparing a demo or sales presentation based on research findings

### Deck Types

#### 1. Customer Story Deck (8–12 slides)
For showcasing how AI transforms a specific customer's business:

| Slide | Content |
|-------|---------|
| 1. Title | Customer name, logo placeholder, tagline |
| 2. About the Customer | Company profile from website-research (industry, size, market) |
| 3. The Challenge | 3–4 key pain points from product-discovery |
| 4. Current State | Existing workflows with inefficiencies highlighted |
| 5. AI Opportunity | Top 3 AI use cases from ai-opportunity-mapping |
| 6. Proposed Solution | High-level solution overview from PRD |
| 7. Agent Architecture | Visual description of AI agents and their roles |
| 8. User Journey | Before vs. after comparison for the primary journey |
| 9. Key Features | Top 5–8 features with icons/descriptions |
| 10. Implementation Roadmap | Phased rollout (Phase 1: 0–3mo, Phase 2: 3–6mo, Phase 3: 6–12mo) |
| 11. Expected Impact | Metrics: time saved, cost reduction, satisfaction improvement |
| 12. Next Steps | Call to action, contact info placeholder |

#### 2. AI Solution Pitch Deck (10–15 slides)
For pitching an AI product to stakeholders or investors:

| Slide | Content |
|-------|---------|
| 1. Title | Product name, one-line value prop |
| 2. Problem | Market problem with data points |
| 3. Market Opportunity | TAM/SAM indicators from research |
| 4. Solution Overview | Product concept with key differentiators |
| 5. How It Works | Step-by-step user flow (3–5 steps) |
| 6. AI Capabilities | Categorized AI features |
| 7. Agent Architecture | Agent roles and interactions |
| 8. System Architecture | Simplified technical overview |
| 9. Competitive Landscape | Positioning vs. competitors from competitive-analysis |
| 10. Use Cases | 3 concrete use case examples |
| 11. Demo Walkthrough | Screen-by-screen flow description |
| 12. Technology Stack | Key technology choices with logos |
| 13. Roadmap | Feature timeline |
| 14. Team / Partners | Placeholder for team |
| 15. CTA | Next steps and contact |

#### 3. Product Demo Deck (6–10 slides)
For walking through a product demo:

| Slide | Content |
|-------|---------|
| 1. Title | Product name, demo context |
| 2. Scenario Setup | Customer context and use case |
| 3–7. Demo Flow | One slide per key interaction step |
| 8. Behind the Scenes | Agent orchestration during the demo |
| 9. Results | Outcomes and metrics |
| 10. Q&A | Discussion prompts |

### Gamma Output Format

Generate the deck as a structured markdown document that can be pasted into Gamma's AI-assisted editor or imported via Gamma's "Paste in text" feature.

Format each slide as:

```markdown
---

# [Slide Title]

[Slide content — use bullet points, short paragraphs, or tables]

> Speaker notes: [What to say when presenting this slide]

---
```

### Content Rules
- **One idea per slide** — no walls of text
- **Max 6 bullet points per slide** — each under 15 words
- **Use data points** — pull specific numbers, percentages, or metrics from research
- **Visual cues** — suggest icons, charts, or diagrams in brackets (e.g., [Bar chart: support ticket volume before/after])
- **Consistent voice** — professional, confident, outcome-focused
- **Speaker notes** — include talking points for every slide
- **Customer-specific** — reference the actual company, their products, their workflows — never generic

### Pulling Data from Other Skills
- **Company profile** → website-research output
- **Pain points & personas** → product-discovery output
- **Competitor positioning** → competitive-analysis output
- **AI use cases & scores** → ai-opportunity-mapping output
- **Architecture visuals** → system-architecture-design and lyzr-agent-design outputs
- **Features & journeys** → prd-writer output

### Example

Input: `Create a customer story deck for Ulta Beauty AI customer service platform`

Output: 10-slide deck covering Ulta's profile, beauty retail challenges, AI-powered support agents, before/after customer journeys, agent architecture, implementation roadmap, and expected impact on CSAT scores and support costs.

## Output
A markdown file (`gamma-deck.md`) with slide-separated sections ready for Gamma import, plus a slide outline summary at the top.

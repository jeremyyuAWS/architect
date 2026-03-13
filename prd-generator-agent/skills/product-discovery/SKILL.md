---
name: product-discovery
description: Transform website research into structured product definitions with problem statements, personas, user journeys, and product modules
license: MIT
allowed-tools: Read Write Grep
metadata:
  author: prd-generator
  version: "1.0.0"
  category: product-management
---

# Product Discovery

## Purpose
Transform raw research findings into structured product definitions ready for architecture design.

## Instructions

Using the output from the website-research skill:

### 1. Problem Statements
Define 3–5 core problems the AI product will solve:
- Problem description
- Who is affected
- Current workaround
- Impact of not solving (cost, time, user satisfaction)

### 2. User Personas
Create detailed personas (3–5):
- **Name** (archetype, e.g., "Support Manager Sarah")
- **Role** and responsibilities
- **Goals** — what they're trying to achieve
- **Pain Points** — what frustrates them today
- **Tech Comfort** — low / medium / high
- **Success Metrics** — how they measure their own success

### 3. User Journeys
Map 2–4 end-to-end journeys:
- Journey name
- Trigger (what starts the journey)
- Steps (numbered, 5–10 steps each)
- Decision points (where AI can intervene)
- Current pain points per step
- AI-enhanced version of each step

### 4. Product Modules
Define the product's major modules:
- Module name
- Description
- Key features (3–5 per module)
- AI capabilities within the module
- Dependencies on other modules

## Output Format
Structured markdown with clear headers for each section. Personas should use the template format. Journeys should show both current-state and AI-enhanced flows side by side.

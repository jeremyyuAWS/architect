---
name: website-research
description: Analyze company websites to extract product intelligence, business models, user workflows, technology signals, and pain points
license: MIT
allowed-tools: WebFetch WebSearch Read Write Grep
metadata:
  author: prd-generator
  version: "1.0.0"
  category: research
---

# Website Research

## Purpose
Analyze a company's website to extract structured product intelligence that feeds downstream skills.

## Instructions

When given a website URL or company name:

1. **Fetch and analyze** the website's main pages (homepage, product pages, pricing, about, blog)
2. **Extract** the following structured data:

### Company Profile
- Company name, industry, founding year (if available)
- Mission/vision statement
- Company size indicators (team page, office locations)
- Target market

### Products & Services
- List all products/services offered
- Key features per product
- Pricing model (freemium, subscription, enterprise, etc.)
- Target user for each product

### User Personas
- Identify distinct user types from the website
- Role, goals, pain points for each persona
- How they currently interact with the company's products

### Workflows
- Map existing user workflows visible from the product
- Identify manual steps, decision points, handoffs
- Note any existing automation

### Technology Signals
- Tech stack indicators (job postings, documentation, integrations page)
- Existing AI/ML features
- API availability
- Integration partners

### Pain Points & Opportunities
- Gaps in current offerings
- Manual processes ripe for automation
- Areas where AI could add value
- Competitive weaknesses

## Output Format

Return a structured markdown document with clear sections for each category above. Use bullet points for lists and include specific quotes or observations from the website to support findings.

## Example

Input: `Analyze https://ulta.com`

Output sections:
- Company Profile: Ulta Beauty, retail/beauty, omnichannel...
- Products: Beauty products, salon services, loyalty program...
- Personas: Beauty enthusiast, professional stylist, gift shopper...
- Workflows: Product discovery → reviews → cart → checkout → loyalty points...
- Tech signals: Mobile app, AR try-on, personalization engine...
- Pain points: Customer support volume, product recommendation accuracy...

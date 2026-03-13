---
name: industry-compliance-mapper
description: Map industry regulations (HIPAA, SOX, GDPR, PCI-DSS, FINRA, CCPA) to Lyzr Responsible AI features and generate compliance readiness reports
license: MIT
allowed-tools: Read Write WebFetch WebSearch
metadata:
  author: prd-generator
  version: "1.0.0"
  category: compliance
---

# Industry Compliance Mapper

## Purpose
Identify the regulatory requirements for a company's industry and map them to Lyzr's Responsible AI features, producing a compliance readiness report.

## Instructions

### Step 1: Identify Applicable Regulations

Based on company industry, geography, and operations:

| Industry | Regulations |
|----------|------------|
| Healthcare | HIPAA, HITECH, FDA (if medical devices), state privacy laws |
| Banking / Finance | SOX, GLBA, FFIEC, BSA/AML, OCC guidelines, Dodd-Frank |
| Insurance | State insurance regulations, NAIC model laws, SOX |
| Securities | FINRA, SEC Rule 17a-4, MiFID II (EU) |
| Retail / E-commerce | PCI-DSS, state consumer protection laws |
| Any with EU customers | GDPR, AI Act |
| Any with CA customers | CCPA/CPRA |
| Any with children's data | COPPA |
| Government contractors | FedRAMP, NIST 800-53, CMMC |
| Cross-industry AI | EU AI Act, NIST AI RMF, state AI laws |

### Step 2: Map Requirements to Lyzr Features

For each applicable regulation, map specific requirements to Lyzr capabilities:

#### Data Privacy & Protection
| Requirement | Regulation Source | Lyzr Feature |
|-------------|------------------|-------------|
| Data minimization | GDPR Art. 5, CCPA | Knowledge Base scoping — limit agent access to necessary data only |
| Right to erasure | GDPR Art. 17, CCPA | Knowledge Base management — remove specific user data |
| Data encryption at rest | HIPAA, PCI-DSS, GLBA | Platform encryption — enterprise-grade data protection |
| Data encryption in transit | All | TLS/HTTPS — all API communications encrypted |
| Access controls | HIPAA, SOX, PCI-DSS | Role-based access — control who configures and accesses agents |
| Data residency | GDPR, various | Deployment options — control where data is processed |

#### AI-Specific Compliance
| Requirement | Regulation Source | Lyzr Feature |
|-------------|------------------|-------------|
| Explainability | EU AI Act, NIST AI RMF | Hallucination Manager — grounded, traceable responses |
| Bias detection | EU AI Act, state AI laws | Responsible AI — bias monitoring and mitigation |
| Human oversight | EU AI Act, FINRA | Escalation rules — human-in-the-loop for high-risk decisions |
| Audit trails | SOX, HIPAA, FINRA | Logging — comprehensive audit logs of all agent actions |
| Model governance | NIST AI RMF | Orchestration — control which models are used and how |
| Transparency | EU AI Act | Agent disclosure — users know they're interacting with AI |

#### Record Keeping
| Requirement | Regulation Source | Lyzr Feature |
|-------------|------------------|-------------|
| Conversation retention | FINRA, SEC 17a-4 | Audit logs — retain all agent interactions |
| Immutable records | SOX, SEC | Platform logging — tamper-evident audit trail |
| Retention periods | HIPAA (6yr), FINRA (3yr) | Configurable retention policies |
| Searchable archives | SEC, FINRA | Searchable interaction history |

### Step 3: Gap Analysis

Identify any compliance requirements that need additional measures beyond Lyzr's built-in features:

```markdown
| Requirement | Status | Gap | Remediation |
|-------------|--------|-----|-------------|
| [requirement] | ✅ Covered | — | Built into Lyzr |
| [requirement] | ⚠️ Partial | [gap description] | [additional steps needed] |
| [requirement] | ❌ Gap | [gap description] | [external tool or process needed] |
```

### Step 4: Compliance Readiness Score

Rate readiness per regulation:
- **Ready** (90–100%): All requirements covered by Lyzr + standard config
- **Mostly Ready** (70–89%): Minor gaps addressable during implementation
- **Needs Work** (50–69%): Significant gaps requiring additional tools or processes
- **Not Ready** (< 50%): Major compliance blockers

### Step 5: Implementation Recommendations

For each gap, recommend:
- Configuration changes within Lyzr
- Additional tools or services needed
- Process changes (policies, training, documentation)
- Third-party compliance tools to integrate

## Output Format

```markdown
# Compliance Readiness Report: [Company Name]

## Applicable Regulations
[List with brief description of each]

## Compliance Coverage Matrix

| Regulation | Requirements | Covered by Lyzr | Gaps | Readiness |
|-----------|-------------|-----------------|------|-----------|
| GDPR | 12 | 10 | 2 | 83% — Mostly Ready |
| HIPAA | 8 | 7 | 1 | 88% — Mostly Ready |
| [etc.] | | | | |

## Detailed Mapping
[Per-regulation requirement-to-feature mapping tables]

## Gap Analysis
[Gaps with remediation plans]

## Lyzr Responsible AI Features Utilized
[Which features address which requirements]

## Recommendations
[Prioritized list of actions to achieve full compliance]

## Overall Compliance Readiness: [X]% — [Classification]
```

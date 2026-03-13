---
name: architect-output-generator
description: Convert finalized PRDs into structured JSON build plans compatible with Lyzr Architect for direct import and agent creation
license: MIT
allowed-tools: Read Write
metadata:
  author: prd-generator
  version: "1.0.0"
  category: export
---

# Architect Output Generator

## Purpose
Transform the finalized PRD into a structured build plan that Lyzr Architect can import to scaffold the application.

## Instructions

Generate a JSON build plan with the following structure:

### Build Plan Schema

```json
{
  "projectName": "string",
  "version": "1.0.0",
  "description": "string",
  "targetPlatform": "lyzr-architect",
  "agents": [
    {
      "name": "string",
      "role": "string",
      "description": "string",
      "model": "string",
      "temperature": 0.3,
      "tools": [
        {
          "name": "string",
          "type": "knowledge_base | api_call | database | custom",
          "config": {}
        }
      ],
      "knowledgeSources": [
        {
          "name": "string",
          "type": "document | url | database",
          "description": "string"
        }
      ],
      "systemPrompt": "string",
      "outputFormat": "text | json | markdown"
    }
  ],
  "workflows": [
    {
      "name": "string",
      "description": "string",
      "trigger": "user_input | scheduled | event",
      "steps": [
        {
          "agent": "string",
          "action": "string",
          "inputFrom": "user | previous_step",
          "outputTo": "next_step | user | storage"
        }
      ]
    }
  ],
  "dataModel": {
    "entities": [
      {
        "name": "string",
        "fields": [
          {
            "name": "string",
            "type": "string",
            "required": true
          }
        ]
      }
    ]
  },
  "apis": [
    {
      "method": "GET | POST | PUT | DELETE",
      "path": "string",
      "description": "string",
      "auth": "jwt | api_key | none"
    }
  ],
  "config": {
    "vectorDb": "string",
    "embeddingModel": "string",
    "primaryDb": "string",
    "cacheLayer": "string"
  }
}
```

### Generation Rules
1. Map every agent from the PRD's Agent Architecture section
2. Include system prompts derived from each agent's role and instructions
3. Map user journeys to workflows with sequential steps
4. Extract data model from the Data Architecture section
5. List all APIs from the API section
6. Set config based on System Architecture technology choices

### Validation
Before outputting, verify:
- Every agent has at least one tool
- Every workflow references existing agents
- All entity references in workflows exist in the data model
- System prompts are specific and actionable (not generic)

## Output
A single JSON file (`architect-build-plan.json`) containing the complete build plan.

# Lyzr Architect Reference

## Overview
Lyzr Architect is a visual builder for AI agent applications. It accepts structured build plans to scaffold complete agent-based applications.

## Supported Agent Types
- **Chat Agent**: Conversational interface with knowledge base access
- **Task Agent**: Executes specific tasks with tool access
- **Workflow Agent**: Orchestrates multi-step processes
- **Retrieval Agent**: Specialized in knowledge retrieval and RAG

## Tool Types
- `knowledge_base`: Vector search over uploaded documents
- `api_call`: External API integration
- `database`: Structured data queries
- `web_search`: Real-time web search
- `code_executor`: Run code snippets
- `custom`: User-defined tools

## Knowledge Source Types
- `document`: PDF, DOCX, TXT files
- `url`: Web pages (crawled and indexed)
- `database`: Structured data connections
- `api`: Dynamic data from APIs

## Workflow Triggers
- `user_input`: Started by user message
- `scheduled`: Cron-based execution
- `event`: Triggered by system events
- `webhook`: External webhook trigger

## Build Plan Requirements
- Every agent must have a unique name
- System prompts should be specific to the agent's role
- Tools must specify their type and configuration
- Workflows must reference existing agents by name
- Data model entities should cover all referenced data types

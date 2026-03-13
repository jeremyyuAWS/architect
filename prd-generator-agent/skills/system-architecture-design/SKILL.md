---
name: system-architecture-design
description: Design complete system architecture including frontend, APIs, agent orchestration, vector databases, and event pipelines
license: MIT
allowed-tools: Read Write
metadata:
  author: prd-generator
  version: "1.0.0"
  category: architecture
---

# System Architecture Design

## Purpose
Produce a complete technical architecture for the AI product.

## Instructions

Design the following architectural layers:

### 1. Frontend Layer
- Application type (web app, mobile, dashboard, chat interface)
- Key UI components
- Real-time requirements (WebSocket, SSE)
- Authentication flow

### 2. API Layer
- API style (REST, GraphQL, gRPC)
- Core endpoints (list 8–15 endpoints with method, path, description)
- Authentication mechanism (JWT, OAuth2, API keys)
- Rate limiting strategy

### 3. Agent Orchestration Layer
- Agent runtime (Lyzr, LangChain, custom)
- Orchestration pattern (sequential, parallel, hierarchical)
- Agent communication (direct, message queue, event bus)
- State management approach

### 4. Knowledge & Data Layer
- Vector database (Pinecone, Weaviate, Qdrant, pgvector)
- Document processing pipeline
- Embedding model selection
- Knowledge update strategy (batch, real-time)

### 5. Data Storage
- Primary database (PostgreSQL, MongoDB)
- Cache layer (Redis)
- File storage (S3-compatible)
- Data model (key entities and relationships)

### 6. Event Pipeline
- Event bus (Kafka, RabbitMQ, Redis Streams)
- Key events (user actions, agent completions, system events)
- Event consumers and their responsibilities

### 7. Infrastructure
- Deployment model (cloud, hybrid, on-premise)
- Container orchestration (Kubernetes, ECS)
- CI/CD pipeline
- Monitoring and observability

## Output Format
Structured markdown with component descriptions, relationships between layers, and a text-based architecture overview showing how components connect.

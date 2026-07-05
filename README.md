# RAG Agent

[![CI](https://github.com/kogunlowo123/rag-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/kogunlowo123/rag-agent/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Category**: AI Engineering | **Cloud**: MULTI-CLOUD | **LLM**: gpt-4o

Retrieval-Augmented Generation agent that orchestrates document ingestion, chunking strategies, embedding generation, vector search, and context-aware answer synthesis with citation tracking and hallucination mitigation.

---

## Domain-Specific Tools

| Tool | Description |
|------|-------------|
| `ingest_documents` | Ingest and chunk documents into a vector store with configurable strategies |
| `query_knowledge_base` | Retrieve relevant context chunks for a natural language query |
| `rerank_results` | Re-rank retrieved chunks using cross-encoder or LLM-based reranking |
| `generate_answer` | Generate a cited answer from retrieved context using an LLM |
| `evaluate_retrieval` | Evaluate retrieval quality with precision, recall, and MRR metrics |

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/api/v1/rag/ingest` | Ingest documents into knowledge base |
| `POST` | `/api/v1/rag/query` | Query the knowledge base |
| `POST` | `/api/v1/rag/rerank` | Rerank retrieved results |
| `POST` | `/api/v1/rag/evaluate` | Evaluate retrieval quality |
| `GET` | `/api/v1/rag/collections` | List document collections |

## Features

- Document Ingestion
- Chunking Strategies
- Embedding Generation
- Vector Search
- Citation Tracking

## Integrations

- Pinecone
- Weaviate
- Qdrant
- Chromadb
- Opensearch

## Architecture

```
rag-agent/
├── src/
│   ├── agent/              # Domain-specific agent logic
│   │   ├── rag_agent_agent.py  # Main agent with domain tools
│   │   ├── tools.py        # 5 domain-specific tools
│   │   └── prompts.py      # Expert system prompts
│   ├── api/                # FastAPI routes
│   │   └── routes/
│   │       ├── domain.py   # 5 domain-specific endpoints
│   │       └── health.py   # Health check
│   ├── connectors/         # 5 integration connectors
│   ├── config/             # Settings and configuration
│   ├── models/             # Domain-specific Pydantic schemas
│   ├── rag/                # RAG pipeline
│   ├── mcp/                # MCP server
│   └── a2a/                # Agent-to-agent protocol
├── tests/
├── infrastructure/         # Terraform, K8s, Helm, Docker
├── dashboard/              # Next.js frontend
└── docs/                   # Architecture and deployment docs
```

## Quick Start

```bash
# Install
pip install -e ".[dev]"

# Run
make dev

# Test
make test

# Docker
docker compose up -d
```

## Primary Service

**LangChain + LlamaIndex + Vector Databases**

---

Built as part of the Enterprise AI Agent Platform.

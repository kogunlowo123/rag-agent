# RAG Agent Architecture

Retrieval-Augmented Generation agent that orchestrates document ingestion, chunking strategies, embedding generation, vector search, and context-aware answer synthesis with citation tracking and hallucination mitigation.

## Domain Tools

- **ingest_documents**: Ingest and chunk documents into a vector store with configurable strategies
- **query_knowledge_base**: Retrieve relevant context chunks for a natural language query
- **rerank_results**: Re-rank retrieved chunks using cross-encoder or LLM-based reranking
- **generate_answer**: Generate a cited answer from retrieved context using an LLM
- **evaluate_retrieval**: Evaluate retrieval quality with precision, recall, and MRR metrics
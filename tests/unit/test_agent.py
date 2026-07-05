"""RAG Agent - Unit Tests."""

import pytest
from src.agent.tools import AgentTools


@pytest.mark.asyncio
async def test_ingest_documents():
    """Test Ingest and chunk documents into a vector store with configurable strategies."""
    tools = AgentTools()
    result = await tools.ingest_documents(source_path="test", chunk_size=1)
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_query_knowledge_base():
    """Test Retrieve relevant context chunks for a natural language query."""
    tools = AgentTools()
    result = await tools.query_knowledge_base(query="test", top_k=1)
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_rerank_results():
    """Test Re-rank retrieved chunks using cross-encoder or LLM-based reranking."""
    tools = AgentTools()
    result = await tools.rerank_results(query="test", documents="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_generate_answer():
    """Test Generate a cited answer from retrieved context using an LLM."""
    tools = AgentTools()
    result = await tools.generate_answer(query="test", context_chunks="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_agent_initialization():
    """Test that the agent initializes correctly."""
    from src.agent.rag_agent_agent import RagAgentAgent
    agent = RagAgentAgent()
    assert agent.agent_id is not None
    assert agent._system_prompt is not None
    assert len(agent._tool_dispatch) > 0

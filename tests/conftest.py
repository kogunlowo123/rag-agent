"""Test configuration for RAG Agent."""

import pytest


@pytest.fixture
def agent_config():
    return {"name": "rag-agent", "category": "AI Engineering"}

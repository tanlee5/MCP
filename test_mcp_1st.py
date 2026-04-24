"""Basic tests for MCP_1st."""

import importlib


def test_mcp_1st_can_be_imported():
    """Smoke test to ensure the MCP module is importable."""
    module = importlib.import_module("MCP_1st")
    assert module is not None

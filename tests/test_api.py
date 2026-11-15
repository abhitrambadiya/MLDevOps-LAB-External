"""
Integration tests for FastAPI Multiplication Service endpoints.
Uses FastAPI TestClient to test GET, POST, validation, docs, and web UI.
"""

import sys
import os
import pytest
from fastapi.testclient import TestClient

# Ensure src is in sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from main import app

client = TestClient(app)


def test_root_endpoint():
    """Verify root endpoint returns API status and link metadata."""
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "online"
    assert "endpoints" in data


def test_health_endpoint():
    """Verify health check returns status 200 and healthy."""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert "timestamp" in data


def test_multiply_get_success():
    """Test GET /multiply with valid query params."""
    response = client.get("/multiply?a=7&b=8")
    assert response.status_code == 200
    data = response.json()
    assert data["a"] == 7.0
    assert data["b"] == 8.0
    assert data["result"] == 56.0
    assert data["operation"] == "multiplication"


def test_multiply_get_floating_points():
    """Test GET /multiply with floating point values."""
    response = client.get("/multiply?a=2.5&b=4.0")
    assert response.status_code == 200
    data = response.json()
    assert data["result"] == 10.0


def test_multiply_get_missing_params():
    """Test GET /multiply returns 422 Unprocessable Entity when params are missing."""
    response = client.get("/multiply?a=10")
    assert response.status_code == 422


def test_multiply_get_invalid_type():
    """Test GET /multiply returns 422 when param is non-numeric."""
    response = client.get("/multiply?a=hello&b=5")
    assert response.status_code == 422


def test_multiply_post_success():
    """Test POST /multiply with valid JSON body."""
    payload = {"a": 12.0, "b": 5.0}
    response = client.post("/multiply", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["a"] == 12.0
    assert data["b"] == 5.0
    assert data["result"] == 60.0
    assert data["operation"] == "multiplication"


def test_multiply_post_negative_values():
    """Test POST /multiply with negative inputs."""
    payload = {"a": -6.0, "b": 7.0}
    response = client.post("/multiply", json=payload)
    assert response.status_code == 200
    assert response.json()["result"] == -42.0


def test_multiply_post_invalid_body():
    """Test POST /multiply returns 422 for bad payload structure."""
    response = client.post("/multiply", json={"wrong_key": 10})
    assert response.status_code == 422


def test_history_endpoint():
    """Test /history returns list of executed operations."""
    response = client.get("/history")
    assert response.status_code == 200
    data = response.json()
    assert "total_records" in data
    assert "history" in data
    assert isinstance(data["history"], list)


def test_ui_endpoint():
    """Test /ui returns HTML page."""
    response = client.get("/ui")
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]
    assert "Multiplication App" in response.text

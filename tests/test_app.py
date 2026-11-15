import os
import sys
from fastapi.testclient import TestClient

sys.path.insert(0, os.path.abspath("src"))

from math_operations import multiply
from main import app

client = TestClient(app)

def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(-2, 5) == -10
    assert multiply(0, 7) == 0
    assert multiply(2.5, 2) == 5
    assert multiply(10, 10) == 100

def test_api_get():
    res = client.get("/multiply?a=6&b=7")
    assert res.status_code == 200
    assert res.json()["result"] == 42

def test_api_post():
    res = client.post("/multiply", json={"a": 4, "b": 5})
    assert res.status_code == 200
    assert res.json()["result"] == 20

def test_home_ui():
    res = client.get("/")
    assert res.status_code == 200
    assert "<form" in res.text

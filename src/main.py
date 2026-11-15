from fastapi import FastAPI
from fastapi.responses import HTMLResponse

try:
    from math_operations import multiply
except ImportError:
    from src.math_operations import multiply

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <h2>Multiplication Calculator - ML DevOps Lab POE</h2>
    <p>Status: Ready</p>
    <form action="/multiply" method="get">
        Number 1: <input type="number" step="any" name="a" required><br><br>
        Number 2: <input type="number" step="any" name="b" required><br><br>
        <button type="submit">Multiply</button>
    </form>
    """

@app.get("/multiply")
def multiply_get(a: float, b: float):
    return {"a": a, "b": b, "result": multiply(a, b)}

@app.post("/multiply")
def multiply_post(payload: dict):
    a = float(payload.get("a", 0))
    b = float(payload.get("b", 0))
    return {"a": a, "b": b, "result": multiply(a, b)}

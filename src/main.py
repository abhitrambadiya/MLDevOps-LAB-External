"""
FastAPI Application for Multiplication Service
Problem Statement C - ML DevOps POE
"""

from datetime import datetime, timezone
from typing import List, Union
from fastapi import FastAPI, HTTPException, Query, status
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field

try:
    from math_operations import multiply
except ImportError:
    from src.math_operations import multiply

app = FastAPI(
    title="ML DevOps POE - Multiplication Service",
    description="FastAPI service for Problem Statement C: Two number multiplication with Pytest, Jenkins & Evidently integration.",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# In-memory storage for request logs (used for monitoring & Evidently data drift analysis)
request_history: List[dict] = []


class MultiplicationRequest(BaseModel):
    a: float = Field(..., description="First number to multiply", json_schema_extra={"example": 15.0})
    b: float = Field(..., description="Second number to multiply", json_schema_extra={"example": 4.0})


class MultiplicationResponse(BaseModel):
    a: float
    b: float
    operation: str = "multiplication"
    result: float
    timestamp: str


@app.get("/", tags=["General"])
def root():
    """Service status and quick links."""
    return {
        "service": "ML DevOps Multiplication Service",
        "problem_statement": "PS C: Accept two numbers and display multiplication",
        "status": "online",
        "endpoints": {
            "web_ui": "/ui",
            "swagger_docs": "/docs",
            "redoc": "/redoc",
            "get_multiplication": "/multiply?a=10&b=5",
            "post_multiplication": "/multiply",
            "history": "/history",
            "health": "/health",
        },
    }


@app.get("/health", tags=["General"], status_code=status.HTTP_200_OK)
def health_check():
    """Health check endpoint for Jenkins CI/CD pipeline."""
    return {"status": "healthy", "timestamp": datetime.now(timezone.utc).isoformat()}


@app.get("/multiply", tags=["Calculator"], response_model=MultiplicationResponse)
def multiply_get(
    a: float = Query(..., description="First number"),
    b: float = Query(..., description="Second number"),
):
    """
    Multiply two numbers provided as query parameters.
    Example: /multiply?a=12&b=4
    """
    try:
        # Convert to int if whole number for clean display
        val_a = int(a) if a.is_integer() else a
        val_b = int(b) if b.is_integer() else b
        res = multiply(val_a, val_b)
        now_ts = datetime.now(timezone.utc).isoformat()

        record = {
            "a": float(val_a),
            "b": float(val_b),
            "operation": "multiplication",
            "result": float(res),
            "timestamp": now_ts,
        }
        request_history.append(record)

        return record
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Multiplication calculation error: {str(e)}",
        )


@app.post("/multiply", tags=["Calculator"], response_model=MultiplicationResponse)
def multiply_post(payload: MultiplicationRequest):
    """
    Multiply two numbers provided in the JSON body.
    Example payload: {"a": 25.0, "b": 4.0}
    """
    try:
        val_a = int(payload.a) if payload.a.is_integer() else payload.a
        val_b = int(payload.b) if payload.b.is_integer() else payload.b
        res = multiply(val_a, val_b)
        now_ts = datetime.now(timezone.utc).isoformat()

        record = {
            "a": float(val_a),
            "b": float(val_b),
            "operation": "multiplication",
            "result": float(res),
            "timestamp": now_ts,
        }
        request_history.append(record)

        return record
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Multiplication calculation error: {str(e)}",
        )


@app.get("/history", tags=["Monitoring"])
def get_history():
    """Retrieve logged operations history (used for data drift analysis)."""
    return {"total_records": len(request_history), "history": request_history}


@app.get("/ui", tags=["Web UI"], response_class=HTMLResponse)
def web_ui():
    """Interactive Web UI to demonstrate multiplication in browser."""
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>ML DevOps POE - Multiplication Service</title>
        <style>
            * { box-sizing: border-box; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; }
            body { background: #f0f4f8; margin: 0; padding: 40px 20px; display: flex; justify-content: center; align-items: center; min-height: 100vh; }
            .card { background: white; border-radius: 12px; box-shadow: 0 10px 25px rgba(0,0,0,0.08); width: 100%; max-width: 480px; padding: 32px; }
            .badge { display: inline-block; background: #e0f2fe; color: #0284c7; padding: 4px 10px; border-radius: 9999px; font-size: 12px; font-weight: 600; text-transform: uppercase; margin-bottom: 12px; }
            h1 { font-size: 24px; color: #1e293b; margin: 0 0 8px 0; }
            p { color: #64748b; font-size: 14px; margin: 0 0 24px 0; }
            .form-group { margin-bottom: 18px; }
            label { display: block; font-size: 13px; font-weight: 600; color: #334155; margin-bottom: 6px; }
            input[type="number"] { width: 100%; padding: 12px 14px; border: 1.5px solid #cbd5e1; border-radius: 8px; font-size: 16px; outline: none; transition: border 0.2s; }
            input[type="number"]:focus { border-color: #2563eb; ring: 2px solid #93c5fd; }
            button { width: 100%; background: #2563eb; color: white; padding: 12px; border: none; border-radius: 8px; font-size: 16px; font-weight: 600; cursor: pointer; transition: background 0.2s; }
            button:hover { background: #1d4ed8; }
            .result-box { margin-top: 24px; padding: 16px; background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; display: none; }
            .result-title { font-size: 12px; font-weight: 600; color: #64748b; text-transform: uppercase; margin-bottom: 4px; }
            .result-value { font-size: 22px; font-weight: 700; color: #059669; }
            .nav-links { margin-top: 24px; text-align: center; font-size: 13px; }
            .nav-links a { color: #2563eb; text-decoration: none; margin: 0 8px; }
            .nav-links a:hover { text-decoration: underline; }
        </style>
    </head>
    <body>
        <div class="card">
            <span class="badge">ML DevOps POE - PS C</span>
            <h1>Multiplication App</h1>
            <p>Accept two numbers and calculate their product via FastAPI</p>
            <form id="calcForm" onsubmit="event.preventDefault(); calculate();">
                <div class="form-group">
                    <label for="num1">First Number (A)</label>
                    <input type="number" step="any" id="num1" placeholder="e.g. 15" required>
                </div>
                <div class="form-group">
                    <label for="num2">Second Number (B)</label>
                    <input type="number" step="any" id="num2" placeholder="e.g. 4" required>
                </div>
                <button type="submit" id="submitBtn">Multiply Numbers</button>
            </form>
            <div class="result-box" id="resultBox">
                <div class="result-title">Calculation Result</div>
                <div class="result-value" id="resultValue">--</div>
            </div>
            <div class="nav-links">
                <a href="/docs" target="_blank">Swagger Docs</a> &bull;
                <a href="/redoc" target="_blank">ReDoc</a> &bull;
                <a href="/history" target="_blank">API History</a>
            </div>
        </div>

        <script>
            async function calculate() {
                const a = parseFloat(document.getElementById('num1').value);
                const b = parseFloat(document.getElementById('num2').value);
                const btn = document.getElementById('submitBtn');
                btn.textContent = 'Calculating...';
                try {
                    const response = await fetch('/multiply', {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify({ a, b })
                    });
                    const data = await response.json();
                    document.getElementById('resultValue').textContent = `${data.a} × ${data.b} = ${data.result}`;
                    document.getElementById('resultBox').style.display = 'block';
                } catch (err) {
                    alert('Error calculating multiplication: ' + err);
                } finally {
                    btn.textContent = 'Multiply Numbers';
                }
            }
        </script>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

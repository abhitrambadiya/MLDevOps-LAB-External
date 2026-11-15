# ML DevOps Laboratory - POE Answer Book (Problem Statement C)
**Course:** ML DevOps Laboratory (`UAMPC0732` / `UDSPC0732`)  
**Department:** Computer Science & Engineering (AIML & DS)  
**KIT’s College of Engineering (Autonomous), Kolhapur**  

---

## 📌 Problem Statement C
> **Write a Python program to accept two numbers and display its Multiplication.**  
> **Integrate this program using FastAPI, Jenkins, Pytest, Evidently tool. Git is optional. You can use VSCode, NotePad++**  
> **AnswerBook : Mention All commands used for the configuration.**

---

## ⚡ 1. Minimal Working Source Code

### A. Python Program for Multiplication (`src/math_operations.py` - 3 lines)
```python
def multiply(a, b):
    res = float(a) * float(b)
    return int(res) if res.is_integer() else res
```

### B. Interactive CLI Program (`src/cli.py` - 10 lines)
```python
from math_operations import multiply

def main():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print(f"Result: {a} * {b} = {multiply(a, b)}")

if __name__ == "__main__":
    main()
```

### C. FastAPI Integration with Plain HTML UI (`src/main.py` - 25 lines)
```python
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from src.math_operations import multiply

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <h2>Multiplication Calculator</h2>
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
```

### D. Pytest Test Suite (`tests/test_app.py` - 25 lines)
```python
import pytest
from fastapi.testclient import TestClient
from src.math_operations import multiply
from src.main import app

client = TestClient(app)

def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(-2, 5) == -10
    assert multiply(0, 7) == 0
    assert multiply(2.5, 2) == 5

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
```

### E. Evidently AI Monitoring (`src/monitoring.py` - 18 lines)
```python
import os
import pandas as pd
from evidently import Report
from evidently.presets import DataDriftPreset

def run_monitoring():
    os.makedirs("reports", exist_ok=True)
    ref = pd.DataFrame({"a": [1, 2, 3, 4, 5], "b": [10, 20, 30, 40, 50]})
    curr = pd.DataFrame({"a": [2, 3, 4, 5, 6], "b": [15, 25, 35, 45, 55]})
    report = Report(metrics=[DataDriftPreset()])
    res = report.run(reference_data=ref, current_data=curr)
    path = "reports/evidently_drift_report.html"
    res.save_html(path)
    print(f"Evidently report saved to {path}")
    return path

if __name__ == "__main__":
    run_monitoring()
```

### F. Jenkinsfile (`Jenkinsfile` - 25 lines)
```groovy
pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run Pytest') {
            steps {
                sh 'pytest -v'
            }
        }
        stage('Evidently Monitoring') {
            steps {
                sh 'python3 src/monitoring.py'
            }
        }
        stage('FastAPI Smoke Test') {
            steps {
                sh '''
                    python3 -m uvicorn src.main:app --port 8000 &
                    PID=$!
                    sleep 2
                    curl -s "http://127.0.0.1:8000/multiply?a=4&b=5"
                    kill $PID || true
                '''
            }
        }
    }
}
```

---

## 💻 2. All Commands Used for Configuration

```bash
# 1. Install required packages
pip install fastapi uvicorn pytest httpx pandas evidently

# 2. Run CLI Multiplication program
python3 src/cli.py

# 3. Run Pytest test suite
pytest -v

# 4. Run Evidently AI drift monitoring
python3 src/monitoring.py

# 5. Start FastAPI Server
uvicorn src.main:app --reload --port 8000
# Browser: http://127.0.0.1:8000

# 6. Git commands
git init
git add .
git commit -m "feat: minimal working multiplication pipeline"
```

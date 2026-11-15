# ML DevOps Laboratory - POE Answer Book (Problem Statement C)
**Course:** ML DevOps Laboratory (`UAMPC0732` / `UDSPC0732`)  
**Department:** Computer Science & Engineering (AIML & DS)  
**KIT’s College of Engineering (Autonomous), Kolhapur**  
**GitHub Repository Name:** `MLDevOps-LAB-External`

---

## 📌 Problem Statement C
> **Write a Python program to accept two numbers and display its Multiplication.**  
> **Integrate this program using FastAPI, Jenkins, Pytest, Evidently tool. Git is optional. You can use VSCode, NotePad++**  
> **AnswerBook : Mention All commands used for the configuration.**

---

## ⚡ 1. Minimal Working Source Code

### A. Python Multiplication Function (`src/math_operations.py`)
```python
def multiply(a, b):
    res = float(a) * float(b)
    return int(res) if res.is_integer() else res
```

### B. Interactive CLI Program (`src/cli.py`)
```python
from math_operations import multiply

def main():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print(f"Result: {a} * {b} = {multiply(a, b)}")

if __name__ == "__main__":
    main()
```

### C. FastAPI with Plain HTML UI (`src/main.py`)
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

### D. Pytest Test Suite (`tests/test_app.py`)
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

### E. Evidently AI Monitoring (`src/monitoring.py`)
```python
import os, pandas as pd
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

### F. Jenkinsfile with Auto Git Push Trigger & Compile (`Jenkinsfile`)
```groovy
pipeline {
    agent any

    // Automatically triggers pipeline on any push to Git (checks every minute)
    triggers {
        pollSCM('* * * * *')
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Fetching latest code from Git repository...'
                checkout scm
            }
        }

        stage('Compile Code') {
            steps {
                echo 'Compiling Python code to bytecode and checking syntax...'
                sh 'python3 -m compileall src/'
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Installing required packages...'
                sh 'pip install -r requirements.txt --quiet'
            }
        }

        stage('Run Pytest') {
            steps {
                echo 'Executing test suite...'
                sh 'pytest -v'
            }
        }

        stage('Evidently Monitoring') {
            steps {
                echo 'Generating Evidently AI Data Drift report...'
                sh 'python3 src/monitoring.py'
            }
        }

        stage('FastAPI Smoke Test') {
            steps {
                echo 'Testing FastAPI multiplication endpoint...'
                sh '''
                    python3 -m uvicorn src.main:app --port 8000 &
                    PID=$!
                    sleep 2
                    curl -s "http://127.0.0.1:8000/multiply?a=6&b=7"
                    kill $PID || true
                '''
            }
        }
    }
}
```

---

## 💻 2. All Commands Used for Configuration

### A. Git & GitHub Setup (`MLDevOps-LAB-External`)
```bash
cd "PS_C_Multiplication"

# Initialize local git
git init
git add .
git commit -m "feat: complete ML DevOps POE pipeline"

# Link to GitHub repository
git branch -M main
git remote add origin https://github.com/<YOUR_GITHUB_USERNAME>/MLDevOps-LAB-External.git
git push -u origin main
```

### B. Launch & Open Jenkins
```bash
# 1. Start Jenkins via Docker
docker run -d -p 8080:8080 -p 50000:50000 --name jenkins -v jenkins_home:/var/jenkins_home jenkins/jenkins:lts

# 2. Retrieve initial admin password
docker exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword

# 3. Open Jenkins in browser
open http://localhost:8080
```

### C. Jenkins Job Configuration
1. Click **New Item** ➔ Enter name: `MLDevOps-LAB-External` ➔ Select **Pipeline** ➔ Click **OK**.
2. Under **Build Triggers**, check **Poll SCM** (Schedule: `* * * * *`) or **GitHub hook trigger for GITScm polling**.
3. Under **Pipeline**:
   - Definition: **Pipeline script from SCM**
   - SCM: **Git**
   - Repository URL: `https://github.com/<YOUR_GITHUB_USERNAME>/MLDevOps-LAB-External.git`
   - Branch Specifier: `*/main`
   - Script Path: `Jenkinsfile`
4. Click **Save**.

---

## 🎬 3. External Examiner Demonstration Steps

1. **Show Code in VS Code**:
   - `src/math_operations.py`: Multiplication logic.
   - `src/cli.py`: Interactive CLI input.
   - `src/main.py`: FastAPI web service with plain HTML form.
   - `Jenkinsfile`: Git push trigger + Compile + Test + Monitor.
2. **Demonstrate Auto-Trigger on Git Push**:
   - Make a change in VS Code, run `git commit -am "update"` and `git push origin main`.
   - Show Jenkins automatically detecting the push within 60 seconds and starting build.
3. **Show Jenkins Pipeline Execution**:
   - Show all stages turning green:
     `[Checkout] -> [Compile Code] -> [Install Dependencies] -> [Run Pytest] -> [Evidently Monitoring] -> [FastAPI Smoke Test]`
   - Open **Console Output** to verify the compilation (`compileall src/`) and test results.
4. **Show Web Application**:
   - Open `http://localhost:8000` in browser.
   - Enter two numbers into the HTML form and click "Multiply" to see the output.
5. **Show Evidently Monitoring Report**:
   - Open `reports/evidently_drift_report.html` in browser.

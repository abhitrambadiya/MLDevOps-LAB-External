# ML DevOps POE: Problem Statement C - Multiplication Service

**Course:** ML DevOps Laboratory (`UAMPC0732` & `UDSPC0732`)  
**Department:** Computer Science & Engineering (AIML & DS), KIT's College of Engineering (Autonomous), Kolhapur  
**Tech Stack:** Python 3, FastAPI, Pytest, Evidently AI, Jenkins CI/CD, Git, VS Code

---

## 📌 Problem Statement C
> **Write a Python program to accept two numbers and display its Multiplication.**  
> **Integrate this program using FastAPI, Jenkins, Pytest, Evidently tool. Git is optional. You can use VSCode, NotePad++**

---

## 📁 Project Directory Structure

```text
PS_C_Multiplication/
├── src/
│   ├── __init__.py
│   ├── math_operations.py      # Core multiplication logic & input validation
│   ├── cli.py                  # CLI app accepting 2 numbers & displaying product
│   ├── main.py                 # FastAPI service with GET/POST, history & Web UI
│   └── monitoring.py           # Evidently AI data drift & quality report generator
├── tests/
│   ├── __init__.py
│   ├── test_math_operations.py # 9 unit tests for multiplication & edge cases
│   ├── test_api.py             # 11 integration tests for FastAPI endpoints
│   └── test_monitoring.py      # 3 tests for Evidently report generation
├── reports/
│   ├── pytest_report.xml       # JUnit XML test report for Jenkins
│   └── evidently_drift_report.html # Interactive visual drift report
├── Jenkinsfile                 # Declarative CI/CD pipeline definition
├── requirements.txt            # Project dependencies
├── setup_and_run.sh            # 1-Click execution script
├── ANSWERBOOK.md               # Complete lab answer book writeup + Viva Q&A
└── README.md                   # This documentation
```

---

## 🚀 Quickstart Guide

### 1. Run Everything with One Command
```bash
cd PS_C_Multiplication
./setup_and_run.sh
```

### 2. Manual Execution Step-by-Step

#### Step A: Install Dependencies
```bash
pip install -r requirements.txt
```

#### Step B: Run Standalone CLI Script
```bash
# Interactive mode:
python3 src/cli.py

# Or with CLI arguments:
python3 src/cli.py --num1 15 --num2 4
```

#### Step C: Run Pytest Test Suite
```bash
pytest -v
```

#### Step D: Generate Evidently Monitoring Report
```bash
python3 src/monitoring.py
# Opens reports/evidently_drift_report.html in browser
```

#### Step E: Start FastAPI Web Service
```bash
uvicorn src.main:app --reload --port 8000
```
- **Web UI:** [http://localhost:8000/ui](http://localhost:8000/ui)
- **Interactive Swagger Docs:** [http://localhost:8000/docs](http://localhost:8000/docs)
- **ReDoc Documentation:** [http://localhost:8000/redoc](http://localhost:8000/redoc)
- **Health Check:** [http://localhost:8000/health](http://localhost:8000/health)

---

## 🛠️ Jenkins CI/CD Pipeline Setup
1. Open Jenkins at `http://localhost:8080`.
2. Click **New Item** -> Enter `Multiplication-CI-CD` -> Select **Pipeline**.
3. Under **Pipeline Definition**, select **Pipeline script from SCM** -> **Git**.
4. Set Repository URL to your repo path and script path to `Jenkinsfile`.
5. Click **Build Now**.
6. View the build dashboard, test reports (23 passed tests), and archived Evidently HTML report.

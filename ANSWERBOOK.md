# ML DevOps Laboratory - POE Answer Book
**KIT’s College of Engineering (Empowered Autonomous), Kolhapur**  
**Department of Computer Science & Engineering (AIML & DS)**  
**Course Name:** ML DevOps Laboratory | **Course Code:** UAMPC0732 & UDSPC0732  
**POE for A.Y.:** 2026-2027  
**Faculty In-Charge:** Asst. Prof. S. D. Jalane & Asst. Prof. V. S. Prabhavalkar  

---

## 📋 Student & Submission Details
- **Student Name:** __________________________________
- **PRN / Roll No:** __________________________________
- **Branch & Division:** CSE (AIML & DS) - Sem VII / Div _____
- **Problem Statement Allotted:** **Problem Statement C**
- **Date of Performance:** 15th November 2026

---

## 🎯 Problem Statement C
> **Write a Python program to accept two numbers and display its Multiplication.**  
> **Integrate this program using FastAPI, Jenkins, Pytest, Evidently tool. Git is optional. You can use VSCode, NotePad++**  
> **AnswerBook : Mention All commands used for the configuration.**

---

## 🏗️ 1. System Architecture & Workflow

```text
+-----------------------------------------------------------------------------------+
|                              DEVELOPER ENVIRONMENT (VS Code)                      |
|                                                                                   |
|  [math_operations.py] ---> [cli.py] (CLI Multiplication Program)                  |
|          |                                                                        |
|          +---------------> [main.py] (FastAPI Web Service + UI + /docs)           |
|                                                                                   |
|  [tests/] (23 Pytest Unit & Integration Tests)                                    |
|  [monitoring.py] (Evidently AI Data Drift & Quality HTML Report)                  |
+-----------------------------------------------------------------------------------+
                                          |
                                          v  git commit & push
+-----------------------------------------------------------------------------------+
|                                GIT VERSION CONTROL                                |
|  - Tracks source code, test suites, and CI/CD pipelines                           |
|  - .gitignore filters caches, virtual environments, and binaries                  |
+-----------------------------------------------------------------------------------+
                                          |
                                          v  triggers pipeline
+-----------------------------------------------------------------------------------+
|                             JENKINS CI/CD AUTOMATION                              |
|                                                                                   |
|  Stage 1: Checkout SCM (Git)                                                      |
|  Stage 2: Environment Setup & Dependencies (`pip install -r requirements.txt`)    |
|  Stage 3: Code Lint & Syntax Check (`python3 -m compileall src/`)                 |
|  Stage 4: Pytest Suite Execution (`pytest --junitxml=reports/pytest_report.xml`)  |
|  Stage 5: Evidently AI Drift Monitoring (`python3 src/monitoring.py`)             |
|  Stage 6: Archive Artifacts (Test XML reports & Evidently HTML dashboards)        |
|  Stage 7: FastAPI Integration & Smoke Test (`uvicorn` + `curl` health check)      |
+-----------------------------------------------------------------------------------+
```

---

## 💻 2. All Commands Used for Configuration

### A. Directory & Environment Setup Commands
```bash
# 1. Navigate to workspace
cd "/Users/abhitrambadiya/Sem 07/Lab MLDevOps/Lab External POE"

# 2. Create project directory structure
mkdir -p "PS_C_Multiplication/src" "PS_C_Multiplication/tests" "PS_C_Multiplication/reports"
cd "PS_C_Multiplication"

# 3. Create Python Virtual Environment (recommended for isolation)
python3 -m venv .venv

# 4. Activate Virtual Environment
# On macOS / Linux:
source .venv/bin/activate
# On Windows:
# .venv\Scripts\activate

# 5. Upgrade pip package manager
pip install --upgrade pip

# 6. Install required dependencies
pip install fastapi uvicorn pydantic pytest httpx pandas evidently
# Or from requirements file:
pip install -r requirements.txt
```

---

### B. Git Version Control Commands
```bash
# 1. Initialize Git repository
git init

# 2. Check repository status
git status

# 3. Stage all source files and test suites
git add .

# 4. Commit files with meaningful commit message
git commit -m "feat: complete ML DevOps POE solution for Problem Statement C (Multiplication with FastAPI, Pytest, Evidently, Jenkins)"

# 5. Check commit history
git log --oneline -n 5
```

---

### C. Program Execution Commands

#### 1. CLI Python Program (Accept Two Numbers & Display Multiplication)
```bash
# Interactive Mode (Prompts for inputs):
python3 src/cli.py

# Command Line Arguments Mode:
python3 src/cli.py --num1 12.5 --num2 4
# Output: Multiplication Result: 12.5 * 4 = 50.0
```

#### 2. Pytest Execution Commands
```bash
# Run all unit and integration tests with verbose output:
pytest -v

# Run tests and generate JUnit XML report for Jenkins integration:
pytest --junitxml=reports/pytest_report.xml -v

# Run only math unit tests:
pytest tests/test_math_operations.py -v

# Run only FastAPI integration tests:
pytest tests/test_api.py -v
```

#### 3. Evidently AI Monitoring Commands
```bash
# Run Evidently Data Drift and Data Summary monitoring script:
python3 src/monitoring.py

# View generated interactive HTML report in browser:
# macOS:
open reports/evidently_drift_report.html
# Linux:
# xdg-open reports/evidently_drift_report.html
# Windows:
# start reports/evidently_drift_report.html
```

#### 4. FastAPI Service Commands
```bash
# Start FastAPI application using Uvicorn server:
uvicorn src.main:app --host 127.0.0.1 --port 8000 --reload

# Test endpoints using cURL:
# Health check:
curl -s http://127.0.0.1:8000/health

# GET Multiplication:
curl -s "http://127.0.0.1:8000/multiply?a=25&b=4"

# POST Multiplication:
curl -s -X POST http://127.0.0.1:8000/multiply \
     -H "Content-Type: application/json" \
     -d '{"a": 15.0, "b": 6.0}'

# View History:
curl -s http://127.0.0.1:8000/history
```

---

### D. Jenkins CI/CD Setup Commands

#### 1. Running Jenkins Locally
```bash
# Option A: Run Jenkins via Docker
docker run -d -p 8080:8080 -p 50000:50000 --name jenkins-mldevops -v jenkins_home:/var/jenkins_home jenkins/jenkins:lts

# Option B: Run Jenkins via Homebrew (macOS)
brew install jenkins-lts
brew services start jenkins-lts
```

#### 2. Jenkins Pipeline Configuration Steps in UI
1. Open web browser and access `http://localhost:8080`.
2. Retrieve initial admin password:
   `cat ~/.jenkins/secrets/initialAdminPassword` (or docker logs).
3. Install suggested plugins (**Git**, **Pipeline**, **JUnit Plugin**, **HTML Publisher Plugin**).
4. Click **New Item** -> Name: `Multiplication-CI-CD` -> Select **Pipeline** -> Click **OK**.
5. In Pipeline configuration:
   - Select **Pipeline script from SCM**.
   - SCM: **Git**.
   - Repository URL: Path to local folder or GitHub remote URL.
   - Script Path: `Jenkinsfile`.
6. Click **Save** and click **Build Now**.
7. View execution results in Stage View:
   - Stage 1: Checkout
   - Stage 2: Environment Setup & Dependencies
   - Stage 3: Code Syntax & Lint Check
   - Stage 4: Run Pytest Test Suite
   - Stage 5: Evidently Data Drift Monitoring
   - Stage 6: FastAPI Smoke Test

---

## 📝 3. Source Code Listings

### A. Core Multiplication Logic (`src/math_operations.py`)
```python
from typing import Union

Number = Union[int, float]

def multiply(a: Number, b: Number) -> Number:
    """Multiply two numbers and return the product with type validation."""
    if isinstance(a, bool) or isinstance(b, bool):
        raise TypeError(f"Invalid input: booleans not allowed (a={a}, b={b})")
    if not isinstance(a, (int, float)):
        try:
            a = float(a)
        except (ValueError, TypeError):
            raise TypeError(f"Invalid input: 'a' must be numeric, got {type(a).__name__}")
    if not isinstance(b, (int, float)):
        try:
            b = float(b)
        except (ValueError, TypeError):
            raise TypeError(f"Invalid input: 'b' must be numeric, got {type(b).__name__}")
    result = a * b
    if isinstance(a, int) and isinstance(b, int):
        return int(result)
    return round(float(result), 10)
```

### B. Interactive CLI Program (`src/cli.py`)
```python
import sys, argparse
from math_operations import multiply

def main():
    parser = argparse.ArgumentParser(description="Multiply two numbers")
    parser.add_argument("--num1", "-a", type=float, default=None)
    parser.add_argument("--num2", "-b", type=float, default=None)
    args = parser.parse_args()

    if args.num1 is not None and args.num2 is not None:
        print(f"Multiplication Result: {args.num1} * {args.num2} = {multiply(args.num1, args.num2)}")
        return 0

    print("=" * 60)
    print(" ML DevOps POE - Problem Statement C: Number Multiplication ")
    print("=" * 60)
    a = float(input("Enter the first number: ").strip())
    b = float(input("Enter the second number: ").strip())
    result = multiply(a, b)
    print(f"Result: {a} * {b} = {result}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
```

### C. FastAPI Web Service (`src/main.py`)
```python
from datetime import datetime, timezone
from fastapi import FastAPI, HTTPException, Query, status
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field
from src.math_operations import multiply

app = FastAPI(title="ML DevOps POE - Multiplication Service", version="1.0.0")
request_history = []

class MultiplicationRequest(BaseModel):
    a: float = Field(..., example=15.0)
    b: float = Field(..., example=4.0)

class MultiplicationResponse(BaseModel):
    a: float
    b: float
    operation: str = "multiplication"
    result: float
    timestamp: str

@app.get("/health")
def health_check():
    return {"status": "healthy", "timestamp": datetime.now(timezone.utc).isoformat()}

@app.get("/multiply", response_model=MultiplicationResponse)
def multiply_get(a: float = Query(...), b: float = Query(...)):
    res = multiply(a, b)
    record = {"a": a, "b": b, "operation": "multiplication", "result": res, "timestamp": datetime.now(timezone.utc).isoformat()}
    request_history.append(record)
    return record

@app.post("/multiply", response_model=MultiplicationResponse)
def multiply_post(payload: MultiplicationRequest):
    res = multiply(payload.a, payload.b)
    record = {"a": payload.a, "b": payload.b, "operation": "multiplication", "result": res, "timestamp": datetime.now(timezone.utc).isoformat()}
    request_history.append(record)
    return record
```

### D. Evidently AI Monitoring (`src/monitoring.py`)
```python
import os, numpy as np, pandas as pd
from evidently import Report
from evidently.presets import DataDriftPreset, DataSummaryPreset
from src.math_operations import multiply

def run_evidently_report(output_dir="reports"):
    os.makedirs(output_dir, exist_ok=True)
    report_path = os.path.join(output_dir, "evidently_drift_report.html")

    np.random.seed(42)
    ref_df = pd.DataFrame({
        "num1": np.random.uniform(1.0, 50.0, 100),
        "num2": np.random.uniform(1.0, 50.0, 100)
    })
    ref_df["product"] = [multiply(a, b) for a, b in zip(ref_df.num1, ref_df.num2)]

    curr_df = pd.DataFrame({
        "num1": np.random.uniform(50.0, 200.0, 100),
        "num2": np.random.uniform(50.0, 200.0, 100)
    })
    curr_df["product"] = [multiply(a, b) for a, b in zip(curr_df.num1, curr_df.num2)]

    report = Report(metrics=[DataDriftPreset(), DataSummaryPreset()])
    snapshot = report.run(reference_data=ref_df, current_data=curr_df)
    snapshot.save_html(report_path)
    return report_path
```

---

## 📊 4. Test Results & Verification

### Pytest Test Execution Output:
```text
============================= test session starts ==============================
collected 23 items

tests/test_api.py::test_root_endpoint PASSED                             [  4%]
tests/test_api.py::test_health_endpoint PASSED                           [  8%]
tests/test_api.py::test_multiply_get_success PASSED                      [ 13%]
tests/test_api.py::test_multiply_get_floating_points PASSED              [ 17%]
tests/test_api.py::test_multiply_get_missing_params PASSED               [ 21%]
tests/test_api.py::test_multiply_get_invalid_type PASSED                 [ 26%]
tests/test_api.py::test_multiply_post_success PASSED                     [ 30%]
tests/test_api.py::test_multiply_post_negative_values PASSED             [ 34%]
tests/test_api.py::test_multiply_post_invalid_body PASSED                [ 39%]
tests/test_api.py::test_history_endpoint PASSED                          [ 43%]
tests/test_api.py::test_ui_endpoint PASSED                               [ 47%]
tests/test_math_operations.py::test_positive_integers PASSED             [ 52%]
tests/test_math_operations.py::test_negative_numbers PASSED              [ 56%]
tests/test_math_operations.py::test_multiplication_with_zero PASSED      [ 60%]
tests/test_math_operations.py::test_multiplication_with_one PASSED       [ 65%]
tests/test_math_operations.py::test_floating_point_numbers PASSED        [ 69%]
tests/test_math_operations.py::test_commutative_property PASSED          [ 73%]
tests/test_math_operations.py::test_string_numeric_conversion PASSED     [ 78%]
tests/test_math_operations.py::test_invalid_type_raises_type_error PASSED [ 82%]
tests/test_math_operations.py::test_boolean_rejection PASSED             [ 86%]
tests/test_monitoring.py::test_reference_data_generation PASSED          [ 91%]
tests/test_monitoring.py::test_current_data_generation PASSED            [ 95%]
tests/test_monitoring.py::test_evidently_html_report_generation PASSED   [100%]

======================== 23 passed in 3.14s ========================
```

---

## 🎓 5. POE Viva-Voce Questions & Model Answers

### Q1. What is your understanding about Git, GitHub, and GitLab?
- **Git:** A distributed version control system running locally to record code revisions, manage branches, and track changes across commits.
- **GitHub:** A cloud-based hosting platform for Git repositories with collaboration features, pull requests, issue tracking, and GitHub Actions for CI/CD.
- **GitLab:** A DevOps lifecycle platform providing Git repository hosting, integrated CI/CD pipelines, container registry, and security scanning in a single tool.

### Q2. What is your understanding about MLflow Tool? Which different features do you know?
- **MLflow:** An open-source platform for managing the end-to-end machine learning lifecycle.
- **Key Features:**
  1. *MLflow Tracking:* Logs parameters, code versions, metrics, and output files (artifacts) during runs.
  2. *MLflow Projects:* Packages reusable data science code in standard format (conda/docker).
  3. *MLflow Models:* Deploys models to diverse serving platforms (REST API, Docker, SageMaker).
  4. *MLflow Model Registry:* Centralized collaborative hub for model versioning, stage transitions (Staging, Production, Archived), and approvals.

### Q3. What is your understanding about AWS IAM and its concepts? What IAM configuration will you suggest for your final year project?
- **AWS IAM (Identity and Access Management):** Controls who is authenticated (signed in) and authorized (has permissions) to AWS resources.
- **Concepts:** Users (identities), Groups (collections of users), Roles (assumable identities with temporary credentials), and Policies (JSON documents specifying Allow/Deny actions on resources).
- **Project Suggestion:** Follow the Principle of Least Privilege (PoLP). Create an IAM group for developers with limited read/write access to S3 and CloudWatch, and an IAM Role for EC2/Lambda with fine-grained access only to the model artifact S3 bucket.

### Q4. What is your understanding about AWS S3 buckets and its use? Which part of your project can be moved to S3?
- **AWS S3:** Scalable, highly available object storage service with 99.999999999% (11 9s) durability.
- **Project Usage:** Store training/validation datasets, raw incoming inference batches, serialized model weights (`.pkl`, `.onnx`), and Evidently AI HTML drift monitoring reports.

### Q5. What is your understanding about AWS EC2 and its use? Which part of your project can be moved to AWS EC2?
- **AWS EC2:** Elastic Compute Cloud provides resizable virtual machine capacity in the cloud.
- **Project Usage:** Host the production FastAPI web service with Uvicorn/Gunicorn behind an NGINX reverse proxy, or run self-hosted Jenkins agents to execute CI/CD build pipelines.

### Q6. What is your understanding about Docker? If Docker needs to be created for your project, explain the same.
- **Docker:** Containerization platform packaging application code and all its dependencies into an isolated, portable container image.
- **Project Dockerfile:**
  ```dockerfile
  FROM python:3.11-slim
  WORKDIR /app
  COPY requirements.txt .
  RUN pip install --no-cache-dir -r requirements.txt
  COPY . .
  EXPOSE 8000
  CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
  ```

### Q7. What is your understanding about Kubernetes (K8s) and its features?
- **Kubernetes:** Open-source container orchestration system for automating deployment, scaling, and management of containerized applications.
- **Key Features:** Pod management, automated rollouts and rollbacks, horizontal pod autoscaling (HPA), service discovery, load balancing, and self-healing (restarting failed containers).

### Q8. How have you used AWS SageMaker? Which tools of SageMaker have you used?
- **SageMaker:** Fully managed service for building, training, and deploying ML models.
- **Key Tools:** SageMaker Studio (IDE), SageMaker Notebooks (EDA), SageMaker Training Jobs, SageMaker Pipelines (CI/CD for ML), and SageMaker Endpoints (real-time serverless inference).

### Q9. What is your understanding about Pytest? How are key points of Pytest from today's problem statement?
- **Pytest:** A testing framework for Python supporting simple asserts, test discovery, parameterized tests, fixtures, and JUnit XML report generation.
- **In Today's Lab:** We implemented 23 tests testing:
  - Arithmetic correctness (positive, negative, zero, float).
  - Mathematical properties (commutativity $a \times b = b \times a$, identity $a \times 1 = a$).
  - Boundary cases and type rejections (rejecting non-numeric types and booleans).
  - FastAPI HTTP response codes (200 OK, 422 Unprocessable Entity for invalid schema).

### Q10. What is your understanding about Evidently? How are key points of Evidently from today's problem statement?
- **Evidently AI:** Open-source ML observability and monitoring tool that detects data drift, target drift, model performance decay, and data quality degradation.
- **In Today's Lab:** Evaluated incoming calculation requests against a baseline dataset using statistical two-sample tests (Kolmogorov-Smirnov and PSI) and generated an interactive HTML report (`reports/evidently_drift_report.html`) to visualize distribution shifts.

### Q11. For any GenAI Application, if you have to think about MLOps lifecycle, which tools will you use and why?
- **Lifecycle & Tools:**
  1. *Prompt Engineering & Tracking:* Langfuse / MLflow GenAI / Trulens.
  2. *Evaluation:* Ragas (context precision, faithfulness, answer relevance).
  3. *Vector Storage:* ChromaDB / Pinecone / pgvector for semantic retrieval.
  4. *Serving & Guardrails:* vLLM / NeMo Guardrails / FastAPI.
  5. *CI/CD:* GitHub Actions or Jenkins to evaluate prompt changes automatically against regression benchmarks.

### Q12. Do you know any data pipeline open-source MLOps tools? Have you tried any?
- **Open-source Pipeline Tools:** Apache Airflow, Prefect, Kubeflow Pipelines, Luigi, and DVC (Data Version Control). Airflow and Prefect schedule and orchestrate DAGs (Directed Acyclic Graphs) of tasks like data ingestion, validation, and training.

### Q13. Do you know any products used in AI/Data Science domain where data pipeline feature is inbuilt available?
- **Products:**
  - **Databricks:** Lakeflow and Delta Live Tables (DLT) for streaming/batch pipelines.
  - **AWS SageMaker:** SageMaker Pipelines for step-by-step DAG workflow creation.
  - **Google Cloud Vertex AI:** Vertex AI Pipelines powered by Kubeflow.
  - **Snowflake:** Snowpark and Dynamic Tables.

### Q14. Have you worked on APIs and Testing? Which application have you created APIs for?
- **Yes:** Created RESTful APIs using **FastAPI** for our Multiplication Service.
- **Features Tested:** Request validation with Pydantic schemas, query parameters (`/multiply?a=10&b=20`), JSON body requests via POST, Swagger UI documentation (`/docs`), and automated regression testing with Pytest's `TestClient`.

### Q15. Have you checked MLOps Engineer job postings on LinkedIn? What CV changes do you need to do to fit the role?
- **Required Industry Skills:** CI/CD pipeline automation (Jenkins, GitHub Actions), Container orchestration (Docker, Kubernetes), Model tracking and registries (MLflow), Data/Model monitoring (Evidently, Prometheus), and Cloud infrastructure (AWS/GCP).
- **CV Modifications:**
  1. Highlight hands-on CI/CD pipeline implementations and test suites.
  2. Add quantified metrics (e.g., "Automated model testing reducing deployment regression errors by 90%").
  3. Include specialized sections for MLOps tools: Docker, K8s, MLflow, Pytest, Evidently, FastAPI.

### Q16. Two Target MLOps Job Postings Analysis:
1. **MLOps Engineer - FinTech/Banking:**
   - *Core Requirements:* Python, Docker, Kubernetes, CI/CD with Jenkins/GitLab, Model monitoring for drift detection (Evidently AI), Data governance.
2. **Platform Engineer (ML/AI) - Cloud/SaaS:**
   - *Core Requirements:* AWS (SageMaker, S3, IAM, EKS), Terraform, MLflow, FastAPI microservices, automated unit/integration testing with Pytest.

### Q17. Tool Architecture Diagram for Today's POE Problem Statement:
```text
+-----------------------------------------------------------------------------------+
|  [VS Code IDE]           [Python 3.14 CLI]          [FastAPI Web Microservice]    |
|   Code Authoring          `src/cli.py`               `src/main.py`                |
|   & Debugging             Accepts 2 numbers          REST Endpoints & Web UI      |
+-----------------------------------------------------------------------------------+
                                         |
                                         v
+-----------------------------------------------------------------------------------+
|  [Pytest Framework]                              [Evidently AI Tool]              |
|   `tests/` (23 unit & API tests)                  `src/monitoring.py`             |
|   Generates `reports/pytest_report.xml`           Generates `evidently_drift.html`|
+-----------------------------------------------------------------------------------+
                                         |
                                         v
+-----------------------------------------------------------------------------------+
|  [Git Version Control]                           [Jenkins CI/CD Automation]       |
|   Local repo & commit tracking                    `Jenkinsfile` Automated Stages: |
|   Branching & history                             Lint -> Test -> Monitor -> Smoke|
+-----------------------------------------------------------------------------------+
```

---
*Student Signature:* __________________________ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; *Examiner Signature:* __________________________

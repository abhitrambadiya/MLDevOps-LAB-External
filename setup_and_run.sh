#!/usr/bin/env bash
# ==============================================================================
# ML DevOps Laboratory - POE Solution Runner
# Problem Statement C: Accept two numbers and display its Multiplication
# Stack: Python, FastAPI, Pytest, Evidently, Jenkins, Git
# ==============================================================================

set -e

PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$PROJECT_DIR"

echo "=================================================================="
echo "    ML DevOps POE - Problem Statement C Execution Script         "
echo "=================================================================="

# Step 1: Environment Check
echo "[1/5] Checking Python environment..."
python3 --version

# Step 2: Install dependencies
echo "[2/5] Installing project dependencies..."
pip install -r requirements.txt --quiet

# Step 3: Run Pytest Test Suite
echo "[3/5] Running Pytest unit and integration tests..."
pytest --junitxml=reports/pytest_report.xml -v

# Step 4: Run Evidently AI Data Drift Report
echo "[4/5] Running Evidently AI data drift and summary monitoring..."
python3 src/monitoring.py

# Step 5: Demonstration of CLI script
echo "[5/5] Testing Multiplication CLI script with sample input (8 * 9)..."
python3 src/cli.py --num1 8 --num2 9

echo "=================================================================="
echo " All automated steps completed successfully!"
echo " "
echo " To start the FastAPI interactive server and Web UI, run:"
echo "    cd PS_C_Multiplication"
echo "    uvicorn src.main:app --reload --port 8000"
echo " "
echo " Then open in your browser:"
echo "    - Web UI:       http://localhost:8000/ui"
echo "    - Swagger Docs: http://localhost:8000/docs"
echo "    - Evidently:    file://${PROJECT_DIR}/reports/evidently_drift_report.html"
echo "=================================================================="

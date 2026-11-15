#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"

echo "=== Running Pytest ==="
pytest -v

echo "=== Running Evidently ==="
python3 src/monitoring.py

echo "=== Testing CLI ==="
python3 src/cli.py <<EOF
4
5
EOF

echo "=== Starting FastAPI Server (http://127.0.0.1:8000) ==="
uvicorn src.main:app --reload --port 8000

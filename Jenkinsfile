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

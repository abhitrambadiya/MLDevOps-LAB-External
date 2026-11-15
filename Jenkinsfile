pipeline {
    agent any

    // Automatically triggers pipeline on git push (checks every minute)
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
                sh 'pip install --break-system-packages -r requirements.txt --quiet || pip install -r requirements.txt --quiet'
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

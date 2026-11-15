pipeline {
    agent any

    environment {
        PYTHONUNBUFFERED = '1'
        VENV_NAME = '.venv'
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out source code...'
                checkout scm
            }
        }

        stage('Environment Setup & Dependencies') {
            steps {
                echo 'Setting up Python virtual environment and installing packages...'
                sh '''
                    if [ ! -d "${VENV_NAME}" ]; then
                        python3 -m venv ${VENV_NAME}
                    fi
                    . ${VENV_NAME}/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Code Syntax & Lint Check') {
            steps {
                echo 'Checking python syntax and compilation...'
                sh '''
                    . ${VENV_NAME}/bin/activate
                    python3 -m compileall src/
                '''
            }
        }

        stage('Run Pytest Test Suite') {
            steps {
                echo 'Executing unit and integration tests via Pytest...'
                sh '''
                    . ${VENV_NAME}/bin/activate
                    pytest --junitxml=reports/pytest_report.xml -v
                '''
            }
            post {
                always {
                    junit allowEmptyResults: true, testResults: 'reports/pytest_report.xml'
                }
            }
        }

        stage('Evidently Data Drift Monitoring') {
            steps {
                echo 'Generating Evidently AI Data Drift & Model Monitoring Report...'
                sh '''
                    . ${VENV_NAME}/bin/activate
                    python3 src/monitoring.py
                '''
            }
            post {
                always {
                    archiveArtifacts artifacts: 'reports/*.html', allowEmptyArchive: true
                }
            }
        }

        stage('FastAPI Integration Smoke Test') {
            steps {
                echo 'Launching FastAPI in background and validating endpoints...'
                sh '''
                    . ${VENV_NAME}/bin/activate
                    python3 -m uvicorn src.main:app --host 127.0.0.1 --port 8000 &
                    APP_PID=$!
                    sleep 3
                    echo "Checking /health endpoint..."
                    curl -s -f http://127.0.0.1:8000/health || (kill $APP_PID && exit 1)
                    echo "Checking /multiply calculation endpoint..."
                    curl -s -f "http://127.0.0.1:8000/multiply?a=15&b=4" || (kill $APP_PID && exit 1)
                    kill $APP_PID || true
                    echo "FastAPI smoke tests passed successfully!"
                '''
            }
        }
    }

    post {
        success {
            echo '==================================================='
            echo ' ML DevOps POE: Multiplication Pipeline SUCCEEDED! '
            echo '==================================================='
        }
        failure {
            echo 'Pipeline failed! Please inspect logs above.'
        }
    }
}

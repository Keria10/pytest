pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
        REPORT_DIR = 'reports'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
                sh 'pwd && ls -la'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    python3 -m venv ${VENV_DIR}
                    . ${VENV_DIR}/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Unit Tests') {
            steps {
                sh '''
                    . ${VENV_DIR}/bin/activate
                    pytest test_case.py --junitxml=${REPORT_DIR}/unit-results.xml
                '''
            }
        }

        stage('Run API Tests') {
            steps {
                sh '''
                    . ${VENV_DIR}/bin/activate
                    pytest test_API.py --junitxml=${REPORT_DIR}/api-results.xml
                '''
            }
        }

//         stage('Run Tests') {
//             steps {
//                 sh '''
//                     . ${VENV_DIR}/bin/activate
//                     mkdir -p ${REPORT_DIR}
//                     pytest --junitxml=${REPORT_DIR}/results.xml --html=${REPORT_DIR}/report.html --self-contained-html
//                 '''
//             }
            post {
                always {
                    junit "${REPORT_DIR}/results.xml"
                    publishHTML([
                        reportDir: "${REPORT_DIR}",
                        reportFiles: 'report.html',
                        reportName: 'Pytest HTML Report',
                        allowMissing: false,
                        alwaysLinkToLastBuild: true,
                        keepAll: true
                    ])
                }
            }
        }
//     }

    post {
        always {
            echo '测试执行完成！'
        }
        failure {
            echo '测试有失败用例，请检查报告。'
        }
    }
}
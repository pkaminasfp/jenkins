pipeline {
    agent any

    stages {
        stage('Clonar repositorio') {
            steps {
                git 'https://github.com/pkaminasfp/jenkins.git'
            }
        }

        stage('Instalar dependencias') {
            steps {
                sh 'pip install -r requirements.txt || true'
            }
        }

        stage('Ejecutar pruebas') {
            steps {
                sh 'python -m unittest test_calculadora.py'
            }
        }
    }

    post {
        always {
            junit '**/test-results/*.xml'
        }
        success {
            echo 'Las pruebas pasaron correctamente.'
        }
        failure {
            echo 'Algunas pruebas fallaron.'
        }
    }
}

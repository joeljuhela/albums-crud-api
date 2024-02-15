pipeline {
    agent any
    stages {
        stage('Linter') {
            steps {
                sh 'flake8 ./api'
            }
        }
    }
}
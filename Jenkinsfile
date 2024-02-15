pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'api:test'
    }

    stages {
        stage('Build test image') {
            steps {
                script {
                    docker.build(env.DOCKER_IMAGE, './api')
                }
            }
        }
        stage('Linter') {
            steps {
                dockerImage = docker.build 
                sh 'flake8 ./api'
            }
        }
    }
}
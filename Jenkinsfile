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
                script {
                    docker.image(env.DOCKER_IMAGE).inside {
                        sh 'flake8 ./api'
                    }
                }
            }
        }
    }
}
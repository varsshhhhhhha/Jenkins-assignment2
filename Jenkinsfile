pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "your-dockerhub-username/flask-app"
        DOCKER_CREDENTIALS_ID = "Docker"
    }

    stages {
        stage('Checkout Code') {
            steps {
                git credentialsId: 'github-credentials', url: 'https://github.com/varsshhhhhhha/Jenkins-assignment2.git', branch: 'main'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("${DOCKER_IMAGE}:latest")
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    docker.image("${DOCKER_IMAGE}:latest").inside {
                        sh "pytest"
                    }
                }
            }
        }

        stage('Push Image to Docker Hub') {
            steps {
                script {
                    docker.withRegistry('https://index.docker.io/v1/', DOCKER_CREDENTIALS_ID) {
                        docker.image("${DOCKER_IMAGE}:latest").push()
                    }
                }
            }
        }

        stage('Deploy Locally') {
            steps {
                script {
                    sh "docker pull ${DOCKER_IMAGE}:latest"
                    sh "docker-compose up -d"
                }
            }
        }
    }
}

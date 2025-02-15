pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "varsshhhhhhha/flask-app"
        DOCKER_CREDENTIALS_ID = "Docker"
        GIT_CREDENTIALS_ID = "a8736c91-7400-45a2-ad60-a4e98dfa4bda"
        GIT_REPO = "https://github.com/varsshhhhhhha/Jenkins-assignment2.git"
        BRANCH = "main"
    }

    stages {
        stage('Checkout Code') {
            steps {
                script {
                    echo "Cloning repository..."
                    checkout([
                        $class: 'GitSCM',
                        branches: [[name: "*/${BRANCH}"]],
                        userRemoteConfigs: [[
                            url: "${GIT_REPO}",
                            credentialsId: "${GIT_CREDENTIALS_ID}"
                        ]]
                    ])
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    echo "Building Docker image..."
                    docker.build("${DOCKER_IMAGE}:latest")
                }
            }
        }

        

        stage('Push Image to Docker Hub') {
            steps {
                script {
                    echo "Pushing Docker image to Docker Hub..."
                    docker.withRegistry('https://index.docker.io/v1/', DOCKER_CREDENTIALS_ID) {
                        docker.image("${DOCKER_IMAGE}:latest").push()
                    }
                }
            }
        }

        stage('Deploy Locally') {
            steps {
                script {
                    echo "Deploying application using Docker Compose..."
                    
                    // Stop and remove old container if running
                    sh """
                    docker stop flask-app || true
                    docker rm flask-app || true
                    docker pull ${DOCKER_IMAGE}:latest
                    docker-compose up -d --force-recreate
                    """
                }
            }
        }
    }

    post {
        success {
            echo "Pipeline executed successfully!"
        }
        failure {
            echo "Pipeline failed! Check the logs for errors."
        }
    }
}

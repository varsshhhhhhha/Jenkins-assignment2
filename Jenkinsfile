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

        stage('Run Tests') {
            steps {
                script {
                    echo "Running tests inside the container..."
                    docker.image("${DOCKER_IMAGE}:latest").inside("--workdir /app") { 
                        sh "pytest || { echo 'Tests failed'; exit 1; }"
                    }
                }
            }
        }

        stage('Push Image to Docker Hub') {
            steps {
                script {
                    echo "Running tests..."
                    sh "docker run --rm -w /app ${DOCKER_IMAGE}:latest pytest"
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

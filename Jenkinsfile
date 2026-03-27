pipeline {
    agent any

    environment {
        AWS_REGION = "ap-south-1"
        ECR_REPO = "272084046243.dkr.ecr.ap-south-1.amazonaws.com/flask-app"
        IMAGE_TAG = "${BUILD_NUMBER}"
    }

    stages {

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t flask-app:$IMAGE_TAG .'
            }
        }

        stage('Tag Image') {
            steps {
                sh 'docker tag flask-app:$IMAGE_TAG $ECR_REPO:$IMAGE_TAG'
            }
        }

        stage('Login to ECR') {
            steps {
                sh '''
                aws ecr get-login-password --region $AWS_REGION \
                | docker login --username AWS --password-stdin $ECR_REPO
                '''
            }
        }

        stage('Push to ECR') {
            steps {
                sh 'docker push $ECR_REPO:$IMAGE_TAG'
            }
        }

        stage('Deploy to Kubernetes (Helm)') {
            steps {
                sh '''
                helm upgrade --install flask-app ./flask-app \
                --set image.tag=$IMAGE_TAG
                '''
            }
        }
    }
}
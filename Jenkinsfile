pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git 'https://github.com/SankuriDev/flask-app.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t flask-app:latest .'
            }
        }

        stage('Run Container (Test)') {
            steps {
                sh 'docker run -d -p 5000:5000 flask-app:latest || true'
            }
        }
    }
}

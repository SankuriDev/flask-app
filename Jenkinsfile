pipeline {
    agent any

    stages {

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t flask-app:latest .'
            }
        }

        stage('Run Container (Test)') {
            steps {
                sh 'docker stop myapp1 || true'
                sh 'docker rm myapp1 || true`'
                sh 'docker run -d -p 5000:5000 --name myapp flask-app:latest || true'
            }
        }
    }
}

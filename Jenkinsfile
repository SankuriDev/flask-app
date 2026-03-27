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
                sh 'docker stop myapp1'
                sh 'docker rm myapp1'
                sh 'docker run -d -p 5000:5000 --name myapp flask-app:latest || true'
            }
        }
    }
}

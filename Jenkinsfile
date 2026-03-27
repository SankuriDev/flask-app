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
                sh '''
                set +e
                docker stop myapp1 || true
                docker rm myapp1 || true
                set -e
                
                docker run -d -p 5000:5000 --name myapp1 flask-app:latest
                '''
            }
        }
    }
}

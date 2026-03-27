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
                sh(script: 'docker rm -f myapp1', returnStatus: true)
                sh 'docker run -d -p 5000:5000 --name myapp1 flask-app:latest'
            }
        }
    }
}

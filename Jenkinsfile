pipeline {
    agent any

    stages {

        stage('Build') {
            steps {
                bat 'docker build -t employee-api .'
            }
        }

        stage('Run') {
            steps {
                bat 'docker compose up -d'
            }
        }
    }
}

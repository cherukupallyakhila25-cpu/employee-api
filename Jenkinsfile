pipeline {

    agent any

    stages {

        stage('Clone') {
            steps {
                git 'https://github.com/cherukupallyakhila25-cpu/employee-api.git'
            }
        }

        stage('Build') {
            steps {
                sh 'docker build -t employee-api .'
            }
        }

        stage('Run') {
            steps {
                sh 'docker-compose up -d'
            }
        }
    }
}

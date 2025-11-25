pipeline {
    agent any

    environment {
    IMAGE = "krishnachaitanya1605/imt2023039:latest"
}


    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest -v'
            }
        }

        stage('Build Docker Image') {
            when {
                expression { currentBuild.currentResult == "SUCCESS" }
            }
            steps {
                sh 'docker build -t $IMAGE .'
            }
        }

        stage('Push Docker Image') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'Docker-creds',
                                                  usernameVariable: 'USER',
                                                  passwordVariable: 'PASS')]) {
                    sh '''
                      echo $PASS | docker login -u $USER --password-stdin
                      docker push $IMAGE
                    '''
                }
            }
        }
    }
}

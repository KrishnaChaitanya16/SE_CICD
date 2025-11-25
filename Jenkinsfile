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
                sh 'python3 -m pip install --upgrade pip'
                sh 'python3 -m pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'python3 -m pytest -v'
            }
        }

        stage('Build Docker Image') {
            when {
                expression { currentBuild.currentResult == "SUCCESS" }
            }
            steps {
                sh 'DOCKER_CONFIG=/tmp /usr/local/bin/docker build -t $IMAGE .'
            }
        }

        stage('Push Docker Image') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'Docker-creds',
                                                  usernameVariable: 'USER',
                                                  passwordVariable: 'PASS')]) {
                    sh """
                      DOCKER_CONFIG=/tmp
                      echo \$PASS | /usr/local/bin/docker login -u \$USER --password-stdin
                      /usr/local/bin/docker push $IMAGE
                    """
                }
            }
        }
    }
}

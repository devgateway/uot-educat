pipeline {
    agent any
    environment {
        COMPOSE_ENV_FILE = ".env.${env.BRANCH_NAME}"
        COMPOSE_PROJECT_NAME = "out-odoo-${env.BRANCH_NAME}"
//        echo COMPOSE_PROJECT_NAME
    }
    stages {
        stage('Test') {
            steps {
                 echo 'Building testing..'

                sh './run-tests.sh'

            }
        }

        stage('Deploy') {
            when {
                anyOf { branch "develop"; branch "staging"; branch "hotfix"; }
            }
            steps {
              echo 'deploying'
                sh './up.sh'
            }
        }

        /*
        stage('Deploy to Production') {
            when {
                branch: "master"
            }
            environment {
                SSH_CREDS = credentials('odoo-production-ssh-creds')
            }
            steps {
                sh 'ssh $SSH_CREDS_USR@prod.example.com -i $SSH_CREDS ./deploy.sh'
            }
        }*/
    }
}


pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker') {
            steps {
                sh 'docker build -t devops-fp050-app:main .'
            }
        }

        stage('Deploy Production') {
            steps {
                sh '''
                    ssh -i /var/lib/jenkins/jenkins-deploy-key \
                        -p 2223 \
                        -o BatchMode=yes \
                        -o ConnectTimeout=10 \
                        devops@127.0.0.1 '
                            set -e

                            if [ ! -d "$HOME/devops-fp050-production/.git" ]; then
                                git clone -b main https://github.com/moliverru/devops-fp050-producto2.git "$HOME/devops-fp050-production"
                            fi

                            git -C "$HOME/devops-fp050-production" pull --ff-only origin main

                            minikube image build -t devops-fp050-app:main "$HOME/devops-fp050-production"

                            kubectl apply -f "$HOME/devops-fp050-production/k8s/deployment-production.yaml" -f "$HOME/devops-fp050-production/k8s/service-production.yaml"

                            kubectl -n production rollout restart deployment/devops-fp050-app

                            kubectl -n production rollout status deployment/devops-fp050-app --timeout=180s

                            kubectl -n production get pods
                        '
                '''
         }
        }
    }


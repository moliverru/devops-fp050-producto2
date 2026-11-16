
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
                sh 'docker build -t devops-fp050-app:develop .'
            }
        }

        stage('Deploy Kubernetes') {
            steps {
                sh '''
                    ssh -i /var/lib/jenkins/jenkins-deploy-key \
                        -p 2223 \
                        -o BatchMode=yes \
                        -o ConnectTimeout=10 \
                        devops@127.0.0.1 '
                            set -e
                            git -C ~/devops-fp050-deploy pull --ff-only origin develop
                            minikube image build -t devops-fp050-app:develop ~/devops-fp050-deploy
                            kubectl apply -f ~/devops-fp050-deploy/k8s/deployment.yaml -f ~/devops-fp050-deploy/k8s/service.yaml
                            kubectl rollout restart deployment/devops-fp050-app
                            kubectl rollout status deployment/devops-fp050-app --timeout=180s
                            kubectl get pods
                        '
                '''
            }
        }
    }
}

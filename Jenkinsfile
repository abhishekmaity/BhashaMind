pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/ContextLogic/bhashamind.git' // Replace with your actual repository URL
            }
        }

        stage('Python Backend') {
            steps {
                dir('backend-python') {
                    sh '''
                    python -m pip install --upgrade pip
                    pip install -r requirements.txt
                    pytest tests
                    '''
                }
            }
        }

        stage('Java Gateway') {
            steps {
                dir('backend-java') {
                    sh './mvnw clean install'
                }
            }
        }

        stage('React Frontend') {
            steps {
                dir('frontend-react') {
                    sh '''
                    npm install
                    npm test
                    npm run build
                    '''
                }
            }
        }
    }
}

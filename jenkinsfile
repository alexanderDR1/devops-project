pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building...'
		sh """pip install -r requirements.txt
		      python setup.py build"""
            }
        }
        stage('Test') {
            steps {
                echo 'Testing...'
		sh """export PYTHONPATH=$WORKSPACE/src
		      pytest tests"""
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying...'
            }
        }
    }
}

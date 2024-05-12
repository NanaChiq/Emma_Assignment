pipeline {
    agent any

     // Setuping our environment
    environment {
        APP_NAME = 'mainMBIApp'
        // Set the application version
        APP_VERSION = '1.0'
    }

    stages {
        // Checking if github exist
        stage('Checkout') {
            steps {
                // Print on the teminal.
                echo 'Checkout stage'
                
                // Checking out for the GitHub repository
                checkout scmGit(branches: [[name: '*/master']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/NanaChiq/Emma_Assignment.git']])
     
            }
        }

        stage('Preparation_Stage') {
            steps {
                
                // Print on the teminal.
                echo "Preparation stage"

                // The CPython is a ShiningPanda plugin which adds Python support to Jenkins with some useful 
                // builders (Python builder, virtualenv builder, tox builder...) 
                // and the ability to use a Python axis in multi-configuration projects 
                // (for testing on multiple versions of Python). 
                // https://plugins.jenkins.io/shiningpanda/
                withPythonEnv('CPython-3.1.1') {
                    //bat "pip install -r requirements.txt" No python libraries a needed

                    // Display the python's version
                    bat 'python --version'

                    
                }
                
            }
        }

        stage('Building_Stage') {
            steps {
                withPythonEnv('CPython-3.1.1') {
                    echo "Building stage completed"

                    // Build the application for the GitHub repository
                    bat 'python mainApp.py'
                }
                
            }
        }

        stage('Testing_Stage') {
            steps {
                withPythonEnv('CPython-3.1.1') {
                    //echo "Testing stage completed"

                    // Running a simple test script 
                    bat 'python test_bmiApp.py'
                }
                
                
            }
        }

    }
}

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

    }
}

pipeline {
    agent any

     // Setuping our environment
    environment {
        // Setuping out virtual envrionment
        VIRTUAL_ENV = 'venv'
        // Give the name of the application
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
                sh 'python3 --version'

                // Checking out for the GitHub repository
               checkout scmGit(branches: [[name: '*/master']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/NanaChiq/Emma_Assignment.git']])
     
            }
        }

        stage('Preparation_Stage') {
            steps {
                
                // Print on the teminal.
                echo "Preparation stage"

                // Setting up my virtual environment
                sh "python3 -m venv $VIRTUAL_ENV"

                // Activate the virtual environment
                sh ". $VIRTUAL_ENV/bin/activate"
                
                // Install dependencies, assuming all the neccessary requirements.txt
                //sh "pip install -r requirements.txt"
                //sh "apt install python3-tkinter"
                
                // Additional dependencies for the PyInstaller using the PiP 
                //sh "pip install pyinstaller"
                //sh "apt install python3-pyinstaller"
                
            }
        }

         stage('Compiling_Stage') {
            steps {
                
                echo "compliation stage completed"
                // Compiling the Tkinter app to a standalone executable with PyInstaller
                ////sh ". $VIRTUAL_ENV/bin/activate && pyinstaller --onefile --windowed ${mainMBIApp}.py"
            
            }
        }

        stage('Building_Stage') {
            steps {
                echo "Building stage completed"
                // Clone the BMIApp code from the GitHub repository
                /////git 'https://github.com/NanaChiq/Emma_Assignment.git'

                // Build the application for the GitHub repository
                /////sh 'python mainApp.py'

            }
        }

        stage('Testing_Stage') {
            steps {
                
                echo "Testing stage completed"
                // Running a simple test script 
                ////sh ". $VIRTUAL_ENV/bin/activate && python test_${mainMBIApp}.py"
                
            }
        }

        stage('Package_Stage') {
            steps {
                
                echo "Package stage completed"
                // Move the executable to a customized directory
                // Create a directory named output for the deployment application
                //////sh "mkdir -p output"

                // Copy the executable file into created deployment directory
                /////sh "cp ${APP_NAME}.py output/${mainMBIApp}"
            }
        }

        stage('Cleanup_Stage') {
            steps {
                echo "Cleaning stage completed"
                // Clean up environment if neccesary
                //////cleanWs()
            }
        }
    }

    // To be executed after all the stages above are done
    post {
        // Must run only if all the stages runs successfully
        success {
            echo "Completed all stages successfuly"
        }

        // Must run only if a failure occurs
        failure {
            echo "Failed to complete"
        }

        always {
            // Must record the results of the outcome of the 
            // stages and archive in a jar file.
            /////junit '**/target/surefire-reports/TEST-*.xml'
            /////archiveArtifacts 'target/*.jar'

            // Additional commands to clean up after pipeline execution
            echo "Cleaning up virtual environment and temporary files..."
            //////sh "rm -rf $VIRTUAL_ENV dist build ${mainMBIApp}.spec"
        }
    }
}

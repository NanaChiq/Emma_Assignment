====================================================================
       Jenkins Build Script for BMI Application using Tkinter 
====================================================================

Introduction:
-------------
This README provides instructions on how to run the Jenkins pipeline script for compiling, testing, and packaging a Tkinter-based BMI application into an executable file.

Prerequisites:
--------------
1. Install of docker as contianer to Jenkins application
2.Jenkins server with the Python plugin installed.
2. Python 3.x and PyInstaller installed on the Jenkins agent.
3. A Jenkins job configured to use declarative pipeline script.

Steps to Run the Build Script:
------------------------------
1. Log in to your Jenkins server crendentials.
2. Navigate to the Jenkins job configured to build the Tkinter application.
3. Click on "Build Now" to start the pipeline.
4. Monitor the build progress in the "Console Output" of the build.
5. Once the build completes, the executable will be available in the "output" directory within the workspace of the Jenkins job.

Notes:
------
- Ensure that the Jenkinsfile is placed at the root of your project repository.
- The `requirements.txt` file must list all Python dependencies required by the application.
- The test script should be designed to be recognized and run by pytest or adjust the pipeline script if using another testing framework.


The follow is the declarative pipeline script
----------------------------------------------





pipeline {
    agent any

    tools {
        python 'Python3'
    }

    environment {
        VIRTUAL_ENV = 'venv'
        APP_NAME = 'mainMBIApp'
    }

    stages {
        stage('Preparation_Stage') {
            steps {
                script {
                    // Setting up my virtual environment
                    sh "python3 -m venv $VIRTUAL_ENV"
                    sh ". $VIRTUAL_ENV/bin/activate"
                    
                    // Install dependencies, assuming all the neccessary requirements.txt
                    sh "pip install -r requirements.txt"
                    
                    // Additional dependencies for the PyInstaller using the PiP 
                    sh "pip install pyinstaller"
                }
            }
        }

        stage('Compiling_Stage') {
            steps {
                script {
                    // Compiling the Tkinter app to a standalone executable with PyInstaller
                    sh ". $VIRTUAL_ENV/bin/activate && pyinstaller --onefile --windowed ${mainMBIApp}.py"
                }
            }
        }

        stage('Testing_Stage') {
            steps {
                script {
                    // Running a simple test script 
                    sh ". $VIRTUAL_ENV/bin/activate && python test_${mainMBIApp}.py"
                }
            }
        }

        stage('Package_Stage') {
            steps {
                script {
                    // Move the executable to a customized directory
                    sh "mkdir -p output"
                    sh "mv dist/${APP_NAME} output/${mainMBIApp}"
                }
            }
        }

        stage('Cleanup_Stage') {
            steps {
                // Clean up environment if neccesary
                cleanWs()
            }
        }
    }

    post {
        always {
            // Additional commands to clean up after pipeline execution
            echo "Cleaning up virtual environment and temporary files..."
            sh "rm -rf $VIRTUAL_ENV dist build ${mainMBIApp}.spec"
        }
    }
}

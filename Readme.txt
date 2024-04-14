pipeline {
    agent any

    tools {
       
        python 'Python3'
    }

    environment {
        VIRTUAL_ENV = 'venv'
        APP_NAME = 'mainBMIApp'
    }

    stages {
        stage('Prepare') {
            steps {
                script {
                    // Setup virtual environment
                    sh "python3 -m venv $VIRTUAL_ENV"
                    sh ". $VIRTUAL_ENV/bin/activate"
                    
                    // Install dependencies, assuming they are listed in requirements.txt
                    sh "pip install -r requirements.txt"
                    
                    // Additional dependencies for PyInstaller
                    sh "pip install pyinstaller"
                }
            }
        }

        stage('Compile') {
            steps {
                script {
                    // Compiling the Tkinter app to a standalone executable with PyInstaller
                    sh ". $VIRTUAL_ENV/bin/activate && pyinstaller --onefile --windowed ${mainBMIApp}.py"
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    // Running a simple test script if available
                    sh ". $VIRTUAL_ENV/bin/activate && python test_${mainBMIApp}.py"
                }
            }
        }

        stage('Package') {
            steps {
                script {
                    // Move the executable to a known directory
                    sh "mkdir -p output"
                    sh "mv dist/${mainBMIApp} output/${mainBMIApp}"
                }
            }
        }

        stage('Cleanup') {
            steps {
                // Clean up environment
                cleanWs()
            }
        }
    }

    post {
        always {
            // Additional commands to clean up after pipeline execution
            echo "Cleaning up virtual environment and temporary files..."
            sh "rm -rf $VIRTUAL_ENV dist build ${mainBMIApp}.spec"
        }
    }
}

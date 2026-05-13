pipeline {

	agent any
    
	environment {
		PYTHON = 'C:\\Users\\admin\\AppData\\Local\\Microsoft\\WindowsApps\\python.exe'
	}

	stages {
		stage ('Checkout code') {
			steps {
				checkout scm
			}
		}

		stage ('Check python version') {
			steps {
				bat "${env.PYTHON} --version"
			}
		}

		stage ('Run extract.py') {
			steps {
				bat "${env.PYTHON} extract.py"
			}
		}
	}
}

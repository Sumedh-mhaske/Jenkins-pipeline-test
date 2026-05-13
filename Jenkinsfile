pipeline {

	agent any
    environment  {
        PYTHON = 'C:\\Python313\\python.exe'
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

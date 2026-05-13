pipeline {

	agent any

	stages {
		stage ('Checkout code') {
			steps {
				checkout scm
			}
		}

		stage ('Check python version') {
			steps {
				bat python --version
			}
		}

		stage ('Run extract.py') {
			steps {
				bat python extract.py
			}
		}
	}
}

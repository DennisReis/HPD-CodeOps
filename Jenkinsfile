pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        sh 'echo "iniciando o build"'
        sh 'docker build -t dmpr.lab .'
      }
    }
    stage('Tests') {
      steps {
        sh 'pwd'
      }
    }
    stage('Aprovação') {
      steps {
        input 'Aprova o Deploy?'
      }
    }
    stage('Deploy') {
      steps {
        sh 'echo "fazendo o deploy"'
      }
    }
  }
}

pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        sh 'echo "iniciando o build"'
        sh 'ls -l'
      }
    }
    stage('Tests') {
      steps {
        sh 'pwd'
      }
    }
    stage('Aporva��o') {
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
pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        sh 'echo "iniciando o build"'
        sh 'docker build -t dmpr.lab .'
        sh '/usr/local/share/gems/gems/fpm-1.10.0/bin/fpm -m "CodeOps,
        <help@codeops.com.br>" --url "https://codeops.com.br" --description "A
        test package" -a noarch -s dir -t rpm -n myapplab --rpm-user root
        --rpm-group root -v 1.0.0 --prefix /opt/myapplab/ .'
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

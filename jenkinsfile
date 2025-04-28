/*pipeline {
    
    agent any;
    
    stages{
        stage("code clone"){
            steps{
                git url : "https://github.com/lokesh-madireddi/webapplication.git", branch : "main"
                echo "code Build successfully"
            }
            
        }
        stage("Build"){
            steps{
                
                sh "docker build -t webapplication ."
            }
            
        }
        stage("Deploy"){
            steps{
                sh "docker run -p 5000:5000 webapplication:latest"
            }
        }
    }
}*/



/*@Library("Shared") _ */
pipeline{
    
    agent any;
    
    stages{
        stage("Code Clone"){
            steps{
               script{
                   git url : "https://github.com/lokesh-madireddi/webapplication.git", branch : "main"
               }
            }
        }
        /*stage("Trivy File System Scan"){
            steps{
                script{
                    trivy_fs()
                }
            }
        }*/
        stage("Build"){
            steps{
                sh "docker build -t webapplication ."
            }
            
        }
        stage("Test"){
            steps{
                echo "Testing will happen here"
            }
            
        }
        stage("Push to Docker Hub"){
            steps{
                withCredentials([usernamePassword(
                    credentialsId:"DockerHub",passwordVariable:"pass",usernameVariable:"user")])
                {
                    sh "docker login -u ${env.user} -p ${env.pass}"
                    sh "docker image tag webapplication ${env.user}/webapplication"
                    sh "docker push ${env.user}/webapplication:latest"
                }  
            }
        }
        stage("Deploy"){
            steps{
                sh "docker run -p 5000:5000 webapplication:latest"
            }
        }
    }

/*post{
        success{
            script{
                emailext from: 'mentor@trainwithshubham.com',
                to: 'mentor@trainwithshubham.com',
                body: 'Build success for Demo CICD App',
                subject: 'Build success for Demo CICD App'
            }
        }
        failure{
            script{
                emailext from: 'mentor@trainwithshubham.com',
                to: 'mentor@trainwithshubham.com',
                body: 'Build Failed for Demo CICD App',
                subject: 'Build Failed for Demo CICD App'
            }
        }
    }*/
} 


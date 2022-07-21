pipeline 
{
    agent any

    stages 
    {
        stage('Build') 
        {
            steps 
            {
                echo 'Build'
            }
        }
        
        stage('Test') 
        {
            steps 
            {
                echo 'Test'
                bat 'python hello_develop.py'
            }
        }

        stage('Deploy') 
        {
            steps 
            {
                echo 'Deploy'
            }
        }
    }
}

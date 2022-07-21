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
                python hello_develop.py
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

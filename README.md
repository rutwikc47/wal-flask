# Python/Flask Walmart Assignment
### Step 1:- Build the docker image by running the command
* docker image build -t walmart-flask .
### Step 2:- Run the dockerized flask app by executing the command
* docker run -d walmart-flask
### Step 3:- Access the container id by using the command
* docker container ls
### Step 4:- Execute the curl get command to see the health results of the application
* docker exec -it #container-id# curl http://localhost:8080/healthz where #container-id# is the id which can be accessed by running step 3

#### The Extra Endpoint I added is execution_time which can be used to figure out if the server is loaded or not or if there is some internal issue causing longer execution times, using which the load balancer can route the requests to other server 

## CI/CD Pipeline
* The CI pipeline results can be seen in the Actions tab in the repository and the yaml script for the workflow can also be accessed from the .github folder
* I have set up a CI pipeline using Github Actions where the tests are triggered on each push/pull request on the master branch
* On each PR created by the developer the pytests are run to check whether the flask app is running correctly (future check: execution time under certain limit)
* Since its a flask based application I believe Github Actions can be a good light weight candidate
* I believe the Build, Test, Deploy phases should be added onto the pipeline
    * During each build stage the flask app would be compiled and the docker image would be built
    * In the test stage the flask app unit testing would determine if any new changes are breaking the app or increasing the execution time
    * Deploy stage would push the current build into production like a docker repo in this case if everything is working correctly

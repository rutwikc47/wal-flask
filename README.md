# Hello Python/Flask Walmart Assignment
### Step 1:- Build the docker file by running the command
* docker image build -t walmart-flask .
### Step 2:- Run the dockerized flask app by executing the command
* docker run -d walmart-flask
### Step 3:- Access the container id by using the command
* docker container ls
### Step 4:- Execute the curl get command to see the health results of the application
* docker exec -it <container-id> curl http://localhost:8080/healthz where <container-id> is the id which can be accessed by running step 3

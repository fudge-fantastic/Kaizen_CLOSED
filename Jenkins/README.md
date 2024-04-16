# Jenkins

---

### Steps
Source Code in Git ---> Perform Model Training ---> Testing ---> Deployment on Docker Container ---> Trigger Notification   <br>

### Pre-requisites for Jenkins
1. Prepare and Package ML Models
2. Create FastAPI app
3. Dockerization of the ML App
4. Test Locally

### Steps
1. Create or Copy paste the package you made into the new_folder (let's call it Jenkins)
2. In Jenkins, create a new folder called 'src', and init paste the whole package folder.
3. Install the requirements.txt file and install the package we made too: pip install src/. 
(Made some serious changes in the packages, try configuring the setup file by adding your choice of files)
4. Create a main.py file, and execute it using command: python main.py.

```json
{
  "Gender": "Male",
  "Married": "No",
  "Dependents": "2",
  "Education": "Graduate",
  "Self_Employed": "No",
  "ApplicantIncome": 5849,
  "CoapplicantIncome": 0,
  "LoanAmount": 1000,
  "Loan_Amount_Term": 1,
  "Credit_History": "1.0",
  "Property_Area": "Rural"
}
``` 

(status : didn't worked)
5. Let's do some Docker Deployement
  - Build a Docker Image: docker build -t image19 .
  - Run the Container (with Port Mapping): docker run -d -it --name container19 -p 5000:3000 image19:v1 bash; Verify using: docker ps
  - docker exec -it container19 bash; pip install uvicorn; pytest -v --junitxml testresults_2.xml --cache-clear
  - Get Test Results: docker cp container19:/code/src/testresults_2.xml .
  - Run the App: docker exec -d container19 uvicorn /code/main:app --proxy-headers --host localhost --port 8005 

(status : didn't worked)
5. Now follow the Dockerfile given in the folder. Next, build the docker file using command (this one is from udemy): 
  - Create a new one: docker buildx build --tag bluesalt321/cicd:version_1 . (will create a Docker Image)
  - And push the Container: docker push bluesalt321/cicd:version_1
  - Now to run it in the Container Instance, we'll use: docker run -d -it --name testing_loan_model -p 8005:8005 bluesalt321/cicd:version_1 bash
  - Next, run the command to test the Docker Locally: docker exec testing_loan_model python MLPackages/training_pipeline.py
  - After the success, use this command for:  docker exec testing_loan_model pytest -v --junitxml testresults.xml --cache-clear
    - -v: This flag mounts a volume from the host machine into the container.
    - JUnit XML is a framework that generates XML files for test execution. It's a common XML format for generating test results, and most CI systems support it so that more advanced reports can be displayed
  - To get the results of the in the XML file, we can use: docker cp testing_loan_model:/code/src/testresults.xml .
  - It has created and deployed the application on the Docker Container, run the command: docker exec -d -w /code testing_loan_model python main.py (doesn't work)
  - docker exec -d testing_loan_model python /code/main.py (worked) 

(status : didn't worked)
5. Create Docker File, Docker-Compose.yaml file, and make sure to configure main.py file
  - Build the Docker image using: docker-compose build
  - Run the Docker image using: docker-compose up

(status : worked, how?)
5. Explaination: Make sure we're using = uvicorn.run(app, host="0.0.0.0", port=8000) in the application; and the port is exposed at 8000 (or any other port) in the docker file. Next make sure to follow these steps mentioned below:
  - Create a Docker file; docker buid -t imagename . (will create a Docker Image, make sure to add that '.' at the end)
  - docker run -p (host_port):(docker_port) imagename
  - docker run -p 8000:8000 imagename

6. Launch a Instance using Ubuntu as the AMI (try using the t2.medium, if using) 
  - Connect the instance using SSH client, following are the steps:
  - Download the key-pair, open the folder where you have the key-pair
  - via cmd, use the command: chmod 400 "yourkeypairname.pem"
  - then use this command: ssh -i "yourkeypairname.pem" ubuntu@ec2-13-233-200-240.ap-south-1.compute.amazonaws.com; enter yes, and proceed.
  - We're now sucessfully running our AWS Ubuntu server on our terminal
  - Copy paste the Long Term Support code into the terminal, and after the first installation, copy-paste the Java Installation's first three lines and run the command (https://www.jenkins.io/doc/book/installing/linux/) (Java is mandatory to run the jenkins)
  - Run these three command below at the same time.

```
sudo systemctl enable jenkins
sudo systemctl start jenkins
sudo systemctl status jenkins
```
  - it should look something like: Active: active (running) since Tue 2024-04-16 09:07:04 UTC; 37ms ago; What it does is, it validates whether the jenkins is active.
  - Now head to the running (current) instance and goto Security Tab ---> Select any Security Groups ---> And add a inbound rule (Types should be All TCP, Source should be Anywhere-IPv4 and Anywhere-IPv6) 
  - In Networking tab, copy paste the Public IPv4 address and paste it in the browser, it should look like: http://13.232.62.129:8080/
  - Next, (https://docs.docker.com/engine/install/ubuntu/) install the docker in ubuntu (can be found in 'Install using the apt repository' in the given link) copy-paste into the running terminal of Ubuntu AWS, follow all 3 steps (till verifying)
  - While trying to run the command: docker ps; We get a permission denied, because, we need to run it as a super-user.
  - Meaning, use the command: sudo docker ps; Now, we're able to run the docker ps command.
  - You can prevent this by granting the user persmissons, so that we won't have to use sudo everytime.
  - sudo usermod -a -G docker jenkins; sudo usermod -a -G docker $USER: this will provide access to the jenkins and current user. Make sure to restart/reboot the instance by clicking 'Reboot Instance' in the instances. Reconnect the instance by copy-pasting the (ssh -i "youkeypair.pem" ubuntu@ec2-13-232-62-129.ap-south-1.compute.amazonaws.com)
  - This time, while using the command: docker ps; you won't have to use the sudo command.

7. Now, create a different repository for the one where you were testing your docker deployment application
  - Copy-paste the entire folder from Jenkins to the new-repository.
  - Complete the setup, git push everything into the repository.
  - Next step involves, generating personal access tokens and storing it in the Jenkins; This token can be found in the Github Settings ---> Developer Settings ---> Personal Access Token ---> Tokens (classics) ---> Generate new token (classic) ---> Fill out each check boxes and generate the token 
  - To log in, use the username: "admin" and the administrator password you used to access the setup wizard.
  - To access the Jenkins, use this command in the Ubuntu server: sudo cat /var/lib/jenkins/secrets/initialAdminPassword
  - Select plugins of our choice ---> checkbox Junit, Github, and Email Extension Plugin.
  - After getting inside the Jenkins, goto credentials and click ---> global ---> add credentials ---> add you secret token (git-token)
  into the secret text. 
  - Now, we have to setup the webhooks ---> goto the project repo; settings; webhooks; In Payload URL, we have to copy paste the ServerID on which the Jenkins is running (for instance, Jenkins is running on AWS Ubuntu server: http://3.108.221.179:8080/) (and we setup it as: http://3.108.221.179:8080/github-webhook/)  and set it as application/json, then create the webhook.
  - Since, in Jenkins, we're using Github plugin, we want to setup the plugin for it to work; goto Manage Jenkins ---> Look for Github; Give any name, select credentials, Checkbox Manage Hooks, and test the connection. 

8. Create a new project in Jenkins, and select the project type as 

#### Error logs:
- pywin32 incompatibility (status:fixed, how? removed it, lol)
- pytest failed the test in the tests/test_prediction.py


### Notes
##### 1. What is CORSMiddleware
CORS is a web security mechanism that restricts how a web page from one domain can request resources from a different domain. It's important to manage CORS appropriately to prevent unauthorized access to your API from untrusted origins. <br>
Middleware in FastAPI: <br>
Middleware is a layer of software that sits between the web server and your application code. It can perform various tasks like request processing, logging, and handling CORS.
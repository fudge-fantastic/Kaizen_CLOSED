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

5. Let's do some Docker Deployement
  - Build a Docker Image: docker build -t image19 .
  - Run the Container (with Port Mapping): docker run -d -it --name container19 -p 5000:3000 image19:v1 bash; Verify using: docker ps
  - docker exec -it container19 bash; pip install uvicorn; pytest -v --junitxml testresults_2.xml --cache-clear
  - Get Test Results: docker cp container19:/code/src/testresults_2.xml .
  - Run the App: docker exec -d container19 uvicorn /code/main:app --proxy-headers --host localhost --port 8005 

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

5. Create Docker File, Docker-Compose.yaml file, and make sure to configure main.py file
  - Build the Docker image using: docker-compose build
  - Run the Docker image using: docker-compose up

5. Create a Docker file; docker buid -t imagename .(will create a Docker Image)
  - docker run -p 8000:8000 imagename


#### Error logs:
- pywin32 incompatibility (status:fixed, how? removed it, lol)
- pytest failed the test in the tests/test_prediction.py

### Notes
##### 1. What is CORSMiddleware
CORS is a web security mechanism that restricts how a web page from one domain can request resources from a different domain. It's important to manage CORS appropriately to prevent unauthorized access to your API from untrusted origins. <br>
Middleware in FastAPI: <br>
Middleware is a layer of software that sits between the web server and your application code. It can perform various tasks like request processing, logging, and handling CORS.
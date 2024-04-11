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
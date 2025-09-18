

# 🚀 MLOps Project – Fintech Data Pipeline

> **An end-to-end MLOps pipeline** Welcome to this MLOps project, designed to demonstrate a robust pipeline for managing fintech payment data. This project aims to showcasing the various tools, techniques, services, and features that go into building and deploying a machine learning pipeline for real-world data management. Follow along to learn about project setup, data processing, model deployment, and CI/CD automation! 

---

## ✨ Features

* 📦 **Project Template Automation** with `template.py`
* ⚙️ **Local Package Management** via `setup.py` & `pyproject.toml`
* 🐍 **Isolated Environments** using `venv`
* 🍃 **Data Storage** on **MongoDB Atlas** (cloud hosted NoSQL DB)
* 📑 **Structured Logging & Exception Handling**
* 📊 **EDA & Feature Engineering** notebooks
* 🔄 **Data Ingestion → Validation → Transformation → Training** workflow
* ☁️ **AWS Integration**: S3 for model registry, ECR for images, EC2 for hosting
* 🐳 **Containerization** with Docker
* 🔐 **GitHub Secrets** for AWS credentials
* 🤖 **CI/CD with GitHub Actions** + **self-hosted runners on EC2**
* 🌐 **Deployed Web App** (Flask/FastAPI) running on **port 5000**

---

## 🛠️ Tech Stack

| Layer                | Tools & Services                                               |
| -------------------- | -------------------------------------------------------------- |
| **Programming**      | Python 3.13                                                    |
| **Version Control**  | Git, GitHub                                                    |
| **Environment Mgmt** | venv                                                           |
| **Database**         | MongoDB Atlas                                                  |
| **Orchestration**    | Modular ML pipeline (constants, config, components, artifacts) |
| **Cloud**            | AWS S3, EC2, IAM, ECR                                          |
| **Containerization** | Docker                                                         |
| **CI/CD**            | GitHub Actions, self-hosted runners                            |
| **Deployment**       | Flask/FastAPI app on EC2                                       |

---

## ⚡ Project Setup and Structure

### 1️⃣ Setup Project Template

Step 1: Start by executing the template.py file to create the initial project template, which includes the required folder structure and placeholder files.

### Package Management

Step 2:
Write the setup for importing local packages in setup.py and pyproject.toml files.
Tip: Learn more about these files from crashcourse.txt.

---

### 2️⃣ Create Virtual Environment

Create a virtual environment and install required dependencies from requirements.txt

```bash
# Get Python path
python -c "import sys; print(sys.executable)"

# Create & activate venv
python -m venv insurance
.\insurance\Scripts\Activate

# Install requirements
pip install -r requirements.txt
```
Verify the local packages by running:

```bash
pip list
```

---

### 3️⃣ Setup MongoDB Atlas

Step 3: MongoDB Atlas Configuration
Sign up for MongoDB Atlas and create a new project.
Set up a free M0 cluster, configure the username and password, and allow access from any IP address (0.0.0.0/0).
Retrieve the MongoDB connection string for Python and save it (replace <password> with your password).
Step 4: Pushing Data to MongoDB
Create a folder named notebook, add the dataset, and create a notebook file mongoDB_demo.ipynb.
Use the notebook to push data to the MongoDB database.
Verify the data in MongoDB Atlas under Database > Browse Collections.

* Create **M0 cluster**, set DB user + password
* Add IP: `0.0.0.0/0`
* Get **connection string** (Python driver, v3.6+)
* Save as environment variable `MONGODB_URL`

---

📝 Logging, Exception Handling, and EDA

Step 5: Set Up Logging and Exception Handling
Create logging and exception handling modules. Test them on a demo file demo.py.
Step 6: Exploratory Data Analysis (EDA) and Feature Engineering
Analyze and engineer features in the EDA and Feature Engg notebook for further processing in the pipeline.

---

### 4️⃣ Run Notebooks

* `notebook/mongoDB_demo.ipynb` → push sample data to MongoDB
* `EDA & Feature Engineering` notebooks

---

### 5️⃣ Data Pipeline Components

Step 7: Data Ingestion Pipeline
Define MongoDB connection functions in configuration.mongo_db_connections.py.
Develop data ingestion components in the data_access and components.data_ingestion.py files to fetch and transform data.
Update entity/config_entity.py and entity/artifact_entity.py with relevant ingestion configurations.
Run demo.py after setting up MongoDB connection as an environment variable.

Setting Environment Variables
Set MongoDB URL:
For Bash-
export MONGODB_URL="mongodb+srv://<username>:<password>...."
For Powershell-
$env:MONGODB_URL = "mongodb+srv://<username>:<password>...."

Note: On Windows, you can also set environment variables through the system settings.

---

🔍 Data Validation, Transformation & Model Training

Step 8: Data Validation
Define schema in config.schema.yaml and implement data validation functions in utils.main_utils.py.
Step 9: Data Transformation
Implement data transformation logic in components.data_transformation.py and create estimator.py in the entity folder.
Step 10: Model Training
Define and implement model training steps in components.model_trainer.py using code from estimator.py.

---

### 🌐 AWS Setup for Model Evaluation & Deployment

Step 11: AWS Setup
1. Log in to the AWS console, create an IAM user, and grant AdministratorAccess.

Set AWS credentials as environment variables.

  ```bash
  export AWS_ACCESS_KEY_ID=xxx
  export AWS_SECRET_ACCESS_KEY=yyy
  ```

2. Configure S3 Bucket and add access keys in constants.__init__.py.

Step 12: Model Evaluation and Pushing to S3
1. Create an S3 bucket named my-model-mlopsproj in the us-east-1 region.
2. Develop code to push/pull models to/from the S3 bucket in src.aws_storage and entity/s3_estimator.py.

---

🚀 Model Evaluation, Model Pusher, and Prediction Pipeline

Step 13: Model Evaluation & Model Pusher
1. Implement model evaluation and deployment components.
2. Create Prediction Pipeline and set up app.py for API integration.
Step 14: Static and Template Directory
Add static and template directories for web UI.

---

### 🔄 Deployment: CI/CD Setup with Docker, GitHub Actions, and AWS

Step 15: Docker and GitHub Actions
1. Create Dockerfile and .dockerignore.
2. Set up GitHub Actions with AWS authentication by creating secrets in GitHub for:
AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
AWS_DEFAULT_REGION
ECR_REPO
Step 16: AWS EC2 and ECR
1. Set up an EC2 instance for deployment.
2. Install Docker on the EC2 machine.
3. Connect EC2 as a self-hosted runner on GitHub.
Step 17: Final Steps
1. Open the 5000 port on the EC2 instance.
2. Access the deployed app by visiting http://<public_ip>:5000.

---

## 📈 Highlights

✅ **Demonstrates full MLOps lifecycle** – data → ML → deployment
✅ **Cloud-native** with AWS (IAM, S3, ECR, EC2)
✅ **Production-ready CI/CD** with GitHub Actions & Docker
✅ **Secure credentials** via GitHub Secrets
✅ **Scalable architecture** with modular pipeline design
✅ **Hands-on with both ML & DevOps** aspects

---

## 🎯 Project Workflow Summary

- 📥 **Data Ingestion** ➔ 🔍 **Data Validation** ➔ 🔄 **Data Transformation**  
- 🤖 **Model Training** ➔ 📊 **Model Evaluation** ➔ 📦 **Model Deployment**  
- ⚙️ **CI/CD Automation** with **GitHub Actions**, **Docker**, **AWS ECR**, and **EC2**

---

## 💬 Connect
If you found this project helpful or have any questions, feel free to reach out!

📱 Phone: (+91) 7008-62-6663
📧 Email: sandeepdashmlops@gmail.com
💻 GitHub: https://github.com/sandeepdash-mlops
---

This README provides a structured walkthrough of the MLOps FinTech Domain project, showcasing the end-to-end pipeline, cloud integration, CI/CD setup, and robust data handling capabilities.

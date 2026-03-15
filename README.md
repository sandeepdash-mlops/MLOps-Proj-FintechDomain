<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d1117,50:1a2a1a,100:0ea5e9&height=220&section=header&text=FinTech-MLOps&fontSize=80&fontColor=ffffff&fontAlignY=38&desc=Binary%20Classification%20Pipeline%20for%20BaaS%20Payment%20Prediction&descAlignY=64&descSize=20&descColor=7dd3fc" alt="FinTech MLOps Banner"/>

[![Python](https://img.shields.io/badge/Python-3.13-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![MongoDB](https://img.shields.io/badge/MongoDB_Atlas-Database-47A248?style=for-the-badge&logo=mongodb&logoColor=white)](https://mongodb.com/atlas)
[![Docker](https://img.shields.io/badge/Docker-Containerization-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://docker.com/)
[![AWS S3](https://img.shields.io/badge/AWS_S3-Model_Registry-FF9900?style=for-the-badge&logo=amazons3&logoColor=white)](https://aws.amazon.com/s3/)
[![AWS ECR](https://img.shields.io/badge/AWS_ECR-Image_Registry-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white)](https://aws.amazon.com/ecr/)
[![AWS EC2](https://img.shields.io/badge/AWS_EC2-Deployment-FF9900?style=for-the-badge&logo=amazonec2&logoColor=white)](https://aws.amazon.com/ec2/)
[![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-CI%2FCD-2088FF?style=for-the-badge&logo=githubactions&logoColor=white)](https://github.com/features/actions)
[![Status](https://img.shields.io/badge/Status-Production_Ready-16a34a?style=for-the-badge)]()

<br/>

> **End-to-end MLOps pipeline for a fintech binary classification model — predicting customer payment service adoption for banks and NBFCs via iServeU's BaaS platform — with MongoDB Atlas, AWS cloud integration, Docker containerization, and GitHub Actions CI/CD on self-hosted EC2 runners.**

</div>

---

## 📌 What This Project Solves

Banks and NBFCs onboarded to **iServeU's Banking-as-a-Service (BaaS) platform** need to know which customers are likely to adopt payment services — UPI, IMPS, QR, POS, or Cards — to drive targeted activation campaigns.

This project delivers a **production-ready binary classification model** wrapped in a REST API, deployed on AWS, with a fully automated CI/CD pipeline from code push to live inference.

---

## 🏗️ Architecture Overview

```
  ┌──────────────────────────────────────────────────────────────────────┐
  │                         Data Layer                                   │
  │   Raw Data → MongoDB Atlas (Cloud NoSQL) → Data Ingestion Pipeline   │
  └──────────────────────────────┬───────────────────────────────────────┘
                                 │
  ┌──────────────────────────────▼───────────────────────────────────────┐
  │                        ML Pipeline                                   │
  │  Ingestion → Validation → Transformation → Training → Evaluation     │
  └──────────────────────────────┬───────────────────────────────────────┘
                                 │
                    ┌────────────▼────────────┐
                    │      AWS S3 Bucket       │
                    │   Model Registry / Store │
                    └────────────┬────────────┘
                                 │
  ┌──────────────────────────────▼───────────────────────────────────────┐
  │                     CI/CD — GitHub Actions                           │
  │        Push → Test → Docker Build → Push to ECR → Deploy to EC2     │
  └──────────────────────────────┬───────────────────────────────────────┘
                                 │
              ┌──────────────────▼──────────────────┐
              │           AWS ECR                    │
              │       Docker Image Registry          │
              └──────────────────┬──────────────────┘
                                 │
              ┌──────────────────▼──────────────────┐
              │     AWS EC2 (Self-Hosted Runner)     │
              │   Flask/FastAPI App on port 5000     │
              │   http://<public_ip>:5000            │
              └─────────────────────────────────────┘
```

---

## ✨ Key Features

| Feature | Detail |
|---|---|
| 🏦 **Fintech Domain** | Payment service adoption prediction for BaaS — UPI, IMPS, QR, POS, Cards |
| 🍃 **Cloud NoSQL Storage** | MongoDB Atlas M0 cluster for raw data ingestion and access |
| 🔄 **Modular ML Pipeline** | 4-stage pipeline: Ingestion → Validation → Transformation → Training |
| ☁️ **AWS Native** | S3 model registry, ECR image store, EC2 deployment, IAM access control |
| 🐳 **Containerized** | Dockerized Flask/FastAPI app with `.dockerignore` and ECR push |
| 🔐 **Secrets Management** | AWS credentials via GitHub Secrets — never hardcoded |
| 🤖 **Self-Hosted CI/CD** | GitHub Actions runner on EC2 — build and deploy on your own infra |
| 📝 **Production Code Quality** | Structured logging, exception handling, config & artifact entities |

---

## 📁 Repository Structure

```
fintech-mlops/
├── template.py                          # 🏗️ Project scaffold generator
├── setup.py / pyproject.toml           # 📦 Local package management
├── requirements.txt                     # 📋 Dependencies
├── app.py                               # 🌐 Flask/FastAPI inference API
├── demo.py                              # 🧪 Pipeline test runner
├── Dockerfile / .dockerignore           # 🐳 Container definition
├── .github/workflows/                   # 🔄 GitHub Actions CI/CD
├── notebook/
│   ├── mongoDB_demo.ipynb               # 🍃 Push data to MongoDB Atlas
│   └── EDA_Feature_Engineering.ipynb   # 📊 Exploratory analysis
├── src/
│   ├── configuration/
│   │   └── mongo_db_connections.py      # 🔗 MongoDB connection handler
│   ├── data_access/                     # 📥 MongoDB data fetch layer
│   ├── components/
│   │   ├── data_ingestion.py            # 📥 Ingest from MongoDB
│   │   ├── data_validation.py           # 🔍 Schema & quality checks
│   │   ├── data_transformation.py       # 🔄 Feature transformation
│   │   └── model_trainer.py             # 🏋️ Model training
│   ├── entity/
│   │   ├── config_entity.py             # ⚙️  Pipeline config definitions
│   │   ├── artifact_entity.py           # 📦 Artifact path definitions
│   │   ├── estimator.py                 # 🤖 Model wrapper
│   │   └── s3_estimator.py              # ☁️  S3 model push/pull
│   ├── aws_storage/                     # ☁️  S3 integration layer
│   ├── utils/main_utils.py              # 🔧 Shared utilities
│   ├── logger/                          # 📝 Structured logging
│   └── constants/__init__.py            # 🔑 S3 bucket & region constants
├── config/schema.yaml                   # 📐 Data schema definition
└── static/ & templates/                 # 🖥️ Web UI assets
```

---

## ⚡ Quick Setup

### 1️⃣ Environment

```bash
# Create and activate virtual environment
python -m venv venv
source venv/bin/activate          # Linux/Mac
.\venv\Scripts\Activate           # Windows

pip install -r requirements.txt
pip list                          # verify local packages installed
```

### 2️⃣ MongoDB Atlas

```bash
# Set connection string as environment variable
export MONGODB_URL="mongodb+srv://<username>:<password>@cluster.mongodb.net/"

# Push sample data to Atlas
jupyter notebook notebook/mongoDB_demo.ipynb
```

> Create a free **M0 cluster** on [MongoDB Atlas](https://cloud.mongodb.com), set DB user credentials, and allow `0.0.0.0/0` for IP access.

### 3️⃣ AWS Credentials

```bash
export AWS_ACCESS_KEY_ID=<your-key>
export AWS_SECRET_ACCESS_KEY=<your-secret>
export AWS_DEFAULT_REGION=us-east-1
```

> Create an IAM user with `AdministratorAccess`, then create an S3 bucket `my-model-mlopsproj` in `us-east-1`.

### 4️⃣ Run ML Pipeline

```bash
python demo.py        # runs full ingestion → training pipeline
```

### 5️⃣ Docker Build & Run Locally

```bash
docker build -t fintech-app:latest .
docker run -p 5000:5000 fintech-app:latest
# Visit http://localhost:5000
```

### 6️⃣ Deploy to AWS EC2 via CI/CD

Add the following secrets to your GitHub repository:

| Secret | Value |
|---|---|
| `AWS_ACCESS_KEY_ID` | IAM user access key |
| `AWS_SECRET_ACCESS_KEY` | IAM user secret key |
| `AWS_DEFAULT_REGION` | `us-east-1` |
| `ECR_REPO` | Your ECR repository URI |

Every push to `main` triggers:
```
Test → Docker Build → Push to ECR → Pull & Run on EC2 (self-hosted runner)
```

Access the live app at `http://<EC2-public-ip>:5000`

---

## 🔄 ML Pipeline Stages

```
📥 Data Ingestion
   └── Fetch from MongoDB Atlas → save raw artifact

🔍 Data Validation
   └── Schema check (config/schema.yaml) → drift detection → validation report

🔄 Data Transformation
   └── Feature engineering → preprocessing pipeline → transformed artifact

🏋️ Model Training
   └── Scikit-Learn estimator → train/test split → model artifact

📊 Model Evaluation
   └── Compare vs production model in S3 → accept/reject decision

📦 Model Pusher
   └── Push accepted model to S3 bucket → ready for inference
```

---

## 📐 Design Decisions

**Why MongoDB Atlas over a relational DB?**
Fintech transaction and customer data is often semi-structured and schema-flexible. MongoDB Atlas handles this natively and provides cloud-hosted access without infra overhead.

**Why self-hosted EC2 runner over GitHub-hosted?**
Self-hosted runners allow the CI/CD pipeline to deploy directly onto the same EC2 instance that serves the app — no external SSH or deploy keys needed, and it keeps AWS egress costs zero.

**Why S3 as model registry over MLflow?**
For this deployment pattern (single model, EC2 inference), S3 gives a lightweight, always-available model store. The `s3_estimator.py` abstraction makes push/pull clean without a full tracking server dependency.

---

## 💬 Connect

<div align="center">

📧 **Email:** sandeepdashmlops@gmail.com
&nbsp;&nbsp;|&nbsp;&nbsp;
💻 **GitHub:** [github.com/sandeepdash-mlops](https://github.com/sandeepdash-mlops)

</div>

---

<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0ea5e9,50:1a2a3a,100:0d1117&height=120&section=footer" alt="footer"/>

*From raw data to live prediction — fully automated.*

</div>

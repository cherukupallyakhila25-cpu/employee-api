#  Employee API (Flask + PostgreSQL + Docker + Jenkins)

##  Project Overview

This is a simple **Employee Management REST API** built using **Flask** and **PostgreSQL**, fully containerized using **Docker** and automated with **Jenkins CI/CD pipeline**.

It supports basic CRUD operations for employee data and demonstrates a complete DevOps workflow from GitHub → Jenkins → Docker → Deployment.

---

##  Technologies Used

* Python 3
* Flask (REST API)
* PostgreSQL (Database)
* Docker & Docker Compose
* Jenkins (CI/CD Pipeline)
* GitHub (Version Control)
* Postman (API Testing)

---

##  Project Structure

```text
employee-api/
│
├── app.py               # Flask application
├── requirements.txt     # Python dependencies
├── Dockerfile           # Docker image build file
├── docker-compose.yml   # Multi-container setup
├── Jenkinsfile          # CI/CD pipeline
├── README.md            # Project documentation
```

---

##  Features

* Add Employee
* Get All Employees
* Update Employee
* Delete Employee
* Store data in PostgreSQL database
* Fully containerized application
* Automated CI/CD pipeline using Jenkins

---

## How to Run Locally

### 1️ Clone Repository

```bash
git clone https://github.com/<your-username>/employee-api.git
cd employee-api
```

---

### 2️ Build and Run with Docker

```bash
docker-compose up --build
```

---

### 3️ Access Application

* API Base URL:

```
http://localhost:5000
```

---

##  API Endpoints

### Home

```http
GET /
```

---

### Add Employee

```http
POST /employees
```

**Request Body:**

```json
{
  "name": "John",
  "role": "Developer",
  "salary": 70000
}
```

---

### Get All Employees

```http
GET /employees
```

---

### Update Employee

```http
PUT /employees/{id}
```

---

### Delete Employee

```http
DELETE /employees/{id}
```

---

## PostgreSQL Setup

The database is automatically created using Docker Compose.

Database details:

* Database: `employee_db`
* Username: `postgres`
* Password: `postgres`
* Host: `db`

---

## Docker Setup

Two containers run together:

* Flask API container
* PostgreSQL database container

```bash
docker-compose up --build
```

---

## Jenkins CI/CD Pipeline

The Jenkins pipeline performs:

1. Clone code from GitHub
2. Build Docker image
3. Start containers using Docker Compose

---

### Jenkinsfile Flow

```groovy
pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                git 'https://github.com/<your-username>/employee-api.git'
            }
        }

        stage('Build') {
            steps {
                sh 'docker build -t employee-api .'
            }
        }

        stage('Deploy') {
            steps {
                sh 'docker-compose up -d'
            }
        }
    }
}
```

---

## Testing API

Use **Postman** or curl.

Example:

```bash
curl -X GET http://localhost:5000/employees
```

---

## Future Enhancements

* JWT Authentication
* Swagger API Documentation
* Kubernetes Deployment
* AWS Deployment (EC2 / EKS)
* Unit Testing (PyTest)
* Logging & Monitoring

---









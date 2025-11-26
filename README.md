#  To-Do List CLI – CI/CD Pipeline (Jenkins + Docker)

This project implements a simple **To-Do List Command Line Application** in Python and integrates it with a full **CI/CD pipeline** using Jenkins, GitHub, Docker, and Docker Hub.

The pipeline ensures that every change is automatically tested and containerized before deployment.

This Repo includes Screenshots of Output Logs and Pipline Overview

---

##  Features

### Application Features
* **Add Tasks:** Create new to-do items easily.
* **List Tasks:** View all current tasks with their status (Pending/Done).
* **Update Status:** Mark tasks as completed.
* **Delete Tasks:** Remove unwanted items from the list.

### DevOps Features
* **Automated Testing:** Runs Pytest automatically on every commit.
* **Dockerized Application:** The app is packaged into a lightweight container.
* **CI/CD Integration:** Jenkins handles the workflow from code checkout to registry push.
* **Docker Hub Push:** Automatically uploads successful builds to the public registry.

---

## 📁 Project Structure

```text
SE_CICD/
├── app.py             # Main application executable
├── test_app.py        # Unit test suite
├── Dockerfile         # Container definition
├── Jenkinsfile        # CI/CD Pipeline configuration
├── requirements.txt   # Dependencies list
└── README.md          # Project documentation

```
Docker HUB URL : [Docker Repo Link](https://hub.docker.com/r/krishnachaitanya1605/imt2023039)


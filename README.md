# 🐳 Cloud Deployment Lab: Python App + MySQL + GitHub Actions + AWS ECR

This project demonstrates how to containerize a Python web application, connect it with a MySQL database, and deploy it automatically to **AWS Elastic Container Registry (ECR)** using **GitHub Actions**.

---

## 🚀 Tech Stack

- **Python 3.9** – Web application (`app.py`)
- **Docker** – Containerize the app and DB
- **MySQL** – SQL database (schema in `mysql.sql`)
- **GitHub Actions** – CI/CD pipeline (`ecr-push.yml`)
- **AWS ECR** – Docker image repository
- **HTML/CSS** – Static frontend with Flask templating

---

## 📁 Project Structure

| File/Folder | Description |
|-------------|-------------|
| `Dockerfile` | Defines container build steps |
| `app.py` | Python web app logic |
| `mysql.sql` | SQL dump to set up initial DB |
| `templates/index.html` | Homepage HTML |
| `static/style.css` | Styling for the app |
| `.github/workflows/ecr-push.yml` | GitHub Actions workflow to build and push to AWS |
| `requirements.txt` | Python dependencies |

---

## ⚙️ Deployment Workflow

1. **Dockerfile** builds the app container  
2. **GitHub Actions** workflow runs on push to `main`:
   - Builds the Docker image
   - Logs in to AWS ECR
   - Pushes the image to ECR

3. ECR now holds the production-ready container

---

## 🛠 How to Run Locally

```bash
# Clone the project
git clone https://github.com/mrdaniel98/cloud-infra-deployment-lab.git
cd cloud-infra-deployment-lab

# Build the Docker image
docker build -t cloud-app .

# Run it
docker run -p 81:81 cloud-app

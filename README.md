# FastAPI Microservice

A lightweight, Dockerized FastAPI application featuring automated health checks, environment-based secret management, and a GitHub Actions CI/CD pipeline.

## 🚀 Features

* **FastAPI & Uvicorn**: High-performance asynchronous API server.
* **Docker Ready**: Pre-configured Dockerfile using a lightweight Python 3.14-slim base.
* **Secure Secrets**: Environment variable integration for safe credential management.
* **Automated Testing**: CI pipeline via GitHub Actions to build and test container endpoints on every push.

---

## 🛠️ Prerequisites

Before you begin, ensure you have the following installed:
* [Python 3.11+](https://www.python.org/downloads/) (if running locally)
* [Docker](https://docs.docker.com/get-docker/) 
* [Git](https://git-scm.com/)

---

## 💻 Local Development Setup

1. **Clone the repository:**
   ```bash
   git clone git@github.com:USERNAME/REPO.git
   cd REPO

```

2. **Create and activate a virtual environment:**
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate

```


3. **Install dependencies:**
```bash
pip install -r requirements.txt

```


4. **Set up environment variables:**
Copy the example environment file and add your actual secret.
```bash
cp .env.example .env

```


*Note: Ensure `.env` is listed in your `.gitignore` to prevent leaking secrets.*
5. **Run the development server:**
```bash
uvicorn main:app --reload --host 127.0.0.1 --port 8000

```



---

## 🐳 Docker Deployment

This project uses the ArvanCloud registry mirror for optimized builds.

1. **Build the Docker image:**
```bash
docker build -t fastapi-app .

```


2. **Run the container (passing secrets securely):**
```bash
docker run -d -p 8000:8000 --env-file .env --name my-fastapi fastapi-app

```


*Alternatively, pass a single secret inline:*
```bash
docker run -p 8000:8000 -e APP_SECRET="YourSecretHere" fastapi-app

```



---

## 📡 API Endpoints

Once the application is running (either locally or via Docker), you can access the following endpoints:

| Method | Endpoint | Description | Expected Response |
| --- | --- | --- | --- |
| `GET` | `/` | Root endpoint. Verifies if the `APP_SECRET` loaded successfully. | `{"msg": "Hello World!", "secret_loaded": true}` |
| `GET` | `/health` | Health check endpoint for monitoring uptime. | `{"status": "OK"}` |
| `GET` | `/docs` | Interactive Swagger UI API documentation (auto-generated). | *Web Interface* |

---

## ⚙️ CI/CD (GitHub Actions)

This repository includes a GitHub Actions workflow (`.github/workflows/build.yml`) that automatically triggers on pushes and pull requests to the `master` and `dev` branches.

**The pipeline performs the following:**

1. Checks out the code.
2. Builds the Docker image.
3. Injects the `APP_SECRET` from GitHub Secrets.
4. Spins up the container and runs `curl` tests against the `/` and `/health` endpoints to ensure successful deployment.

**Required Setup:**
You must add your `APP_SECRET` to the repository's **Settings > Secrets and variables > Actions** for the pipeline to pass.

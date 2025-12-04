# demo-cicd 
This repository demonstrates a complete CI/CD pipeline for a simple FastAPI application using GitHub Actions, Docker, GitHub Container Registry (GHCR), Minikube, and ArgoCD. The main goal is to showcase how to automate the build, test, and deployment process of a FastAPI application to a local Kubernetes cluster. After following the steps below, you will have a fully functional CI/CD pipeline that automatically builds and deploys your FastAPI application whenever changes are pushed to the GitHub repository. Make sure to replace placeholders like `<your-repo-url>` and `<your-github-username>` with your actual repository URL and GitHub username. 

Short description of the components used:
- **FastAPI**: A modern, fast (high-performance) web framework for building APIs with Python 3.7+ based on standard Python type hints.
- **Uvicorn**: A lightning-fast ASGI server implementation, using uvloop and httptools.
- **Docker**: A platform for developing, shipping, and running applications in containers.
- **GitHub Actions**: A CI/CD service that allows you to automate your build, test, and deployment pipeline directly from your GitHub repository.
- **GitHub Container Registry (GHCR)**: A service provided by GitHub to host and manage Docker container images.
- **Minikube**: A tool that makes it easy to run Kubernetes locally.
- **ArgoCD**: A declarative, GitOps continuous delivery tool for Kubernetes.



## ⭐ Step 1 — Setup Instructions for FastAPI Application

### 1. Create project folder and move to it
```bash
mkdir demo-cicd
cd demo-cicd
```

### 2. Create a virtual environment and activate it
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Update pip and install FastAPI and Uvicorn
```bash
pip install --upgrade pip
pip install fastapi uvicorn
pip freeze > requirements.txt
```

### 4. Create the main application file
Create `app.py` with your FastAPI application code (see app.py for details).

### 5. Run the FastAPI application
```bash
uvicorn app:app --reload
```

### 6. Access the application
Open your browser and navigate to `http://127.0.0.1:8000`

### Troubleshooting
- Ensure all dependencies are installed correctly
- Verify the virtual environment is activated
- Check that port 8000 is available (not blocked by firewalls or other applications)
- If port is blocked by another application, run Uvicorn on a different port:
```bash
uvicorn app:app --reload --port 8001
```
- Alternatively, you can find and terminate the process occupying the port:
```bash
lsof -i :8000
kill -9 <PID>
```
Replace `<PID>` with the process ID from the output above.

## ⭐ Step 2 — Create Dockerfile

### 1. Create a Dockerfile
Create a file named `Dockerfile` in the project root as given in the Dockerfile in this repository.

### 2. Build the Docker image and test it locally using port binding
```bash
docker build -t demo-cicd .
docker run -d -p 8000:8000 demo-cicd
```

### 3. Access the application running in Docker container
Open your browser and navigate to `http://localhost:8000`, or use curl:
```bash
curl http://localhost:8000
```
### Troubleshooting Docker
- Ensure Docker is installed and running on your machine
- Verify the Dockerfile is correctly set up
- Check for any errors during the build process and resolve them accordingly
- If the container fails to start, check the logs using:
```bash
docker logs <container_id>
```

## ⭐ Step 3 — Push the code to GitHub

### 1. Initialize a git repository
```bash
git init
```

### 2. Add the remote repository
```bash
git remote add origin <your-repo-url>
```

### 3. Stage and commit your changes
```bash
git add .
git commit -m "initial commit"
```

### 4. Push to GitHub
```bash
git push origin main
```

**Note:** Replace `<your-repo-url>` with your actual GitHub repository URL (e.g., `https://github.com/username/demo-cicd.git`)

## ⭐ Step 4 — Set up GitHub Actions for CI and push Docker image to GitHub Container Registry (GHCR)
### 1. Create GitHub Actions workflow file
Create a file at `.github/workflows/ci.yml` with the content provided in the `ci.yml` file in this repository

```bash
mkdir -p .github/workflows
nano .github/workflows/ci.yml
```

Then add the content from `ci.yml` file in this repository.

### 2. Commit and push the workflow file
```bash
git add .github/workflows/ci.yml
git commit -m "Add GitHub Actions workflow for CI"
git push origin main
```

### 3. Monitor the GitHub Actions workflow
your first CI pipeline is ready. Check in GitHub > Actions.

### 4. Verify Docker image in GitHub Container Registry
After a successful workflow run, navigate to the "Packages" section of your GitHub repository to see the pushed Docker image. 

### Troubleshooting GitHub Actions
- Ensure the workflow file is correctly placed in `.github/workflows/ci.yml`
- Verify the syntax of the YAML file is correct
- Check the GitHub Actions logs for any errors and resolve them accordingly
- Make sure you have permissions to push to the GitHub Container Registry (GHCR)
- Ensure that the GitHub Secrets (if any) are correctly configured in your repository settings

## ⭐ Step 5 — Setup Minikube cluster locally on your machine

### 1. Make sure you have minikube installed. If not, install it.
- For macOS using Homebrew:
```bash
brew install minikube
```
- For other OS, follow the instructions at: https://minikube.sigs.k8s.io/docs/start/
    
### 2. Start Minikube
```bash
minikube start \
  --driver=docker \
  --kubernetes-version=v1.30.0 \
  --container-runtime=containerd \
  --cpus=4 \
  --memory=6144
```
### 3. Verify Minikube is running
```bash
minikube status
```

## ⭐ Step 6 — Install ArgoCD on Minikube
### 1. Install ArgoCD using kubectl
```bash
kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
```
### 2. Access the ArgoCD server using port forwarding
```bash
kubectl port-forward svc/argocd-server -n argocd 8080:443
```
### 3. Login to ArgoCD UI
- Open your browser and navigate to `http://localhost:8080`
- The default username is `admin`
- To get the default password, run:
```bash
kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d; echo
```

## ⭐ Step 7 — Create Kubernetes YAML for deployment
### 1. Create a k8s folder and add `deployment.yaml` and `service.yaml` file
```bash
mkdir k8s
```
Add a file deployment `k8s/deployment.yaml` with the content provided in the `deployment.yaml` file in this repository and update the image section as below:

```yaml
image: ghcr.io/neerajmythink/demo-cicd:latest
```
replace `neerajmythink` with your GitHub username.

Also add a file service `k8s/service.yaml` with the content provided in the `service.yaml` file in this repository.

### 2. Commit and push the deployment file
```bash
git add k8s/deployment.yaml k8s/service.yaml
git commit -m "Add Kubernetes deployment and service manifests"
git push origin main
```

## ⭐ Step 8 — Configure ArgoCD Application to deploy the FastAPI app
### 1. Create a new application in ArgoCD
- In the ArgoCD UI, click on "New App"
- Fill in the application details:
  - Application Name: demo-cicd
  - Project: default
  - Sync Policy: Automatic
  - Repository URL: `<your-repo-url>`
  - Revision: HEAD
  - Path: k8s

# demo-cicd

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





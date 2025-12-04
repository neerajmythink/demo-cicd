# demo-cicd

## Setup Instructions

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

## Troubleshooting
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



from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello from CI/CD Pipeline!"}

@app.get("/info")
def info():
    return {"message": "This is a sample FastAPI application for demonstrating CI/CD pipeline."}

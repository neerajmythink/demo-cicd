from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello from CI/CD Pipeline! to demonstrate continuous integration and deployment."}
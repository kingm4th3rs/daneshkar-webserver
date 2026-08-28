import os
from fastapi import FastAPI, status

app = FastAPI()

APP_SECRET = os.getenv("APP_SECRET")

@app.get("/", status_code=status.HTTP_200_OK)
def read_root():
    return {
        "msg": "Hello World!",
        "secret_loaded": APP_SECRET is not None 
    }

@app.get("/health", status_code=status.HTTP_200_OK)
def health_check():
    return {"status": "OK"}

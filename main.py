from fastapi import FastAPI, status

app = FastAPI()


@app.get("/", status_code=status.HTTP_200_OK)
def read_root():
    return {"msg": "Hello World!"}

@app.get("/health", status_code=status.HTTP_200_OK)
def health_check():
    return {"status": "OK"}

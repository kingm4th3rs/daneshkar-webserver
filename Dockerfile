FROM docker.arvancloud.ir/python:3.14-slim

WORKDIR /app

COPY requrements.txt ./

RUN pip install -r requirements.txt

COPY main.py ./

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

from fastapi import FastAPI
from redis import Redis
import os
import time

app = FastAPI()
redis = Redis(host='redis', port=6379, decode_responses=True)

# Счетчик запросов
@app.get("/")
def root():
    count = redis.incr("request_count")
    return {"message": "Hello Godka!", "requests": count, "server": os.getenv("HOSTNAME", "unknown")}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/metrics")
def metrics():
    return {"requests": redis.get("request_count") or 0}
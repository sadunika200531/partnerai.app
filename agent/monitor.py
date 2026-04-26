import psutil
import requests
import time
import os

API_URL = os.getenv("SERVER_URL", "http://localhost:8000/api/v1/metrics")
API_KEY = os.getenv("SERVER_API_KEY")

def collect_metrics():
    return {
        "cpu_usage": psutil.cpu_percent(),
        "ram_usage": psutil.virtual_memory().percent
    }

while True:
    try:
        data = collect_metrics()
        requests.post(API_URL, json=data, headers={"x-api-key": API_KEY})
    except Exception as e:
        print(f"Error: {e}")
    time.sleep(60)
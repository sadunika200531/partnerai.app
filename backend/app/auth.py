from fastapi import Header, HTTPException, Depends
import os

API_KEY = os.getenv("SERVER_API_KEY", "default-secret")

async def verify_api_key(x_api_key: str = Header(...)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=403, detail="Invalid API Key")
    return x_api_key
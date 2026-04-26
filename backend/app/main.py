from fastapi import FastAPI
from .database import engine, Base
from .routes import metrics, ai

app = FastAPI(title="AI Personal Server Monitor")

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

app.include_router(metrics.router, prefix="/api/v1")
app.include_router(ai.router, prefix="/api/v1")
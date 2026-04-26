from fastapi import APIRouter, Depends
from ..database import AsyncSessionLocal
from ..models import Metric
from ..schemas import MetricCreate, MetricResponse
from ..auth import verify_api_key

router = APIRouter()

@router.post("/metrics", dependencies=[Depends(verify_api_key)])
async def add_metric(data: MetricCreate):
    async with AsyncSessionLocal() as session:
        new_metric = Metric(**data.dict())
        session.add(new_metric)
        await session.commit()
        return {"status": "success"}
from pydantic import BaseModel
from datetime import datetime

class MetricCreate(BaseModel):
    cpu_usage: float
    ram_usage: float

class MetricResponse(MetricCreate):
    id: int
    timestamp: datetime
    class Config:
        orm_mode = True
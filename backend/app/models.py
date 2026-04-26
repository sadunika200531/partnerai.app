from sqlalchemy import Column, Integer, String, Float, DateTime
from .database import Base
import datetime

class Metric(Base):
    __tablename__ = "metrics"
    id = Column(Integer, primary_key=True)
    cpu_usage = Column(Float)
    ram_usage = Column(Float)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
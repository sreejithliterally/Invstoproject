# schemas.py
from pydantic import BaseModel
import datetime

class StockCreate(BaseModel):
    datetime: datetime.datetime
    close: float
    high: float
    low: float
    open: float
    volume: int
    instrument: str

class StockOut(BaseModel):
   
    datetime: datetime.datetime
    close: float
    high: float
    low: float
    open: float
    volume: int
    instrument: str

    class Config:
        orm_mode = True


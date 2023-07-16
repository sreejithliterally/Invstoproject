from database import Base
from sqlalchemy import Column, DateTime, Float, Integer, String


class Stock(Base):
    __tablename__ = 'Stock'


    datetime = Column(DateTime,primary_key=True)
    close = Column(Float)
    high = Column(Float)
    low = Column(Float)
    open = Column(Float)
    volume = Column(Integer)
    instrument = Column(String)

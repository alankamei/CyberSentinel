from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from app.database.connection import Base


class Log(Base):
    __tablename__ = "logs"

    id = Column(Integer, primary_key=True, index=True)
    event = Column(String, nullable=False)
    ip_address = Column(String, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)

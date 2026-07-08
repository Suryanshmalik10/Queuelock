from sqlalchemy import Column, Integer, String, TIMESTAMP, func

from app.core.db import Base


class Seat(Base):
    __tablename__ = "seats"

    id = Column(Integer, primary_key=True)
    seat_number = Column(String, nullable=False, unique=True)
    status = Column(String, nullable=False, default="available")
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())

from sqlalchemy import Column, Integer, String, TIMESTAMP, func

from app.core.db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())

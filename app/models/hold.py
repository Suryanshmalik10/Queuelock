from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey, func

from app.core.db import Base


class Hold(Base):
    __tablename__ = "holds"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    seat_id = Column(Integer, ForeignKey("seats.id", ondelete="CASCADE"), nullable=False)
    status = Column(String, nullable=False, default="active")
    expires_at = Column(TIMESTAMP(timezone=True), nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())

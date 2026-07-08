from sqlalchemy import Column, Integer, String, Numeric, TIMESTAMP, ForeignKey, func

from app.core.db import Base


class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    hold_id = Column(Integer, ForeignKey("holds.id", ondelete="CASCADE"), nullable=False)
    amount = Column(Numeric(10, 2), nullable=False)
    status = Column(String, nullable=False, default="pending")
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())

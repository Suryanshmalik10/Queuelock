from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey, func

from app.core.db import Base


class Booking(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    seat_id = Column(Integer, ForeignKey("seats.id", ondelete="CASCADE"), nullable=False)
    payment_id = Column(Integer, ForeignKey("payments.id", ondelete="CASCADE"), nullable=False)
    status = Column(String, nullable=False, default="confirmed")
    booked_at = Column(TIMESTAMP(timezone=True), server_default=func.now())

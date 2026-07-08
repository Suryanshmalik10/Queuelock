from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey, func
from sqlalchemy.dialects.postgresql import JSONB

from app.core.db import Base


class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True)
    type = Column(String, nullable=False)
    payload = Column(JSONB, nullable=False)
    status = Column(String, nullable=False, default="pending")
    run_at = Column(TIMESTAMP(timezone=True), server_default=func.now())
    attempts = Column(Integer, nullable=False, default=0)
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())
    updated_at = Column(TIMESTAMP(timezone=True), server_default=func.now())


class JobLock(Base):
    __tablename__ = "job_locks"

    id = Column(Integer, primary_key=True)
    job_id = Column(Integer, ForeignKey("jobs.id", ondelete="CASCADE"), nullable=False)
    locked_at = Column(TIMESTAMP(timezone=True), server_default=func.now())
    locked_by = Column(String, nullable=False)

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url: str = "postgresql+psycopg2://queuelock:queuelock@localhost:5432/queuelock"
    worker_poll_interval_seconds: float = 1.0
    default_hold_ttl_seconds: int = 120

    class Config:
        env_file = ".env"


settings = Settings()

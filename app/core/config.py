from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url: str = "postgresql://queuelock:queuelock@localhost:5432/queuelock"
    worker_poll_interval_seconds: float = 1.0
    default_hold_ttl_seconds: int = 120

    class Config:
        env_file = ".env"

    @property
    def database_url_psycopg2(self) -> str:
        # Strip a SQLAlchemy-style "+psycopg2" dialect tag if present,
        # since plain psycopg2 doesn't understand it.
        return self.database_url.replace("postgresql+psycopg2://", "postgresql://")


settings = Settings()

import psycopg2
import psycopg2.extras

from app.core.config import settings


def get_connection():
  
    conn = psycopg2.connect(
        settings.database_url_psycopg2,
        cursor_factory=psycopg2.extras.RealDictCursor,
    )
    return conn

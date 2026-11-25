import sqlite3
from pathlib import Path

from .exceptions import DatabaseError

_ROOT = Path(__file__).resolve().parent.parent
DB_PATH = _ROOT / "data" / "sample.db"


def get_connection():
    try:
        DB_PATH.parent.mkdir(parents=True, exist_ok=True)
        return sqlite3.connect(DB_PATH)
    except Exception as e:
        raise DatabaseError(f"DB connection failed: {e}") from e


def run_query(query: str):
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(query)
            return cursor.fetchall()
    except Exception as e:
        raise DatabaseError(f"Error running query: {e}") from e
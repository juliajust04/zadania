import sqlite3
from pathlib import Path


DATABASE = Path(__file__).resolve().parent / "queue.db"


def get_connection() -> sqlite3.Connection:
    connection = sqlite3.connect(DATABASE, timeout=30)
    connection.row_factory = sqlite3.Row
    return connection


def init_database() -> None:
    connection = get_connection()

    try:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                task TEXT NOT NULL,
                status TEXT NOT NULL CHECK (
                    status IN ('pending', 'in_progress', 'done')
                )
            )
        """)

        connection.commit()
    finally:
        connection.close()

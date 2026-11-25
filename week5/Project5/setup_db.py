import sqlite3
from pathlib import Path

_ROOT = Path(__file__).resolve().parent
DB_PATH = _ROOT / "data" / "sample.db"


def setup_database() -> None:
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("DROP TABLE IF EXISTS customers")
    cursor.execute(
        """
    CREATE TABLE customers (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        policy_number TEXT NOT NULL,
        policy_type TEXT,
        premium REAL,
        status TEXT,
        date TEXT
    )
    """
    )

    customers = [
        (1, "Alice", "POL12345", "Health", 1200, "Alive", "2025-08-31"),
        (2, "Bob", "POL54321", "Life", 1500, "Alive", "2025-08-31"),
        (3, "Bob", "POL54321", "Life", 1500, "Alive", "2025-08-31"),
        (4, "Charlie", "POL67890", "Health", 1800, "Deceased", "2025-08-31"),
    ]

    cursor.executemany(
        """
    INSERT INTO customers (id, name, policy_number, policy_type, premium, status, date)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """,
        customers,
    )

    conn.commit()
    conn.close()
    print(f"Database setup complete at {DB_PATH}")


if __name__ == "__main__":
    setup_database()
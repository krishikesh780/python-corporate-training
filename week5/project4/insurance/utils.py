import json
from pathlib import Path

from .exceptions import FileReadError, FileWriteError

_ROOT = Path(__file__).resolve().parent.parent
DATA_FILE = _ROOT / "data" / "customers.json"


def read_customers() -> list:
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError as e:
        raise FileReadError("Error: Data file not found.") from e
    except json.JSONDecodeError as e:
        raise FileReadError("Error: Invalid JSON format in file.") from e


def write_customers(customers: list) -> None:
    try:
        DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(customers, f, indent=4)
        print("Data saved successfully.")
    except Exception as e:
        raise FileWriteError(f"Error while writing file: {e}") from e
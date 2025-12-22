import csv
from pathlib import Path
from typing import Any
from ..constants import FIELDNAMES

OUTPUT_DATA_DIR = Path("output/data")


def create_csv(category_name: str) -> Path:
    OUTPUT_DATA_DIR.mkdir(parents=True, exist_ok=True)
    file_name = "_".join(category_name.lower().split())
    file_path = OUTPUT_DATA_DIR / f"{file_name}.csv"

    try:
        with file_path.open("w", encoding="utf-8", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=FIELDNAMES)
            writer.writeheader()
    except Exception as e:
        print(f"[ERROR] Cannot create CSV: {e}")

    return file_path


def append_row(file_path: Path, book_data: dict[str, Any]) -> None:
    try:
        with file_path.open("a", encoding="utf-8", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=FIELDNAMES)
            writer.writerow(book_data)
            print(f"[INFO] Appended data for {book_data.get('title')}")
    except Exception as e:
        print(f"[ERROR] Cannot write to CSV: {e}")

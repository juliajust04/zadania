import csv
from pathlib import Path

from filelock import FileLock


QUEUE_FILE = Path(__file__).resolve().parent / "queue.csv"
LOCK = FileLock(str(QUEUE_FILE) + ".lock")
FIELDS = ["id", "task", "status"]


def read_queue() -> list[dict]:
    if not QUEUE_FILE.exists():
        return []

    with QUEUE_FILE.open(
        "r", newline="", encoding="utf-8"
    ) as file:
        return list(csv.DictReader(file))


def write_queue(tasks: list[dict]) -> None:
    temp_file = QUEUE_FILE.with_suffix(".tmp")

    with temp_file.open(
        "w", newline="", encoding="utf-8"
    ) as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(tasks)

    temp_file.replace(QUEUE_FILE)

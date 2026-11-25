import os
import time

from database import get_connection, init_database


def get_task() -> dict | None:
    connection = get_connection()

    try:
        connection.execute("BEGIN IMMEDIATE")

        task = connection.execute("""
            SELECT * FROM tasks
            WHERE status = 'pending'
            ORDER BY id
            LIMIT 1
        """).fetchone()

        if task is None:
            connection.commit()
            return None

        connection.execute(
            "UPDATE tasks SET status = ? WHERE id = ?",
            ("in_progress", task["id"])
        )

        connection.commit()
        return dict(task)
    finally:
        connection.close()


def finish_task(task_id: int) -> None:
    connection = get_connection()

    try:
        connection.execute(
            "UPDATE tasks SET status = ? WHERE id = ?",
            ("done", task_id)
        )

        connection.commit()
    finally:
        connection.close()


def consume() -> None:
    init_database()
    consumer_id = os.getpid()

    print(f"Uruchomiono consumera {consumer_id}")

    while True:
        task = get_task()

        if task is None:
            print("Brak zadan. Oczekiwanie 5 sekund...")
            time.sleep(5)
            continue

        task_id = task["id"]

        print(
            f"Consumer {consumer_id}: "
            f"rozpoczynam zadanie {task_id}"
        )

        time.sleep(30)

        finish_task(task_id)

        print(
            f"Consumer {consumer_id}: "
            f"zakonczono zadanie {task_id}"
        )


if __name__ == "__main__":
    try:
        consume()
    except KeyboardInterrupt:
        print("\nZatrzymano consumera")

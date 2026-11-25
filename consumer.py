import os
import time

from queue_utils import LOCK, read_queue, write_queue


def get_task() -> dict | None:
    with LOCK:
        tasks = read_queue()

        for task in tasks:
            if task["status"] == "pending":
                task["status"] = "in_progress"
                write_queue(tasks)
                return task

    return None


def finish_task(task_id: str) -> None:
    with LOCK:
        tasks = read_queue()

        for task in tasks:
            if task["id"] == task_id:
                task["status"] = "done"
                break

        write_queue(tasks)


def consume() -> None:
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

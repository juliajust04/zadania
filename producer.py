from queue_utils import LOCK, read_queue, write_queue


def produce() -> None:
    with LOCK:
        tasks = read_queue()

        task_id = max(
            (int(task["id"]) for task in tasks),
            default=0
        ) + 1

        task = {
            "id": task_id,
            "task": f"Rozmowa telefoniczna {task_id}",
            "status": "pending"
        }

        tasks.append(task)
        write_queue(tasks)

    print(f"Dodano zadanie {task_id}")


if __name__ == "__main__":
    produce()

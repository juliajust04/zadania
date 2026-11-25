from database import get_connection, init_database


def produce() -> None:
    init_database()
    connection = get_connection()

    try:
        cursor = connection.execute(
            "INSERT INTO tasks (task, status) VALUES (?, ?)",
            ("Rozmowa telefoniczna", "pending")
        )

        task_id = cursor.lastrowid
        connection.commit()
    finally:
        connection.close()

    print(f"Dodano zadanie {task_id}")


if __name__ == "__main__":
    produce()

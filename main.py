import json

from tasks import add_task, complete_task, remove_task
from storage import load_tasks, save_tasks


def print_tasks(tasks):
    for i, t in enumerate(tasks):
        status = "x" if t["done"] else " "
        print(f"[{status}] {i}: {t['title']}")


def main():
    try:
        tasks = load_tasks()
    except FileNotFoundError:
        tasks = []
    except json.JSONDecodeError:
        print("Erro ao carregar as tarefas.")
        tasks = []

    while True:
        print("1. Add task")
        print("2. Complete task")
        print("3. Remove task")
        print("4. List tasks")
        print("5. Exit")
        choice = input("Choose: ")

        if choice == "1":
            title = input("Task title: ")
            tasks = add_task(tasks, title)
        elif choice == "2":
            print_tasks(tasks)
            raw_idx = input("Task number: ")
            if not raw_idx.isdigit():
                print("Por favor insere um número válido.")
                continue
            result = complete_task(tasks, int(raw_idx))
            if result is None:
                print("Índice inválido.")
            else:
                tasks = result
        elif choice == "3":
            print_tasks(tasks)
            raw_idx = input("Task number: ")
            if not raw_idx.isdigit():
                print("Por favor insere um número válido.")
                continue
            result = remove_task(tasks, int(raw_idx))
            if result is None:
                print("Índice inválido.")
            else:
                tasks = result
        elif choice == "4":
            print_tasks(tasks)
        elif choice == "5":
            save_tasks(tasks)
            break


if __name__ == "__main__":
    main()
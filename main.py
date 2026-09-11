import json
from tasks import add_task, complete_task, remove_task, list_tasks
from storage import load_tasks, save_tasks


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
            list_tasks(tasks)
            raw_idx = input("Task number: ")
            if not raw_idx.isdigit():
                print("Por favor insere um número válido.")
                continue
            idx = int(raw_idx) 
            tasks = complete_task(tasks, idx)
        elif choice == "3":
            list_tasks(tasks)
            raw_idx = input("Task number: ")
            if not raw_idx.isdigit():
                print("Por favor insere um número válido.")
                continue
            idx = int(raw_idx)
            tasks = remove_task(tasks, idx)
        elif choice == "4":
            list_tasks(tasks)
        elif choice == "5":
            save_tasks(tasks)
            break


if __name__ == "__main__":
    main()
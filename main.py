import json

from tasks import add_task, complete_task, remove_task
#storage import JSONTaskRepository
from sqlite_storage import SQLiteTaskRepository



class TaskManager:
    def __init__(self, repo):
        self.repo = repo
        self.tasks = self.repo.load()

    def add_task(self, title):
        self.tasks = add_task(self.tasks, title)
        self.save()

    def complete_task(self, index):
        result = complete_task(self.tasks, index)
        if result is not None:
            self.tasks = result[0]
            self.save()

    def remove_task(self, index):
        result = remove_task(self.tasks, index)
        if result is not None:
            self.tasks = result[0]
            self.save()

    def list_tasks(self):
        for i, t in enumerate(self.tasks):
            status = "x" if t["done"] else " "
            print(f"[{status}] {i}: {t['title']}")

    def save(self):
        self.repo.save(self.tasks)


def main():
    #repo = JSONTaskRepository()
    repo = SQLiteTaskRepository()
    manager = TaskManager(repo)

    while True:
        print("1. Add task")
        print("2. Complete task")
        print("3. Remove task")
        print("4. List tasks")
        print("5. Exit")
        choice = input("Choose: ")

        if choice == "1":
            title = input("Task title: ")
            manager.add_task(title)
        elif choice == "2":
            manager.list_tasks()
            raw_idx = input("Task number: ")
            if not raw_idx.isdigit():
                print("Por favor insere um número válido.")
                continue
            manager.complete_task(int(raw_idx))
        elif choice == "3":
            manager.list_tasks()
            raw_idx = input("Task number: ")
            if not raw_idx.isdigit():
                print("Por favor insere um número válido.")
                continue
            manager.remove_task(int(raw_idx))
        elif choice == "4":
            manager.list_tasks()
        elif choice == "5":
            break


if __name__ == "__main__":
    main()
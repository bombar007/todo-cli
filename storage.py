import json
from abc import ABC, abstractmethod
import sqlite3


class TaskRepository(ABC):
    @abstractmethod
    def load(self) -> list:
        pass

    @abstractmethod
    def save(self, tasks: list) -> None:
        pass


class JSONTaskRepository(TaskRepository):
    def __init__(self, filename="tasks.json"):
        self.filename = filename

    def load(self) -> list:
        try:
            with open(self.filename, "r") as f:
                data = json.load(f)
        except FileNotFoundError:
            data = []
        except json.JSONDecodeError:
            print("Erro ao carregar as tarefas.")
            data = []
        return data

    def save(self, tasks: list) -> None:
        with open(self.filename, "w") as f:
            json.dump(tasks, f)
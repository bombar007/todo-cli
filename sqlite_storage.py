import json
from storage import TaskRepository
import sqlite3


class SQLiteTaskRepository(TaskRepository):
    def __init__(self, filename="tasks.db"):
        self.filename = filename
        self.create_table()

    def create_table(self):
        with sqlite3.connect(self.filename) as conn:
            c = conn.cursor()
            c.execute('''CREATE TABLE IF NOT EXISTS tasks
                         (id INTEGER PRIMARY KEY AUTOINCREMENT,
                          title TEXT NOT NULL,
                          done BOOLEAN NOT NULL,
                          tags TEXT NOT NULL)''')
            conn.commit()

    def load(self) -> list:
        with sqlite3.connect(self.filename) as conn:
            c = conn.cursor()
            c.execute("SELECT * FROM tasks")
            rows = c.fetchall()
            tasks = [
                {"title": row[1], "done": bool(row[2]), "tags": json.loads(row[3])}
                for row in rows
            ]
            return tasks

    def save(self, tasks: list) -> None:
        with sqlite3.connect(self.filename) as conn:
            c = conn.cursor()
            c.execute("DELETE FROM tasks")
            for task in tasks:
                c.execute("INSERT INTO tasks (title, done, tags) VALUES (?, ?, ?)", (task["title"], task["done"], json.dumps(task["tags"])))
            conn.commit()
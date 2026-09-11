import json


def load_tasks(filename="tasks.json"):
    with open(filename, "r") as f:
        data = json.load(f)
    return data

def save_tasks(tasks, filename="tasks.json"):
    with open(filename, "w") as f:
        json.dump(tasks, f)


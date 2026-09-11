def add_task(tasks, title, done=False, tags=None):
    if tags is None:
        tags = []
    task = {"title": title, "done": done, "tags": tags}
    tasks.append(task)
    return tasks

def complete_task(tasks, index):
    if index < 0 or index >= len(tasks):
        print("Índice inválido.")
        return tasks
    tasks[index]["done"] = True
    return tasks


def remove_task(tasks, index):
    if index < 0 or index >= len(tasks):
        print("Índice inválido.")
        return tasks
    del tasks[index]
    return tasks


def list_tasks(tasks):
    for i in range(len(tasks)):
        t = tasks[i]
        status = "x" if t["done"] == True else " "
        print("[" + status + "] " + str(i) + ": " + t["title"])
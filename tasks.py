def add_task(tasks, title, done=False, tags=None):
    if tags is None:
        tags = []
    task = {"title": title, "done": done, "tags": tags}
    tasks.append(task)
    return tasks


def complete_task(tasks, index):
    if index < 0 or index >= len(tasks):
        return None
    tasks[index]["done"] = True
    return tasks


def remove_task(tasks, index):
    if index < 0 or index >= len(tasks):
        return None
    del tasks[index]
    return tasks
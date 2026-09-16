from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from tasks import add_task, complete_task, remove_task
from storage import JSONTaskRepository


app = FastAPI()
repo = JSONTaskRepository()


class Task(BaseModel):
    title: str


@app.get("/tasks")
async def list_tasks():
    tasks = repo.load()
    return tasks


@app.post("/tasks")
async def create_task(task: Task):
    tasks = repo.load()
    tasks = add_task(tasks, task.title)
    repo.save(tasks)
    return tasks


@app.patch("/tasks/{index}/complete")
async def complete_task_endpoint(index: int):
    tasks = repo.load()
    result = complete_task(tasks, index)
    if result is None:
        raise HTTPException(status_code=404, detail="Índice inválido")
    repo.save(result)
    return {"message": "Tarefa concluída com sucesso"}


@app.delete("/tasks/{index}")
async def remove_task_endpoint(index: int):
    tasks = repo.load()
    result = remove_task(tasks, index)
    if result is None:
        raise HTTPException(status_code=404, detail="Índice inválido")
    repo.save(result)
    return {"message": "Tarefa removida com sucesso"}
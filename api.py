from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import APIKeyHeader
#from fastapi import FastAPI, HTTPException, Request, Depends
from pydantic import BaseModel
from tasks import add_task, complete_task, remove_task
from sqlite_storage import SQLiteTaskRepository
from dotenv import load_dotenv
import secrets, os


app = FastAPI()
#repo = JSONTaskRepository()
repo = SQLiteTaskRepository()

load_dotenv()

API_KEY = os.getenv("API_KEY")


class Task(BaseModel):
    title: str


#def verify_api_key(request: Request):
#    api_key = request.headers.get("X-API-Key")
#    if not api_key or not secrets.compare_digest(api_key, API_KEY):
#        raise HTTPException(status_code=401, detail="Chave de API inválida ou em falta")

api_key_header = APIKeyHeader(name="X-API-Key")

def verify_api_key(api_key: str = Depends(api_key_header)):
    if not api_key or not secrets.compare_digest(api_key, API_KEY):
        raise HTTPException(
            status_code=401,
            detail="Chave de API inválida ou em falta"
        )


@app.get("/tasks", dependencies=[Depends(verify_api_key)])
async def list_tasks():
    tasks = repo.load()
    return tasks


@app.post("/tasks", dependencies=[Depends(verify_api_key)])
async def create_task(task: Task):
    tasks = repo.load()
    tasks = add_task(tasks, task.title)
    repo.save(tasks)
    return tasks


@app.patch("/tasks/{index}/complete", dependencies=[Depends(verify_api_key)])
async def complete_task_endpoint(index: int):
    tasks = repo.load()
    result = complete_task(tasks, index)
    if result is None:
        raise HTTPException(status_code=404, detail="Índice inválido")
    repo.save(result)
    return {"message": "Tarefa concluída com sucesso"}


@app.delete("/tasks/{index}", dependencies=[Depends(verify_api_key)])
async def remove_task_endpoint(index: int):
    tasks = repo.load()
    result = remove_task(tasks, index)
    if result is None:
        raise HTTPException(status_code=404, detail="Índice inválido")
    repo.save(result)
    return {"message": "Tarefa removida com sucesso"}
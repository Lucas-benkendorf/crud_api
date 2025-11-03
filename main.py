from fastapi import FastAPI, HTTPException
from typing import List
from models import Tarefa
from database import tarefas

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/tarefas/", response_model=List[Tarefa])
def listar_tarefas():
    return list(tarefas.values())

@app.get("/tarefas/{tarefa_id}", response_model=Tarefa)
def ler_tarefa(tarefa_id: int):
    if tarefa_id not in tarefas:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    return tarefas[tarefa_id]

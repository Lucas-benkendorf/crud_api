from fastapi import FastAPI, HTTPException
from typing import List
from models import Tarefa, TarefaUpdate
from database import tarefas, proximo_id

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/tarefas/", response_model=Tarefa)
def criar_tarefa(tarefa: Tarefa):
    global proximo_id
    tarefas[proximo_id] = tarefa.model_dump()
    tarefas[proximo_id]["id"] = proximo_id
    proximo_id += 1
    return tarefas[proximo_id - 1]

@app.get("/tarefas/", response_model=List[Tarefa])
def listar_tarefas():
    return list(tarefas.values())

@app.get("/tarefas/{tarefa_id}", response_model=Tarefa)
def ler_tarefa(tarefa_id: int):
    if tarefa_id not in tarefas:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    return tarefas[tarefa_id]

@app.put("/tarefas/{tarefa_id}", response_model=Tarefa)
def atualizar_tarefa(tarefa_id: int, tarefa_update: TarefaUpdate):
    if tarefa_id not in tarefas:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    
    tarefa_existente = tarefas[tarefa_id]
    update_data = tarefa_update.model_dump(exclude_unset=True)
    
    for key, value in update_data.items():
        tarefa_existente[key] = value
        
    return tarefa_existente

@app.delete("/tarefas/{tarefa_id}")
def deletar_tarefa(tarefa_id: int):
    if tarefa_id not in tarefas:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    del tarefas[tarefa_id]
    return {"mensagem": "Tarefa deletada com sucesso"}

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastapi.testclient import TestClient
from main import app

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_criar_tarefa():
    response = client.post("/tarefas/", json={"titulo": "Teste", "descricao": "abc", "status": "pendente"})
    assert response.status_code == 200

def test_listar_tarefas():
    response = client.get("/tarefas/")
    assert response.status_code == 200

def test_atualizar_tarefa():
    client.post("/tarefas/", json={"titulo": "X", "descricao": "", "status": "pendente"})
    response = client.put("/tarefas/1", json={"status": "concluida"})
    assert response.status_code == 200

def test_deletar_tarefa():
    client.post("/tarefas/", json={"titulo": "Y", "descricao": "", "status": "pendente"})
    response = client.delete("/tarefas/2")
    assert response.status_code == 200

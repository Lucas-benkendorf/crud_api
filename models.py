from pydantic import BaseModel
from typing import Optional

class Tarefa(BaseModel):
    titulo: str
    descricao: Optional[str] = None
    status: str = "pendente"

class TarefaUpdate(BaseModel):
    titulo: Optional[str] = None
    descricao: Optional[str] = None
    status: Optional[str] = None

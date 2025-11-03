# Sistema Backend Simples de Gerenciamento de Tarefas (CRUD)

Este projeto implementa um sistema backend simples de Gerenciamento de Tarefas (CRUD - Create, Read, Update, Delete) utilizando o framework **FastAPI** em Python. O código foi estruturado em módulos para melhor organização e segue o princípio de simplicidade.

## Estrutura do Projeto

```
crud_api/
├── database.py    # Simulação do banco de dados (dicionário em memória)
├── main.py        # Lógica principal da API e definição dos endpoints
├── models.py      # Definição dos modelos de dados (Pydantic)
├── requirements.txt # Dependências do projeto
└── run.sh         # Script para iniciar o servidor
```

## Requisitos

Para rodar este projeto, você precisa ter o **Python 3.10+** instalado.

## Como Rodar

Siga os passos abaixo para configurar e iniciar o servidor:

1.  **Navegue até a pasta do projeto:**
    ```bash
    cd crud_api
    ```

2.  **Instalar as dependências:**

    Certifique-se de que você tem o `pip` instalado e execute o seguinte comando para instalar as bibliotecas necessárias:

    ```bash
    pip install -r requirements.txt
    ```

3.  **Tornar o script de execução executável:**

    ```bash
    chmod +x run.sh
    ```

4.  **Executar o Servidor:**

    Inicie o servidor com o script de execução:

    ```bash
    ./run.sh
    ```

    O servidor estará acessível em `http://127.0.0.1:8000`.

## Endpoints da API

A API fornece os seguintes endpoints para gerenciar tarefas:

| Método | Endpoint | Descrição |
| :--- | :--- | :--- |
| `POST` | `/tarefas/` | Cria uma nova tarefa. |
| `GET` | `/tarefas/` | Lista todas as tarefas. |
| `GET` | `/tarefas/{tarefa_id}` | Retorna uma tarefa específica pelo ID. |
| `PUT` | `/tarefas/{tarefa_id}` | Atualiza uma tarefa existente pelo ID. |
| `DELETE` | `/tarefas/{tarefa_id}` | Deleta uma tarefa pelo ID. |

### Documentação Interativa

O FastAPI gera automaticamente a documentação interativa (Swagger UI). Você pode acessá-la em:

`http://127.0.0.1:8000/docs`

Use esta interface para testar todos os endpoints da API.

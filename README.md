# Sistema de Gerenciamento de Clientes

API REST para gerenciamento de clientes, desenvolvida com Python e FastAPI.

## 🚀 Tecnologias

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- Pydantic
- Uvicorn

## 📁 Estrutura do projeto
```text
app/
├── database/
│   ├── database.py
│   └── models.py
├── routes/
│   └── clientes.py
├── schemas/
│   └── cliente.py
└── main.py
```


## ⚙️Funcionalidades
Criar cliente
Listar clientes
Buscar cliente por ID
Atualizar cliente
Deletar cliente
Validação de e-mail
Validação de nome
Validação de telefone
Tratamento de cliente não encontrado
Tratamento de e-mail duplicado

## 🔌 Endpoints
Método	        Endpoint	          Descrição
GET	            /clientes/	          Lista todos os clientes
POST	        /clientes/	          Cria um cliente
GET	            /clientes/{id}	      Busca um cliente
PUT	            /clientes/{id}	      Atualiza um cliente
DELETE	        /clientes/{id}	      Remove um cliente


## ▶️ Como executar

Clone o projeto e entre na pasta:

```bash
cd sistema_gerenciamento_clientes
```

Crie e ative o ambiente virtual:

```bash
python -m venv venv
```

No Windows:

```bash
venv\Scripts\activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Configure o arquivo `.env`:

```env
DATABASE_URL=postgresql://postgres:SUA_SENHA@localhost:5432/sistema_clientes
```

Execute a API:

```bash
uvicorn app.main:app --reload
```

A documentação da API estará disponível em:

```text
http://127.0.0.1:8000/docs
```
## 📌 Status
Projeto em desenvolvimento.
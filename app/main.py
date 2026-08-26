from fastapi import FastAPI

from app.routes.usuarios import router as usuarios_router
from app.routes.clientes import router as clientes_router

from app.exceptions.exceptions import (
    ClienteNaoEncontradoError,
    EmailDuplicadoError
)

from app.exceptions.handlers import (
    cliente_nao_encontrado_handler,
    email_duplicado_handler,
    erro_interno_handler
)


app = FastAPI()


app.add_exception_handler(
    ClienteNaoEncontradoError,
    cliente_nao_encontrado_handler
)

app.add_exception_handler(
    EmailDuplicadoError,
    email_duplicado_handler
)

app.add_exception_handler(
    Exception,
    erro_interno_handler
)


app.include_router(clientes_router)
app.include_router(usuarios_router)


@app.get("/")
def home():
    return {"teste": "API funcionando!"}
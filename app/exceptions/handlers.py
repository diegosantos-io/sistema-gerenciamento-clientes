from fastapi import Request
from fastapi.responses import JSONResponse

from app.exceptions import (
    ClienteNaoEncontradoError,
    EmailDuplicadoError
)


def cliente_nao_encontrado_handler(
    request: Request,
    exc: ClienteNaoEncontradoError
):
    return JSONResponse(
        status_code=404,
        content={
            "detail": "Cliente não encontrado."
        }
    )


def email_duplicado_handler(
    request: Request,
    exc: EmailDuplicadoError
):
    return JSONResponse(
        status_code=409,
        content={
            "detail": "Este e-mail já está cadastrado.Tente novamente"
        }
    )
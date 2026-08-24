from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.exceptions import (
    ClienteNaoEncontradoError,
    EmailDuplicadoError
)

from app.schemas.cliente import ClienteCreate
from app.database import models

def listar_clientes(db: Session) -> list[models.Cliente]:
    return db.query(models.Cliente).all()


def criar_cliente(
    db: Session,
    cliente: ClienteCreate
) -> models.Cliente:

    novo_cliente = models.Cliente(
        nome=cliente.nome,
        email=cliente.email,
        telefone=cliente.telefone
    )

    db.add(novo_cliente)

    try:
        db.commit()
        db.refresh(novo_cliente)

    except IntegrityError:
        db.rollback()
        raise EmailDuplicadoError

    return novo_cliente


def buscar_cliente(
    db: Session,
    cliente_id: int
) -> models.Cliente:

    cliente_db = db.query(models.Cliente).filter(
        models.Cliente.id == cliente_id
    ).first()

    if cliente_db is None:
        raise ClienteNaoEncontradoError

    return cliente_db


def atualizar_cliente(
    db: Session,
    cliente_id: int,
    cliente: ClienteCreate
) -> models.Cliente:

    cliente_db = db.query(models.Cliente).filter(
        models.Cliente.id == cliente_id
    ).first()

    if cliente_db is None:
        raise ClienteNaoEncontradoError

    cliente_db.nome = cliente.nome
    cliente_db.email = cliente.email
    cliente_db.telefone = cliente.telefone

    try:
        db.commit()
        db.refresh(cliente_db)

    except IntegrityError:
        db.rollback()
        raise EmailDuplicadoError

    return cliente_db


def deletar_cliente(
    db: Session,
    cliente_id: int
) -> models.Cliente:

    cliente_db = db.query(models.Cliente).filter(
        models.Cliente.id == cliente_id
    ).first()

    if cliente_db is None:
        raise ClienteNaoEncontradoError

    db.delete(cliente_db)
    db.commit()

    return cliente_db
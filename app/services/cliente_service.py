from sqlalchemy.orm import Session
from app.schemas.cliente import ClienteCreate

from app.database import models


def listar_clientes(db:Session):
    return db.query(models.Cliente).all()


def criar_cliente(db:Session,cliente:ClienteCreate):
    novo_cliente = models.Cliente(
        nome = cliente.nome,
        email = cliente.email,
        telefone = cliente.telefone
    )

    db.add(novo_cliente)
    db.commit()
    db.refresh(novo_cliente)

    return novo_cliente


def buscar_cliente(db:Session,cliente_id: int):
    return db.query(models.Cliente).filter(
        models.Cliente.id == cliente_id
    ).first()


def atualizar_cliente(
        db: Session,
        cliente_id:int,
        cliente:ClienteCreate
        ):
    
    cliente_db = db.query(models.Cliente).filter(
        models.Cliente.id == cliente_id
    ).first()

    if cliente_db is None:
        return None

    cliente_db.nome = cliente.nome
    cliente_db.email = cliente.email
    cliente_db.telefone = cliente.telefone

    db.commit()
    db.refresh(cliente_db)

    return cliente_db



def deletar_cliente(db: Session, cliente_id:int):
    cliente_db = db.query(models.Cliente).filter(
        models.Cliente.id == cliente_id
    ).first()

    if cliente_db is None:
        return None

    db.delete(cliente_db)
    db.commit()

    return cliente_db
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.exc import IntegrityError
from app.database.database import get_db
from app.database import models
from app.schemas.cliente import Cliente



router =  APIRouter(
    prefix= "/clientes" ,
    tags= ["Clientes"]
)


@router.get("/")
def listar_clientes(db = Depends(get_db)):
    clientes = db.query(models.Cliente).all()

    return clientes


@router.post("/")
def criar_cliente(cliente: Cliente, db=Depends(get_db)):
    

    novo_cliente = models.Cliente(
        nome = cliente.nome, 
        email = cliente.email, 
        telefone = cliente.telefone
    )
    try:
        db.add (novo_cliente)
        db.commit()
        db.refresh(novo_cliente)

    except IntegrityError:
        db.rollback()
        db.close()

        raise HTTPException(
        status_code= 409,
        detail="este email ja esta cadastrado"
    )

    db.close()
    return novo_cliente


@router.get("/{cliente_id}")
def buscar_cliente(cliente_id: int,db = Depends(get_db)):
    cliente_db = db.query(models.Cliente).filter(
        models.Cliente.id == cliente_id
        ).first()

    db.close()

    if cliente_db is None:
        raise HTTPException(
            status_code= 404,
            detail="cliente nao foi encontrado"
        )

    return cliente_db

@router.put("/{cliente_id}")
def atualizar_cliente(cliente_id: int, cliente: Cliente,db =Depends(get_db)):
    cliente_db = db.query(models.Cliente).filter(
        models.Cliente.id == cliente_id
    ).first()

    if cliente_db is None:
        db.close()
        raise HTTPException(
            status_code=404,
            detail= "cliente nao foi encontrado"
        )
        
    cliente_db.nome = cliente.nome
    cliente_db.email = cliente.email
    cliente_db.telefone = cliente.telefone

    try:
        db.commit()
        db.refresh(cliente_db)
    except IntegrityError:
        db.rollback()
        db.close()

        raise HTTPException(
            status_code=409,
            detail="este email ja esta cadastrado. Tente novamente"
        )
    db.close()

    return cliente_db


@router.delete("/{cliente_id}")
def deletar_cliente(cliente_id:int,db= Depends(get_db)):
    cliente_db = db.query(models.Cliente) .filter(
        models.Cliente.id == cliente_id
    ).first()

    if cliente_db is None:
        db.close()
        raise HTTPException(
            status_code=404,
            detail="cliente nao foi encontrado"
        )
        
    db.delete(cliente_db)
    db.commit()
    db.close()

    return{"mensagem" : "cliente deletado com sucesso"}


    

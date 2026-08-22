from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.schemas.cliente import ClienteCreate, ClienteResponse
from app.services import cliente_service



router =  APIRouter(
    prefix= "/clientes" ,
    tags= ["Clientes"]
)


@router.get("/", response_model=list[ClienteResponse])
def listar_clientes(db:Session = Depends(get_db)):
    return cliente_service.listar_clientes(db)

@router.post("/",response_model=ClienteResponse)
def criar_cliente(cliente: ClienteCreate, db:Session = Depends(get_db)):
    try:
        return cliente_service.criar_cliente(db,cliente)

    except IntegrityError:
        db.rollback()

        raise HTTPException(
            status_code = 409,
            detail="Este e-mail já está cadastrado.Tente novamente"
        )
    
@router.get("/{cliente_id}", response_model= ClienteResponse)
def buscar_cliente(cliente_id: int,db:Session = Depends(get_db)):
    cliente_db = cliente_service.buscar_cliente(db,cliente_id)

    
    if cliente_db is None:
        raise HTTPException(
            status_code= 404,
            detail="Cliente não encontrado."
        )

    return cliente_db

@router.put("/{cliente_id}", response_model=ClienteResponse)
def atualizar_cliente(cliente_id: int, cliente: ClienteCreate,db:Session = Depends(get_db)):

    try:
        cliente_db = cliente_service.atualizar_cliente(
            db,
            cliente_id,
            cliente
        )

        if cliente_db is None:
            raise HTTPException(
                status_code= 404,
                detail="Cliente não encontrado.Tente novamente"
            )
   

        return cliente_db
    
    except IntegrityError:
        db.rollback()

        raise HTTPException(
            status_code= 409,
            detail="Este e-mail já está cadastrado. Tente novamente"
        )


@router.delete("/{cliente_id}")
def deletar_cliente(cliente_id:int,db:Session = Depends(get_db)):
    cliente_db = cliente_service.deletar_cliente(db,cliente_id)

    if cliente_db is None:
        raise HTTPException(
            status_code= 404,
            detail="Cliente não encontrado."
        )

    return{"mensagem": "Cliente deletado com sucesso"}
    

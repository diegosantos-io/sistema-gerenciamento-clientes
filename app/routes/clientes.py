from fastapi import APIRouter, Depends


from sqlalchemy.orm import Session
from app.database.database import get_db
from app.schemas.cliente import ClienteCreate, ClienteResponse
from app.services import cliente_service



router = APIRouter(
    prefix="/clientes",
    tags=["Clientes"]
)


@router.get("/", response_model=list[ClienteResponse])
def listar_clientes(db: Session = Depends(get_db)):
    return cliente_service.listar_clientes(db)


@router.post("/", response_model=ClienteResponse)
def criar_cliente(
    cliente: ClienteCreate,
    db: Session = Depends(get_db)
):
    return cliente_service.criar_cliente(db, cliente)


@router.get("/{cliente_id}", response_model=ClienteResponse)
def buscar_cliente(
    cliente_id: int,
    db: Session = Depends(get_db)
):
    return cliente_service.buscar_cliente(db, cliente_id)


@router.put("/{cliente_id}", response_model=ClienteResponse)
def atualizar_cliente(
    cliente_id: int,
    cliente: ClienteCreate,
    db: Session = Depends(get_db)
):
    return cliente_service.atualizar_cliente(
        db,
        cliente_id,
        cliente
    )


@router.delete("/{cliente_id}")
def deletar_cliente(
    cliente_id: int,
    db: Session = Depends(get_db)
):
    cliente_service.deletar_cliente(db, cliente_id)

    return {
        "mensagem": "Cliente deletado com sucesso"
    }

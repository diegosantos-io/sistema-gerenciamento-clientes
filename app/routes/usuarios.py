from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.usuario import UsuarioCreate, UsuarioResponse
from app.services import usuario_service

router = APIRouter(
    prefix= "/usuarios",
    tags= ["Usuários"]
)


@router.post("/", response_model= UsuarioResponse)
def criar_usuario(
    usuario: UsuarioCreate,
    db:Session = Depends(get_db)
):
    
    return usuario_service.criar_usuario(db, usuario)
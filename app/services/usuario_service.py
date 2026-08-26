import bcrypt

from sqlalchemy.orm import Session

from app.database.models_usuario import Usuario
from app.schemas.usuario import UsuarioCreate


def criar_usuario(
    db: Session,
    usuario: UsuarioCreate
) -> Usuario:

    senha_hash = bcrypt.hashpw(
        usuario.senha.encode("utf-8"),
        bcrypt.gensalt()
    ).decode("utf-8")

    novo_usuario = Usuario(
        username=usuario.username,
        senha_hash=senha_hash
    )

    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)

    return novo_usuario
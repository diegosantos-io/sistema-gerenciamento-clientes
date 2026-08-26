from dotenv import load_dotenv

load_dotenv(".env.test", override=True)

import pytest

from app.database.database import engine, Base
from app.database import models
from app.database.models_usuario import Usuario


@pytest.fixture(autouse=True)
def limpar_banco():
    Base.metadata.create_all(bind=engine)

    tabelas = [
        models.Cliente.__table__,
        Usuario.__table__
    ]

    with engine.begin() as connection:
        for tabela in tabelas:
            connection.execute(tabela.delete())

    yield

    with engine.begin() as connection:
        for tabela in tabelas:
            connection.execute(tabela.delete())
from dotenv import load_dotenv

load_dotenv(".env.test", override=True)

import pytest

from app.database.database import engine,Base
from app.database import models

@pytest.fixture(autouse=True)
def limpar_banco():
    Base.metadata.create_all(bind =engine)

    db = models.Cliente.__table__

    with engine.begin() as connection:
        connection.execute(db.delete())

    yield

    with engine.begin() as connection:
        connection.execute(db.delete())


from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_listar_clientes():
    response = client.get("/clientes/")

    assert response.status_code == 200



def test_criar_cliente():
    response = client.post(
        "/clientes/",
        json={
            "nome": "Cliente Teste",
            "email": "cliente.teste04@teste.com",
            "telefone": "11999999999"
        }
    )

    assert response.status_code == 200
    data = response.json()
    assert data ["nome"] == "Cliente Teste"
    assert data ["email"] == "cliente.teste04@teste.com"
    assert data ["telefone"] == "11999999999"
    assert "id" in data


def test_buscar_cliente():
    response = client.post(
        "/clientes/",
        json={
            "nome": "Cliente Busca",
            "email": "cliente.busca04@buscar.com",
            "telefone": "11999999999"
        }
    )

    assert response.status_code == 200

    cliente_criado = response.json()
    client_id = cliente_criado["id"]

    response = client.get(f"/clientes/{client_id}")

    assert  response.status_code == 200

    data = response.json()

    assert data ["id"] == client_id
    assert data ["nome"] == "Cliente Busca"
    assert data ["email"] == "cliente.busca04@buscar.com"
    assert data ["telefone"] == '11999999999'

def test_atualizar_cliente():
    response = client.post(
        "/clientes/",
        json={
            "nome": "Cliente Atualizar",
            "email": "cliente.atualizar01@teste.com",
            "telefone": "11999999999"
        }
    )   

    assert response.status_code == 200
    cliente_criado = response.json()
    cliente_id = cliente_criado["id"]

    response = client.put(
        f"/clientes/{cliente_id}",
        json={
            "nome": "Cliente Atualizado",
            "email": "cliente.atualizado01@teste.com",
            "telefone": "11999999999"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == cliente_id
    assert data["nome"] == "Cliente Atualizado"
    assert data["email"] == "cliente.atualizado01@teste.com"
    assert data["telefone"] == "11999999999"


def test_deletar_cliente():
    response = client.post(
        "/clientes/",
        json={
            "nome": "Cliente Deletar",
            "email":"cliente.delet@teste.com",
            "telefone": "11999999999"
        }
    )
    assert response.status_code == 200
    cliente_criado = response.json()
    client_id = cliente_criado["id"]

    response = client.delete(f"/clientes/{client_id}")

    assert response.status_code == 200


def test_buscar_cliente_inexistente():
    response = client.get("/clientes/999999")

    assert response.status_code == 404
    assert response.json()["detail"] == "Cliente não encontrado."


def test_email_duplicado():
    cliente = {
        "nome": "Cliente Duplicado",
        "email": "email.duplicado@teste.com",
        "telefone": "11999999999"
    }

    response = client.post("/clientes/", json = cliente)
    
    assert response.status_code == 200

    response = client.post("/clientes", json=cliente)

    assert response.status_code == 409
    assert response.json()['detail'] == "Este e-mail já está cadastrado.Tente novamente"


def test_nome_invalido():
    response = client.post(
        "/clientes/",
        json={
            "nome": "AB",
            "email": "nome.invalido@teste.com",
            "telefone": "11999999999"
        }
    )

    assert response.status_code == 422 

def test_email_invalido():
    response = client.post(
        "/clientes/",
        json={
            "nome": "Cliente Email",
            "email": "email-invalido",
            "telefone": "11999999999",
        }
        
    )

    assert response.status_code == 422

def test_telefone_invalido():
    response = client.post(
        "/clientes/",
        json={
            "nome": "Cliente Telefone",
            "email": "cliente.telefone@teste.com",
            "telefone": "1199999abc"
        }
    )

    assert response.status_code == 422


def test_atualizar_cliente_email_duplicado():
    cliente_1 = client.post(
        "/clientes/",
        json={
            "nome": "Cliente um",
            "email": "cliente.um@teste.com",
            "telefone": "11999999999"
        }
    )

    assert cliente_1.status_code == 200


    cliente_2 = client.post(
        "/clientes/",
        json={
            "nome": "Cliente Dois",
            "email": "cliente.dois@teste.com",
            "telefone": "11999999999" 
        }
    )
    assert cliente_2.status_code == 200

    cliente_2_id = cliente_2.json()["id"]

    response = client.put(
        f"/clientes/{cliente_2_id}",
        json={
            "nome": "Cliente dois Atualizado",
            "email": "cliente.um@teste.com",
            "telefone": "11955555656"
        }
    )

    assert response.status_code == 409

def test_atualizar_cliente_inexistente():
    response = client.put(
        "/clientes/999999",
        json={
            "nome": "Cliente Atualizado",
            "email": "cliente.atualizado@teste.com",
            "telefone": "11999999999"

        }
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "Cliente não encontrado.Tente novamente"


def test_deletar_cliente_inexistente():
    response = client.delete("/clientes/999999")

    assert response.status_code == 404
    assert response.json()["detail"] == "Cliente não encontrado."


def test_telefone_tamanho_invalido():
    response = client.post(
        "/clientes/",
        json={
            "nome": "Cliente Telefone",
            "email": "telefone.tamanho@teste.com",
            "telefone": "119999999"
        }
    )

    assert response.status_code == 422


def test_nome_vazio():
    response = client.post(
        "/clientes/",
        json={
            "nome": "",
            "email": "nome.vazio@teste.com",
            "telefone": "11999999999"
        }
    )

    assert response.status_code == 422
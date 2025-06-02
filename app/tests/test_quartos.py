# tests/test_quartos.py
def test_criar_quarto(client):
    response = client.post("/quartos/", json={
        "numero": 101,
        "tipo": "luxo",
        "preco": 200
    })

    assert response.status_code == 201
    data = response.get_json()
    assert data["numero"] == 101
    assert data["tipo"] == "luxo"
    assert data["preco"] == 200

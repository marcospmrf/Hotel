# tests/conftest.py
import pytest
from app import create_app, db

@pytest.fixture
def client():
    app = create_app(testing=True)

    with app.app_context():
        db.create_all()  # Cria tabelas no banco de teste (em memória)
        yield app.test_client()
        db.drop_all()  # Limpa as tabelas após o teste

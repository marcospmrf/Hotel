from app import create_app, db
from sqlalchemy import text

app = create_app()

with app.app_context():
    try:
        # Consulta usando mappings() para receber como dicionários
        resultado = db.session.execute(text("SELECT * FROM usuario")).mappings().all()

        if not resultado:
            print("⚠️ Nenhum usuário encontrado.")
        else:
            print("✅ Usuários encontrados:")
            for linha in resultado:
                print(linha)  # linha já é um dicionário!
    except Exception as e:
        print("❌ Erro ao buscar usuários:")
        print(e)

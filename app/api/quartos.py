import os
from flask import Blueprint, request, jsonify
from werkzeug.utils import secure_filename
from app import db
from app.models import Quarto

api_bp = Blueprint('api_quartos', __name__)

UPLOAD_FOLDER = 'app/static/img'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'webp'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@api_bp.route("/api/quartos", methods=["POST"])
def criar_quarto():
    try:
        print("📥 Recebendo dados do formulário...")

        numero = int(request.form["numero"])
        tipo = request.form["tipo"]
        preco = float(request.form["preco"])
        descricao = request.form.get("descricao", "")
        imagem_file = request.files.get("imagem")

        print(f"➡️ Dados recebidos: numero={numero}, tipo={tipo}, preco={preco}, descricao={descricao}")
        print(f"📷 Arquivo de imagem: {imagem_file.filename if imagem_file else 'Nenhum'}")

        if Quarto.query.get(numero):
            print("⚠️ Já existe um quarto com esse número.")
            return jsonify({"erro": "Já existe um quarto com esse número."}), 400

        if not imagem_file or not allowed_file(imagem_file.filename):
            print("❌ Imagem ausente ou inválida.")
            return jsonify({"erro": "Imagem inválida ou ausente."}), 400

        
        filename = secure_filename(f"quarto_{numero}_" + imagem_file.filename)
        caminho_imagem = os.path.join(UPLOAD_FOLDER, filename)
        imagem_file.save(caminho_imagem)

        print(f"📁 Imagem salva em: {caminho_imagem}")

        
        novo_quarto = Quarto(
            numero_quarto=numero,
            tipo=tipo,
            preco_diaria=preco,
            descricao=descricao,
            imagem=f"img/{filename}"
        )

        db.session.add(novo_quarto)
        db.session.commit()
        print("✅ Quarto inserido com sucesso no banco.")

        return jsonify({
            "mensagem": "Quarto cadastrado com sucesso!",
            "numero": numero
        }), 201

    except Exception as e:
        db.session.rollback()
        print(f"❌ Erro ao cadastrar quarto: {e}")
        return jsonify({"erro": str(e)}), 500

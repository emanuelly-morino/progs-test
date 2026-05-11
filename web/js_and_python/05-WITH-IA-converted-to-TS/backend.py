from flask import Flask, request, jsonify
from flask_cors import CORS
from pony.orm import Database, Required, db_session, select

# Flask app
app = Flask(__name__)
CORS(app)

# Pony ORM setup
db = Database()


class Filme(db.Entity):
    nome: str = Required(str)
    ano: int = Required(int)
    categoria: str = Required(str)
    classificacao: int = Required(int)


# Bind SQLite database
db.bind(provider='sqlite', filename='filmes.db', create_db=True)
db.generate_mapping(create_tables=True)



# DEFAULT ROUTE
@app.route('/')
def index():
    return "API de Filmes está rodando!"

# CREATE
@app.route('/filmes', methods=['POST'])
@db_session
def criar_filme():
    data = request.json

    filme = Filme(
        nome=data['nome'],
        ano=data['ano'],
        categoria=data['categoria'],
        classificacao=data['classificacao']
    )

    return jsonify({
        "id": filme.id,
        "nome": filme.nome,
        "ano": filme.ano,
        "categoria": filme.categoria,
        "classificacao": filme.classificacao
    }), 201


# READ ALL
@app.route('/filmes', methods=['GET'])
@db_session
def listar_filmes():
    
    # 
    filmes = select(f for f in Filme).list()
    # filmes = select(f for f in Filme)[:]
    
    # em caso de erro do comando acima, seguem alternativas
    # erros podem ocorrer devido a versões de python, pony, etc
    #
    # filmes = Filme.select()[:]
    # filmes = list(select(f for f in Filme))
    # filmes = db.select_by_sql("SELECT * FROM Filme")

    return jsonify([
        {
            "id": f.id,
            "nome": f.nome,
            "ano": f.ano,
            "categoria": f.categoria,
            "classificacao": f.classificacao
        }
        for f in filmes
    ])


# READ ONE
@app.route('/filmes/<int:filme_id>', methods=['GET'])
@db_session
def buscar_filme(filme_id):
    filme = Filme.get(id=filme_id)

    if not filme:
        return jsonify({"erro": "Filme não encontrado"}), 404

    return jsonify({
        "id": filme.id,
        "nome": filme.nome,
        "ano": filme.ano,
        "categoria": filme.categoria,
        "classificacao": filme.classificacao
    })


# UPDATE
@app.route('/filmes/<int:filme_id>', methods=['PUT'])
@db_session
def atualizar_filme(filme_id):
    filme = Filme.get(id=filme_id)

    if not filme:
        return jsonify({"erro": "Filme não encontrado"}), 404

    data = request.json

    filme.nome = data.get('nome', filme.nome)
    filme.ano = data.get('ano', filme.ano)
    filme.categoria = data.get('categoria', filme.categoria)
    filme.classificacao = data.get('classificacao', filme.classificacao)

    return jsonify({
        "id": filme.id,
        "nome": filme.nome,
        "ano": filme.ano,
        "categoria": filme.categoria,
        "classificacao": filme.classificacao
    })


# DELETE
@app.route('/filmes/<int:filme_id>', methods=['DELETE'])
@db_session
def deletar_filme(filme_id):
    filme = Filme.get(id=filme_id)

    if not filme:
        return jsonify({"erro": "Filme não encontrado"}), 404

    filme.delete()
    return jsonify({"mensagem": "Filme deletado com sucesso"})


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")

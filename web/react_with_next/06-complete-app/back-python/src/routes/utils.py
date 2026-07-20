from config import *

# rota padrão
@app.route('/')
def index():
    return "Backend operante :-)"

# uma rota para criar o banco de dados, caso necessário
@app.route("/criar_banco", methods=['GET'])
def criar_banco():
    # é necessário "entrar" em um contexto
    with app.app_context():
        # criar as tabelas (na primeira execução)
        db.create_all() 
    return jsonify({"resultado":"ok", 
                    "detalhes":"Banco de dados criado com sucesso!"})
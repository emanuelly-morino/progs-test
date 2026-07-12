from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

# CONFIGURAÇÕES
# -------------

# Inicialização e configuração do aplicativo Flask
app = Flask(__name__)

# A chave secreta é usada para proteger proteger sessões e formulários (CSRF)
app.config['SECRET_KEY'] = 'kfjad fkjasdlkfja;sldkfj39480293afKJ KJD:'

# pega o caminho no qual está este arquivo
caminho = os.path.dirname(os.path.abspath(__file__))
# soma o caminho ao nome do arquivo
arquivobd = os.path.join(caminho, 'pessoas.db')
# configura o arquivo de banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + arquivobd

# Inicialização da extensão SQLAlchemy
db = SQLAlchemy(app)

# MODELOS
# -------

class Pessoa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), nullable=False)
    telefone = db.Column(db.String(200), nullable=True)  

    def json(self):
        return {
            "id":self.id,
            "nome":self.nome,
            "email":self.email,
            "telefone":self.telefone
            }

# ROTAS
# -----

# rota padrão
@app.route('/')
def index():
    return "Backend operante :-)"





'''
TESTE DE ROTA - Pessoa - POST

curl http://localhost:5000/pessoa -X POST -H "Content-Type:application/json" -d '{"nome":"João da Silva", "email":"josilva@gmail.com","telefone":"47 9 1234 5678"}'
{
  "detalhes": {
    "email": "josilva@gmail.com",
    "id": 1,
    "nome": "Jo\u00e3o da Silva",
    "telefone": "47 9 1234 5678"
  },
  "resultado": "ok"
}

'''

# rota para inserir uma pessoa
@app.route('/pessoa', methods=['POST'])
def criar_pessoa():
    # ler os dados em json
    data = request.json
    
    # se faltou algum dado obrigatório...
    if not data or not data.get('nome') or not data.get('email'):
        # retorna erro
        return jsonify({"resultado":"erro", "detalhes":"Nome e email são obrigatórios"}), 400
    
    # criar a pessoa
    pessoa = Pessoa(
        nome=data['nome'],
        email=data['email'],
        telefone=data.get('telefone')
    )
    
    # salvar no banco de dados
    db.session.add(pessoa)
    db.session.commit()
    
    # retornar mensagem de sucesso :-)
    return jsonify({
        "resultado":"ok", 
        "detalhes":pessoa.json()
    }), 201


'''
TESTE DE ROTA - Pessoa - GET

curl http://localhost:5000/pessoas
{
  "detalhes": [
    {
      "email": "josilva@gmail.com",
      "id": 1,
      "nome": "Jo\u00e3o da Silva",
      "telefone": "47 9 1234 5678"
    }
  ],
  "resultado": "ok"
}
'''

# rota para listar pessoas
@app.route('/pessoas', methods=['GET'])
def listar_pessoas():
    # buscar todas as pessoas no banco de dados
    pessoas = Pessoa.query.all()
    
    # retornar a lista de pessoas em JSON
    return jsonify({
        "resultado":"ok",
        "detalhes":[pessoa.json() for pessoa in pessoas]
    })

# PROGRAMA PRINCIPAL
# ------------------

if __name__ == '__main__':
    # criar o contexto da aplicação (necessário no flask)
    with app.app_context():
        # criar as tabelas (na primeira execução)
        db.create_all() 
        # iniciar o servidor backend
        app.run(debug=True, host='0.0.0.0', port=5000)
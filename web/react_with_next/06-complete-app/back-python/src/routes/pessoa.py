from config import *
from models.pessoa import Pessoa
import services.pessoa as pessoa_service

'''
TESTE DE ROTA - Pessoa - POST

curl http://localhost:5000/pessoa -X POST -H "Content-Type:application/json" -d '{"nome":"Maria Oliveira", "email":"maliv@gmail.com","telefone":"47 9 1122 3344", "login":"maliv","senha":"maliv123"}'
{"detalhes":
  {"email":"maliv@gmail.com",
    "id":1,"login":"maliv",
    "nome":"Maria Oliveira",
    "senha":"$2b$12$ymgii0YggsCxiO2fSBBU5.YU9E97yD51X8wnoxEPehUY3/kaCKGqW",
    "telefone":"47 9 1122 3344"},
"resultado":"ok"}

'''

# rota para inserir uma pessoa
@app.route('/pessoa', methods=['POST'])
@jwt_required()  # exige que o usuário esteja autenticado para acessar esta rota
def criar_pessoa():
    # ler os dados em json
    dados = request.json
    
    # se faltou algum dado obrigatório...
    if not dados or not dados.get('nome') or not dados.get('email') or not dados.get('login') or not dados.get('senha'):
        # retorna erro
        return jsonify({"resultado":"erro", "detalhes":"Nome, email, login e senha são obrigatórios"}), 400
    
    # chama o serviço de criação de pessoa
    pessoa = pessoa_service.criar_pessoa(dados)    
    
    # retornar mensagem de sucesso :-)
    return jsonify({
        "resultado":"ok", 
        "detalhes":pessoa.json()
    }), 201


'''
TESTE DE ROTA - Pessoa - GET

curl localhost:5000/pessoas
{
  "detalhes": [
    {
      "email": "maliv@gmail.com",
      "id": 1,
      "login": "maliv",
      "nome": "Maria Oliveira",
      "senha": "$2b$12$ymgii0YggsCxiO2fSBBU5.YU9E97yD51X8wnoxEPehUY3/kaCKGqW",
      "telefone": "47 9 1122 3344"
    }
  ],
  "resultado": "ok"
}

'''

# rota para listar pessoas
# rota liberada para listagem pública :-) não requer JWT
@app.route('/pessoas', methods=['GET'])
def retornar_pessoas():

    # buscar as pessoas
    pessoas = pessoa_service.retornar_pessoas()
    
    # retornar a lista de pessoas em JSON
    return jsonify({
        "resultado":"ok",
        "detalhes":[pessoa.json() for pessoa in pessoas]
    })

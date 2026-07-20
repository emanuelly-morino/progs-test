from config import *
import services.pessoa as pessoa_service


'''
curl http://localhost:5000/login -X POST -H "Content-Type:application/json" -d '{"login":"maliv", "senha":"maliv123"}'
{"detalhes":{"token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTc4NDU3OTg2MSwianRpIjoiMzBlM2M1YTAtMWIzMC00N2NkLTlkNDAtNTljNzU2NDM5NWYwIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6MSwibmJmIjoxNzg0NTc5ODYxLCJjc3JmIjoiOTNiYWFlOTktNjJkYy00NGNjLTkyZjYtMTcwMGI4YzU4ODA4IiwiZXhwIjoxNzg0NTgwNzYxfQ.djHuaqM3JyePOzCYgY-A3W_5Qk0dR1Ty-pPNd_LwRi4"},"resultado":"ok"}

'''

# rota para fornecer uma JWT
@app.route('/login', methods=['POST'])
def login():
    # ler os dados em json
    dados = request.json
    
    # se faltou algum dado obrigatório...
    if not dados or not dados.get('login') or not dados.get('senha'):
        # retorna erro
        return jsonify({"resultado":"erro", "detalhes":"Login e senha são obrigatórios"}), 400
    
    # chama o serviço de login
    token = pessoa_service.gerar_token(dados['login'], dados['senha'])
    
    if token:
        # retornar mensagem de sucesso :-)
        return jsonify({
            "resultado":"ok", 
            "detalhes":{"token":token}
        }), 200
    else:
        return jsonify({"resultado":"erro", 
                        "detalhes":"Login ou senha inválidos"}), 401
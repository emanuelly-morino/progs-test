from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, jwt_required, create_access_token
import os

# biblioteca para cifrar a senha
import bcrypt

# CONFIGURAÇÕES
# -------------

# Inicialização e configuração do aplicativo Flask
app = Flask(__name__)

# A chave secreta é usada para proteger 
# sessões e formulários (CSRF - Cross-Site Request Forgery)
app.config['SECRET_KEY'] = 'kfjad fkjasdlkfja;sldkfj39480293afKJ KJD:'

# aplicar CORS
CORS(app)

# configurar JWT
app.config['JWT_SECRET_KEY'] = 'kfjad fkjasdlkfja;sldkfj39480293afKJ KJD:'
jwt = JWTManager(app)

# pega o caminho no qual está este arquivo
caminho = os.path.dirname(os.path.abspath(__file__))
# soma o caminho ao nome do arquivo
arquivobd = os.path.join(caminho, 'database/pessoas.db')
# configura o arquivo de banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + arquivobd

# Inicialização da extensão SQLAlchemy
db = SQLAlchemy(app)
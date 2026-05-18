# PARTE 1: definição da classe Pessoa
class Pessoa:
    def __init__(self, nome, email, telefone):
        self.nome = nome
        self.email = email
        self.telefone = telefone

# PARTE 2: conectar a um banco de dados MySQL no servidor local
# importar a biblioteca para trabalhar com MySQL
import mysql.connector

# conectar ao servidor MySQL com usuário e senha root
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root"
)
# criar um cursor para executar comandos SQL
cursor = conn.cursor()

# PARTE 3: obter as pessoas do BD MySQL
# selecionar o banco de dados
cursor.execute("USE pessoas_db")
# executar o comando SQL para selecionar todas as pessoas
cursor.execute('SELECT nome, email, telefone FROM pessoas')
# obter os resultados da consulta
pessoas = cursor.fetchall()

# PARTE 4: listar as pessoas
# percorrer a lista de pessoas obtidas
for pessoa in pessoas:
    # mostrar as informações de cada pessoa
    print(f'Nome: {pessoa[0]}, Email: {pessoa[1]}, Telefone: {pessoa[2]}')

# PARTE 5: fechar a conexão com o banco de dados
conn.close()
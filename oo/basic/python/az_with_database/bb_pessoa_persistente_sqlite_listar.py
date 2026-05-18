# PARTE 1: definição da classe Pessoa
class Pessoa:
    def __init__(self, nome, email, telefone):
        self.nome = nome
        self.email = email
        self.telefone = telefone

# PARTE 2: encontrar o caminho no qual este arquivo está sendo executado
from pathlib import Path
caminho = Path(__file__).resolve().parent 

# PARTE 3: conectar a um banco de dados SQLite
# importar a biblioteca para trabalhar com SQLite
import sqlite3
arquivo = caminho / 'pessoas.db'
conn = sqlite3.connect(arquivo)
cursor = conn.cursor()

# PARTE 4: executar um comando SQL para selecionar todas as pessoas
cursor.execute('SELECT nome, email, telefone FROM pessoas')
# obter os resultados da consulta
pessoas = cursor.fetchall()

# PARTE 5: listar as pessoas
# percorrer a lista de pessoas obtidas
for pessoa in pessoas:
    # mostrar as informações de cada pessoa
    print(f'Nome: {pessoa[0]}, Email: {pessoa[1]}, Telefone: {pessoa[2]}')

# PARTE 6: fechar a conexão com o banco de dados
conn.close()
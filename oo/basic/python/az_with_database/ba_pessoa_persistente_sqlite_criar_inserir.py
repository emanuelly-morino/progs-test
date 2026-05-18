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
# juntar o caminho com o nome do arquivo do banco de dados
# o operador "/" é usado para juntar caminhos de forma segura, 
# independentemente do sistema operacional
# ele está aplicado a um objeto Path, então o resultado é um novo objeto Path 
# representando o caminho completo do arquivo do banco de dados
arquivo = caminho / 'pessoas.db'
# conectar ao banco de dados (o arquivo será criado se não existir)
conn = sqlite3.connect(arquivo)
# criar um cursor para executar comandos SQL
cursor = conn.cursor()

# PARTE 4: criar a tabela de pessoas
cursor.execute('''CREATE TABLE IF NOT EXISTS pessoas
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   nome TEXT NOT NULL,
                   email TEXT NOT NULL,
                   telefone TEXT NOT NULL)''')
# confirmar a criação da tabela
conn.commit()

# PARTE 5: criar uma pessoa
pessoa1 = Pessoa("João Silva", "jo@gmail.com", "47 91234567")

# PARTE 6: inserir a pessoa no banco de dados
cursor.execute('''INSERT INTO pessoas (nome, email, telefone) VALUES (?, ?, ?)''', 
               (pessoa1.nome, pessoa1.email, pessoa1.telefone))
# confirmar a inserção
conn.commit()

# PARTE 7: fechar a conexão com o banco de dados
conn.close()
# PARTE 1: definição da classe Pessoa
class Pessoa:
    def __init__(self, nome, email, telefone):
        self.nome = nome
        self.email = email
        self.telefone = telefone

class Celular:
    def __init__(self, numero, marca, operadora, pessoa):
        self.numero = numero
        self.marca = marca
        self.operadora = operadora
        self.pessoa = pessoa


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
arquivo = caminho / 'pessoa_celular_NA_MAO.db'
# conectar ao banco de dados (o arquivo será criado se não existir)
conn = sqlite3.connect(arquivo)
# criar um cursor para executar comandos SQL
cursor = conn.cursor()

# PARTE 4: criar a tabela de pessoas e celulaer
cursor.execute('''CREATE TABLE IF NOT EXISTS pessoa
                  (id_pessoa INTEGER PRIMARY KEY AUTOINCREMENT,
                   nome TEXT NOT NULL,
                   email TEXT NOT NULL,
                   telefone TEXT NOT NULL)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS celular
                  (id_celular INTEGER PRIMARY KEY AUTOINCREMENT,
                   numero TEXT NOT NULL,
                   marca TEXT NOT NULL,
                   operadora TEXT NOT NULL,
                   id_pessoa INTEGER,
                   FOREIGN KEY (id_pessoa) REFERENCES pessoa (id_pessoa))''')
# confirmar a criação da tabela
conn.commit()

# PARTE 5: criar uma pessoa
pessoa1 = Pessoa("João Silva", "jo@gmail.com", "47 91234567")
celular1 = Celular("47 91234567", "Samsung", "Vivo", pessoa1)

# PARTE 6: inserir a pessoa no banco de dados
cursor.execute('''INSERT INTO pessoa (nome, email, telefone) VALUES (?, ?, ?)''', 
               (pessoa1.nome, pessoa1.email, pessoa1.telefone))

# pega o ID da pessoa que foi gravada
cursor.execute('''SELECT id_pessoa FROM pessoa WHERE nome = ?''', (pessoa1.nome,))
# retorna o primeiro registro
id_pessoa1 = cursor.fetchone()[0]
# inserir o celular
cursor.execute('''INSERT INTO celular (numero, marca, operadora, id_pessoa) VALUES (?, ?, ?, ?)''', 
               (celular1.numero, celular1.marca, celular1.operadora, id_pessoa1))

# confirmar a inserção
conn.commit()

# PARTE 7: fechar a conexão com o banco de dados
conn.close()
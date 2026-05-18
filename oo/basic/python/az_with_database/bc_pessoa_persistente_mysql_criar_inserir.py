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
# criar o banco de dados se não existir e selecioná-lo
cursor.execute("CREATE DATABASE IF NOT EXISTS pessoas_db")
cursor.execute("USE pessoas_db")
# confirmar a criação do BD
conn.commit()

# PARTE 3: criar a tabela de pessoas
cursor.execute('''CREATE TABLE IF NOT EXISTS pessoas
                  (id INT AUTO_INCREMENT PRIMARY KEY,
                   nome VARCHAR(255) NOT NULL,
                   email VARCHAR(255) NOT NULL,
                   telefone VARCHAR(50) NOT NULL)''')
# confirmar a criação da tabela e do banco de dados
conn.commit()

# PARTE 4: criar uma pessoa
pessoa1 = Pessoa("João Silva", "jo@gmail.com", "47 91234567")

# PARTE 5: inserir a pessoa no banco de dados
cursor.execute('INSERT INTO pessoas (nome, email, telefone) VALUES (%s, %s, %s)', 
               (pessoa1.nome, pessoa1.email, pessoa1.telefone))
# confirmar a inserção
conn.commit()

# PARTE 6: fechar a conexão com o banco de dados
conn.close()
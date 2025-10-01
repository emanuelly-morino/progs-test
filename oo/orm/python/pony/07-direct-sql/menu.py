from pony.orm import *
from datetime import date
import os

# vínculo com o PONY
db = Database()

# definição da classe
class Pessoa(db.Entity):
    id = PrimaryKey(int, auto=True)
    nome = Required(str)
    email = Required(str)

# remove o arquivo para evitar duplicidade de dados
if os.path.exists("pessoas.db"):
    os.remove("pessoas.db")

# conexão com o BD
db.bind(provider='sqlite', filename='pessoas.db', create_db=True)
db.generate_mapping(create_tables=True)

with db_session:

    # cria 3 pessoas
    Pessoa(nome="Ana Maria", email="ama@gmail.com")
    Pessoa(nome="Marcelo Silva", email="marsil@gmail.com")
    Pessoa(nome="Joana Hertz", email="tihe@gmail.com")

    # grava :-)
    commit()
    
    # executa um SQL
    results = db.select("SELECT * FROM pessoa order by nome desc")

    # mostra os resultados
    for linha in results:
        print(f"Nome: {linha.nome} - Email: {linha.email}")
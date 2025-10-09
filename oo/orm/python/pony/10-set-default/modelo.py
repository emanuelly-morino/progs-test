from pony.orm import Database, Required, Optional, Set
from datetime import date

# Inicializa o banco de dados (pode ser SQLite, PostgreSQL, etc.)
db = Database()

# ======================================================
# 1. Classe Pessoa
# ======================================================
class Pessoa(db.Entity):
    nome = Required(str)
    data_cadastro = Optional(date, default=date.today, sql_default='CURRENT_DATE', nullable=True)
    email = Required(str, unique=True)
    telefone = Optional(str, nullable=True)  

# ======================================================
# Configuração do banco
# ======================================================

# Exemplo com SQLite (arquivo local)
db.bind(provider="sqlite", filename="pessoa.db", create_db=True)
db.generate_mapping(create_tables=True)

# Exemplo com MYSQL
#db.bind(provider='mysql', host='localhost', user='root', passwd='root', db='Joao')
#db.generate_mapping(create_tables=True) 



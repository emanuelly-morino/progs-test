from pony.orm import Database, Required, Optional, Set
from datetime import date

# Inicializa o banco de dados (pode ser SQLite, PostgreSQL, etc.)
db = Database()

# ======================================================
# 1. Classe Pessoa
# ======================================================
class Pessoa(db.Entity):
    nome = Required(str)
    email = Required(str, unique=True)
    telefone = Optional(str, nullable=True)
    clientes = Set('Cliente')
    tecnicos = Set('Tecnico')    

class Cliente(db.Entity):
    pessoa = Required(Pessoa)
    endereco = Optional(str, nullable=True)
    servicos = Set('Servico')
    
class Tecnico(db.Entity):
    pessoa = Required(Pessoa)
    servicos = Set('Servico')

class Equipamento(db.Entity):
    nome = Required(str)
    descricao = Required(str)
    servicos = Set('Servico')
    
class Servico(db.Entity):
    cliente = Required(Cliente)
    equipamento = Required(Equipamento)
    tecnico = Optional(Tecnico, nullable=True)
    descricao = Required(str)
    preco = Required(float)
    data_abertura = Required(date, default=date.today)
    data_conclusao = Optional(date, nullable=True)


# ======================================================
# Configuração do banco
# ======================================================

# Exemplo com SQLite (arquivo local)
db.bind(provider="sqlite", filename="consertos.db", create_db=True)
db.generate_mapping(create_tables=True)


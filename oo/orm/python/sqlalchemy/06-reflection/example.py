from sqlalchemy import (
    create_engine,
    Table,
    Column,
    Integer,
    String,
    MetaData,
)

from sqlalchemy.orm import registry, Session

# -------------------------
# Classe original "limpa"
# -------------------------

class Usuario:
    # não é necessário definir __init__
    pass

# -------------------------
# Configuração SQLite
# -------------------------

# cria arquivo banco.db
engine = create_engine("sqlite:///banco.db") # se quiser mostrar os comandos SQL, definir: , echo=True)

metadata = MetaData()
mapper_registry = registry()

# -------------------------
# Definição da tabela
# -------------------------
# A tabela "usuarios" tem as colunas "id" e "nome". O mapeamento imperativo
# associará a classe Usuario a essa tabela, permitindo que objetos da classe
# sejam persistidos e consultados no banco de dados.
usuarios_table = Table(
    "usuarios",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("nome", String(100)),
)

# Mapeamento imperativo
mapper_registry.map_imperatively(
    Usuario,
    usuarios_table
)

# Cria as tabelas no SQLite
metadata.create_all(engine)

# Inserindo dados
with Session(engine) as session:

    u1 = Usuario()
    u1.nome = "Ana"

    u2 = Usuario()
    u2.nome = "Carlos"

    session.add(u1)
    session.add(u2)

    session.commit()

# Consultando dados
with Session(engine) as session:

    usuarios = session.query(Usuario).all()

    print("\nUsuários encontrados:")

    for usuario in usuarios:
        print(f"{usuario.id}: {usuario.nome}")
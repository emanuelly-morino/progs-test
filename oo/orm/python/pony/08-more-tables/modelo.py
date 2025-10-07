from pony.orm import Database, Required, Optional, Set

# Inicializa o banco de dados (pode ser SQLite, PostgreSQL, etc.)
db = Database()

# ======================================================
# 1. Classe Pessoa
# ======================================================
class Pessoa(db.Entity):
    nome = Required(str)
    email = Required(str, unique=True)
    telefone = Optional(str)
    receitas = Set("Receita")
    comentarios = Set("Comentario")

# ======================================================
# 2. Classe Categoria
# ======================================================
class Categoria(db.Entity):
    nome = Required(str, unique=True)
    descricao = Optional(str)
    receitas = Set("Receita")

# ======================================================
# 3. Classe Receita
# ======================================================
class Receita(db.Entity):
    titulo = Required(str)
    descricao = Optional(str)
    modo_preparo = Required(str)
    tempo_preparo = Optional(int)  # em minutos
    
    rendimento = Optional(str)
    autor = Required(Pessoa)
    categoria = Optional(Categoria)
    ingredientes = Set("ItemIngrediente")
    comentarios = Set("Comentario")

# ======================================================
# 4. Classe Ingrediente
# ======================================================
class Ingrediente(db.Entity):
    nome = Required(str, unique=True)
    unidade_padrao = Optional(str)  # ex: 'g', 'ml', 'colher(es)', etc.
    itens = Set("ItemIngrediente")

# ======================================================
# 5. Classe ItemIngrediente (relação N:N entre Receita e Ingrediente)
# ======================================================
class ItemIngrediente(db.Entity):
    receita = Required(Receita)
    ingrediente = Required(Ingrediente)
    quantidade = Required(float)
    unidade = Optional(str)

# ======================================================
# 6. Classe Comentario
# ======================================================
class Comentario(db.Entity):
    pessoa = Required(Pessoa)
    receita = Required(Receita)
    texto = Required(str)
    data = Optional(str)
    nota = Optional(int)  # Avaliação de 1 a 5

# ======================================================
# Configuração do banco
# ======================================================

# Exemplo com SQLite (arquivo local)
db.bind(provider="sqlite", filename="receitas.db", create_db=True)
db.generate_mapping(create_tables=True)


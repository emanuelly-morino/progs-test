# pip3 install pony

# importando a biblioteca
from pony.orm import *

# conectando-se ao pony
db = Database()

# definição da classe
class Pessoa(db.Entity):
    nome = Required(str)
    email = Required(str)
    telefone = Optional(str)

# especificando o BD; o BD será criado caso não exista
db.bind(provider='sqlite', filename='person.db', create_db=True)

# optando por criar as tabelas
db.generate_mapping(create_tables=True)

# iniciando a sessão
with db_session:

    # criando a pessa
    jo = Pessoa(nome='João da Silva', email='josilva@gmail.com')
    # salvando
    commit()
    # exibindo os dados
    print(jo.nome, jo.email)
    # existe um ID?
    print(jo.id)

# tipos de atributos:
# https://docs.ponyorm.org/entities.html#attribute-data-types
from pony.orm import *

db = Database()

class Pessoa(db.Entity):
    nome = Required(str)
    email = Required(str)
    telefone = Optional(str)
    def __str__(self):
        return f'{self.nome}, {self.email}, {self.telefone}'

db.bind(provider='sqlite', filename='person.db', create_db=True)
db.generate_mapping(create_tables=True)

with db_session:

    # inserindo
    jo = Pessoa(nome='João da Silva', email='josilva@gmail.com')
    commit()
    print(jo)

    # alterando
    jo.telefone = "47 9 1234 5678"
    commit()
    print("alterada:", jo)

    # listando
    # https://docs.ponyorm.org/firststeps.html#writing-queries

    ma = Pessoa(nome='Maria Oliveira', email='maliv@gmail.com')
    commit()
    print("listando:")
    pessoas = Pessoa.select()
    # pessoas = select(p for p in Pessoa) # outra maneira
    for p in pessoas:
        print(p)

    # excluindo
    Pessoa[ma.id].delete()
    print("depois da exclusão:")
    for p in pessoas:
        print(p)
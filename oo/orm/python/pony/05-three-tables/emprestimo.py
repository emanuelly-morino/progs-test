from pony.orm import *

db = Database()

class Pessoa(db.Entity):
    nome = Required(str)
    email = Required(str)
    emprestimos = Set('Emprestimo')  # atributo reverso

class Livro(db.Entity):
    titulo = Required(str) 
    ano = Required(str)
    autores = Required(str)
    emprestimos = Set('Emprestimo')  # atributo reverso

class Emprestimo(db.Entity):
    pessoa = Required(Pessoa)
    livro = Required(Livro)
    data_emprestimo = Required(str)
    data_devolucao = Optional(str)

db.bind(provider='sqlite', filename='emprestimo.db', create_db=True)
db.generate_mapping(create_tables=True)

with db_session:
    p1 = Pessoa(nome="João da Silva", email="josilva@gmail.com")
    p2 = Pessoa(nome="Maria Oliveira", email="maliv@gmail.com")
    L1 = Livro(titulo="Dom Quixote de la Mancha", ano="1605", autores="Miguel de Cervantes")
    L2 = Livro(titulo="Os três mosqueteiros", ano="1844", autores="Alexandre Dumas")
    e1 = Emprestimo(pessoa=p1, livro=L1, data_emprestimo="10/09/2025", data_devolucao="14/09/2025")
    e2 = Emprestimo(pessoa=p2, livro=L2, data_emprestimo="15/09/2025")
    p3 = Pessoa(nome="Tiago Kreuch", email="tikreuch@gmail.com")
    l4 = Livro(titulo="Dom Casmurro", ano="1899", autores="Machado de Assis")
    commit()
    

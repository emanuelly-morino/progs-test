from pony.orm import *
from datetime import date

db = Database()

class Pessoa(db.Entity):
    nome = Required(str)
    email = Required(str)
    emprestimos = Set('Emprestimo')  # atributo reverso

class Livro(db.Entity):
    titulo = Required(str) 
    ano = Required(int)
    autores = Required(str)
    emprestimos = Set('Emprestimo')  # atributo reverso

class Emprestimo(db.Entity):
    pessoa = Required(Pessoa)
    livro = Required(Livro)
    data_emprestimo = Required(date)
    data_devolucao = Optional(date, nullable=True)

db.bind(provider='sqlite', filename='emprestimo.db', create_db=True)
db.generate_mapping(create_tables=True)

with db_session:
    p1 = Pessoa(nome="João da Silva", email="josilva@gmail.com")
    p2 = Pessoa(nome="Maria Oliveira", email="maliv@gmail.com")
    L1 = Livro(titulo="Dom Quixote de la Mancha", ano="1605", autores="Miguel de Cervantes")
    L2 = Livro(titulo="Os três mosqueteiros", ano="1844", autores="Alexandre Dumas")
    e1 = Emprestimo(pessoa=p1, livro=L1, data_emprestimo=date(2025, 9, 15), data_devolucao=date(2025, 9, 20))
    e2 = Emprestimo(pessoa=p2, livro=L2, data_emprestimo=date(2025, 5, 15))
    p3 = Pessoa(nome="Tiago Kreuch", email="tikreuch@gmail.com")
    L3 = Livro(titulo="Dom Casmurro", ano="1899", autores="Machado de Assis")
    e3 = Emprestimo(pessoa=p1, livro=L3, data_emprestimo=date(2025, 9, 11))
    e4 = Emprestimo(pessoa=p3, livro=L2, data_emprestimo=date(2025, 8, 12), data_devolucao=date(2025, 8, 25)) 

    commit()
    

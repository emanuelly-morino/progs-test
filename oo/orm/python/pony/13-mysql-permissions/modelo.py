from pony.orm import *
from datetime import date

db = Database()

class Pessoa(db.Entity):
    _table_='hylson_pessoa'
    nome = Required(str)
    email = Required(str)
    emprestimos = Set('Emprestimo')  # atributo reverso

class Livro(db.Entity):
    _table_='hylson_livro'
    titulo = Required(str) 
    ano = Required(int)
    autores = Required(str)
    emprestimos = Set('Emprestimo')  # atributo reverso

class Emprestimo(db.Entity):
    _table_='hylson_emprestimo'
    pessoa = Required(Pessoa)
    livro = Required(Livro)
    data_emprestimo = Required(date)
    data_devolucao = Optional(date, nullable=True)

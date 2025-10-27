'''
instalar biblioteca para acessar mysql:
pip install pymysql

no linux:
pip3 install pymysql --break-system-packages

'''

from pony.orm import *
from datetime import date

from modelo import *

# db.bind(provider='sqlite', filename='emprestimo.db', create_db=True)

# usuario root
db.bind(provider="mysql", host="localhost", user="root", passwd="root", db="hylson")

# usuario mariasilva, senha msilva
#db.bind(provider="mysql", host="localhost", user="mariasilva", passwd="msilva", db="hylson")

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
    

# é necessário instalar a biblioteca simple-term-menu
# linux:
#     pip3 install simple-term-menu --break-system-packages
# windows:
#     pip install simple-term-menu

from simple_term_menu import TerminalMenu

from pony.orm import *
from datetime import date

db = Database()

class Pessoa(db.Entity):
    id = PrimaryKey(int, auto=True)
    nome = Required(str)
    email = Required(str)

db.bind(provider='sqlite', filename='pessoas.db', create_db=True)
db.generate_mapping(create_tables=True)

with db_session:

    while True:
        # cria opções do menu
        options = ["Cadastrar nova pessoa", 
                   "Listar pessoas cadastradas", 
                   "Sair"]
        
        # monta o menu
        terminal_menu = TerminalMenu(options)

        # mostra o menu e espera seleção
        op = terminal_menu.show()

        if op == 0:
            print("* Cadastrar nova pessoa")
            nome = input("Nome: ")
            email = input("Email: ")
            Pessoa(nome=nome, email=email)
            commit()
            print("Pessoa cadastrada com sucesso!")

        elif op == 1:
            print("* Pessoas cadastradas:")
            pessoas = Pessoa.select()
            for pessoa in pessoas:
                print(f"ID: {pessoa.id}, Nome: {pessoa.nome}, Email: {pessoa.email}")
            print("-" * 30)
        
        elif op == 2:
            print("Saindo...")
            break
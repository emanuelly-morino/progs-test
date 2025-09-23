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
        print("\n \n CADASTRO DE PESSOAS")
        print("1 - Cadastrar nova pessoa")
        print("2 - Listar pessoas cadastradas")
        print("9 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("* Cadastrar nova pessoa")
            nome = input("Nome: ")
            email = input("Email: ")
            Pessoa(nome=nome, email=email)
            commit()
            print("Pessoa cadastrada com sucesso!")

        elif opcao == "2":
            print("* Pessoas cadastradas:")
            pessoas = Pessoa.select()
            for pessoa in pessoas:
                print(f"ID: {pessoa.id}, Nome: {pessoa.nome}, Email: {pessoa.email}")
            print("-" * 30)
        
        elif opcao == "9":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

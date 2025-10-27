from pony.orm import *
from datetime import date

from modelo import *

# usuario mariasilva, senha msilva
db.bind(provider="mysql", host="localhost", user="mariasilva", passwd="msilva", db="hylson")

db.generate_mapping(create_tables=False)

with db_session:
    # alterar o email de uma pessoa
    p1 = Pessoa.get(nome="João da Silva")
    p1.email = "josilva2@gmail.com"
    commit()
    print(f"Email alterado: {p1.nome} - {p1.email}")

    # se tentar fazer outra coisa, dá erro
    try:
        p2 = Pessoa(nome="Ana Paula", email="apaula@gmail.com")
        commit()
    except Exception as e:
        print("Erro ao inserir nova pessoa:", e)
    

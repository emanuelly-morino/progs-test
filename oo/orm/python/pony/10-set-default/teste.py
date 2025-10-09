from pony.orm import db_session
from modelo import *

with db_session:
    # Cria uma nova pessoa
    nova_pessoa = Pessoa(nome="João Silva", 
                         email="josilva@gmail.com", 
                         telefone="(11) 99999-9999",
                         data_cadastro=date(2024, 6, 15))
    print(f"Pessoa criada: {nova_pessoa.nome}, Email: {nova_pessoa.email}, Telefone: {nova_pessoa.telefone}, Data de Cadastro: {nova_pessoa.data_cadastro}")  

    # cria outra pessoa
    outra_pessoa = Pessoa(nome="Maria Oliveira", email="maliv@gmail.com")
    print(f"Pessoa criada: {outra_pessoa.nome}, Email: {outra_pessoa.email}, Telefone: {outra_pessoa.telefone}, Data de Cadastro: {outra_pessoa.data_cadastro}")

    # Consulta todas as pessoas
    todas_pessoas = Pessoa.select()[:]
    print("Todas as pessoas cadastradas:")
    for pessoa in todas_pessoas:
        print(f"- {pessoa.nome}, Email: {pessoa.email}, Telefone: {pessoa.telefone}, Data de Cadastro: {pessoa.data_cadastro}")

    
                                                                                                                                
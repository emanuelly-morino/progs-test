from a_config import *
from b_model import *

# inicia uma sessão
with Session(engine) as session:

    # INCLUSÃO (Create) ----------------------------------------
    # cria um objeto
    alguem = Pessoa(nome = "Joao da Silva", 
                    email = "josilva@gmail.com", 
                    telefone = "47 9 9234 1324")

    # persiste 
    session.add(alguem)

    # confirma a gravação
    session.commit()

    # mostra as informações
    print(alguem)

    # cria mais pessoas
    outro = Pessoa(nome = "Maria Oliveira", 
                    email = "maliv@gmail.com", 
                    telefone = "47 9 9198 8765")
    maisum = Pessoa(nome = "Tiago Braun", 
                    email = "tibru@gmail.com", 
                    telefone = "47 9 9881 1223")
    
    # grava o pessoal
    session.add_all([outro, maisum])
    session.commit()

    print(outro, maisum)

    # ATUALIZAÇÃO (Update) ----------------------------------------
    # https://docs.sqlalchemy.org/en/20/orm/quickstart.html#make-changes

    # muda o campo
    alguem.email = "josilva@hotmail.com"

    # efetiva a alteração
    session.commit()

    print("após atualização:", alguem)
    
    # EXCLUIR (Delete)
    # https://docs.sqlalchemy.org/en/20/orm/quickstart.html#some-deletes
       
    # deleta ;-p
    session.delete(outro)

    # efetiva a exclusão
    session.commit()

    # LISTAGEM / CONSULTA (Retrieve) ----------------------------
    # https://docs.sqlalchemy.org/en/20/orm/quickstart.html#simple-select

    # faz a consulta
    stmt = select(Pessoa).where(Pessoa.nome.in_(["Joao da Silva", "Tiago Braun"]))

    # percorre os resultados
    for p in session.scalars(stmt):
       print(p)
    
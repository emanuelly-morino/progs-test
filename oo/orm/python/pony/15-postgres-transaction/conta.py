from pony.orm import *
from datetime import date

db = Database()

class Aluno(db.Entity):
    _table_ = '15_transaction_alunos_COLOQUE_SEU_NOME_AQUI'
    nome = Required(str)
    email = Optional(str, unique=True, nullable=True)
    contas = Set('Conta')
    
class Conta(db.Entity):
    _table_ = '15_transaction_contas_COLOQUE_SEU_NOME_AQUI'
    saldo = Required(float)
    aluno = Required(Aluno, column='aluno_id')
    
db.bind(provider='postgres', user='postgres', password='root', host='localhost', database='hylson')
db.generate_mapping(create_tables=True)

@db_session
def executar_transferencia_com_erro_com_perda(id_conta1, id_conta2):
    # obter os dados
    conta1 = obter_conta(id_conta1)
    conta2 = obter_conta(id_conta2)

    # Transferência COM ERRO e COM PERDA
    conta1.saldo -= 500.0
    commit()
    try:
        raise Exception("Erro forçado para teste de perda")
        # não vai executar a linha abaixo porque aconteceu um erro simulado :-)
        conta2.saldo += 500.0
    except:
        print("ERRO! Saldo foi debitado, dinheiro SUMIU!")

@db_session
def executar_transferencia_com_erro_sem_perda(id_conta1, id_conta2):
    # obter os dados
    conta1 = obter_conta(id_conta1)
    conta2 = obter_conta(id_conta2)

    # realizando débito
    conta1.saldo -= 500.0
    try:
        # realizando o crédito
        conta2.saldo += 500.0
        # forçando um erro
        raise Exception("Erro forçado para testar rollback")
    except:
        # desfazendo todas as operações dentro da transação / sessão
        rollback()
        print("Erro capturado, mas o saldo foi restaurado. Sem perda de dinheiro.")

@db_session
def executar_transferencia_sem_erro(id_conta1, id_conta2):
    # obter os dados
    conta1 = obter_conta(id_conta1)
    conta2 = obter_conta(id_conta2)

    # Transferência SEM ERRO (e sem perda)
    conta1.saldo -= 500.0
    conta2.saldo += 500.0
    print("Transferência realizada com sucesso, sem erros.")

@db_session
def limpar_dados():
    Aluno.select().delete(bulk=True)
    Conta.select().delete(bulk=True)

@db_session
def criar_dados():
    # Criando um aluno
    aluno1 = Aluno(nome="João Silva", email="jo@gmail.com")
    aluno2 = Aluno(nome="Maria Souza", email="ma@gmail.com")
    # Criando contas para os alunos
    conta1 = Conta(saldo=15000.0, aluno=aluno1)
    conta2 = Conta(saldo=25000.0, aluno=aluno2)  

    # efetivar criação dos dados
    commit()
    # retornar dados criados
    return conta1.id, conta2.id

@db_session
def exibir_saldos():
    print("Saldos:")
    for aluno in Aluno.select():
        print(aluno.nome, end='')
        for conta in aluno.contas:
            print(f", conta saldo: {conta.saldo}")

@db_session
def obter_conta(conta_id):
    return Conta.get(id=conta_id)


#
# programa principal
#


limpar_dados()
id_conta1, id_conta2 = criar_dados()

while True:
    exibir_saldos()
    
    # menu
    print("Opções")
    print("1 - Executar transferência COM ERRO e COM PERDA")
    print("2 - Executar transferência COM ERRO mas SEM PERDA")
    print("3 - Executar transferência SEM ERRO (e sem perda)")
    print("9 - Sair")
    op = input("O que deseja fazer? => ")
    
    if op == '1':
        executar_transferencia_com_erro_com_perda(id_conta1, id_conta2)
    elif op == '2':
        executar_transferencia_com_erro_sem_perda(id_conta1, id_conta2)
    elif op == '3':
        executar_transferencia_sem_erro(id_conta1, id_conta2)
    elif op == '9':
        print("Saindo...")
        break

# limpeza de dados
limpar_dados()





''' instalar biblioteca de acesso postgres:
 LINUX:
 pip3 install psycopg2-binary --break-system-packages

'''
from pony.orm import *
from datetime import date

db = Database()

class Aluno(db.Entity):
    nome = Required(str)
    email = Required(str, unique=True)
    pagamentos = Set('Pagamento')
    def __str__(self):
        return f"Aluno: {self.nome}, Email: {self.email}"

class Pagamento(db.Entity):
    valor = Required(float)
    data = Required(date)
    aluno = Required(Aluno, column='aluno_id')
    observacao = Optional(str, nullable=True)
    def __str__(self):
        return f"Pagamento de {self.valor} em {self.data} para {self.aluno.nome}"

db.bind(provider='sqlite', filename='students.db', create_db=True)
db.generate_mapping(create_tables=True)

with db_session:
    # Criando um aluno
    aluno1 = Aluno(nome="João Silva", email="jo@gmail.com")
    aluno2 = Aluno(nome="Maria Souza", email="ma@gmail.com")
    commit()
    # Adicionando pagamentos para o aluno1
    pagamento1 = Pagamento(valor=150.0, data=date(2023, 1, 15), aluno=aluno1, observacao="Mensalidade Janeiro")
    pagamento2 = Pagamento(valor=150.0, data=date(2023, 2, 15), aluno=aluno1, observacao="Mensalidade Fevereiro")
    # Adicionando pagamento para o aluno2
    pagamento3 = Pagamento(valor=200.0, data=date(2023, 1, 20), aluno=aluno2, observacao="Mensalidade Janeiro")
    commit()
    # Consultando alunos e seus pagamentos
    alunos = select(a for a in Aluno)[:]
    for aluno in alunos:
        print(aluno)
        for pagamento in aluno.pagamentos:
            print(f"  - {pagamento}")
    
    # Consultando pagamentos e seus alunos
    pagamentos = select(p for p in Pagamento)[:]
    for pagamento in pagamentos:
        print(pagamento)
        print(f"  - Aluno: {pagamento.aluno.nome}, Email: {pagamento.aluno.email}")
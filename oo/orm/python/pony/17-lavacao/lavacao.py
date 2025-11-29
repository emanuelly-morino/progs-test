from pony.orm import *

db = Database()

class Pessoa(db.Entity):
    pessoa_id = PrimaryKey(int, auto=True)
    nome = Required(str)
    telefone = Required(str)
    cpf = Required(str)
    veiculos = Set('Veiculo')
    clientes = Set('Cliente')
    funcionarios = Set('Funcionario')
    
class Veiculo(db.Entity):
    veiculo_id = PrimaryKey(int, auto=True)
    modelo = Required(str)
    placa = Required(str)
    cor = Required(str)
    pessoa = Optional('Pessoa', nullable=True, default=None, column="pessoa_id")
    servicos = Set('Servico')

class Cliente(db.Entity):
    cliente_id = PrimaryKey(int, auto=True)
    pessoa = Required('Pessoa', column="pessoa_id")

class Cargo(db.Entity):
    cargo_id = PrimaryKey(int, auto=True)
    descricao = Required(str)
    funcionarios = Set('Funcionario')

class Funcionario(db.Entity):
    funcionario_id = PrimaryKey(int, auto=True)
    cargo = Required('Cargo', column="cargo_id")
    pessoa = Required('Pessoa', column="pessoa_id")
    operacoes = Set('Operacao')

class TipoServico(db.Entity):
    tipo_servico_id = PrimaryKey(int, auto=True)
    descricao = Required(str)
    operacoes = Set('Operacao')

class Servico(db.Entity):
    servico_id = PrimaryKey(int, auto=True)
    descricao = Required(str)
    veiculo = Required('Veiculo', column="veiculo_id")
    operacoes = Set('Operacao')

class Operacao(db.Entity):
    operacao_id = PrimaryKey(int, auto=True)
    servico = Required(Servico, column="servico_id")
    tipo_servico = Required("TipoServico", column="tipo_servico_id")
    funcionario = Required('Funcionario', column="funcionario_id")
    valor = Required(float)

    
db.bind(provider='sqlite', filename='lavacao.db', create_db=True)
db.generate_mapping(create_tables=True)

with db_session:

    # vamos popular o banco de dados
    if not Cargo.select().exists():
        cargos = ['Lavador', 'Atendente', 'Gerente']
        for descricao in cargos:
            Cargo(descricao=descricao)
    
    if not TipoServico.select().exists():
        tipos_servico = ['Lavagem Simples', 'Lavagem Completa', 'Polimento']
        for descricao in tipos_servico:
            TipoServico(descricao=descricao)

    # criar alguns funcionários de exemplo
    if not Funcionario.select().exists():
        pessoa1 = Pessoa(nome='João Silva', telefone='(11) 99999-9999', cpf='123.456.789-00')
        pessoa2 = Pessoa(nome='Maria Oliveira', telefone='(11) 98888-8888', cpf='987.654.321-00')
        cargo_lavador = Cargo.get(descricao='Lavador')
        cargo_atendente = Cargo.get(descricao='Atendente')
        lav1 = Funcionario(pessoa=pessoa1, cargo=cargo_lavador)
        at1 = Funcionario(pessoa=pessoa2, cargo=cargo_atendente)

    # criar clientes
    if not Cliente.select().exists():
        pessoa3 = Pessoa(nome='Carlos Pereira', telefone='(11) 97777-7777', cpf='111.222.333-44')
        cli1 = Cliente(pessoa=pessoa3)

    # criar veículos
    if not Veiculo.select().exists():
        Veiculo(modelo='Ford Fiesta', placa='ABC-1234', cor='Vermelho', pessoa=cli1.pessoa)
        Veiculo(modelo='Chevrolet Onix', placa='XYZ-5678', cor='Preto', pessoa=cli1.pessoa)

    # criar operações de serviço
    if not Operacao.select().exists():
        tipo_servico = TipoServico.get(descricao='Polimento')
        servico = Servico(descricao='Polimento do Ford Fiesta', veiculo=Veiculo.get(placa='ABC-1234'))
        Operacao(servico=servico, tipo_servico=tipo_servico, funcionario=lav1, valor=150.0 )
        # mais operações
        tipo_servico2 = TipoServico.get(descricao='Lavagem Completa')
        servico2 = Servico(descricao='Lavagem Completa do Chevrolet Onix',
                            veiculo=Veiculo.get(placa='XYZ-5678'))
        Operacao(servico=servico2, tipo_servico=tipo_servico2, funcionario=lav1, valor=100.0 )
        # outra operação
        tipo_servico3 = TipoServico.get(descricao='Lavagem Simples')
        servico3 = Servico(descricao='Lavagem Simples do Ford Fiesta',
                            veiculo=Veiculo.get(placa='ABC-1234'))
        Operacao(servico=servico3, tipo_servico=tipo_servico3, funcionario=lav1, valor=50.0 )

    # finaliza a transação  
    commit()
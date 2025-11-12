from pony.orm import db_session
from modelo import *

with db_session:
    # cria um cliente
    pessoa1 = Pessoa(nome="Ana Silva", email="anasilva@gmail.com")
    cliente1 = Cliente(pessoa=pessoa1, endereco="Rua A, 123")
    print(f"Cliente criado: {cliente1.pessoa.nome}, Email: {cliente1.pessoa.email}, Endereço: {cliente1.endereco}")
    
    # cria um técnico
    pessoa2 = Pessoa(nome="Carlos Souza", email="carlos@gmail.com")
    tecnico1 = Tecnico(pessoa=pessoa2)
    print(f"Técnico criado: {tecnico1.pessoa.nome}, Email: {tecnico1.pessoa.email}")
    
    # cria outro técnico
    pessoa3 = Pessoa(nome="Mariana Lima", email="malima@gmail.com")
    tecnico2 = Tecnico(pessoa=pessoa3)
    print(f"Técnico criado: {tecnico2.pessoa.nome}, Email: {tecnico2.pessoa.email}")

    # mais um técnico
    pessoa4 = Pessoa(nome="João Pedro", email="jope@gmail.com")
    tecnico3 = Tecnico(pessoa=pessoa4)
    print(f"Técnico criado: {tecnico3.pessoa.nome}, Email: {tecnico3.pessoa.email}")

    # cria um NOTEBOOK
    equipamento1 = Equipamento(nome="Notebook Dell", descricao="Notebook Dell Inspiron 1500")
    print(f"Equipamento criado: {equipamento1.nome}, Descrição: {equipamento1.descricao}")
    
    # serviços para o notebook
    servico1 = Servico(cliente=cliente1, equipamento=equipamento1, tecnico=tecnico1,
                       descricao="Troca de tela", preco=250.0)
    print(f"Serviço criado: {servico1.descricao}, Preço: {servico1.preco}, Técnico: {servico1.tecnico.pessoa.nome}")
    
    # cria um serviço sem técnico (técnico opcional)
    servico2 = Servico(cliente=cliente1, equipamento=equipamento1, tecnico=None,
                       descricao="Limpeza geral", preco=100.0, data_conclusao="2025-11-15")
    print(f"Serviço criado: {servico2.descricao}, Preço: {servico2.preco}, Técnico: {servico2.tecnico}")
    
    # cria outro serviço para o técnico 2
    servico3 = Servico(cliente=cliente1, equipamento=equipamento1, tecnico=tecnico2,
                       descricao="Troca de bateria", preco=150.0)
    print(f"Serviço criado: {servico3.descricao}, Preço: {servico3.preco}, Técnico: {servico3.tecnico.pessoa.nome}")

    # cria um SMARTPHONE (para o cliente 2)
    equipamento2 = Equipamento(nome="Smartphone Samsung", descricao="Samsung Galaxy S10")
    print(f"Equipamento criado: {equipamento2.nome}, Descrição: {equipamento2.descricao}")

    # um técnico virou cliente :-)
    cliente2 = Cliente(pessoa=tecnico3.pessoa, endereco="Rua B, 456")
    print(f"Cliente criado: {cliente2.pessoa.nome}, Email: {cliente2.pessoa.email}, Endereço: {cliente2.endereco}")

    # mais um serviço para o primeiro técnico
    servico4 = Servico(cliente=cliente2, equipamento=equipamento2, tecnico=tecnico1,
                       descricao="Atualização de software", preco=80.0, data_conclusao="2025-11-16")
    print(f"Serviço criado: {servico4.descricao}, Preço: {servico4.preco}, Técnico: {servico4.tecnico.pessoa.nome}")

    servico5 = Servico(cliente=cliente2, equipamento=equipamento2, tecnico=tecnico2,
                       descricao="Reparo de tela", preco=120.0)
    print(f"Serviço criado: {servico5.descricao}, Preço: {servico5.preco}, Técnico: {servico5.tecnico.pessoa.nome}")

    # outro equipamento; TABLET
    equipamento3 = Equipamento(nome="Tablet Apple", descricao="iPad Pro 11''")
    print(f"Equipamento criado: {equipamento3.nome}, Descrição: {equipamento3.descricao}")
    
    # criando um serviço para o terceiro equipamento
    servico6 = Servico(cliente=cliente2, equipamento=equipamento3, tecnico=tecnico1
                          , descricao="Substituição de tela", preco=300.0)
    print(f"Serviço criado: {servico6.descricao}, Preço: {servico6.preco}, Técnico: {servico6.tecnico.pessoa.nome}")

    # consulta serviços
    servicos = Servico.select()[:]
    for servico in servicos:
        tecnico_nome = servico.tecnico.pessoa.nome if servico.tecnico else "Sem técnico"
        print(f"Serviço: {servico.descricao}, Cliente: {servico.cliente.pessoa.nome}, Técnico: {tecnico_nome}, Preço: {servico.preco}")
from pony.orm import db_session
from modelo import *

with db_session:
    # Cria um autor
    joao = Pessoa(nome="João Silva", email="joao@email.com")
    maria = Pessoa(nome="Maria Souza", email="masouza@gmail.com")

    # Cria uma categoria
    doce= Categoria(nome="Sobremesa", descricao="Doces e sobremesas")
    pizza = Categoria(nome="Pizza", descricao="Pizzas de diversos sabores")
    salgadinho = Categoria(nome="Salgadinho", descricao="Salgadinhos para festas")    

    # Cria uma receita
    pudim = Receita(
        titulo="Pudim de Leite Condensado",
        descricao="Clássico pudim brasileiro",
        modo_preparo="Bata tudo, asse em banho-maria por 1 hora.",
        tempo_preparo=60,
        rendimento="8 porções",
        autor=joao,
        categoria=doce
    )

    # Cria ingredientes
    leite = Ingrediente(nome="Leite", unidade_padrao="ml")
    leite_condensado = Ingrediente(nome="Leite Condensado", unidade_padrao="lata")

    # Associa ingredientes à receita
    ItemIngrediente(receita=pudim, ingrediente=leite, quantidade=500)
    ItemIngrediente(receita=pudim, ingrediente=leite_condensado, quantidade=1)

    # Adiciona um comentário
    Comentario(pessoa=joao, receita=pudim, texto="Ficou ótimo!", data="2025-10-07", nota = 5)
    Comentario(pessoa=maria, receita=pudim, texto="Muito fácil de fazer.", data="2025-10-08", nota = 4)      

    # Cria outra receita
    calabresa = Receita(
        titulo="Pizza de Calabresa",
        descricao="Pizza sabor calabresa com cebola",
        modo_preparo="Prepare a massa, adicione molho, calabresa e cebola. Asse por 20 minutos.",
        tempo_preparo=90,
        rendimento="1 pizza grande",
        autor=maria,
        categoria=pizza
    )
    # Cria ingredientes
    calabresa_ing = Ingrediente(nome="Calabresa", unidade_padrao="g")
    cebola = Ingrediente(nome="Cebola", unidade_padrao="unidade")   
    molho = Ingrediente(nome="Molho de Tomate", unidade_padrao="ml")
    queijo = Ingrediente(nome="Queijo Mussarela", unidade_padrao="g")
    farinha = Ingrediente(nome="Farinha de Trigo", unidade_padrao="g")
    fermento = Ingrediente(nome="Fermento Biológico", unidade_padrao="g")
    agua = Ingrediente(nome="Água", unidade_padrao="ml")
    azeite = Ingrediente(nome="Azeite", unidade_padrao="ml")
    sal = Ingrediente(nome="Sal", unidade_padrao="g")
    acucar = Ingrediente(nome="Açúcar", unidade_padrao="g")

    # Associa ingredientes à receita
    ItemIngrediente(receita=calabresa, ingrediente=calabresa_ing, quantidade=200)
    ItemIngrediente(receita=calabresa, ingrediente=cebola, quantidade=1)
    ItemIngrediente(receita=calabresa, ingrediente=molho, quantidade=150)
    ItemIngrediente(receita=calabresa, ingrediente=queijo, quantidade=200)
    ItemIngrediente(receita=calabresa, ingrediente=farinha, quantidade=300)
    ItemIngrediente(receita=calabresa, ingrediente=fermento, quantidade=10)
    ItemIngrediente(receita=calabresa, ingrediente=agua, quantidade=180)
    ItemIngrediente(receita=calabresa, ingrediente=azeite, quantidade=20)
    ItemIngrediente(receita=calabresa, ingrediente=sal, quantidade=5)
    ItemIngrediente(receita=calabresa, ingrediente=acucar, quantidade=5)
    
    # Adiciona um comentário
    Comentario(pessoa=maria, receita=calabresa, texto="Deliciosa!", data="2025-10-09", nota = 5)    
    Comentario(pessoa=joao, receita=calabresa, texto="Use calabrasa não muito picante!", data="2025-10-10", nota = 3)

    # Cria outra receita
    coxinha = Receita(
        titulo="Coxinha de Frango",
        descricao="Coxinha crocante recheada com frango desfiado",
        modo_preparo="Prepare a massa, recheie com frango, modele em forma de coxinha e frite.",
        tempo_preparo=120,
        rendimento="20 unidades",
        autor=joao,
        categoria=salgadinho
    )
    
    # Cria ingredientes
    frango = Ingrediente(nome="Frango Desfiado", unidade_padrao="g")
    creme_leite = Ingrediente(nome="Creme de Leite", unidade_padrao="ml")
    caldo_galinha = Ingrediente(nome="Caldo de Galinha", unidade_padrao="g")
    manteiga = Ingrediente(nome="Manteiga", unidade_padrao="g")
    ovo = Ingrediente(nome="Ovo", unidade_padrao="unidade")
    farinha_milho = Ingrediente(nome="Farinha de Milho", unidade_padrao="g")
    pimenta = Ingrediente(nome="Pimenta do Reino", unidade_padrao="g")
    oleo = Ingrediente(nome="Óleo para Fritar", unidade_padrao="ml")
    farinha_roca = Ingrediente(nome="Farinha de Rosca", unidade_padrao="g")
    alho = Ingrediente(nome="Alho", unidade_padrao="dente")
    salsa = Ingrediente(nome="Salsa", unidade_padrao="g")
    
    # Associa ingredientes à receita
    ItemIngrediente(receita=coxinha, ingrediente=frango, quantidade=300)
    ItemIngrediente(receita=coxinha, ingrediente=creme_leite, quantidade=100)
    ItemIngrediente(receita=coxinha, ingrediente=caldo_galinha, quantidade=10)
    ItemIngrediente(receita=coxinha, ingrediente=manteiga, quantidade=50)
    ItemIngrediente(receita=coxinha, ingrediente=ovo, quantidade=2)
    ItemIngrediente(receita=coxinha, ingrediente=farinha_milho, quantidade=200)
    ItemIngrediente(receita=coxinha, ingrediente=farinha, quantidade=100)
    ItemIngrediente(receita=coxinha, ingrediente=leite, quantidade=300)
    ItemIngrediente(receita=coxinha, ingrediente=pimenta, quantidade=2)
    ItemIngrediente(receita=coxinha, ingrediente=oleo, quantidade=1000)
    ItemIngrediente(receita=coxinha, ingrediente=farinha_roca, quantidade=150)
    ItemIngrediente(receita=coxinha, ingrediente=cebola, quantidade=1)
    ItemIngrediente(receita=coxinha, ingrediente=alho, quantidade=2)
    ItemIngrediente(receita=coxinha, ingrediente=salsa, quantidade=10)
    ItemIngrediente(receita=coxinha, ingrediente=azeite, quantidade=20)
    ItemIngrediente(receita=coxinha, ingrediente=sal, quantidade=5)
    ItemIngrediente(receita=coxinha, ingrediente=acucar, quantidade=5)
    ItemIngrediente(receita=coxinha, ingrediente=fermento, quantidade=10)
    ItemIngrediente(receita=coxinha, ingrediente=agua, quantidade=200)
    ItemIngrediente(receita=coxinha, ingrediente=queijo, quantidade=100)   
    
    # Adiciona um comentário
    Comentario(pessoa=joao, receita=coxinha, texto="Perfeita para festas!", data="2025-10-11", nota = 5)    
    Comentario(pessoa=maria, receita=coxinha, texto="Sugiro usar menos óleo", data="2025-10-12", nota = 4) 

    # Consulta e imprime todas as receitas com seus ingredientes e comentários
    receitas = Receita.select()
    for r in receitas:
        print(f"\nReceita: {r.titulo} (Autor: {r.autor.nome}, Categoria: {r.categoria.nome if r.categoria else 'N/A'})")
        print("Ingredientes:")
        for item in r.ingredientes:
            print(f" - {item.quantidade} {item.unidade or item.ingrediente.unidade_padrao or ''} de {item.ingrediente.nome}")
        print("Comentários:")
        for c in r.comentarios:
            print(f" - {c.pessoa.nome} ({c.data}): {c.texto} - Nota: {c.nota if c.nota else 'N/A'}")

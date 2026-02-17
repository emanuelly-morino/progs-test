''' Estratégia: armazenar pessoas em uma lista.

Cada pessoa será uma lista com nome, email e telefone.

Exemplo:

pessoas = [
             ["Maria Oliveira", "ma@gmail.com", "3237-1234"],
             ["João Silva", "jo@gmail.com", "3237-4321"]
          ]

'''

print("Sistema de cadastro de pessoas")

# inicializa uma lista vazia
pessoas = []

while True:

    # exibir o menu de opções
    print("menu ---------------")
    print("1 - listar pessoas")
    print("2 - cadastrar pessoa")
    print("3 - sair")
    print("opção: ")

    # solicitar o que o usuário quer fazer
    op = input()

    if op == '1': # usuário deseja listar pessoas?
        print("Listagem de pessoas")
        for p in pessoas: # percorre a lista de pessoas
            
            # exibe os dados da pessoa
            print("=>", p[0], p[1], p[2])

    elif op == '2': # usuário quer cadastrar alguém?

        # solicita os dados
        nome = input("Nome: ")
        email = input("Email: ")
        telefone = input("Telefone: ")

        # cria a pessoa
        nova = [nome, email, telefone]

        # adiciona na lista
        pessoas.append(nova)
        print("A pessoa foi cadastrada.")

    elif op == '3': # encerrar o sistema?
        break # sai do while

    else: # usuário escolheu outra coisa?
        print("Opção inválida") # usuário cabeção
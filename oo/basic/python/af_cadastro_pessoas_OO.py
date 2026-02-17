''' Armazenar pessoas em uma lista.

Cada pessoa agora será um objeto da classe Pessoa.

'''

# definição da classe
class Pessoa:
    def __init__(self, nome, email, telefone):
        self.nome = nome
        self.email = email
        self.telefone = telefone

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
            print("=>", p.nome, p.email, p.telefone)

    elif op == '2': # usuário quer cadastrar alguém?

        # solicita os dados
        nome = input("Nome: ")
        email = input("Email: ")
        telefone = input("Telefone: ")
        
        # cria a pessoa
        nova = Pessoa(nome, email, telefone)

        # adiciona na lista
        pessoas.append(nova)
        print("A pessoa foi cadastrada.")

    elif op == '3': # encerrar o sistema?
        break # sai do while
    
    else: # usuário escolheu outra coisa?
        print("Opção inválida") # usuário cabeção
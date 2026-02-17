# definição da classe Pessoa
class Pessoa:
    def __init__(self, nome, email, telefone):
        self.nome = nome
        self.email = email
        self.telefone = telefone

# solicitar os dados
nome = input("Nome: ")
email = input("Email: ")
telefone = input("Telefone: ")
# criar a pessoa
nova = Pessoa(nome, email, telefone)
# exibir os dados
print(nova.nome, nova.email, nova.telefone)
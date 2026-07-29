class Pessoa:
    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        if len(novo_nome) >= 3: # não deixa criar um nome com menos que 3 caracteres
            self.__nome = novo_nome
        else:
            print(f"Nome inválido: {novo_nome}")

# TESTE

p = Pessoa("Carlos")

print(p.nome)

p.nome = "Ana"
print(p.nome)

p.nome = "Jo"
# definições das classes
class Pessoa:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
    def __str__(self):
        return f'''
                O nome da pessoa é : {self.nome}
                O email da pessoa é: {self.email}
                :-p
               '''
class Celular:
    def __init__(self, numero, marca, operadora, pessoa):
        self.numero = numero
        self.marca = marca
        self.operadora = operadora
        self.pessoa = pessoa
    def __str__(self):
        return f"{self.numero}, {self.marca}, {self.operadora}, {self.pessoa}"

# teste das classes
jo = Pessoa("Joao", "jo@gmail.com")
c1 = Celular("991234567", "Xioami", "Claro", jo)
#print(jo.nome, jo.email)
print(c1)
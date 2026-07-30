# definições das classes
class Pessoa:
    def __init__(self, id : int, nome : str, email : str):
        self.id = id
        self.nome = nome
        self.email = email
    def __str__(self):
        return f"(id:{self.id}), nome: {self.nome}, email: {self.email}"
    
class Celular:
    def __init__(self, id, numero : str, marca : str, operadora : str, pessoa : Pessoa):
        self.id = id
        self.numero = numero
        self.marca = marca
        self.operadora = operadora
        self.pessoa = pessoa
    def __str__(self):
        return f'''| Celular (id:{self.id}) da {self.marca}, operadora {self.operadora}, 
| número {self.numero}, dono => {self.pessoa}'''
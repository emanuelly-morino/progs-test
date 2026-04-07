from datetime import date

class Pessoa:
    def __init__(self, nome: str, telefone: str, data_nascimento: date):
        self.nome = nome
        self.telefone = telefone
        self.data_nascimento = data_nascimento
    def __str__(self):
        return f'''
        Nome: {self.nome}
        Telefone: {self.telefone}
        Data de nascimento: {self.data_nascimento}
        '''
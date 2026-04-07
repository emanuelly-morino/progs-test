from Pessoa import *

class Cliente:
    def __init__(self, pessoa: Pessoa, email: str):
        self.pessoa = pessoa
        self.email = email
    def __str__(self):
        return f'''
        Pessoa: {self.pessoa}
        Email: {self.email}
        '''
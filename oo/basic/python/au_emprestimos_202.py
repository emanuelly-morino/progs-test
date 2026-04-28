from datetime import date

class Pessoa:
    def __init__(self, nome, email):
        self.nome = nome
        self.idade = email

class Livro:
    def __init__(self, nome:str, autor:str, dono:Pessoa):
        self.nome = nome
        self.autor = autor
        self.dono = dono
    
class Emprestimo:
    def __init__(self, livro:Livro, pessoa:Pessoa, data_pegou:date):
        self.livro = livro
        self.pessoa = pessoa
        self.data_pegou = data_pegou

p1 = Pessoa("João", "jo@gmail.com")
liv1 = Livro("O Senhor dos Anéis", "J.R.R. Tolkien", p1)
p2 = Pessoa("Maria", "ma@gmail.com")
e1 = Emprestimo(liv1, p2, date(2024, 6, 1))

# nome do dono do livro emprestado
print(e1.livro.dono.nome)
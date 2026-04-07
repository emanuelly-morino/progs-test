class Servico:
    def __init__(self, descricao, valor):
        self.descricao = descricao
        self.valor = valor
    def __str__(self):
        return f'''
        Descrição do serviço: {self.descricao}
        Valor: {self.valor}
        '''

s1 = Servico("Troca de óleo", 50)
#print(s1.descricao, s1.valor)
print(s1)

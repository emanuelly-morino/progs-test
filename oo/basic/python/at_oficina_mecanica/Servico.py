class Servico:
    def __init__(self, descricao: str, valor: float):
        self.descricao = descricao
        self.valor = valor
    def __str__(self):
        return f'''
        Descrição do serviço: {self.descricao}
        Valor: {self.valor}
        '''
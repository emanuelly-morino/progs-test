class Receita:
    def __init__(self, nome, tempo_preparo, modo_preparo, ingredientes):
        self.nome = nome
        self.tempo_preparo = tempo_preparo
        self.modo_preparo = modo_preparo
        self.ingredientes = ingredientes
    # como expressar uma receita em formato textual        
    def __str__(self):
        # preparar uma versão string dos ingredientes
        x = ""
        # percorrer os ingredientes
        for ing in self.ingredientes:
            # concatena o ingrediente versão string em "x" (acumulador)
            x += str(ing)
        
        return f'''
        Receita: {self.nome}
        Tempo de preparo: {self.tempo_preparo} minutos
        Como preparar: {self.modo_preparo}
        Ingredientes: {x}
        '''

class Ingrediente:
    def __init__(self,nome, quantidade, unidade):
        self.nome=nome
        self.quantidade = quantidade
        self.unidade = unidade
    def __str__(self):
        return f'{self.quantidade} {self.unidade} de {self.nome}, '

# teste da classe

i1= Ingrediente("Milho", 1, "lata")
i2= Ingrediente("Leite", 1, "lata (milho)")
i3= Ingrediente("Açúcar", 1, "lata (milho)")
i4= Ingrediente("Ovos", 3, "unidades")
i5= Ingrediente("Óleo", 0.5, "lata (milho)")
i6= Ingrediente("Fermento", 1, "colher de chá")

r1 = Receita("Bolo de Milho", 50,
              "Bater tudo no liquidificador e colocar no forno",
              [i1, i2, i3, i4, i5, i6])    

print(r1)

'''
        Receita: Bolo de Milho
        Tempo de preparo: 50 minutos
        Como preparar: Bater tudo no liquidificador e colocar no forno
        
Milho 1 lata
Leite 1 lata
Açúcar 1 lata
Ovos 3 unidade
Óleo 0.5 lata
Fermento 1 colher de chá
'''
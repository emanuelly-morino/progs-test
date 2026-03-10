class Receita:
    def __init__(self, nome, tempo_preparo, modo_preparo, ingredientes):
        self.nome = nome
        self.tempo_preparo = tempo_preparo
        self.modo_preparo = modo_preparo
        self.ingredientes = ingredientes
    # como expressar uma receita em formato textual        
    def __str__(self):
        x = ""
        for ing in self.ingredientes:
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
        return f"\n{self.quantidade} {self.unidade} de {self.nome}"

# teste da classe

i1= Ingrediente("Milho", 1, "lata")
i2= Ingrediente("Leite", 1, "lata (milho)")
i3= Ingrediente("Açúcar", 0.5, "lata (milho)")
i4= Ingrediente("Ovos", 3, "unidade")
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
        Ingredientes: 
1 lata de Milho
1 lata (milho) de Leite
0.5 lata (milho) de Açúcar
3 unidade de Ovos
0.5 lata (milho) de Óleo
1 colher de chá de Fermento

'''
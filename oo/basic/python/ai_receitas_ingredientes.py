class Receita:
    def __init__(self, nome, tempo_preparo, modo_preparo):
        self.nome = nome
        self.tempo_preparo = tempo_preparo
        self.modo_preparo = modo_preparo
    # como expressar uma receita em formato textual        
    def __str__(self):
        return f'''
        Receita: {self.nome}
        Tempo de preparo: {self.tempo_preparo} minutos
        Como preparar: {self.modo_preparo}
        '''

class Ingrediente:
    def __init__(self,nome):
        self.nome=nome

class IngredienteDaReceita:
    def __init__(self, receita, ingrediente, quantidade, unidade):
        self.receita = receita
        self.ingrediente = ingrediente
        self.quantidade = quantidade
        self.unidade = unidade

# teste da classe

r1 = Receita("Bolo de Milho", 50,
              "Bater tudo no liquidificador e colocar no forno")    

i1= Ingrediente("Milho")
i2= Ingrediente("Leite")
i3= Ingrediente("Açúcar")
i4= Ingrediente("Ovos")
i5= Ingrediente("Óleo")
i6= Ingrediente("Fermento")

ir1 = IngredienteDaReceita(r1, i1, 1, "lata")
ir2 = IngredienteDaReceita(r1, i2, 1, "lata")
ir3 = IngredienteDaReceita(r1, i3, 1, "lata")
ir4 = IngredienteDaReceita(r1, i4, 3, "unidade")
ir5 = IngredienteDaReceita(r1, i5, 0.5, "lata")
ir6 = IngredienteDaReceita(r1, i6, 1, "colher de chá")

irs = [ir1, ir2, ir3, ir4, ir5, ir6]
print(r1) # .nome, r1.tempo_preparo, r1.modo_preparo)
#print(ir1, ir2, ir3, ir4, ir5, ir6)

for ir in irs:
    print(ir.ingrediente.nome, ir.quantidade, ir.unidade)

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
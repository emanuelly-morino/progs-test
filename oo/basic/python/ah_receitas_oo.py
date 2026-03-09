# definição da classe
class Receita:
    def __init__(self, nome, tempo_preparo, modo_preparo, ingredientes):
        self.nome = nome
        self.tempo_preparo = tempo_preparo
        self.modo_preparo = modo_preparo
        self.ingredientes = ingredientes

# teste da classe:

# partes 1 e 2: criar o objeto e colocar informações
r1 = Receita("Bolo de milho",
             50,
             "Bate no liquidificador a farinha, o milho, "+\
             "o leite, óleo e os ovos, até moer bem "+\
             "o milho. Acrescente o fermento e "+\
             "pulse o liquidificador 3 vezes. "+\
             "Despeje na forma e leve a forno"+\
             " por 50 minutos. Espere "+\
             " esfriar e sirva.",
             ['1 lata de milho',
              'leite (medida da lata)',
              'açúcar (medida da lata)',
              '3 ovos',
              '1 colher de fermento',
              '1/2 lata de óleo'])

# parte 3: mostrar os dados
print(r1.nome, r1.tempo_preparo, 
      r1.modo_preparo, r1.ingredientes)

'''
Bolo de milho 50 Bate no liquidificador a farinha, 
o milho, o leite, óleo e os ovos, 
até moer bem o milho. 
Acrescente o fermento e pulse o 
liquidificador 3 vezes. 
Despeje na forma e leve a 
forno por 50 minutos. 
Espere  esfriar e sirva. 
['1 lata de milho', 'leite (medida da lata)', 
'açúcar (medida da lata)', '3 ovos', 
'1 colher de fermento', '1/2 lata de óleo']
'''
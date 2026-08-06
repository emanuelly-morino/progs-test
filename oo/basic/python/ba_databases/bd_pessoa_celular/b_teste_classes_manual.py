from a_classes import *

# criando uma pessoa e um celular da pessoa
jo = Pessoa(1, "Joao", "jo@gmail.com")
c1 = Celular(1, "991234567", "Xioami", "Claro", jo)

print(c1)

# passando dados em forma de tupla 
# no comando fetchall os dados vem como lista de tuplas
dados_maria = (2, "Maria Oliveira","maliv@gmail.com")

# usamos operador ASTERISCO :-) 
# cada elemento da tupla será associado a um atributo
ma = Pessoa(*dados_maria)

print(ma)

# elaborando dados em forma de dicionário
dados_paulo = {"email": "paro@gmail.com",
               "id": 3, 
               "nome":"Paulo Rocha"  }

# usarmos operador DUPLO-ASTERICO :-) 
# cada nome será associado ao atributo
# observe que pode estar fora de ordem (no exemplo, ESTÁ)
pa = Pessoa(**dados_paulo)

print(pa)









# como seria sem usar * e **
# ma = Pessoa(dados_maria[0], dados_maria[1], dados_maria[2])
# pa = Pessoa(dados_paulo["id"], dados_paulo["nome"], dados_paulo["email"])
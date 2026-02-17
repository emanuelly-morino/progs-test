# calcular a área de um triângulo retângulo
# programa procedural

# anunciar o que o programa faz
print("CÁLCULO DA ÁREA DO TRIÂNGULO RETÂNGULO")

# pedir os lados do triângulo
base = input("Informe a base do triângulo (número inteiro maior que zero): ")
altura = input("Informe a altura do triângulo: ")

# converter strings para números
n_base = int(base)
n_altura = int(altura)

# calcular a área
area = (n_base * n_altura) / 2

# exibir a área
print("A área do triângulo é:", area)
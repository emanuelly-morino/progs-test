# calcular a área de um triângulo retângulo
# programa orientado a objeto

# definir a classe 
class Triangulo:
    # definir o construtor do objeto
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    # definir um método que calcula a área
    def area(self):
        return (self.base * self.altura) / 2

# anunciar o que o programa faz
print("CÁLCULO DA ÁREA DO TRIÂNGULO RETÂNGULO")

# pedir os lados do triângulo
base = input("Informe a base do triângulo (número inteiro maior que zero): ")
altura = input("Informe a altura do triângulo: ")

# converter strings para números
n_base = int(base)
n_altura = int(altura)

# criar um objeto
t1 = Triangulo(n_base, n_altura)        

# exibir a área
print("A área do triângulo é:", t1.area())
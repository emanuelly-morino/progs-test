import math

class Circulo:
    def area(self):
        return math.pi * 3 ** 2

class Quadrado:
    def area(self):
        return 4 ** 2

formas = [Circulo(), Quadrado()]

for forma in formas:
    print(forma.area())
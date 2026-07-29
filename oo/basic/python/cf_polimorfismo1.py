class Cachorro:
    def falar(self):
        return "Au au!"

class Gato:
    def falar(self):
        return "Miau!"

class Vaca:
    def falar(self):
        return "Muu!"

animais = [Cachorro(), Gato(), Vaca()]

for animal in animais:
    print(animal.falar())
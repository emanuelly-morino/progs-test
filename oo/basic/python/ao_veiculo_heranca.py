class Veiculo:
    def __init__(self, placa, cor):
        self.placa = placa
        self.cor = cor

class Carro(Veiculo):
    def __init__(self, placa, cor, portas):
        super().__init__(placa, cor)
        self.portas = portas

class Onibus(Veiculo):
    def __init__(self, placa, cor, lugares):
        super().__init__(placa, cor)
        self.lugares = lugares

# Criando um carro
meu_carro = Carro("ABC-1234", "Vermelho", 4)
print(f"Carro: Placa={meu_carro.placa}, Cor={meu_carro.cor}, Portas={meu_carro.portas}")    

# Criando um ônibus
meu_onibus = Onibus("XYZ-5678", "Azul", 40)
print(f"Ônibus: Placa={meu_onibus.placa}, Cor={meu_onibus.cor}, Lugares={meu_onibus.lugares}")
class Veiculo:
    def __init__(self, tipo, placa, cor, portas, lugares):
        self.tipo = tipo
        self.placa = placa
        self.cor = cor
        self.portas = portas
        self.lugares = lugares

# Criando um carro
meu_carro = Veiculo("Carro", "ABC-1234", "Vermelho", 4, 0)
print(f"Carro: Placa={meu_carro.placa}, Cor={meu_carro.cor}, Portas={meu_carro.portas}")

# Criando um ônibus
meu_onibus = Veiculo("Ônibus", "XYZ-5678", "Azul", 0, 40)
print(f"Ônibus: Placa={meu_onibus.placa}, Cor={meu_onibus.cor}, Lugares={meu_onibus.lugares}")


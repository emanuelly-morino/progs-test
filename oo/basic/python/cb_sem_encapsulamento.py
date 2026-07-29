class Conta:
    def __init__(self, saldo):
        self.saldo = saldo

conta = Conta(1000)

# Alteração direta
conta.saldo = -500

print(conta.saldo)
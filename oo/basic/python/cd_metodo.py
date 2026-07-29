class Conta:
    def __init__(self, saldo):
        self.__saldo = saldo

    def depositar(self, valor):
        if valor > 0: # regra de segurança
            self.__saldo += valor

    def sacar(self, valor):
        if valor <= self.__saldo: # regra de segurança
            self.__saldo -= valor
        else:
            print("Saldo insuficiente.")

    def mostrar_saldo(self):
        return self.__saldo

conta = Conta(1000)

print(f"Saldo inicial: {conta.mostrar_saldo()}")
conta.depositar(500)
print(f"Saldo depois de depositar 500: {conta.mostrar_saldo()}")
conta.sacar(200)
print(f"Saldo depois de sacar 200: {conta.mostrar_saldo()}")
conta.sacar(3000)
print(f"Saldo depois de tentar sacar 3000: {conta.mostrar_saldo()}")
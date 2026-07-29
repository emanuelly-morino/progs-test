class Conta:
    def __init__(self, saldo):
        # é possível acessar o atributo dentro da classe
        self.__saldo = saldo

    def mostrar_saldo(self):
        return self.__saldo

conta = Conta(1000)

print(conta.mostrar_saldo())

try:
    print(conta.__saldo)
except:
    print("Erro: não consegui acessar o saldo para mostrar")
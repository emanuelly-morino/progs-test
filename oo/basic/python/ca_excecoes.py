# 1. tratando o erro de divisão por zero

try:
    resultado = 10 / 0
    print(resultado)
except ZeroDivisionError:
    print("---> Erro: não é possível dividir por zero.")

# 2. tratando entrada inválida do usuário

try:
    usuario_digitou = "abc" # deveria ter digitado um número
    idade = int(usuario_digitou)
    print(f"Você tem {idade} anos.")
except ValueError:
    print("---> Erro: digite apenas números inteiros.")

# 3. capturando diferentes tipos de exceção

# tente digitar: 
# a) zero; 
# b) um número que não seja válido, que não seja possível de converter para inteiro

try:
    numero = int(input("Digite um número (NÃO digite zero ou letras): "))
    resultado = 100 / numero
    print(resultado)

except ValueError:
    print("Você deve digitar um número válido.")

except ZeroDivisionError:
    print("Não é possível dividir por zero.")

# 4. usando "else"

try:
    numero = int(input("Digite um número (se digitar número, vai ver o dobro): "))
except ValueError:
    print("Entrada inválida.")
else:
    print(f"O dobro de {numero} é: {numero * 2}")

# 5. usando "finally"

try:
    arquivo = open("dados.txt", "r")
    print(arquivo.read())
except FileNotFoundError:
    print("Arquivo não encontrado (crie um arquivo 'dados.txt')")
finally:
    print("Fim da execução, consegui abrir o arquivo e mostrar seu conteúdo.")

# 6. capturando um tipo de erro específico, e mostrando a mensagem de erro

try:
    lista = [10, 20, 30]
    print(lista[5])
except IndexError as erro:
    print(f"--->Ocorreu um erro: {erro}")

# será mostrado: "Ocorreu um erro: list index out of range"


# 7. capturando qualquer tipo de erro

try:
    x = int(input("Digite um número (pode zoar à vontade): "))
    print(10 / x)
except Exception as erro:
    print(f"Ocorreu um erro inesperado: {erro}")


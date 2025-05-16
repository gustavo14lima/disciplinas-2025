'''
Crie funções para:

    Somar dois números
    Subtrair dois números
    Multiplicar dois números
    Dividir dois números (com verificação de divisão por zero)

Crie um menu no programa principal que permita escolher a operação.
'''

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: Divisão por zero!"
    return a / b

while True:
    print("\nCalculadora:")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "5":
        print("Encerrando...")
        break

    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))

    if opcao == "1":
        print("Resultado:", somar(n1, n2))
    elif opcao == "2":
        print("Resultado:", subtrair(n1, n2))
    elif opcao == "3":
        print("Resultado:", multiplicar(n1, n2))
    elif opcao == "4":
        print("Resultado:", dividir(n1, n2))
    else:
        print("Opção inválida.")

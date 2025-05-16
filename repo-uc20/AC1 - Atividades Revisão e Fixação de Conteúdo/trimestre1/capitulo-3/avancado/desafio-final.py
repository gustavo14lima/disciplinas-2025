'''
Implemente:

    Saldo inicial: 100
    Menu com opções:
        1: Depositar valor
        2: Sacar valor
        3: Ver saldo
        0: Sair
    Trate exceções:
        Saque maior que saldo
        Entrada inválida

Use while com match/case e try/except.
'''

saldo = 100.0

while True:
    print("\nMenu Caixa Escolar\n1: Depositar valor\n2: Sacar valor\n3: Ver saldo\n0: Sair\n")
    opcao_usuario = input("Escolha uma opção: ")

    try:
        match opcao_usuario:
            case "1":
                valor = float(input("Digite o valor para depositar: "))
                saldo += valor
                print("Depósito realizado.")
            case "2":
                valor = float(input("Digite o valor para sacar: "))
                if valor > saldo:
                    print("Erro: saldo insuficiente.")
                else:
                    saldo -= valor
                    print("Saque realizado.")
            case "3":
                print("Saldo atual:", saldo)
            case "0":
                print("Saindo do sistema...")
                break
            case _:
                print("Opção inválida.")
    except ValueError:
        print("Preencha os campos corretamente!")
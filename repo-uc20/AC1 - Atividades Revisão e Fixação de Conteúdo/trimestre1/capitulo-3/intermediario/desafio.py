'''
Crie um menu com opções:

    Ver horário da aula
    Ver nome do professor
    Sair

    Use while para repetir até o usuário sair.
    Use if ou match para tratar as opções.

'''

while True:
    print("\nMenu:\n1 - Ver horário da aula\n2 - Ver nome do professor\n3 - Sair\n")

    opcao_usuario = input("Escolha uma opção: ")

    if opcao_usuario == "1":
        print("Horário da aula: 07:30 às 13:40")
    elif opcao_usuario == "2":
        print("Professor: André Ricardo")
    elif opcao_usuario == "3":
        print("Saindo...")
        break
    else:
        print("Opção inválida. Tente novamente.")

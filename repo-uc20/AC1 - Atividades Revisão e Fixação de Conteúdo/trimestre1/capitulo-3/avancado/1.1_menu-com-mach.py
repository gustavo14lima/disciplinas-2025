'''
Implemente um menu com as opções:

    1: Ver nome do professor
    2: Ver nome da turma
    3: Ver dia da aula
    0: Sair

Use match/case para tratar cada escolha.
'''

while True:
    print("\nMenu:\n1 - Ver nome do professor\n2 - Ver nome da turma\n3 - Ver dia da aula\n0 - Sair")
    opcao = input("Escolha uma opção: ")

    match opcao:
        case "1":
            print("Professor: André Ricardo")
        case "2":
            print("Turma: 3º Ano C")
        case "3":
            print("Dia da aula: Todos!")
        case "0":
            print("Saindo")
            break
        case _:
            print("Preencha os campos corretamente")
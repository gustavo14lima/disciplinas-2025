'''
1.2 Escolha de disciplina

Peça ao usuário a inicial da disciplina:

    p: Python
    r: Redes
    b: Banco de Dados
    Outra: "Opção inválida"
'''

inicial_disciplina = input("Digite a inicial da disciplina (p = Python / r = Redes / b = Banco de Dados): ").lower()

if inicial_disciplina == 'p':
    print("Python")
elif inicial_disciplina == 'r':
    print("Redes")
elif inicial_disciplina == 'b':
    print("Banco de Dados")
else:
    print("Preencha os campos corretamtente!")
'''
2.2 Cadastro com validação
Crie uma função cadastrar_aluno() que solicite nome e duas notas com input() e retorne os dados apenas se forem válidos.
'''

def cadastrar_aluno():
    nome = input("Nome: ")
    try:
        nota1 = float(input("Nota 1: "))
        nota2 = float(input("Nota 2: "))
        if 0 <= nota1 <= 10 and 0 <= nota2 <= 10:
            return [nome, nota1, nota2]
        else:
            print("Notas inválidas.")
            return None
    except ValueError:
        print("Erro: digite números válidos.")
        return None

aluno = cadastrar_aluno()
if aluno:
    print("Aluno cadastrado:", aluno)

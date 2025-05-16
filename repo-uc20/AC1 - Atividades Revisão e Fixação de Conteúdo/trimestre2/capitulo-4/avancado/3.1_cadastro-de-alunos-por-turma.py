'''
3.1 Cadastro de alunos por turma

    Crie três listas: turma_a, turma_b, turma_c
    Deixe o usuário cadastrar alunos e escolher em qual turma inserir.
    Exiba ao final:
        Quantos alunos em cada turma
        Nomes organizados por turma
'''

turma_a = []
turma_b = []
turma_c = []

for _ in range(5):
    nome = input("Nome do aluno: ")
    turma = input("Turma (A, B ou C): ").strip().upper()

    if turma == 'A':
        turma_a.append(nome)
    elif turma == 'B':
        turma_b.append(nome)
    elif turma == 'C':
        turma_c.append(nome)
    else:
        print("Turma inválida!")

print("\n📚 Resumo das Turmas:")
print(f"Turma A ({len(turma_a)}): {turma_a}")
print(f"Turma B ({len(turma_b)}): {turma_b}")
print(f"Turma C ({len(turma_c)}): {turma_c}")

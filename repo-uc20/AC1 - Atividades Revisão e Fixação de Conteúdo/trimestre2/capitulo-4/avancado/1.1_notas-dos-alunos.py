'''
1.1 Notas dos alunos

    Receba o nome e duas notas de 4 alunos.
    Armazene em uma lista de listas no formato: [nome, nota1, nota2]
    Exiba a média de cada aluno com nome.
'''

alunos = []

for i in range(4):
    nome = input(f"Nome do aluno {i+1}: ")
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    alunos.append([nome, nota1, nota2])

print("\nMédias dos alunos:")
for aluno in alunos:
    media = (aluno[1] + aluno[2]) / 2
    print(f"{aluno[0]} - Média: {media:.2f}")

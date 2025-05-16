'''
2.1 Filtro de notas altas

    Dada uma lista de alunos com nome e média, exiba somente os com média ≥ 7.
'''

alunos = [
    ["João", 8.5],
    ["Maria", 6.9],
    ["Pedro", 7.2],
    ["Ana", 5.8]
]

print("Alunos com média maior ou igual a 7:")
for aluno in alunos:
    if aluno[1] >= 7:
        print(f"{aluno[0]} - Média: {aluno[1]}")

'''
Implemente:

    Cadastro de alunos com nome e 3 notas
    Cálculo da média automática
    Armazenamento em lista de listas
    Exibição do boletim com:
        Nome | Nota1 | Nota2 | Nota3 | Média | Situação
    Filtros por situação:
        Aprovado (média ≥ 7)
        Recuperação (média entre 5 e 6.9)
        Reprovado (média < 5)
'''

alunos = []

for i in range(5):
    nome = input(f"Nome do aluno {i+1}: ")
    notas = []
    for j in range(3):
        nota = float(input(f"Nota {j+1}: "))
        notas.append(nota)
    media = sum(notas) / 3

    if media >= 7:
        situacao = "Aprovado"
    elif media >= 5:
        situacao = "Recuperação"
    else:
        situacao = "Reprovado"

    alunos.append([nome, *notas, media, situacao])

print("\n📋 Boletim Escolar:")
print("Nome       | Nota1 | Nota2 | Nota3 | Média | Situação")
print("-"*55)
for a in alunos:
    print(f"{a[0]:10} | {a[1]:5.1f} | {a[2]:5.1f} | {a[3]:5.1f} | {a[4]:5.1f} | {a[5]}")

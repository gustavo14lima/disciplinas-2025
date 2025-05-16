'''
Analisador de Notas

Crie um programa que:

    Receba o nome e 3 notas de 5 alunos.
    Armazene os nomes em uma lista e as médias em outra.
    Mostre:
        Aluno com maior média
        Quantos tiraram nota acima de 7
        A média geral da turma
'''

nomes = []
medias = []

for i in range(5):
    nome = input(f"Digite o nome do aluno {i+1}: ")
    notas = []
    for j in range(3):
        nota = float(input(f"Nota {j+1} de {nome}: "))
        notas.append(nota)
    
    media = sum(notas) / 3
    nomes.append(nome)
    medias.append(media)

maior_media = max(medias)
indice_maior = medias.index(maior_media)
aluno_maior_media = nomes[indice_maior]

acima_de_7 = sum(1 for m in medias if m > 7)

media_geral = sum(medias) / len(medias)

print("\n Resultados:")
print(f"Aluno com maior média: {aluno_maior_media} ({maior_media:.2f})")
print(f"Alunos com média acima de 7: {acima_de_7}")
print(f"Média geral da turma: {media_geral:.2f}")

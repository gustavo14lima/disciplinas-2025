'''
3.1 Média e Situação

Crie avaliar_aluno(n1, n2) que retorna:

    A média
    A situação como texto: "Aprovado", "Recuperação" ou "Reprovado"
'''

def avaliar_aluno(n1, n2):
    media = (n1 + n2) / 2
    if media >= 7:
        situacao = "Aprovado"
    elif media >= 5:
        situacao = "Recuperação"
    else:
        situacao = "Reprovado"
    return media, situacao

n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
media, status = avaliar_aluno(n1, n2)
print(f"Média: {media:.2f} | Situação: {status}")

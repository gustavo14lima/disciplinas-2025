'''
Peça duas notas, calcule a média e classifique:

    Média ≥ 7 → Aprovado
    Média entre 5 e 6.9 → Recuperação
    Média < 5 → Reprovado

'''

try:
    nota_1 = float(input('Digite a sua primeira nota: '))
    nota_2 = float(input('Digite a sua segunda nota: '))

    media = (nota_1 + nota_2) / 2

    if media < 5:
        print('Reprovado')
    elif media <= 6.9:
        print('Recuperação')
    else:
        print('Aprovado')
except ValueError:
    print('Preencha os campos corretamente!')
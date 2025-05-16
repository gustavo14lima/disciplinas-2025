'''
2.1 Classificação etária

Peça a idade do usuário e classifique:

    até 11: Criança
    12 a 17: Adolescente
    18 a 59: Adulto
    60+: Idoso
'''

try:
    idade_usuario = int(input('Digite a sua idade: '))

    if idade_usuario <= 11:
        print('Criança')
    elif idade_usuario <= 17:
        print('Adolescente')
    elif idade_usuario <= 59:
        print('Adulto')
    else:
        print('Idoso')

except ValueError:
    print('Preencha os campos corretamente!')
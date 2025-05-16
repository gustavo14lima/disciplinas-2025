'''
3.1 Comparações entre valores

Peça dois números e mostre:

    Se são iguais
    Qual é maior
    Se o primeiro é múltiplo do segundo
'''

try:
    valor1 = float(input('Digite o primeiro número: '))
    valor2 = float(input('Digite o segundo número: '))
    sao_iguais = False

    if valor1 == valor2:
        sao_iguais = True
        if sao_iguais:
            print('Os valores são iguais!')
    elif valor1 > valor2:
        print(f'O valor 1 ({valor1}) é maior')
    elif valor1 < valor2:
        print(f'O valor 2 ({valor2}) é maior')

    if valor1 % valor2 == 0:
        print('O primeiro número é múltiplo do segundo')
    else:
        print('O primeiro número não é múltiplo do segundo')

except ValueError:
    print('Preencha os campos corretamente!')
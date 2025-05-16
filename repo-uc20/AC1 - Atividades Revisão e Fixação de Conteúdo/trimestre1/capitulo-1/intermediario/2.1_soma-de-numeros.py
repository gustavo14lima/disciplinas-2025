'''
Peça dois números com input() e exiba a soma corretamente (converta com int() ou float()).
'''

try:
    numero1 = float(input('Digite o primeiro número: '))
    numero2 = float(input('Digite o segundo número: '))

    soma = numero1 + numero2

    print(f'A soma dos números {numero1} e {numero2} é {soma}')
except ValueError:
    print('Preencha os campos corretamente!')
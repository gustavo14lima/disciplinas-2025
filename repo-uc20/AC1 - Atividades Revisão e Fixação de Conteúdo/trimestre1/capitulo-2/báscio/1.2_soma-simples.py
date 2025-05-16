'''
1.2 Soma simples

Peça dois números e mostre:

    A soma
    O tipo do resultado com type()
'''

try:
    numero1 = float(input('Digite o primeiro número: '))
    numero2 = float(input('Digite o segundo número: '))

    soma = numero1 + numero2
    tipo_dado = type(soma)

    print(f'A soma dos número {numero1} e {numero2} é {soma}. E o seu tipo de dados é {tipo_dado}')
except ValueError:
    print('Preencha os campos corretamente!')
'''
3.2 Booleanos

    Crie expressões que resultem em True e False usando >, <, ==, !=
'''

try:
    numero_1 = int(input('Digite um número inteiro: '))
    numero_2 = int(input('Digite outro número inteiro: '))

    print(numero_1 > numero_2)
    print(numero_1 != numero_2)
    print(numero_1 == numero_2)
    print(numero_1 < numero_2)

except ValueError:
    print('Preencha os campos de dados corretamente!')
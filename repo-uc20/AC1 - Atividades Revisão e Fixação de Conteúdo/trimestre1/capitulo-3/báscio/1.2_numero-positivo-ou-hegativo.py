'''
1.2 Número positivo ou negativo
Peça um número e exiba se ele é positivo, negativo ou zero.
'''

try:
    numero_usuario = int(input('Digite um número inteiro: '))

    if numero_usuario > 0:
        print('Seu número é positivo!')
    elif numero_usuario == 0:
        print('Seu número é Zero!')
    else:
        print('Seu número é negativo...')
except ValueError:
    print('Preencha os campos corretamente!')
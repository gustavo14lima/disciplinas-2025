'''
2.1 Tabuada
Peça um número e mostre a tabuada de 1 a 10 usando for.
'''

try:
    numero_tabuada = int(input('Digite um número para descobrir sua tabuada: '))
    contador = 1

    for x in range(10):
        print(f'{numero_tabuada} * {contador} = {numero_tabuada * contador}\n')
        contador += 1
except ValueError:
    print('Preencha os campos corretamente!')
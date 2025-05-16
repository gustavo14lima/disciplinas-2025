'''
3.3 Reorganizando dados

    Crie uma lista com os números [3, 1, 4, 2]
    Ordene de forma crescente e depois decrescente.
    Inverta a ordem atual com .reverse()
'''

numeros = [3, 1, 4, 2]

numeros.sort()
print(f'Crescente: {numeros}')

numeros.sort(reverse=True)
print(f'Decrescente: {numeros}')

numeros.reverse()
print(f'Invertido: {numeros}')

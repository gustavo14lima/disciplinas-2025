'''
1.2 Caracteres e tamanho

Peça um nome e exiba:

    A primeira e última letra
    O total de letras com len()
'''

nome_usuario = input('Digite o seu nome: ')
primeira_letra = nome_usuario[0:1]
invertendo_letra = nome_usuario[::-1]
ultima_letra = invertendo_letra[0:1]

quantidade_letras = len(nome_usuario)

print(f'A primeira letra é {primeira_letra}', f'A última letra é {ultima_letra}', f'O total de letras é {quantidade_letras}', sep='\n')
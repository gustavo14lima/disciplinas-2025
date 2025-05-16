'''
3.1 Parar com break
Peça palavras em loop até que o usuário digite “sair”.
'''

while True:
    palavra_usuario = input('Digite palavras (digite "sair" para parar): ').lower()

    if palavra_usuario == 'sair':
        break
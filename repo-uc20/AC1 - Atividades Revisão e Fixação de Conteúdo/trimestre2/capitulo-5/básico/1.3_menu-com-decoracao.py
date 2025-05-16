'''
1.3 Menu com Decoração
Crie uma função menu() que recebe um texto e imprime uma "caixa" de título formatado com - em cima e embaixo.
'''

def menu():
    titulo = input("Digite o título do menu: ")
    largura = len(titulo) + 4 
    print('-' * largura)
    print(f'| {titulo} |')
    print('-' * largura)

menu()


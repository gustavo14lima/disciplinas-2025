'''
3.3 Título com parâmetro opcional
Crie a função titulo(texto, estilo='=') que imprima o texto com a linha de enfeite desejada.
'''

texto = input("Digite um título: ")
simbolo = input("Escolha um símbolo para enfeitar (Enter para usar '='): ")

def titulo(texto, estilo='='):
    print(estilo * len(texto))
    print(texto)
    print(estilo * len(texto))

if simbolo == "":
    titulo(texto)
else:
    titulo(texto, estilo=simbolo)

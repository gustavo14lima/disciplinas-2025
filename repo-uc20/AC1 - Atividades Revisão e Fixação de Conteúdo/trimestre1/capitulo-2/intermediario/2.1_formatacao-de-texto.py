'''
2.1 Formatação de texto

Peça um texto e aplique:

    .upper()
    .lower()
    .capitalize()
    .title()
'''

texto_usuario = input('Digite um texto: ')

texto_maiusculo = texto_usuario.upper()
texto_minusculo = texto_usuario.lower()
texto_capitalize = texto_usuario.capitalize()
primeiras_letras_maiusculas = texto_usuario.title()

print(texto_usuario)
print(texto_maiusculo)
print(texto_minusculo)
print(texto_capitalize)
print(primeiras_letras_maiusculas)
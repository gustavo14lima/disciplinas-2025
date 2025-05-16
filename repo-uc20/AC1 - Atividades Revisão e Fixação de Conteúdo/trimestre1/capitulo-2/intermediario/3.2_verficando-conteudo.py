'''
3.2 Verificando conteúdo

Peça uma string e use:

    .isdigit()
    .isalpha()
    .isalnum()
'''

texto_usuario = input('Digite um texto: ')

verficando_numero = 'Seu texto apresenta apenas números!' if texto_usuario.isdigit() else 'Seu texto não apresenta nenhum número'
verificando_letra = 'Seu texto apresenta apenas letras!' if texto_usuario.isalpha() else 'Seu texto não apresenta nenhuma letra'
verificando_misto = "Seu texto possui tanto letras quanto números!" if texto_usuario.isalnum() else 'Seu texto não tem nem letras e nem números...'

print(verficando_numero)
print(verificando_letra)
print(verificando_misto)
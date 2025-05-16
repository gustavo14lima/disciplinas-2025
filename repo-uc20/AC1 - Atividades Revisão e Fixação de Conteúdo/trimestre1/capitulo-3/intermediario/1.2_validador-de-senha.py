'''
1.2 Validador de senha

Peça uma senha até que o usuário digite “python123”. Ao acertar, exiba “Acesso liberado”.
'''

senha_correta = 'python123'
usuario_errou = True

while usuario_errou == True:
    palpite_usuario = input('Tente adivinhar a senha: ')

    if palpite_usuario == senha_correta:
        print('Acesso Liberado')
        usuario_errou = False
    else:
        print('Você errou... Tente novamente!')
        palpite_usuario
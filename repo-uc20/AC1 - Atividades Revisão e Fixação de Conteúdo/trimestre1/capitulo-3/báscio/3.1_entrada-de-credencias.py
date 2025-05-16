'''
3.1 Entrada de credenciais
Peça usuário e senha. Se forem iguais a “admin” e “1234”, exiba “Acesso liberado”.
'''

try:
    nome_usuario = input('Digite o seu nome de login: ')
    senha_usuario = int(input('Digite a sua senha de usuário: '))

    nome_db = 'admin'
    senha_db = 1234

    verificando_acesso = 'Acesso Liberado!' if nome_usuario == nome_db and senha_usuario == senha_db else 'Acesso Negado'

    print(verificando_acesso)
except ValueError:
    print('Preencha os campos corretamente!')
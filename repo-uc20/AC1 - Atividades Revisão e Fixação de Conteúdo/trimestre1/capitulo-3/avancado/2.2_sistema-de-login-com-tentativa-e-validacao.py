'''
2.2 Sistema de login com tentativa e validação

Implemente um sistema de login:

    Usuário: aluno
    Senha: uc20
    Três tentativas permitidas
'''

usuario_correto = "aluno"
senha_correta = "uc20"
tentativas = 0

while tentativas < 3:
    usuario = input("Digite o usuário: ")
    senha = input("Digite a senha: ")

    if usuario == usuario_correto and senha == senha_correta:
        print("Login bem-sucedido!")
        break
    else:
        print("Usuário ou senha incorretos.")
        tentativas += 1

    if tentativas == 3:
        print("Acesso bloqueado")
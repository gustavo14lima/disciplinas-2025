'''
3.3 Senhas limitadas
Dê 3 tentativas para o usuário digitar a senha correta. Se errar 3 vezes, mostre “Acesso bloqueado”.
'''

senha_correta = "1234"
tentativas = 0

while tentativas < 3:
    senha = input("Digite a senha: ")

    if senha == senha_correta:
        print("Acesso permitido")
        break
    else:
        print("Senha incorreta.")
        tentativas += 1

if tentativas == 3:
    print("Acesso bloqueado")
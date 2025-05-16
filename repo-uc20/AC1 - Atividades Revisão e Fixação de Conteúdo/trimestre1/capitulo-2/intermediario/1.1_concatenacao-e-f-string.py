'''
1.1 Concatenação e f-strings

Peça o nome completo do aluno e exiba:

    "Bem-vindo, [nome]!" usando +
    Refaça usando f-string
'''

nome_completo = input('Digite o seu nome completo: ')
saudacao_mais = 'Bem-vindo(a), ' + nome_completo + '!'
saudacao_fstring = f'Bem-vindo(a), {nome_completo}!'

print(saudacao_mais)
print(saudacao_fstring)
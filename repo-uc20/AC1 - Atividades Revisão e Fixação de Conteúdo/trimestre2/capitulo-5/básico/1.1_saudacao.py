'''
1.1 Saudação

Crie uma função saudacao() que recebe um nome como parâmetro e imprime:

Olá, [nome]! Bem-vindo(a) à aula de Python!
'''

nome = input('Digite o seu nome: ')

def saudacao(nome):
    print(f"Olá, {nome}! Bem-vindo(a) à aula de Python!")

saudacao(nome)
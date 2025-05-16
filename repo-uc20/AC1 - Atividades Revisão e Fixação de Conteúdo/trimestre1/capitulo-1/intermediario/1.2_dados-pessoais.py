'''
1.2 Dados pessoais

Solicite:

    Nome
    Idade
    Cidade

Exiba: Olá, [nome], você tem [idade] anos e mora em [cidade].
'''

try:
    nome_usuario = input('Digite o seu nome: ')
    idade_usuario = int(input('Digite a sua idade: '))
    cidade_usuario = input('Digite o nome da cidade: ')

    print(f'Olá, {nome_usuario}, você tem {idade_usuario} anos e mora em {cidade_usuario}')

except ValueError:
    print('Preencha os campos corretamente!')
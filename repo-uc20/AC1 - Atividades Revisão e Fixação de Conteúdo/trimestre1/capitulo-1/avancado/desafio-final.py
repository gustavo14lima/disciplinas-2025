'''
🧠 Desafio Final – Simulador de Abertura de Conta

Crie um programa que:

    Peça nome, idade, e valor inicial para uma conta
    Valide:
        Idade mínima: 16 anos
        Valor inicial ≥ R$ 50
    Exiba uma tela de confirmação personalizada
'''

try:
    nome_usuario = input('Digite o seu nome: ')
    idade_usuario = int(input('Digite sua idade: '))
    valor_inicial = float(input('Digite o valor inicial: '))

    if idade_usuario < 16 or valor_inicial < 50:
        print('Você não pode criar uma conta!')
    else:
        print(f'Conta criada! Bem-vindo(a) {nome_usuario}')

except ValueError:
    print('Preencha os campos corretamente!')
'''
2.2 Calculadora de idade
Peça o ano de nascimento e calcule a idade aproximada com base no ano atual.
'''

try:
    ano_nascimento = int(input('Digite o seu ano de nascimento: '))
    ano_atual = 2025

    idade_opcao1 = ano_atual - ano_nascimento
    idade_opcao2 = (ano_atual - 1) - ano_nascimento

    print(f'Você deve ter {idade_opcao1} anos ou {idade_opcao2} anos')
except ValueError:
    print('Preencha os campos corretamente!')
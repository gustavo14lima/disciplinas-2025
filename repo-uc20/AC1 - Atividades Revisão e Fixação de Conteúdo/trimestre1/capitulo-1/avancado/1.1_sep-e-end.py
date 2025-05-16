'''
1.1 sep e end

Use sep e end para criar uma saída como esta:

[João] | [Turma 3A] | [2025] 🌟
'''

try:
    nome_usuario = input('Digite o seu nome: ')
    turma_usuario = input('Digite sua turma (ex: 3C): ')
    ano_nascimento = int(input('Digite o ano em que você nasceu: '))

    print(f'{nome_usuario}', f'Turma {turma_usuario}', f'{ano_nascimento}', sep=' | ')
except ValueError:
    print('Preencha os campos corretamente!')
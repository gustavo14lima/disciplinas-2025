'''
3.1 Múltiplos valores com split()
Receba nome, idade e curso na mesma linha separados por vírgula. Exiba os dados separadamente.
'''

try:
    nome_usuario = input('Digite o seu nome: ')
    idade_usuario = int(input('Digite a sua idade: '))
    curso_usuario = input('Digite o seu curso: ')

    print(f'{nome_usuario}', f'{idade_usuario}', f'{curso_usuario}', sep=', ')

except ValueError:
    print('Preencha os campos corretamente!')

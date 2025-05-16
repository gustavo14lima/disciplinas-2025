'''
1.2 Multilinhas com estilo

Exiba informações formatadas como:

=====================
   Ficha do Aluno
=====================
Nome: Ana
Idade: 17
Curso: Python

Utilize f-strings e escape de caracteres (\n, \t).
'''

try:
    nome_usuario = input('Digite o seu nome: ')
    idade_usuario = int(input('Digite a sua idade: '))
    curo_usuario = input('Digite o seu curso: ')

    print(f'=====================', f'   Ficha do Aluno', f'=====================', sep='\n')
    print(f'Nome: {nome_usuario}', f'Idade: {idade_usuario}', f'Curso: {curo_usuario}', sep='\n')

except ValueError:
    print('Preencha os campos corretamente!')
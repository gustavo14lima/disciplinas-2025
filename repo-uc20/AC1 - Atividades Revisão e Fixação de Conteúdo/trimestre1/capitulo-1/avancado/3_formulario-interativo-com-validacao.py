'''
Crie um script cadastro_simples.py que:

    Peça:
        Nome
        Idade
        Curso
        Matrícula (número inteiro obrigatório)
    Valide todos os campos
    Exiba a ficha formatada se tudo for preenchido corretamente
'''

try:
    nome_usuario = input('Digite o seu nome: ')
    idade_usuario = int(input('Digite sua idade: '))
    curso = input('Digite o seu curso: ')
    matricula = int(input('Digite o número da sua matricula: '))

    if nome_usuario == '' or idade_usuario == '' or curso == '' or matricula == '':
        print('Preencha os campos corretamente!')
    else:
        print(f'Nome: {nome_usuario}', f'Idade: {idade_usuario}', f'Curso: {curso}', f'Matrícula: {matricula}', sep='\n')
except ValueError:
    print('Preencha os campos corretamente!')
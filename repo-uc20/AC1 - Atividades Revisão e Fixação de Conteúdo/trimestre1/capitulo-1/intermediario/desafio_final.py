'''
🧠 Desafio Final

Crie um script que simula o início de uma ficha escolar. Peça:

    Nome
    Turma
    3 notas

Exiba um pequeno resumo da ficha com as informações formatadas.
'''

try:
    nome_usuario = input('Digite o seu nome: ')
    turma_usuario = input('Digite sua turma (ex: 3°C): ')
    print('Me informe 3 notas')
    nota1 = float(input('Digite a nota 1: '))
    nota2 = float(input('Digite a nota 2: '))
    nota3 = float(input('Digite a nota 3: '))

    print(f'Nome: {nome_usuario}', f'Turma: {turma_usuario}', f'Notas:', f'{nota1}', f'{nota2}', f'{nota3}', sep='\n')

except ValueError:
    print('Preencha os campos corretamente!')

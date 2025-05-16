'''
3.2 Valores padrão
Peça o nome do aluno. Se ele não digitar nada, use “Aluno Anônimo” como valor padrão.
'''

nome_usuario = input('Digite o seu nome: ')

verificando_vazio = nome_usuario if nome_usuario != '' else 'Aluno Anônimo'

print(verificando_vazio)
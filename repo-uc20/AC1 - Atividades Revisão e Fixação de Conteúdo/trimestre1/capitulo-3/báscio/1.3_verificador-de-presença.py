'''
1.3 Verificador de presença
Peça se o aluno está presente (s ou n). Exiba “Presente” ou “Ausente”.
'''

aluno_presente = input('O aluno está presente? (responda com "s" para Sim e "n" para Não): ').lower()

if aluno_presente == 's':
    print('Presente!')
elif aluno_presente == 'n':
    print('Ausente!')
else:
    print('Preenche os campos corretamente!')
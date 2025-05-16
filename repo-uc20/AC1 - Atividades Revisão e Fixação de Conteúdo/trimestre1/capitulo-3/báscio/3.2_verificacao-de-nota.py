'''
3.2 Verificação de nota
Peça uma nota entre 0 e 10. Verifique se está dentro do intervalo com and. Se estiver fora, avise.
'''

try:
    nota_usuario = float(input('Digite sua nota: '))

    verificacao_nota = 'Está dentro do intervalo!' if nota_usuario >= 0 and nota_usuario <= 10 else 'Não está fora do intervalo..'

    print(verificacao_nota)
except ValueError:
    print('Preencha os campos corretamente!')
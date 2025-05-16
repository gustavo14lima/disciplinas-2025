'''
4.2 Montador de mensagem com **kwargs

Função mensagem(**info) que recebe qualquer quantidade de informações e imprime:

nome: João
idade: 17
turma: 3ºC
'''

def mensagem(**info):
    for chave, valor in info.items():
        print(f"{chave}: {valor}")

mensagem(nome="João", idade=17, turma="3ºC")

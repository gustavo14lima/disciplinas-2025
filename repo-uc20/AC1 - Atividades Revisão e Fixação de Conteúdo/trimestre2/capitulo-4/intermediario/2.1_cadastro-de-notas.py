'''
2.1 Cadastro de notas

    Peça ao usuário para inserir 5 notas e armazene em uma lista.
    Exiba a lista ao final.
'''

try:
    lista_usuario = input('Digite 5 notas, mas separadas por espaço: ').split()
    quantidade_nota = len(lista_usuario)

    if quantidade_nota < 5:
        print('Quantidade de notas insuficiente!')
    else:
        print(lista_usuario)

except ValueError:
    print('Preencha os campos corretamente!')
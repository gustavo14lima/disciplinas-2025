'''
2.1 Removendo elementos

    Use .remove() para retirar um nome da lista.
    Use .pop() para remover o último nome e mostre qual foi removido.
'''

lista_colegas = ['brunholi', 'kevin', 'faria', 'luiz', 'uchida']

lista_colegas.remove('uchida')
lista_colegas.pop(-1)

print(lista_colegas)
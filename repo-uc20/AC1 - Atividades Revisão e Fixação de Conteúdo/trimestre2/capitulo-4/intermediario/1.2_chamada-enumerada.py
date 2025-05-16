'''
1.2 Chamada enumerada

    Use enumerate() para exibir cada nome precedido por número de chamada.
'''

lista_colegas = ['brunholi', 'kevin', 'faria', 'luiz', 'uchida']

for i, nome in enumerate(lista_colegas, start=1):
    print(f"{i}. {nome}")
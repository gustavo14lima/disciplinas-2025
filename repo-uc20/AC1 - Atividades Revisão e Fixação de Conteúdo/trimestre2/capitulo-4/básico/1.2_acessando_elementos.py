'''
1.2 Acessando elementos

    Exiba o primeiro, o último e o terceiro elemento da lista.
    Tente acessar um índice inexistente e comente o erro.
'''

lista_colegas = ['brunholi', 'kevin', 'faria', 'luiz', 'uchida']

primeiro_elemnto = lista_colegas[0]
invertendo_lista = lista_colegas[::-1]
ultimo_elemento = invertendo_lista[0]
terceiro_elemento = lista_colegas[2]
'''
elemento_inexistente = lista_colegas[69]
    aconte um erro ao tentar acessar um índece inexistente, avisando que está fora do alcance
'''

print(primeiro_elemnto)
print(ultimo_elemento)
print(terceiro_elemento)
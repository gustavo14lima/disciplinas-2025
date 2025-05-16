'''
2.2 Contando e ordenando

    Crie uma lista com notas: [8, 5, 7, 10, 6, 5]
    Conte quantas vezes o número 5 aparece.
    Ordene a lista de forma crescente com .sort()
'''

lista_notas = [8, 5, 7, 10, 6, 5]
contagem_5 = 0
lista_notas.sort()

for x in lista_notas:
    if x == 5:
        contagem_5 += 1

print(contagem_5)
print(lista_notas)
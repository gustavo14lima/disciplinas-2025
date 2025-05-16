'''
2.2 Lista de presença

    Peça 5 nomes e armazene em uma lista.
    Em seguida, peça para digitar quais estiveram presentes.
    Crie duas listas: presentes e ausentes.
'''

lista_nomes = input('Digite uma lista com 5 nomes: ').split()
lista_nomes_presentes = input('Digite os nomes de quem estava presente: ').split()

lista_presentes = []
lista_ausentes = []

for nome in lista_nomes:
    if nome in lista_nomes_presentes:
        lista_presentes.append(nome)
    else:
        lista_ausentes.append(nome)

print("Presentes:", lista_presentes)
print("Ausentes:", lista_ausentes)
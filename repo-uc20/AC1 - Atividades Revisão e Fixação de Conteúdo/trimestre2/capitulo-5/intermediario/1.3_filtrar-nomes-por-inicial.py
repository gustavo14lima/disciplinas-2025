'''
1.3 Filtrar nomes por inicial
Crie uma função filtrar_por_letra(nomes, letra) que retorne apenas os nomes que começam com a letra dada (case insensitive).
'''

nomes = input("Digite os nomes separados por espaço: ").split()
letra = input("Filtrar por letra: ")

def filtrar_por_letra(nomes, letra):
    return [nome for nome in nomes if nome.lower().startswith(letra.lower())]

print("Nomes filtrados:", filtrar_por_letra(nomes, letra))

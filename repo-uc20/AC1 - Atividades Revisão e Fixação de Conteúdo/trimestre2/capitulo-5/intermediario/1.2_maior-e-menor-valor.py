'''
1.2 Maior e menor valor
Crie a função extremos(lista) que receba uma lista de números e retorne o menor e o maior valor.
'''

def extremos(lista):
    return min(lista), max(lista)
numeros = [int(input("Digite um número: ")) for _ in range(5)]
menor, maior = extremos(numeros)

print(f"Menor: {menor} | Maior: {maior}")

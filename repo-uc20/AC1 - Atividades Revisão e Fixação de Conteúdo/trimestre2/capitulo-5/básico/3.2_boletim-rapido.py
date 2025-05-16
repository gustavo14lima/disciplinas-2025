'''
3.2 Boletim Rápido
Crie uma função media_final(n1, n2) que calcule e retorne a média de duas notas.
'''

n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))

def media_final(n1, n2):
    return (n1 + n2) / 2

print(f"Média final: {media_final(n1, n2)}")

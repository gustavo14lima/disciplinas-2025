'''
4.1 Soma com *args
Função soma(*valores) que recebe qualquer quantidade de números e retorna a soma total.
'''

def soma(*valores):
    return sum(valores)

print("Digite quantos quiser. Digite 0 para parar.")
entradas = []
while True:
    n = float(input("Número: "))
    if n == 0:
        break
    entradas.append(n)

print("Soma total:", soma(*entradas))

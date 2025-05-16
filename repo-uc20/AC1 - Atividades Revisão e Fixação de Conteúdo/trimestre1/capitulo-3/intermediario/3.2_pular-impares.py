'''
3.2 Pular ímpares
Mostre os números de 1 a 10, mas pule os ímpares usando continue.
'''

for numero in range(1, 11):
    if numero % 2 != 0:
        continue 
    print(numero)

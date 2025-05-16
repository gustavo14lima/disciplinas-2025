'''
3.1 Convertendo tipos
Peça dois números como string, converta para int e float, e calcule a média.
'''

numero_1 = input('Digite o primeiro número: ')
numero_2 = input('Digite o segundo número: ')

conversao_int1 = int(numero_1)
conversao_int2 = int(numero_2)

conversao_float1 = float(numero_1)
conversao_float2 = float(numero_2)

media = (conversao_float1 + conversao_float2) / 2


print(f'Tipo de dado do número 1 = {type(numero_1)}')
print(f'Tipo de dado do número 1 convertido para inteiro = {type(conversao_int1)}')
print(f'Tipo de dado do número 1 convertido para decimal {type(conversao_float1)}')
print(f'Media dos número {media}')
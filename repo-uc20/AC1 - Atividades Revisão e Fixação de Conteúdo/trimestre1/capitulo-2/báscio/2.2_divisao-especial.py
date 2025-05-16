'''
2.2 Divisão especial

Com os mesmos dois valores:

    Divisão inteira //
    Resto da divisão %
    Potência **
'''

try:
    valor1 = float(input('Digite o primeiro número: '))
    valor2 = float(input('Digite o primeiro número: '))

    if valor1 == 0 or valor2 == 0:
        print('Não é possível fazer a divisão!')
    else:
        divisao_inteira = valor1 // valor2
        resto_divisao = valor1 % valor2
        print(divisao_inteira)
        print(resto_divisao)

    potencia = valor1 ** valor2
    print(potencia)

except ValueError:
    print('Preencha os campos corretamente!')
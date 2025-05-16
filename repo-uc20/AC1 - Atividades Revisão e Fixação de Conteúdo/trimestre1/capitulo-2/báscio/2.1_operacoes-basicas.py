'''
2.1 Operações básicas

Peça dois valores e mostre:

    Soma
    Subtração
    Multiplicação
    Divisão
'''

try:
    valor1 = float(input('Digite o primeiro número: '))
    valor2 = float(input('Digite o primeiro número: '))

    soma = valor1 + valor2
    subtracao = valor1 - valor1
    multiplicacao = valor1 * valor2

    print(soma)
    print(subtracao)
    print(multiplicacao)

    if valor1 == 0 or valor2 == 0:
        print('Não é possível fazer a divisão!')
    else:
        divisao = valor1 / valor2
        divisao_inteira = valor1 // valor2
        print(round(divisao, 2))
        print(divisao_inteira)

except ValueError:
    print('Preencha os campos corretamente!')
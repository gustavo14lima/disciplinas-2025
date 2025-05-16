'''
2.2 Calculadora simples
Peça dois números e a operação desejada (+, -, *, /) e calcule o resultado com base na escolha do usuário.
'''

try:
    numero_1 = float(input('Digite o primeiro número: '))
    numero_2 = float(input('Digite o segundo número: '))
    operacao = input('Escolha a operação desejada (+, -, *, /): ')

    soma = numero_1 + numero_2
    subtracao = numero_1 - numero_2
    multiplicacao = numero_1 * numero_2
    divisao = numero_1 / numero_2

    if operacao == '+':
        print(soma)
    elif operacao == '-':
        print(subtracao)
    elif operacao == '*':
        print(multiplicacao)
    elif operacao == '/':
        if numero_1 == 0 or numero_2 == 0:
            print('Não é possível realizar divisão por Zero!')
        else:
            print(divisao)
    else:
        print('Escolha a operação corretamente!')
except ValueError:
    print('Preencha os campos corretamente!')
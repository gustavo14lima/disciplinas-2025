'''
2.1 Conversão segura
Peça dois valores e exiba a soma. Use try/except para impedir erro se o usuário digitar letras.
'''

try:
    valor1 = int(input('Digite o primeiro valor: '))
    valor2 = int(input('Digite o segundo valor: '))

    soma = valor1 + valor2

    print(f'A soma dos valores {valor1} com o {valor2} é {soma}')

except ValueError:
    print('Preencha os campos corretamente!')
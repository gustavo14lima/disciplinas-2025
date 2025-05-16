'''
1.3 Fatiamento

Peça um CPF no formato "123.456.789-00" e mostre apenas:

    Os três primeiros números
    Os dois últimos
'''

cpf_usuario = input('Digite um CPF (ex: 123.456.789-00): ')

primeiros_numeros = cpf_usuario[0:3]
invertendo_cpf = cpf_usuario[::-1]
ultimos_numeros = invertendo_cpf[0:2]

print(f'Os três primeiros são: {primeiros_numeros}', f'Os últimos dois números é: {ultimos_numeros}')
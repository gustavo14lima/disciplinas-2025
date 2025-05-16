'''
1.3 Conversão entre tipos

    Converta um número decimal para inteiro com int()
    Converta um número para string com str() e exiba o tipo
'''

try:
    numero_decimal = float(input('Digite um número decimal: '))
    numero_inteiro = int(numero_decimal)
    convertendo_string = str(numero_inteiro)
    tipo_string = type(convertendo_string)

    print(f'O número decimal {numero_decimal}, foi convertido para número inteiro, ficando {numero_inteiro}. Agora, convertendo para string {convertendo_string}, seu tipo é {tipo_string}')
except ValueError:
    print('Preencha os campos corretamente!')
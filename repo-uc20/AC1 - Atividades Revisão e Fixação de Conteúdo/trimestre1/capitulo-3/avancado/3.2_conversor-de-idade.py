'''
3.2 Conversor de idade
Peça a idade. Converta para inteiro com int() e trate caso o usuário digite letras.
'''

try:
    idade = int(input("Digite sua idade: "))
    print(f'Sua idade é {idade}')
except ValueError:
    print('Preencha os campos corretamente!')
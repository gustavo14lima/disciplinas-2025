'''
1.1 Verificador de idade
Peça a idade do usuário. Se for maior ou igual a 18, exiba “Maior de idade”. Caso contrário, exiba “Menor de idade”.
'''

try:
    idade_usuario = int(input('Digite sua idade: '))

    verificador_idade = 'Maior de idade' if idade_usuario >= 18 else 'Menor de idade'

    print(verificador_idade)
except ValueError:
    print('Preencha os campos corretamente!')
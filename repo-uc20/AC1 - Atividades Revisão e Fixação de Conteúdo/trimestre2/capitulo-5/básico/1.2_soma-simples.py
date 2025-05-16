'''
1.2 Soma Simples
Crie uma função soma() que recebe dois números e retorna a soma.
'''

try:
    numero_1 = int(input('Digite o primeiro número: '))
    numero_2 = int(input('Digite o segundo número: '))

    def soma(numero_1, numero_2):
        return numero_1 + numero_2

    resultado = soma(numero_1, numero_2)
    print(f"Soma: {resultado}")

except ValueError:
    print('Preencha os campos corretamente!')

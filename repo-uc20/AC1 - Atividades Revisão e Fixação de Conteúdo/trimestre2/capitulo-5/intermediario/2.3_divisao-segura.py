'''
2.3 Divisão segura
Crie uma função dividir_seguro(a, b) que trate divisão por zero com try/except e retorne o resultado ou uma mensagem de erro.
'''

def dividir_seguro(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Erro: divisão por zero!"

a = float(input("Digite o numerador: "))
b = float(input("Digite o denominador: "))
print("Resultado:", dividir_seguro(a, b))

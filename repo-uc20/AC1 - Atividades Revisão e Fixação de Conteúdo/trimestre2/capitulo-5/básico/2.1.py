'''
Explique com comentários no código a diferença entre usar print() e return dentro de uma função.
'''

def mostrar_dobro(x):
    # print apenas exibe o resultado, não pode ser usado depois
    print(x * 2)

def calcular_dobro(x):
    # return devolve o resultado, que pode ser usado em outras operações
    return x * 2

mostrar_dobro(5)
resultado = calcular_dobro(5)
print(resultado + 10)

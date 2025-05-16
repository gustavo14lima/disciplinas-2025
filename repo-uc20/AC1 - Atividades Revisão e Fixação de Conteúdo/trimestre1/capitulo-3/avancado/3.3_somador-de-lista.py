'''
3.3 Somador de lista
Peça 5 números. Se algum for inválido, ignore com try/except e continue a soma.
'''

soma = 0

for x in range(5):
    try:
        numero_usuario = float(input(f"Digite o {x + 1}º número: "))
        soma += numero_usuario
    except ValueError:
        print("Preencha os campos corretamente!")

print(f'Soma total: {soma}')
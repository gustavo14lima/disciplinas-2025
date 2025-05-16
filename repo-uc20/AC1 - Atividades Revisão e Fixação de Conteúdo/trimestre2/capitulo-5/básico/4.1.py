a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))

def maior_valor(a, b):
    return a if a > b else b

print("Maior valor:", maior_valor(a, b))
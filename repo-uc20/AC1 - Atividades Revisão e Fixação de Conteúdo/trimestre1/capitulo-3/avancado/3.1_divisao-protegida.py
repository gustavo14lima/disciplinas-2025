'''
3.1 Divisão protegida

Peça dois números. Faça a divisão e:

    Trate ZeroDivisionError
    Trate ValueError para entrada inválida

'''

try:
    numero_1 = float(input("Digite o primeiro número: "))
    numero_2 = float(input("Digite o segundo número: "))

    resultado = numero_1 / numero_2

    print(resultado)
except ZeroDivisionError:
    print("Não é possivel fazer a divisão por zero.")
except ValueError:
    print("Preencha os campos corretamente!")
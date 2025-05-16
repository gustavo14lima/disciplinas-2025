'''
3.2 Removendo com segurança

    Crie uma lista com números de 1 a 5.
    Peça ao usuário um número para remover e verifique com in antes de aplicar .remove().
'''

numeros = [1, 2, 3, 4, 5]
remover = int(input("Digite um número para remover: "))

if remover in numeros:
    numeros.remove(remover)
    print(f"Número {remover} removido com sucesso.")
else:
    print("Número não encontrado na lista.")

print(f"Lista atual: {numeros}")

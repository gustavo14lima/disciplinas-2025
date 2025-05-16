'''
Crie um sistema com:

    Lista de produtos, cada um com nome, preço e quantidade
    Menu com opções:
        Adicionar produto
        Listar produtos
        Calcular valor total do estoque
    Use listas aninhadas ou listas de dicionários
'''

estoque = []

while True:
    print("\nMenu:")
    print("1 - Adicionar produto")
    print("2 - Listar produtos")
    print("3 - Calcular valor total")
    print("4 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome do produto: ")
        preco = float(input("Preço: "))
        quantidade = int(input("Quantidade: "))
        estoque.append([nome, preco, quantidade])

    elif opcao == "2":
        print("\nProdutos:")
        for produto in estoque:
            print(f"{produto[0]} - R${produto[1]:.2f} x {produto[2]}")

    elif opcao == "3":
        total = sum(prod[1] * prod[2] for prod in estoque)
        print(f"Valor total em estoque: R${total:.2f}")

    elif opcao == "4":
        break

    else:
        print("Opção inválida.")

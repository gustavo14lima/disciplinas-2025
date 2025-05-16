'''
Crie um programa com as funções:

    cadastrar_alunos() – cadastra n alunos com nome e média
    listar_alunos(lista) – exibe todos com posição e média
    filtrar_aprovados(lista) – exibe apenas os com média ≥ 7
    buscar_aluno(lista, nome) – retorna dados do aluno pesquisado

Utilize funções pequenas, bem organizadas e modulares.
'''

def cadastrar_alunos():
    lista = []
    qtd = int(input("Quantos alunos deseja cadastrar? "))
    for _ in range(qtd):
        nome = input("Nome: ")
        media = float(input("Média: "))
        lista.append([nome, media])
    return lista

def listar_alunos(lista):
    for i, aluno in enumerate(lista):
        print(f"{i+1}. {aluno[0]} - Média: {aluno[1]}")

def filtrar_aprovados(lista):
    print("Alunos aprovados:")
    for aluno in lista:
        if aluno[1] >= 7:
            print(f"{aluno[0]} - Média: {aluno[1]}")

def buscar_aluno(lista, nome):
    for aluno in lista:
        if aluno[0].lower() == nome.lower():
            return aluno
    return "Aluno não encontrado."

# Programa principal
alunos = cadastrar_alunos()
print("\nTodos os alunos:")
listar_alunos(alunos)

print("\nFiltrando aprovados:")
filtrar_aprovados(alunos)

nome_busca = input("\nDigite o nome de um aluno para buscar: ")
resultado = buscar_aluno(alunos, nome_busca)
print("Resultado:", resultado)

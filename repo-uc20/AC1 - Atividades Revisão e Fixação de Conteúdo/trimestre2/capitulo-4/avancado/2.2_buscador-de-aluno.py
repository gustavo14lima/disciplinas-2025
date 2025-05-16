'''
2.2 Buscador de aluno

    Permita ao usuário digitar um nome.
    Busque na lista e exiba os dados ou uma mensagem de "aluno não encontrado".
'''

alunos = [
    ["João", 8.5],
    ["Maria", 6.9],
    ["Pedro", 7.2],
    ["Ana", 5.8]
]

nome_busca = input("Digite o nome do aluno que deseja buscar: ")
encontrado = False

for aluno in alunos:
    if aluno[0].lower() == nome_busca.lower():
        print(f"{aluno[0]} - Média: {aluno[1]}")
        encontrado = True
        break

if not encontrado:
    print("Aluno não encontrado.")

'''
🔧 Projeto: Sistema de Gestão de Boletins

Crie um programa completo com menu interativo que permita ao usuário:

    Cadastrar alunos e notas
    Listar todos os alunos
    Gerar boletim com média e situação
    Buscar aluno por nome
    Excluir aluno
    Sair

🧩 Requisitos Técnicos
Funções obrigatórias:

    menu() → Exibe as opções disponíveis
    cadastrar_aluno(lista) → Recebe nome e 2 notas, armazena como sublista
    calcular_media(n1, n2) → Retorna média simples
    situacao(m) → Retorna situação textual com base na média
    listar_alunos(lista) → Mostra todos os alunos com notas e situação
    buscar_aluno(lista, nome) → Retorna as informações de um aluno específico
    excluir_aluno(lista, nome) → Remove aluno da lista
    salvar_em_arquivo(lista) → Exporta dados para um .txt ou .csv (bônus)

🔄 Regras de Implementação

    Use listas de listas: [ ['João', 8.0, 7.5], ... ]
    Crie um while principal com match/case
    Aplique tratamento de exceções com try/except onde necessário
    Organize o código com comentários e funções pequenas e reutilizáveis
    Utilize if __name__ == "__main__": para estrutura principal
'''

import csv

def menu():
    print("\n--- SISTEMA DE GESTÃO DE BOLETINS ---")
    print("1. Cadastrar aluno")
    print("2. Listar alunos")
    print("3. Gerar boletim")
    print("4. Buscar aluno por nome")
    print("5. Excluir aluno")
    print("6. Salvar em arquivo")
    print("7. Sair")
    return input("Escolha uma opção: ")

def cadastrar_aluno(lista):
    nome = input("Nome do aluno: ")
    try:
        nota1 = float(input("Nota 1: "))
        nota2 = float(input("Nota 2: "))
        if 0 <= nota1 <= 10 and 0 <= nota2 <= 10:
            lista.append([nome, nota1, nota2])
            print("Aluno cadastrado com sucesso.")
        else:
            print("Notas devem ser entre 0 e 10.")
    except ValueError:
        print("❌ Entrada inválida. Use números nas notas.")

def calcular_media(n1, n2):
    return (n1 + n2) / 2

def situacao(media):
    if media >= 7:
        return "Aprovado"
    elif media >= 5:
        return "Recuperação"
    else:
        return "Reprovado"

def listar_alunos(lista):
    if not lista:
        print("Nenhum aluno cadastrado.")
        return
    print("\n--- LISTA DE ALUNOS ---")
    for aluno in lista:
        media = calcular_media(aluno[1], aluno[2])
        status = situacao(media)
        print(f"Nome: {aluno[0]} | Nota1: {aluno[1]} | Nota2: {aluno[2]} | Média: {media:.1f} | Situação: {status}")

def buscar_aluno(lista, nome):
    for aluno in lista:
        if aluno[0].lower() == nome.lower():
            media = calcular_media(aluno[1], aluno[2])
            status = situacao(media)
            return f"Nome: {aluno[0]} | Nota1: {aluno[1]} | Nota2: {aluno[2]} | Média: {media:.1f} | Situação: {status}"
    return "❌ Aluno não encontrado."

def excluir_aluno(lista, nome):
    for i, aluno in enumerate(lista):
        if aluno[0].lower() == nome.lower():
            del lista[i]
            return "Aluno removido com sucesso."
    return "❌ Aluno não encontrado."

def salvar_em_arquivo(lista):
    try:
        with open("boletim.csv", "w", newline='') as arquivo:
            escritor = csv.writer(arquivo)
            escritor.writerow(["Nome", "Nota1", "Nota2", "Média", "Situação"])
            for aluno in lista:
                media = calcular_media(aluno[1], aluno[2])
                status = situacao(media)
                escritor.writerow([aluno[0], aluno[1], aluno[2], f"{media:.1f}", status])
        print("Dados salvos em 'boletim.csv'.")
    except Exception as e:
        print("❌ Erro ao salvar:", e)
if __name__ == "__main__":
    alunos = []

    while True:
        opcao = menu()

        match opcao:
            case "1":
                cadastrar_aluno(alunos)
            case "2":
                listar_alunos(alunos)
            case "3":
                listar_alunos(alunos)
            case "4":
                nome = input("Digite o nome do aluno: ")
                print(buscar_aluno(alunos, nome))
            case "5":
                nome = input("Nome do aluno a excluir: ")
                print(excluir_aluno(alunos, nome))
            case "6":
                salvar_em_arquivo(alunos)
            case "7":
                print("Encerrando o sistema. Até logo!")
                break
            case _:
                print("❌ Opção inválida.")

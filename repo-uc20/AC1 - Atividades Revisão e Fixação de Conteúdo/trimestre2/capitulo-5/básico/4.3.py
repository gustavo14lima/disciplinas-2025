nome = input("Digite seu nome: ")
hora = int(input("Digite a hora atual (0 a 23): "))

def saudacao_horario(nome, hora):
    if 6 <= hora < 12:
        saudacao = "Bom dia"
    elif 12 <= hora < 18:
        saudacao = "Boa tarde"
    else:
        saudacao = "Boa noite"
    print(f"{saudacao}, {nome}!")

saudacao_horario(nome, hora)

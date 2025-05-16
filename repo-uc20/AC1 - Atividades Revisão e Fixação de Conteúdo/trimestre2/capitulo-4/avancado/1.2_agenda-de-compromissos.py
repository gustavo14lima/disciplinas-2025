'''
1.2 Agenda de compromissos

    Cadastre 5 compromissos com data, hora e descrição.
    Armazene em uma lista de listas.
    Exiba em formato de agenda organizada.
'''

agenda = []

for i in range(5):
    data = input("Data (DD/MM): ")
    hora = input("Hora (HH:MM): ")
    descricao = input("Descrição: ")
    agenda.append([data, hora, descricao])

print("\nAgenda:")
for item in agenda:
    print(f"{item[0]} às {item[1]} - {item[2]}")

'''
2.1 Classificação com nota e presença

Peça nota e faltas. Aprovado se:

    Nota ≥ 7 e faltas ≤ 5
    Caso contrário, "Reprovado"

'''

nota = float(input("Digite a sua nota: "))
faltas = int(input("Digite o número de faltas: "))

if nota >= 7 and faltas <= 5:
    print("Aprovado")
else:
    print("Reprovado")
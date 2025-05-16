'''
1.1 Quantos alunos passaram?
Crie uma função contar_aprovados(lista) que receba uma lista de médias e retorne quantos alunos têm média ≥ 7.
'''

notas = [float(input(f"Nota do aluno {i+1}: ")) for i in range(5)]

def contar_aprovados(lista):
    return len([nota for nota in lista if nota >= 7])

# Entrada
print("Alunos aprovados:", contar_aprovados(notas))
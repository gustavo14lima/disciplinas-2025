'''
🧠 Desafio Final

Crie um script calculadora_notas.py que:

    Peça duas notas
    Calcule a média
    Verifique se a média é maior ou igual a 7
    Exiba True para aprovado, False para reprovado

Use operadores aritméticos e booleanos juntos.
'''

try:
    nota_1 = float(input('Digite a primeira nota: '))
    nota_2 = float(input('Digite a segunda nota: '))
    media = (nota_1 + nota_2) / 2
    aluno_aprovado = False

    if media >= 7:
        aluno_aprovado = True
    else:
        aluno_aprovado = False
    
    print(aluno_aprovado)


except ValueError:
    print('Preencha os campos corretamente!')
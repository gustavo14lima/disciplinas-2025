'''
1.3 Boletim com zip()

    Crie uma lista com 5 nomes e outra com 5 médias.
    Use zip() para mostrar o boletim:

Aluno: João | Média: 8.5
'''

lista_colegas = ['brunholi', 'kevin', 'faria', 'luiz', 'uchida']
lista_medias = [8, 9, 7, 7.5, 5]

for colegas, media in zip(lista_colegas, lista_medias):
    print(f"Aluno: {colegas}\t| Média: {media}")
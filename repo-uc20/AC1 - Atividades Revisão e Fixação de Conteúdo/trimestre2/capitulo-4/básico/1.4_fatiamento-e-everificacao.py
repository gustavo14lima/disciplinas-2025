'''
1.4 Fatiamento e verificação

    Exiba os 3 primeiros nomes usando fatiamento.
    Verifique se o nome "Ana" está presente na lista com in.
'''

lista_colegas = ['brunholi', 'kevin', 'faria', 'luiz', 'Ana']

tres_nomes = lista_colegas[0:3]

verificando_ana = 'O nome Ana está presente na lista!' if 'Ana' in lista_colegas else 'O nome Ana não está presente na lista'

print(tres_nomes)
print(verificando_ana)
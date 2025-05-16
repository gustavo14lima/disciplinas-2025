'''
3.2 Acesso e verificação

    Exiba a segunda fruta.
    Verifique se "banana" está presente na tupla.
'''

frutas = ('banana', 'abacaxi', 'maçã', 'uva verde')
exibindo_segunda = frutas[1]

verificando_banana = 'A fruta banana está presente!' if 'banana' in frutas else 'A fruta banana não está presente...'

print(exibindo_segunda)
print(verificando_banana)
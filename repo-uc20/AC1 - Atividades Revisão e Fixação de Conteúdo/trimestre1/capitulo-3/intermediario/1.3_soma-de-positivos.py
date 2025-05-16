'''
1.3 Soma de positivos
Solicite números até que o usuário digite 0. Some apenas os valores positivos digitados.
'''

try:
    usuario_errou = True
    soma_numeros = 0

    while usuario_errou:
        palpite_usuario = int(input('Digite um número natural: '))

        if palpite_usuario > 0:
            soma_numeros += palpite_usuario
        elif palpite_usuario == 0:
            print(f'Você acertou o número! A soma de todos os outros números positivos foram {soma_numeros}')
            usuario_errou = True

except ValueError:
    print('Preencha os campos corretamente!')
'''
🧠 Desafio Final – Normalizador de Texto

Peça ao usuário digitar uma frase. O script deve:

    Remover acentos (dica: use biblioteca unicodedata)
    Transformar para minúsculas
    Remover espaços extras
    Exibir a frase final limpa
'''

import unicodedata

frase_usuario = input('Digite uma frase: ')

frase_sem_acentos = ''.join(
        c for c in unicodedata.normalize('NFKD', frase_usuario)
        if not unicodedata.combining(c)
    )

frase_minuscula = frase_sem_acentos.lower()
separando_frase = frase_minuscula.split()
frase_limpa = ' '.join(separando_frase)

print(frase_limpa)

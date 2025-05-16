'''
2.2 Limpeza de dados
Receba uma frase com espaços extras e aplique .strip(), .replace() e .split().
'''

frase_usuario = input('Digite uma frase: ')
frase_strip = frase_usuario.strip()
frase_replace = frase_usuario.replace('  ', ' ')
frase_split = frase_usuario.split()

frase_perfeita = frase_strip.replace('  ', ' ')

print(f'Frase com strip: {frase_strip}')
print(f'Frase com replace: {frase_replace}')
print(f'Frase com split: {frase_split}')
print(f'Frase perfeita (strip + replace): {frase_perfeita}')
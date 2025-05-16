'''
3.2 Estatísticas de Lista
Função estatisticas(lista) que retorna: média, maior, menor e total de elementos.
'''

def estatisticas(lista):
    media = sum(lista) / len(lista)
    return media, max(lista), min(lista), len(lista)

valores = [float(input("Digite um número: ")) for _ in range(5)]
m, maior, menor, total = estatisticas(valores)
print(f"Média: {m:.2f} | Maior: {maior} | Menor: {menor} | Total: {total}")

'''
Desafio 🚀: Crie um segundo script que use listas e dicionários para montar um pequeno relatório de pacotes instalados (ex.: {"PyQt5": "x.y.z", "setuptools": "...", "wheel": "..."}) e imprima em formato organizado.
'''

import pkg_resources

def gerar_relatorio():
    pacotes_instalados = {}

    for distrib in pkg_resources.working_set:
        pacotes_instalados[distrib.project_name] = distrib.version

    print("Relatório de Pacotes Instalados:")
    print("-" * 40)

    for pacote, versao in pacotes_instalados.items():
        print(f"{pacote}: {versao}")

    print("-" * 40)
if __name__ == "__main__":
    gerar_relatorio()

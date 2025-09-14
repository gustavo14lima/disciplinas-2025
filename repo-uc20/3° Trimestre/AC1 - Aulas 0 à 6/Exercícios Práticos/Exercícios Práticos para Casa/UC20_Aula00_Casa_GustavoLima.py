'''
Gere um script que imprime:

    a versão do Python,
    a versão do pip (via python -m pip --version),
    a versão do PyQt5 (se instalado; caso contrário, exibir mensagem amigável).
'''

import sys
import subprocess

def verificar_versao_python():
    print(f"Versão do Python: {sys.version}")

def verificar_versao_pip():
    resultado = subprocess.run(['python', '-m', 'pip', '--version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if resultado.returncode == 0:
        print(f"Versão do pip: {resultado.stdout.strip()}")
    else:
        print("Erro ao verificar a versão do pip.")

def verificar_versao_pyqt5():
    resultado = subprocess.run(['python', '-m', 'pip', 'show', 'PyQt5'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    if resultado.returncode == 0:
        for line in resultado.stdout.splitlines():
            if line.startswith('Version:'):
                print(f"Versão do PyQt5: {line.split(' ')[1]}")
                break
    else:
        print("PyQt5 não está instalado. Por favor, instale-o com 'pip install PyQt5'.")

if __name__ == "__main__":
    verificar_versao_python()
    verificar_versao_pip()
    verificar_versao_pyqt5()

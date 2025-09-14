'''
Crie um script chamado teste_instalacao.py que:

    Importe o PyQt5.
    Crie uma janela com título "Instalação concluída com sucesso".
    Exiba a janela com tamanho 400x200.
'''

# Código 3
from PyQt5.QtWidgets import QApplication, QWidget
import sys

app = QApplication(sys.argv)
janela = QWidget()
janela.setWindowTitle("Instalação concluída com sucesso")
janela.resize(400, 200)
janela.show()
sys.exit(app.exec_())
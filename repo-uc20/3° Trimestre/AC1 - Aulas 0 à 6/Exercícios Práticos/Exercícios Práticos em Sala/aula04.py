'''
    Execute python3 --version e confirme que a versão é 3.12+.
    Verifique a versão do pip com python3 -m pip --version.
    Atualize o pip no seu ambiente.
    Instale o PyQt5 com o pip.
    Execute o Código 3 para abrir a janela de teste.
'''

# Código 3
from PyQt5.QtWidgets import QApplication, QWidget
import sys

app = QApplication(sys.argv)
janela = QWidget()
janela.setWindowTitle("Teste PyQt5 - Aula 04")
janela.resize(300, 150)
janela.show()
sys.exit(app.exec_())
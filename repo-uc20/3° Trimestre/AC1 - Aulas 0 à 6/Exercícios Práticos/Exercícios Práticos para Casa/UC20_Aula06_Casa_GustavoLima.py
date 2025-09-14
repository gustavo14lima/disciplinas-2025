'''
Criar revisao06.py mostrando três colegas (lista de strings) em QLabels numerados.
'''
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
import sys

colegas = ['Kevin', 'Luiz', 'Faria']

app = QApplication(sys.argv)
janela = QWidget()
janela.setWindowTitle("Aula 06 - Exercício Prático")
janela.resize(420, 240)

layout = QVBoxLayout()

rotulo_colegas = QLabel("Amigos:")
layout.addWidget(rotulo_colegas)

for i, colega in enumerate(colegas, start=1):
    layout.addWidget(QLabel(f"{i}) {colega}"))

janela.setLayout(layout)
janela.show()

sys.exit(app.exec_())

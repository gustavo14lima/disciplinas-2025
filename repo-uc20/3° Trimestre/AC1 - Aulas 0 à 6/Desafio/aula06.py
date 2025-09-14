'''
Desafio 🚀: Criar função que recebe (nome, turma, ano) e retorna string formatada exibida em um QLabel.
'''
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
import sys

def cabecalho_aluno(nome, turma, ano):
    return f"Aluno: {nome[0]} | Turma: {turma[2]} | Ano: {ano[2]}"

app = QApplication(sys.argv)
janela = QWidget()
janela.setWindowTitle("Desafio da aula 06")
janela.resize(420, 240)

nome = ['kevin', 'luiz', 'faria']
turma = ['3°A', '3°B', '3°C']
ano = [2023, 2024, 2025]

rotulo_aluno = QLabel(cabecalho_aluno(nome, turma, ano))

janela.setLayout(QVBoxLayout())
janela.layout().addWidget(rotulo_aluno)

janela.show()
sys.exit(app.exec_())

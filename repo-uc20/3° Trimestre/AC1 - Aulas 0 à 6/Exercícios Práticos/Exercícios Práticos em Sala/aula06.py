'''
    Ativar o venv e validar PyQt5 com pip show.
    Executar o Código 1 e confirmar a janela.
    Alterar os dados do dicionário aluno no Código 2.
'''

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
import sys

app = QApplication(sys.argv)

janela = QWidget()

materias = ["Português", "Matemática", "Informática"]
aluno = {"nome": "Luiz", "turma": "3ºC", "ano": 2025}

def cabecalho_aluno(d):
    nome = d.get("nome", "Sem nome")
    turma = d.get("turma", "Sem turma")
    ano = d.get("ano", "Sem ano")
    return f"Aluno: {nome} | Turma: {turma} | Ano: {ano}"

janela.setWindowTitle("Aula 06 - QLabel + Layout")
janela.resize(420, 240) 

rotulo_aluno = QLabel(cabecalho_aluno(aluno))
rotulo_titulo = QLabel("Matérias cadastradas:")

layout = QVBoxLayout()
layout.addWidget(rotulo_aluno)
layout.addWidget(rotulo_titulo)

for i, m in enumerate(materias, start=1):
    layout.addWidget(QLabel(f"{i}) {m}"))

janela.setLayout(layout)

janela.show()

sys.exit(app.exec_())

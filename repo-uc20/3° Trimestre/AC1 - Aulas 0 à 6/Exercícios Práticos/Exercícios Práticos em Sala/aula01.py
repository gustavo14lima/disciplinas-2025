'''
    Altere o título da janela para "UC20 - Aula 01".
    Mude a lista mensagens para conter 3 nomes de colegas. Mostre o segundo nome no QLabel.
    Crie uma função que receba um dicionário {"nome": "André", "turma": "3ºC"} e mostre os valores no QLabel.
'''

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
import sys

def main():
    app = QApplication(sys.argv)
    janela = QWidget()
    janela.setWindowTitle("UC20 - Aula 01")
    janela.resize(400, 200)

    mensagens = ["Kevin", "Luiz", "Faria"]
    dicionario = {"nome": "André", "turma": "3ºC"}

    def segundo_amigo(lista):
        return lista[1]

    rotulo = QLabel(segundo_amigo(mensagens))
    monstrando_dicionario = QLabel(f'Nome: {dicionario['nome']}\nTurma: {dicionario['turma']}')

    layout = QVBoxLayout()
    layout.addWidget(QLabel('O nome do segundo amigo é: '))
    layout.addWidget(rotulo)
    layout.addWidget(monstrando_dicionario)
    janela.setLayout(layout)

    janela.show()
    sys.exit(app.exec_())

main()
'''
Crie uma janela que mostre seu nome e idade, guardados em um dicionário.

    Exemplo: {"nome": "Ana", "idade": 17}
    Mostre os dois valores juntos em um QLabel.

'''

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
import sys

def main():
    app = QApplication(sys.argv)
    janela = QWidget()
    janela.setWindowTitle('Exercício Prático 01')
    janela.resize(500, 300)

    nome_idade = {'nome': 'Gustavo', 'idade': 17}

    exibindo_mensagem = QLabel(f"Nome: {nome_idade['nome']} {'\n'} Idade: {nome_idade['idade']} anos")

    layout = QVBoxLayout()
    layout.addWidget(exibindo_mensagem)
    janela.setLayout(layout)

    janela.show()
    sys.exit(app.exec_())

main()
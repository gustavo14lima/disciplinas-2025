'''
Desafio 🚀 Adapte o programa para mostrar a quantidade de caracteres do seu nome usando uma função Python.
'''

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
import sys

def main():
    app = QApplication(sys.argv)
    janela = QWidget()
    janela.setWindowTitle('Exercício Prático 01')
    janela.resize(500, 300)

    def quantidade_caracter(nome):
        return len(nome)

    nome_idade = {'nome': 'Gustavo', 'idade': 17}

    exibindo_mensagem = QLabel(f"Nome: {nome_idade['nome']} {'\n'} Idade: {nome_idade['idade']} anos {'\n'} Quantidade de caracteres no nome: {quantidade_caracter(nome_idade['nome'])}")

    layout = QVBoxLayout()
    layout.addWidget(exibindo_mensagem)
    janela.setLayout(layout)

    janela.show()
    sys.exit(app.exec_())

main()
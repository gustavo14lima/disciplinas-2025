'''
🏫 Exercícios Práticos em Sala (curtos e crescentes)
Nível 1

    No Diga Olá, ao invés de title(), faça o nome sair todo em maiúsculas com upper().
    No Contador, ao zerar, mude o rótulo para “Zerado! Comece de novo.”.

Nível 2

    No Diga Olá, se o nome tiver menos de 2 caracteres, exiba: “Nome muito curto”.
    No Contador, crie um botão “+5” que incremente 5 de uma vez (dica: estado["contador"] += 5).
'''

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout
import sys

estado = {"contador": 0}

def dizer_ola():
    nome = entrada_nome.text()
    if len(nome) < 2:
        lbl_ola.setText("Nome muito curto")
    else:
        lbl_ola.setText(f"OLÁ, {nome.upper()}!")

def incrementar():
    estado["contador"] += 1
    lbl_contador.setText(str(estado["contador"]))

def incrementar5():
    estado["contador"] += 5
    lbl_contador.setText(str(estado["contador"]))

def zerar():
    estado["contador"] = 0
    lbl_contador.setText("Zerado! Comece de novo.")

def main():
    global entrada_nome, lbl_ola, lbl_contador

    app = QApplication(sys.argv)
    janela = QWidget()
    janela.setWindowTitle("Exercícios Práticos")
    janela.resize(400, 300)


    entrada_nome = QLineEdit()
    entrada_nome.setPlaceholderText("Digite seu nome")
    btn_ola = QPushButton("Dizer Olá")
    btn_ola.clicked.connect(dizer_ola)
    lbl_ola = QLabel("Digite um nome e clique em Dizer Olá")


    lbl_contador = QLabel("0")

    btn_incrementar = QPushButton("+1")
    btn_incrementar.clicked.connect(incrementar)

    btn_incrementar5 = QPushButton("+5")
    btn_incrementar5.clicked.connect(incrementar5)

    btn_zerar = QPushButton("Zerar")
    btn_zerar.clicked.connect(zerar)


    layout = QVBoxLayout()


    layout.addWidget(entrada_nome)
    layout.addWidget(btn_ola)
    layout.addWidget(lbl_ola)


    layout.addWidget(lbl_contador)

    botoes_layout = QHBoxLayout()
    botoes_layout.addWidget(btn_incrementar)
    botoes_layout.addWidget(btn_incrementar5)
    botoes_layout.addWidget(btn_zerar)

    layout.addLayout(botoes_layout)

    janela.setLayout(layout)
    janela.show()
    sys.exit(app.exec_())

main()

'''
## ✅ Exercícios Práticos

1. Crie uma janela com **2 botões** e um **label**.

   - Quando o usuário clicar no **primeiro botão**, o texto deve mudar para "Primeiro botão clicado!".
   - Quando clicar no **segundo**, deve mudar para "Segundo botão clicado!".

2. Crie uma janela com:

   - Um campo de texto (`QLineEdit`)
   - Um botão
   - Um label que exibe o que foi digitado no campo após clicar no botão.

3. Desafie-se:s

   - Altere o layout do código acima para usar `QHBoxLayout` (horizontal).

---
'''

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout

class MinhaJanela(QWidget):
    def __init__(self):
        super().__init__()

        # Configurações da janela
        self.setWindowTitle("Exercício Prático - Aula 03")
        self.setGeometry(300, 200, 350, 200)

        # Widgets
        self.label = QLabel("Clique em um botão...")
        self.botao1 = QPushButton("Botão 1")
        self.botao2 = QPushButton("Botão 2")

        # Conectar eventos
        self.botao1.clicked.connect(self.clicou_botao1)
        self.botao2.clicked.connect(self.clicou_botao2)

        # Layout (vertical)
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.botao1)
        layout.addWidget(self.botao2)

        self.setLayout(layout)

    def clicou_botao1(self):
        self.label.setText("Primeiro botão clicado!")

    def clicou_botao2(self):
        self.label.setText("Segundo botão clicado!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = MinhaJanela()
    janela.show()
    sys.exit(app.exec_())

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout

class ContadorPlusMinus(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Contador + / -")
        self.setGeometry(200, 200, 300, 150)

        self.valor = 0

        # Layout principal
        layout = QVBoxLayout()

        # Label
        self.label = QLabel(f"Valor: {self.valor}")
        layout.addWidget(self.label)

        # Layout de botões
        botoes_layout = QHBoxLayout()

        self.botao_mais = QPushButton("+1")
        self.botao_menos = QPushButton("-1")
        self.botao_reset = QPushButton("Zerar")

        self.botao_mais.clicked.connect(self.incrementar)
        self.botao_menos.clicked.connect(self.decrementar)
        self.botao_reset.clicked.connect(self.zerar)

        botoes_layout.addWidget(self.botao_mais)
        botoes_layout.addWidget(self.botao_menos)
        botoes_layout.addWidget(self.botao_reset)

        layout.addLayout(botoes_layout)

        self.setLayout(layout)

    def incrementar(self):
        self.valor += 1
        self.label.setText(f"Valor: {self.valor}")

    def decrementar(self):
        if self.valor > 0:
            self.valor -= 1
        self.label.setText(f"Valor: {self.valor}")

    def zerar(self):
        self.valor = 0
        self.label.setText(f"Valor: {self.valor}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = ContadorPlusMinus()
    janela.show()
    sys.exit(app.exec_())


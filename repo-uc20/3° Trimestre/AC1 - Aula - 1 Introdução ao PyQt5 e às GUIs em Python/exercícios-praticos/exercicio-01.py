import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout

class OlaNome(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Olá, Nome!")

        # Widgets
        self.input_nome = QLineEdit()
        self.botao = QPushButton("Dizer Olá")
        self.label = QLabel("Digite seu nome e clique no botão")

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.input_nome)
        layout.addWidget(self.botao)
        layout.addWidget(self.label)
        self.setLayout(layout)

        # Conectar evento
        self.botao.clicked.connect(self.dizer_ola)

    def dizer_ola(self):
        nome = self.input_nome.text()
        self.label.setText(f"Olá, {nome}!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = OlaNome()
    janela.show()
    sys.exit(app.exec_())

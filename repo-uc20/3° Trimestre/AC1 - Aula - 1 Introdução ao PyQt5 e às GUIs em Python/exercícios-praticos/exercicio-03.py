import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout

class Contador(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Clique Contador")
        self.contagem = 0

        # Widgets
        self.label = QLabel("0")
        self.botao = QPushButton("Contar")

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.botao)
        self.setLayout(layout)

        # Evento
        self.botao.clicked.connect(self.incrementar)

    def incrementar(self):
        self.contagem += 1
        self.label.setText(str(self.contagem))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = Contador()
    janela.show()
    sys.exit(app.exec_())

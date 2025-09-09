import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout

class DuasMensagens(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Qual time você é?")

        # Widgets
        self.label = QLabel("Você é time:")
        self.botaoA = QPushButton("Labubu")
        self.botaoB = QPushButton("Bobbie Goods")

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.botaoA)
        layout.addWidget(self.botaoB)
        layout.addWidget(self.label)
        self.setLayout(layout)

        # Eventos
        self.botaoA.clicked.connect(self.mensagemA)
        self.botaoB.clicked.connect(self.mensagemB)

    def mensagemA(self):
        self.label.setText("Você é do time Labubu!!!")

    def mensagemB(self):
        self.label.setText("Você é do time Bobbie Goods!!!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = DuasMensagens()
    janela.show()
    sys.exit(app.exec_())

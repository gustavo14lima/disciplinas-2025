'''## ✅ Exercícios Práticos

1. **Dois Botões e um Texto**

   - Adicione dois botões à janela.
   - Um deve mudar o texto para "Primeiro botão clicado!".
   - O outro deve mudar para "Segundo botão clicado!".

2. **Layout Combinado**

   - Crie um layout **vertical**.
   - Dentro dele, adicione um layout **horizontal** com dois botões lado a lado.

3. **Escondendo Widgets**

   - Crie um botão que **esconde** o texto (`.hide()`).
   - Crie outro botão que **mostra** o texto novamente (`.show()`).

---'''

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout

class MinhaJanela(QWidget):
    def __init__(self):
        super().__init__()

        
        self.setWindowTitle("Exercício Prático - Aula 04")
        self.setGeometry(200, 200, 400, 250)

        self.label = QLabel("👋 Olá, PyQt5!")
        self.label.setAlignment(Qt.AlignCenter)
        
        self.botao1 = QPushButton("Botão 1")
        self.botao2 = QPushButton("Botão 2")
        
        self.botao_esconder = QPushButton("Esconder Texto")
        self.botao_mostrar = QPushButton("Mostrar Texto")
        
        self.botao1.clicked.connect(lambda: self.label.setText("Primeiro botão clicado!"))
        self.botao2.clicked.connect(lambda: self.label.setText("Segundo botão clicado!"))
        self.botao_esconder.clicked.connect(self.label.hide)
        self.botao_mostrar.clicked.connect(self.label.show)
        
        layout_horizontal = QHBoxLayout()
        layout_horizontal.addWidget(self.botao1)
        layout_horizontal.addWidget(self.botao2)
        
        layout_vertical = QVBoxLayout()
        layout_vertical.addWidget(self.label)
        layout_vertical.addLayout(layout_horizontal)  
        layout_vertical.addWidget(self.botao_esconder)
        layout_vertical.addWidget(self.botao_mostrar)
        
        self.setLayout(layout_vertical)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = MinhaJanela()
    janela.show()
    sys.exit(app.exec_())


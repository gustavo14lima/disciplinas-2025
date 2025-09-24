'''
---

## ✅ Exercícios Práticos

1. Crie uma janela com:

   - Um campo para digitar a idade.
   - Um botão que, ao clicar, exibe se o usuário é **maior ou menor de idade**.

2. Modifique o formulário acima para permitir **escolher mais de um curso**.

3. Crie uma janela com três checkboxes: **Python, Java, JavaScript**.

   - Ao clicar em um botão, exiba quais linguagens foram selecionadas.

---
'''

import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QLineEdit,
    QCheckBox, QVBoxLayout, QMessageBox
)

class Exercicios3(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Exercício 3 - Widgets Interativos")
        self.setGeometry(300, 200, 400, 350)

        self.label_idade = QLabel("Digite sua idade:")
        self.input_idade = QLineEdit()
        self.botao_idade = QPushButton("Verificar idade")
        self.botao_idade.clicked.connect(self.verificar_idade)

        self.label_cursos = QLabel("Escolha seus cursos:")
        self.checkbox_python = QCheckBox("Python")
        self.checkbox_java = QCheckBox("Java")
        self.checkbox_js = QCheckBox("JavaScript")
        self.botao_cursos = QPushButton("Mostrar cursos selecionados")
        self.botao_cursos.clicked.connect(self.mostrar_cursos)

        layout = QVBoxLayout()

        layout.addWidget(self.label_idade)
        layout.addWidget(self.input_idade)
        layout.addWidget(self.botao_idade)

        layout.addWidget(self.label_cursos)
        layout.addWidget(self.checkbox_python)
        layout.addWidget(self.checkbox_java)
        layout.addWidget(self.checkbox_js)
        layout.addWidget(self.botao_cursos)

        self.setLayout(layout)

    def verificar_idade(self):
        texto = self.input_idade.text()
        if texto.isdigit():
            idade = int(texto)
            if idade >= 18:
                QMessageBox.information(self, "Resultado", "Você é maior de idade!")
            else:
                QMessageBox.information(self, "Resultado", "Você é menor de idade!")
        else:
            QMessageBox.warning(self, "Erro", "Digite um número válido!")

    def mostrar_cursos(self):
        selecionados = []
        if self.checkbox_python.isChecked():
            selecionados.append("Python")
        if self.checkbox_java.isChecked():
            selecionados.append("Java")
        if self.checkbox_js.isChecked():
            selecionados.append("JavaScript")

        if selecionados:
            cursos_texto = ", ".join(selecionados)
            QMessageBox.information(self, "Cursos Selecionados", f"Você escolheu: {cursos_texto}")
        else:
            QMessageBox.information(self, "Cursos Selecionados", "Nenhum curso selecionado")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = Exercicios3()
    janela.show()
    sys.exit(app.exec_())

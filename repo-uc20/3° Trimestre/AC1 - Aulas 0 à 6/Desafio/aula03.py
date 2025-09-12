'''
Nível 3 (desafio rápido)

    Na Calculadora de Média, exiba também a maior e a menor nota (use max() e min()), cada uma em um QLabel.
'''

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
import sys

def main():
    app = QApplication(sys.argv)

    janela = QWidget()
    janela.setWindowTitle("Calculadora de Média - Nível 3")
    janela.resize(420, 260)

    instrucao = QLabel("Digite as notas separadas por vírgula (ex.: 7, 8, 6.5):")
    entrada = QLineEdit()
    saida_media = QLabel("Média: --")
    saida_maior = QLabel("Maior nota: --")
    saida_menor = QLabel("Menor nota: --")
    btn_calcular = QPushButton("Calcular")
    btn_limpar = QPushButton("Limpar")

    def parse_notas(texto):
        """Converte '7, 8, 6.5' em [7.0, 8.0, 6.5]."""
        partes = [p.strip() for p in texto.split(",")]
        notas = []
        for p in partes:
            if p == "":
                continue
            try:
                notas.append(float(p))
            except ValueError:
                return None
        return notas

    def calcular(checked=False):
        texto = entrada.text().strip()
        if not texto:
            saida_media.setText("Por favor, digite ao menos uma nota.")
            saida_maior.setText("Maior nota: --")
            saida_menor.setText("Menor nota: --")
            return

        notas = parse_notas(texto)
        if notas is None or len(notas) == 0:
            saida_media.setText("Entrada inválida. Use vírgulas e números (ex.: 7, 8, 6.5).")
            saida_maior.setText("Maior nota: --")
            saida_menor.setText("Menor nota: --")
            return

        media = sum(notas) / len(notas)
        maior = max(notas)
        menor = min(notas)

        saida_media.setText(f"Média: {media:.2f}")
        saida_maior.setText(f"Maior nota: {maior:.2f}")
        saida_menor.setText(f"Menor nota: {menor:.2f}")

    def limpar(checked=False):
        entrada.clear()
        saida_media.setText("Média: --")
        saida_maior.setText("Maior nota: --")
        saida_menor.setText("Menor nota: --")

    btn_calcular.clicked.connect(calcular)
    btn_limpar.clicked.connect(limpar)

    layout = QVBoxLayout()
    layout.addWidget(instrucao)
    layout.addWidget(entrada)
    layout.addWidget(btn_calcular)
    layout.addWidget(btn_limpar)
    layout.addWidget(saida_media)
    layout.addWidget(saida_maior)
    layout.addWidget(saida_menor)

    janela.setLayout(layout)
    janela.show()
    sys.exit(app.exec_())

main()

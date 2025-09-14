'''Escolha 1 obrigatório + 1 opcional

    Obrigatório – “Cadastro Rápido” Crie uma janela com:
        QLineEdit para Nome e Turma
        Botão “Gerar Mensagem”
        QLabel que exibe: Aluno: NOME | Turma: TURMA | Ano: 2025 Regras: usar funções para montar o texto e dicionário para organizar os dados.
    Opcional – “Média de 3 avaliações” Três QLineEdit (AC1, AC2, Prova). Calcular média ponderada (ex.: 3, 3, 4) e exibir resultado.
'''

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
import sys

def gerar_mensagem():
    dados = {
        "nome": entrada_nome.text(),
        "turma": entrada_turma.text(),
        "ano": 2025
    }
    texto = f"Aluno: {dados['nome']} | Turma: {dados['turma']} | Ano: {dados['ano']}"
    lbl_resultado.setText(texto)

def calcular_media():
    try:
        ac1 = float(entrada_ac1.text())
        ac2 = float(entrada_ac2.text())
        prova = float(entrada_prova.text())
        media = (ac1*3 + ac2*3 + prova*4) / 10
        lbl_media.setText(f"Média final: {media:.2f}")
    except ValueError:
        lbl_media.setText("Digite números válidos!")

def main():
    global entrada_nome, entrada_turma, lbl_resultado
    global entrada_ac1, entrada_ac2, entrada_prova, lbl_media

    app = QApplication(sys.argv)
    janela = QWidget()
    janela.setWindowTitle("Cadastro Rápido")
    janela.resize(400, 300)

    entrada_nome = QLineEdit()
    entrada_nome.setPlaceholderText("Digite o Nome")

    entrada_turma = QLineEdit()
    entrada_turma.setPlaceholderText("Digite a Turma")

    btn_gerar = QPushButton("Gerar Mensagem")
    btn_gerar.clicked.connect(gerar_mensagem)

    lbl_resultado = QLabel("Preencha os campos e clique em Gerar")

    entrada_ac1 = QLineEdit()
    entrada_ac1.setPlaceholderText("Nota AC1 (peso 3)")

    entrada_ac2 = QLineEdit()
    entrada_ac2.setPlaceholderText("Nota AC2 (peso 3)")

    entrada_prova = QLineEdit()
    entrada_prova.setPlaceholderText("Nota Prova (peso 4)")

    btn_media = QPushButton("Calcular Média")
    btn_media.clicked.connect(calcular_media)

    lbl_media = QLabel("")

    layout = QVBoxLayout()
    layout.addWidget(entrada_nome)
    layout.addWidget(entrada_turma)
    layout.addWidget(btn_gerar)
    layout.addWidget(lbl_resultado)

    layout.addWidget(entrada_ac1)
    layout.addWidget(entrada_ac2)
    layout.addWidget(entrada_prova)
    layout.addWidget(btn_media)
    layout.addWidget(lbl_media)

    janela.setLayout(layout)
    janela.show()
    sys.exit(app.exec_())

main()

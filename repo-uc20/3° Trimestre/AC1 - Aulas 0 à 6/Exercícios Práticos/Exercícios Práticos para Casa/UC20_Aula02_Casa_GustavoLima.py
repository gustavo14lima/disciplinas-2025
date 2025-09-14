'''
Crie uma janela com título "Meus Dados" que mostre:

    Seu nome (string simples).
    Sua turma (chave/valor de um dicionário).
    O ano atual (valor de uma variável).
'''


from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
import sys  

def main():
    app = QApplication(sys.argv)             
    janela = QWidget()                       
    janela.setWindowTitle("Meus Dados") 
    janela.resize(400, 200)                  

    nome = 'Gustavo Lima'
    turma = {'turma': '3° E.M C'}
    ano_atual = 2025

    exibindo_nome = QLabel(f'Meu nome é: {nome}')
    exibindo_turma = QLabel(f'Minha turma é: {turma['turma']}')
    exibindo_ano = QLabel(f'O ano atual é: {ano_atual}')

    
    layout = QVBoxLayout()
    layout.addWidget(exibindo_nome)
    layout.addWidget(exibindo_turma)
    layout.addWidget(exibindo_ano)
    janela.setLayout(layout)

    janela.show()                            
    sys.exit(app.exec_())                    

main()
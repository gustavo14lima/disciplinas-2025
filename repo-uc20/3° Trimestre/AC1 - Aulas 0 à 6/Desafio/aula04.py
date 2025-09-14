'''
Desafio 🚀 Crie um programa que mostre uma lista de matérias (mínimo 3) em QLabels, confirmando que o PyQt5 funciona com listas e layouts.
'''

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
import sys  

def main():
    app = QApplication(sys.argv)             
    janela = QWidget()                       
    janela.setWindowTitle("Instalação concluída com sucesso") 
    janela.resize(400, 200)                  
    
    layout = QVBoxLayout()

    lista_colegas = ['kevin', 'faria', 'luiz']

    for i in lista_colegas:
        layout.addWidget(QLabel(i))

    
    janela.setLayout(layout)

    janela.show()                            
    sys.exit(app.exec_())                    

main()
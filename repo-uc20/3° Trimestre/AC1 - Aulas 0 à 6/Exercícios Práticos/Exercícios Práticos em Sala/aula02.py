'''
    Altere o título da janela para "UC20 - Aula 02".
    Crie uma lista com 3 nomes de colegas e mostre o segundo nome em um QLabel.
    Crie um dicionário {"curso": "Informática", "ano": 2025} e mostre os valores em um QLabel.
'''

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
import sys  

def main():
    app = QApplication(sys.argv)             
    janela = QWidget()                       
    janela.setWindowTitle("UC20 - Aula 02") 
    janela.resize(400, 200)                  

    lista_colegas = ['kevin', 'faria', 'luiz']
    dicionario = {"curso": "Informática", "ano": 2025}

    def segundo_colega(lista):
        return lista[1]

    exibindo_colega = QLabel(segundo_colega(lista_colegas))
    exibindo_dicionario = QLabel(f'Curso: {dicionario['curso']}{'\n'}Ano: {dicionario['ano']}')

    
    layout = QVBoxLayout()
    layout.addWidget(exibindo_colega)
    layout.addWidget(exibindo_dicionario)
    janela.setLayout(layout)

    janela.show()                            
    sys.exit(app.exec_())                    

main()
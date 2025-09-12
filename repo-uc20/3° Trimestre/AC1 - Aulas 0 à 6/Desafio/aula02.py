'''
Desafio do Exercício Prático em Sala
Desafio extra 🚀: mostre a quantidade de caracteres do nome de um colega usando len().
------------------------------------------------------------------------------------------------------
Desafio do Exercício Prático em Casa
Adapte o programa para mostrar todos os nomes de uma lista de 5 colegas em rótulos (QLabel) separados.
'''

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
import sys  

def main():
    app = QApplication(sys.argv)             
    janela = QWidget()                       
    janela.setWindowTitle("UC20 - Aula 02") 
    janela.resize(400, 200)                  

    lista_colegas = ['kevin', 'faria', 'luiz', 'brunholi', 'gustavinhu']
    dicionario = {"curso": "Informática", "ano": 2025}

    layout = QVBoxLayout()

    def segundo_colega(lista):
        layout.addWidget(QLabel('------------------------------------------------------------------------------------------------------'))
        return lista[1]

    layout.addWidget(QLabel('Exibindo 5 colegas separadamente: '))
    for i in lista_colegas:
        layout.addWidget(QLabel(i))
    

    exibindo_colega = QLabel(segundo_colega(lista_colegas))
    exibindo_quantidade_caracter = QLabel(f'A quantidade de caracter do colega acima é: {len(segundo_colega(lista_colegas))}')
    exibindo_dicionario = QLabel(f'Curso: {dicionario['curso']}{'\n'}Ano: {dicionario['ano']}')

    
    layout.addWidget(exibindo_colega)
    layout.addWidget(exibindo_quantidade_caracter)
    layout.addWidget(exibindo_dicionario)
    janela.setLayout(layout)

    janela.show()                            
    sys.exit(app.exec_())                    

main()
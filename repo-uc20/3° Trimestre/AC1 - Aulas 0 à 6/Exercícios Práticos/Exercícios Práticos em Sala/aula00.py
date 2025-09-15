'''
Exercícios Práticos em Sala

Atualize o sistema e confirme python3 --version.

Instale python3-venv e crie ~/UC20/venv.

Ative o venv e atualize pip, setuptools e wheel.

Instale o PyQt5 e valide com:

python -c "import PyQt5; print(PyQt5.__version__)"
python -m pip show PyQt5

(Opcional) Rode o hello_pyqt.py e confirme a janela.
'''

from PyQt5.QtWidgets import QApplication, QLabel, QWidget
import sys

app = QApplication(sys.argv)
janela = QWidget()
janela.setWindowTitle("Hello PyQt5 - Aula 00")
janela.resize(400, 200)
rotulo = QLabel("Ambiente configurado com sucesso!", janela)
rotulo.move(60, 80)
janela.show()
sys.exit(app.exec_())
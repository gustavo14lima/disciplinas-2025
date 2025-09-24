# 🧠 Mapa Mental — PyQt5 (Aulas 03, 04 e 05)

## 🎨 Aula 03 — Fundamentos de uma Aplicação com Janela

- **Objetivos**

  - Entender o que é uma Windowed Application
  - Diferenciar Main Window x Widgets
  - Layouts (linhas e colunas)
  - Principais módulos do PyQt
  - Estrutura "Code Burger" 🍔
  - Criar primeira aplicação em PyQt5
- **Aplicação com Janela**

  - Main Window (janela principal)
  - Widgets (botões, labels, listas, inputs)
  - Metáfora do Jarro (janela contém tudo)
- **Widgets comuns**

  - Caixa de Texto
  - Checkbox
  - Botão
  - Lista
  - Label
- **Layouts**

  - Row → horizontal
  - Column → vertical
- **Módulos PyQt**

  - QtGui → gráficos, fontes
  - QtWidgets → botões, caixas, listas
  - QtCore → eventos, sinais
  - QtSql → bancos SQL
  - QtBluetooth → dispositivos Bluetooth
- **Code Burger**

  1. Imports
  2. Main App Objects
  3. Criação de Widgets
  4. Layout
  5. Aplicar Layout na Main Window
  6. Executar App

---

## 🖥️ Aula 04 — Conectando-se ao PyQt

- **Objetivos**

  - Importar módulos PyQt
  - Conhecer classes fundamentais
  - Métodos principais
  - Criar app funcional com botão e label
- **Imports**

  - QtCore (alinhamento, utilidades)
  - QtWidgets (elementos visuais)
- **Classes Fundamentais**

  - QApplication → motor do app
  - QWidget → janela principal
  - QLabel → exibe texto
  - QPushButton → botão
  - QVBoxLayout → vertical
  - QHBoxLayout → horizontal
- **Métodos Importantes**

  - `.addWidget()`
  - `.setText()`
  - `.addLayout()`
  - `.setLayout()`
  - `.show()`
  - `.hide()`

---

## 🧩 Aula 05 — Widgets Comuns no PyQt

- **Objetivos**

  - Conhecer widgets comuns
  - Criar formulário interativo
  - Usar eventos conectados a funções
- **Widgets**

  - QLineEdit → campo de texto
  - QCheckBox → caixa de seleção (sim/não)
  - QRadioButton → opção única
  - QListWidget → lista interativa
- **Exemplo Prático**

  - Nome (QLineEdit)
  - Aceitar termos (QCheckBox)
  - Gênero (QRadioButton)
  - Curso (QListWidget)
  - Botão Inscrever-se
  - `QMessageBox` → mensagens de aviso/sucesso
- **Eventos**

  - `.isChecked()` → checkboxes e radio
  - `.text()` → pega texto digitado
  - `.currentItem().text()` → item da lista selecionado
  - `.clicked.connect(func)` → liga ação a função

---

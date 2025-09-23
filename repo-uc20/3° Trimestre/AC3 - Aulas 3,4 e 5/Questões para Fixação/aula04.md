### Questão 1 – Dissertativa

Explique com suas palavras a diferença entre **QApplication** e **QWidget**.

    QApplication é a classe QApplication é fundamental para iniciar e controlar o ciclo de vida de um aplicativo PyQt. Ela é responsável por gerenciar a execução do aplicativo, incluindo a inicialização dos recursos gráficos e o loop de eventos que mantém a interface do usuário interativa. Sem a instância de QApplication, o aplicativo não funcionaria corretamente, pois ela serve como o "motor" do aplicativo.

    Agora, QWidget é a classe QWidget responsável por criar e gerenciar as interfaces gráficas, como janelas, botões, labels, e outros elementos visuais. Pode ser considerada como a base para todos os componentes visuais do PyQt. Quando criamos uma janela, por exemplo, usamos o QWidget (ou suas subclasses, como QMainWindow).

### Questão 2 – Múltipla Escolha

Qual método usamos para **adicionar um widget dentro de um layout**?

    ❌`.setText()`

   ❌  `.setLayout()`

   ✅  `.addWidget()`

   ❌  `.show()`

### Questão 3 – Associação

Associe os widgets com suas funções:

| Widget       | Função                         |
| ------------ | -------------------------------- |
| QLabel       | ( 2 ) Cria um botão clicável   |
| QPushButton  | ( 3 ) Inicializa e executa o app |
| QApplication | ( 1 ) Exibe texto na tela        |
| QWidget      | ( 4 ) Cria a janela principal    |

### Questão 4 – Verdadeiro ou Falso

1. `QApplication` é opcional para rodar um app em PyQt. **Falso**
2. `.setText()` serve para alterar dinamicamente o texto de um widget. **Verdadeiro**
3. `QVBoxLayout` organiza widgets na horizontal. **Falso**
4. `.hide()` pode ser usado para ocultar widgets temporariamente. **Verdadeiro**

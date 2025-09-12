## 📝 Exercícios Teóricos para Casa (fixação – diversos formatos)

**1. Múltipla escolha**
Em PyQt5, o método correto para **ligar** um clique de botão a uma função é:

* `❌ botao.clicked = funcao`
* ❌ `botao.connect(funcao)`
* ✅ `botao.clicked.connect(funcao)`
* ❌ `connect(botao.clicked, funcao)`

**2. Verdadeiro/Falso**
( V ) O `QLineEdit` serve para entrada de texto do usuário.
( V ) `setText()` atualiza o texto de um `QLabel`.
( F ) `clicked` é um *slot* e `connect` é um  *signal* .
( V ) `sys.argv` deve ser passado a `QApplication` por boas práticas.

**3. Associação** (coloque a letra correta)
A) `QLabel` — ( B ) Entrada de texto
B) `QLineEdit` — ( C ) Botão que dispara ação
C) `QPushButton` — ( A ) Exibe texto

**4. Dissertativa curta (5–8 linhas)**
Explique o que são **signals** e **slots** no PyQt5 e descreva, com suas palavras, o que acontece no código quando o usuário clica em um botão conectado a uma função.
	No PyQt5, signals e slots são mecanismos de comunicação entre objetos. Um signal é um evento disparado por um objeto, como o clique de um botão, enquanto um slot é uma função que reage a esse evento. Quando o usuário clica em um botão, o signal de clique é emitido. Se o botão estiver conectado a um slot, o PyQt5 executa a função associada a esse slot. Esse mecanismo permite que diferentes partes de uma aplicação se comuniquem de maneira eficiente e desacoplada, sem a necessidade de chamadas diretas entre os objetos.


## 📝 Exercícios Teóricos para Casa

1. **Múltipla escolha**
   Qual a principal função de um ambiente virtual em Python?

* ❌ Melhorar a velocidade do Python.
* ✅ Isolar pacotes e dependências.
* ❌ Atualizar o sistema operacional.
* ❌ Criar arquivos executáveis.

2. **Verdadeiro/Falso**
   ( V ) O venv evita conflitos de pacotes entre projetos.
   ( V ) O venv precisa ser ativado para instalar pacotes nele.
   ( F ) O venv substitui o Python global permanentemente.
   ( V ) O comando `deactivate` serve para sair do venv.
3. **Dissertativa**
   Explique com suas palavras por que  **cada projeto deve ter seu próprio venv** .
   	Cada projeto deve ter seu próprio venv porque assim é possível controlar as versões de bibliotecas utilizadas sem causar conflitos entre projetos diferentes. Por exemplo, um projeto pode precisar do Django 3.2 enquanto outro usa Django 5.0. Se usarmos apenas o Python global, essas versões entrariam em conflito. O venv cria um ambiente isolado, garantindo que cada projeto funcione de forma independente, organizado e estável.

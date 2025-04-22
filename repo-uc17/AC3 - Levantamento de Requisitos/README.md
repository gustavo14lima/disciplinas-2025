# 🏆 AC3 - Levantamento de Requisitos

## 📌 Objetivo

O objetivo desta atividade é realizar o levantamento e a documentação dos requisitos do projeto **EcoDescarte**, seguindo as etapas essenciais da **Especificação de Requisitos de Software (ERS)**. O levantamento será conduzido considerando o tema escolhido, com o intuito de garantir que as necessidades dos usuários e as funcionalidades do sistema estejam bem definidas e atendam aos objetivos do projeto.

---

## 📜 Instruções

### 📢 Etapa 1: Entendimento do Projeto

O projeto **EcoDescarte** tem como objetivo principal **reduzir a quantidade de lixo descartado de forma incorreta**, promovendo a conscientização ambiental e incentivando o descarte correto. Para isso, o sistema recompensará os usuários com **pontuação proporcional à quantidade e ao tipo de lixo descartado corretamente**.

O público-alvo inclui **cidadãos preocupados com o meio ambiente e a qualidade de vida nas cidades**, além de oferecer acessibilidade a **moradores em situação de rua**, que poderão utilizar o sistema como uma forma de obter pontos que eventualmente se convertam em benefícios, como acesso a alimentação, vestuário, entre outros itens básicos.

O projeto visa **melhorar o ambiente urbano**, promovendo:

- A redução da poluição visual, do solo, da água e do ar;
- A diminuição de alagamentos causados por entupimento de bueiros;
- A prevenção contra proliferação de pragas urbanas.

Com o uso do sistema, espera-se **estimular o comportamento sustentável**, facilitando o acesso a informações e locais corretos para o descarte de resíduos.

---

### 🗂 Etapa 2: Levantamento de Requisitos

Para identificar os problemas e as necessidades reais da área escolhida, será utilizado o método de **observação direta**, analisando o comportamento da população quanto ao descarte de resíduos e os impactos causados por esse hábito.

Com o avanço da sociedade e o crescimento urbano desordenado, muitos cidadãos passaram a **descartar resíduos de forma irresponsável**, o que resulta em sérios problemas ambientais e urbanos, como:

- Alagamentos frequentes;
- Degradação da paisagem urbana;
- Aumento de vetores de doenças;
- Prejuízos à saúde pública e ao bem-estar coletivo.

O levantamento de requisitos considera essas situações e propõe soluções por meio da **tecnologia** e do **engajamento da população**, utilizando recursos como sistemas de pontuação, geolocalização, estatísticas e relatórios.

## 📝 Documentação dos Requisitos - Projeto EcoDescarte

## 1️⃣ Especificação de Requisitos de Software (ERS)

### 📌 Introdução

O **EcoDescarte** é um sistema voltado à **redução do descarte incorreto de resíduos nas cidades**, promovendo educação ambiental por meio da **pontuação de usuários que realizarem o descarte correto**. O sistema também possibilita o acesso por pessoas em situação de rua, oferecendo uma forma de participação cidadã com possível retorno em benefícios sociais.

### 🎯 Escopo

O sistema permitirá:
- Cadastro e autenticação de usuários.
- Registro de tipos de resíduos descartados.
- Pontuação conforme tipo e quantidade de lixo descartado.
- Localização de pontos de descarte.
- Relatórios de contribuição ambiental.

---

### ✅ Requisitos Funcionais

- **RF001**: O sistema deve permitir o cadastro de usuários com nome e foto.
- **RF002**: O sistema deve oferecer autenticação via nome de usuário e senha.
- **RF003**: O sistema deve permitir o cadastro de usuários sem celular em dispositivos nos pontos de descarte.
- **RF004**: O sistema deve registrar o tipo, descrição e pontuação dos resíduos.
- **RF005**: O sistema deve localizar, em mapa, os pontos de descarte mais próximos com base na localização do usuário.

### 🛠️ Requisitos Não Funcionais

- **RNF001**: O sistema deve ser responsivo, com foco principal em dispositivos móveis.
- **RNF002**: O sistema deve funcionar nos principais navegadores (Chrome, Edge, Opera, Firefox).
- **RNF003**: O sistema deve ser compatível com a legislação ambiental e de proteção de dados.

---

### 📎 Regras de Negócio

- **RN001**: A pontuação do usuário será definida com base na quantidade e categoria do lixo descartado.
- **RN002**: Apenas pontos de coleta oficialmente cadastrados poderão registrar descartes válidos para pontuação.
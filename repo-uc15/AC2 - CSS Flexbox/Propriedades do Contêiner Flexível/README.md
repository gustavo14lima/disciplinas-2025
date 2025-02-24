`flex-direction`
    A propriedade CSS flex-direction define como os itens flexíveis são colocados no contêiner flexível, definindo o eixo principal (eixo X) e a direção (normal ou invertido). Ela pode mudar a ordem de exibição dos itens, podendo ser em linhas ou colunas (ambas invertidas ou normais)
    A seguir, explicarei todos os valores para a propriedade flex-direction:
        row: itens colocados em uma linha, do início para o fim (padrão).
        row-reverse: itens colocados em uma linha, mas com os valores invertidos, indo do fim para o início.
        column: itens colocados em uma coluna, de cima para baixo.
        column-reverse: itens colocados em uma coluna, mas com os valores invertidos, de baixo para cima.
`flex-wrap` 
    A propriedade CSS flex-wrap define se os itens flexíveis são forçados a ficarem na mesma linha ou se podem ser quebradas em varias linhas (pular de linha) com base no tamanho do contêiner e dos itens.
    Se a junção de todos os itens do contêiner for maior que o proprio contêiner, a propriedade flex-wrap decide se os itens vão para a proxima linha ou se eles vão estourar o limite do contêiner.
    A seguir, irei explicar os valores do atributo flex-wrap:
        nowrap: todos os itens ficam em uma única linha, mesmo se ultrapassar o tamanho do container.
        wrap: itens quebram em várias linhas, se os itens ultrapassar o tamanho do container, de cima para baixo.
        wrap-reverse: itens quebram em várias linhas, se os itens ultrapassar o tamanho do container, de baixo para cima.
`flex-flow`
    A propriedade CSS flex-flow é uma junção das propriedades flex-direction e flex-wrap.
    Ambas propriedades explicadas acima.
`justify-content`
    A propriedade CSS justificar-content define como o navegador distribui o espaço entre e ao redor dos itens de conteúdo ao longo do eixo principal (eixo X) de um contêiner flexível.
    A seguir, irei apresentar os valores da propriedade justify-content:
        flex-start: itens alinhados ao início do contêiner.
        flex-end: itens alinhados ao final do contêiner.
        center: itens centralizados no contêiner.
        space-between: espaço igual entre os itens.
        space-around: espaço igual ao redor de cada item.
`align-items` – Alinhamento vertical dos itens
    A propriedade CSS align-items estabelece o alinhamento de um certo item dentro do bloco que o contém. Em Flexbox ele controla o alinhamento dos itens em de acordo com o eixo transversal (eixo Y)
    A seguir, irei explicar todos os valores para a propriedade align-items:
        stretch: itens são esticados para preencher o contêiner (padrão).
        flex-start: itens alinhados ao início do eixo transversal (eixo Y).
        flex-end: itens alinhados ao final do eixo transversal (eixo Y).
        center: itens centralizados ao longo do eixo transversal (eixo Y).
        baseline: itens alinhados à linha de base de seus conteúdos.
`align-content` – Alinhamento em múltiplas linhas
    A propriedade CSS align-content define a distribuição entre e ao redor dos items do conteúdo do eixo transversal (eixo Y) de um contêiner.
    Agora, explicarei os valores para a propriedade align-content:
        lex-start: as linhas são agrupadas no início do contêiner.
        flex-end: as linhas são agrupadas no final do contêiner.
        center: as linhas são agrupadas no centro do contêiner.
        space-between: as linhas são distribuídas uniformemente, com o primeiro item no início e o último no final do contêiner.
        space-around: as linhas são distribuídas com espaçamento igual ao redor de cada linha.
        space-evenly: as linhas são distribuídas com espaçamento igual entre elas.
        stretch: as linhas se estendem para preencher o espaço disponível (valor padrão).

https://developer.mozilla.org/pt-BR/docs/Web/CSS/flex-direction
https://developer.mozilla.org/pt-BR/docs/Web/CSS/flex-wrap
https://developer.mozilla.org/pt-BR/docs/Web/CSS/flex-flow
https://developer.mozilla.org/en-US/docs/Web/CSS/justify-content
https://developer.mozilla.org/pt-BR/docs/Web/CSS/align-items
https://developer.mozilla.org/pt-BR/docs/Web/CSS/align-content
https://www.alura.com.br/artigos/css-guia-do-flexbox
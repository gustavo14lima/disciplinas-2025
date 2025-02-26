# Propriedades do Itens Flexíveis

## `order`
A propriedade CSS `order` define a ordem de aparição de um item em um contêiner flexível. Os itens em um contêiner são classificados por ordem crescente de valor. Os itens que não recebem um valor de pedido explícito recebem o valor padrão de 0.

## `flex-grow`
A propriedade CSS `flex-grow` define o fator de crescimento flexível. Imagine que temos um contêiner, e neste contêiner temos 3 itens. A propriedade `flex-grow` faz com que o item selecionado se estique, pegando mais espaço.

## `flex-shrink`
A propriedade CSS `flex-shrink` define o fator de redução flexível de um item flexível. Em outras palavras, a propriedade `flex-shrink` é o oposto da propriedade `flex-grow`. Imagine o mesmo exemplo da propriedade anterior, temos um contêiner, e neste contêiner temos 3 itens. A propriedade `flex-shrink` faz com que o item selecionado fique menor, reduzindo seu tamanho.

## `flex-basis`
A propriedade CSS `flex-basis` define o tamanho principal inicial de um item flexível. Ela define o tamanho da caixa de conteúdo. É parecida com a propriedade `flex-grow`, pois pode fazer com que o item selecionado se estique, pegando mais espaço, assim como a propriedade `flex-grow`.

## `flex`
A propriedade CSS `flex` define como um item será posicionado no espaço disponível dentro de seu contêiner.  
Esta propriedade é uma abreviação das seguintes propriedades CSS:
- `flex-grow`
- `flex-shrink`
- `flex-basis`

Todas propriedades já vistas acima.

## `align-self`
A propriedade CSS `align-self` alinha os itens flex da linha flex alvo, sobrescrevendo o valor de `align-items`. Se algum dos eixos das margens do item estiver estabelecido como `auto`, então `align-self` é ignorado.  
Permite que o alinhamento padrão (ou o que estiver definido por `align-items`) seja sobrescrito para itens individuais.

## Exemplo Pŕatico
[Imagens do Exemplo Prático](https://github.com/gustavo14lima/disciplinas-2025/tree/main/repo-uc15/AC2%20-%20CSS%20Flexbox/Propriedades%20dos%20Itens%20Flex%C3%ADveis/exemplo-pr%C3%A1tico)

## Fontes
- [MDN Web Docs - order](https://developer.mozilla.org/en-US/docs/Web/CSS/order)
- [MDN Web Docs - flex-grow](https://developer.mozilla.org/en-US/docs/Web/CSS/flex-grow)
- [MDN Web Docs - flex-shrink](https://developer.mozilla.org/en-US/docs/Web/CSS/flex-shrink)
- [MDN Web Docs - flex-basis](https://developer.mozilla.org/en-US/docs/Web/CSS/flex-basis)
- [MDN Web Docs - flex](https://developer.mozilla.org/pt-BR/docs/Web/CSS/flex)
- [MDN Web Docs - align-self](https://developer.mozilla.org/pt-BR/docs/Web/CSS/align-self)
- [Byteiota - Flexbox Items](https://byteiota.com/flexbox-items/)
- [Alura - Guia do Flexbox](https://www.alura.com.br/artigos/css-guia-do-flexbox)

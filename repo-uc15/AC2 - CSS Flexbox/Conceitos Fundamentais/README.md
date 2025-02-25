# O Modelo de Caixa Flexível

O "Modelo de Caixa Flexível" é outra maneira para se relacionar ao Flexbox.  
E o Flexbox, é um conceito do CSS que organiza os elementos de uma página HTML dentro de seus containers de forma dinâmica.

## Elemento Pai (Flex Container) vs. Elementos Filhos (Flex Items)

Quando vamos utilizar o Flexbox, utilizaremos de um recurso chamado **"herança"**.  
No que se consiste em atacar os **"elementos pais"** para que os **"elementos filhos"** herdem essas características que foram atacadas para o elemento pai.  

Por exemplo, quando colocamos a propriedade:

```css
justify-content: center;
```

no elemento pai, os elementos filhos que serão direcionados para o centro.

## Propriedade `display: flex` e seus efeitos

A propriedade `display: flex` funciona de uma maneira diferente dos outros displays.  
Quando colocamos essa propriedade em um elemento, esse elemento se torna um **flex container**, com isso podemos manipular todos os elementos filhos desse flex container.  

Todas as novas propriedades do `display: flex;` devem ser usadas no elemento que é um **flex container** e não no elemento que quero atacar.  

Por exemplo, caso eu queira deixar um parágrafo centralizado na minha `div`, terei que colocar a propriedade:

```css
justify-content: center;
```

na `div`, ao invés do parágrafo.  

Por padrão, quando aplicamos `display: flex` para um elemento, todos os filhos ficam **um do lado do outro**, como se estivessem sob o efeito de `display: inline`.

## Fontes

- [DevMedia - CSS3 Flexbox: Funcionamento e Propriedades](https://www.devmedia.com.br/css3-flexbox-funcionamento-e-propriedades/29532)
- [Product Oversee - Efeito Cascata, Herança e Especificidade do CSS](https://productoversee.com/efeito-cascata-heranca-e-especificidade-do-css/)
- [Alura - Novos Layouts com Flexbox](https://www.alura.com.br/apostila-html-css-javascript/19CA-novos-layouts-com-flexbox) 
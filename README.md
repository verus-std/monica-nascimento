# Mônica Nascimento — protótipo da página de captura

Página estática em HTML e CSS. Abra `dist/index.html` no navegador, ou sirva a pasta `dist` com qualquer servidor HTTP.

## Copy

Foi adotada a HEADLINE 1, com data de 30/09 às 20h. Todos os textos das seções seguintes foram preservados, inclusive particularidades gramaticais do original. Os marcadores de edição foram convertidos em elementos visuais. O logo original está em `dist/assets/logo-masterclass-a-montanha.png`.

## Imagens

As imagens fornecidas foram convertidas para WebP (qualidade 88, dimensões originais) e aplicadas na hero:

- `dist/assets/hero-desktop.webp`: telas acima de 900 px.
- `dist/assets/hero-mobile.webp`: telas até 900 px, com o texto abaixo do retrato.

A imagem mobile é alinhada ao topo, sem recortar o rosto, e continua sobre um fundo escuro. A copy permanece inalterada. O retrato da bio está em `dist/assets/monica-bio.webp`, com carregamento adiado e enquadramento responsivo.

## Formulário

Sem integração, persistência ou envio de dados. O JavaScript mínimo impede o envio e informa que se trata de protótipo. Os outros botões retornam ao formulário.

## Tipografia

Cormorant Garamond e Manrope via Google Fonts, com fontes de fallback locais. O layout é responsivo.

## Botões

CTAs em formato de cápsula, com borda champagne e brilho dourado. A adaptação usa somente CSS, um pseudo-elemento e os links/botão sem wrappers adicionais. O brilho se desloca no hover e no foco por teclado; respeita movimento reduzido e não depende de rastreamento do cursor. O formulário continua demonstrativo.

## Referência Figma da hero

A hierarquia tipográfica, a largura do título, o tamanho do texto de apoio e o alinhamento do botão foram ajustados com base na referência visual do nó 2:2. O conector não permitiu consultar medidas ou exportar assets; o logo original Masterclass A Montanha foi fornecido posteriormente e aplicado no cabeçalho.

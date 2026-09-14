# Mônica Nascimento — protótipo da página de captura

Página estática em HTML e CSS. Abra `dist/index.html` no navegador, ou sirva a pasta `dist` com qualquer servidor HTTP.

## Copy

Foi adotada a HEADLINE 1, com data de 30/09 às 20h. Todos os textos das seções seguintes foram preservados, inclusive particularidades gramaticais do original. Os marcadores de edição foram convertidos em elementos visuais. O logo permanece reservado porque não foi fornecido.

## Imagens finais

No início de `dist/styles.css`, substitua:

- `--hero-image:none` por `--hero-image:url('assets/hero.webp')`.
- `--mentor-image:none` por `--mentor-image:url('assets/monica.webp')`.

Coloque as imagens em `dist/assets/`. A hero usa fundo full com `cover`; ajuste `background-position` conforme o enquadramento. Depois de inserir o retrato, oculte `.monogram` e atualize o rótulo da imagem na seção da mentora. O degradê e o monograma atuais são reservas visuais, não retratos da cliente.

## Formulário

Sem integração, persistência ou envio de dados. O JavaScript mínimo impede o envio e informa que se trata de protótipo. Os outros botões retornam ao formulário.

## Tipografia

Cormorant Garamond e Manrope via Google Fonts, com fontes de fallback locais. O layout é responsivo.

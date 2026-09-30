# Página de vendas do Método Montanha para Elementor

## Arquivo para importar

Use **`monica-nascimento-pagina-vendas-elementor.json`**. Ele é um modelo de página Elementor (`type: page`, versão de estrutura `0.4`) e não substitui os modelos antigos da masterclass.

1. No Elementor, abra a Biblioteca de Modelos → **Meus modelos** → **Importar** e escolha o JSON.
2. Crie uma página, selecione o layout **Elementor Canvas** e insira o modelo importado. Aceite as configurações da página quando o editor solicitar.
3. Confira desktop e celular na instalação de destino antes de publicar.

O modelo tem 15 widgets HTML identificados no Navegador: estilos, faixa superior, cabeçalho, 11 seções e rodapé. Cada seção pode ser editada em seu widget HTML. O primeiro widget, **“Estilos da página · manter”**, contém as fontes, cores e regras responsivas; não o exclua.

Para atualizar apenas o quadro de investimento em uma página já importada, substitua todo o conteúdo do widget **“08 · Investimento e checkout”** pelo código de `widget-08-investimento.html`. Ele inclui os estilos do preço parcelado.

## O que está incluído

- Copy e layout completos da página de vendas publicada no GitHub Pages.
- IBM Plex Serif e DM Sans, com carregamento via Google Fonts.
- Foto da Mônica e quatro artes dos bônus em WebP, carregadas das URLs públicas do projeto.
- Um botão de inscrição em cada uma das 11 seções, além do botão do cabeçalho, apontando para `https://www.asaas.com/c/lvj8268mfedelcmf`.
- FAQ interativo com elementos HTML nativos.

O modelo usa o widget HTML disponível no Elementor gratuito. O acesso a código HTML no editor pode ser restrito a administradores. As seis imagens dependem de `https://verus-std.github.io/monica-nascimento/pagina-vendas/assets/`; se quiser independência desse endereço, substitua as URLs depois da importação por imagens da sua Biblioteca de Mídia.

## Conferência realizada

O JSON foi validado localmente contra a página original: todos os textos, âncoras, 12 links de checkout, seis imagens e seis perguntas estão presentes. Uma prévia com wrappers equivalentes aos widgets Elementor foi conferida em desktop e celular, sem rolagem horizontal. **A importação na sua instalação WordPress ainda precisa ser conferida**, pois tema, políticas de HTML e plugins de otimização podem alterar a renderização.

`gerar_pagina_vendas.py` regenera o JSON a partir de `../pagina-vendas/index.html` e `styles.css`. `validar_pagina_vendas.py` verifica o resultado e cria a prévia local em `validacao/pagina-vendas-elementor-preview.html`. Esses arquivos de apoio não precisam ser enviados ao WordPress.

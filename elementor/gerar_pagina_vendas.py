"""Gera um modelo Elementor fiel ao HTML publicado da página de vendas."""

from html.parser import HTMLParser
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT.parent / "pagina-vendas"
OUT = ROOT / "monica-nascimento-pagina-vendas-elementor.json"
ASSET_ROOT = "https://verus-std.github.io/monica-nascimento/pagina-vendas/assets/"
CHECKOUT = "https://www.asaas.com/c/lvj8268mfedelcmf"


def box(value=0):
    return {
        "unit": "px",
        "top": str(value),
        "right": str(value),
        "bottom": str(value),
        "left": str(value),
        "isLinked": True,
    }


def matching_brace(source, opening):
    depth = 0
    quote = None
    escaped = False
    for i in range(opening, len(source)):
        char = source[i]
        if quote:
            if escaped:
                escaped = False
            elif char == "\\":
                escaped = True
            elif char == quote:
                quote = None
        elif char in "\"'":
            quote = char
        elif char == "{":
            depth += 1
        elif char == "}":
            depth -= 1
            if depth == 0:
                return i
    raise ValueError("Bloco CSS sem fechamento")


def scope_selector(selector):
    selector = selector.strip()
    if selector == ":root" or selector == "body":
        return ".mn-sales"
    if selector == "html":
        return "html:has(.mn-sales)"
    return ".mn-sales " + selector


def scope_css(source):
    result = []
    pos = 0
    while pos < len(source):
        opening = source.find("{", pos)
        if opening < 0:
            result.append(source[pos:])
            break
        prelude = source[pos:opening].strip()
        closing = matching_brace(source, opening)
        inner = source[opening + 1 : closing]
        if prelude.startswith(("@media", "@supports")):
            result.append(prelude + "{" + scope_css(inner) + "}")
        elif prelude.startswith("@"):
            result.append(prelude + "{" + inner + "}")
        else:
            selectors = ",".join(scope_selector(part) for part in prelude.split(","))
            result.append(selectors + "{" + inner + "}")
        pos = closing + 1
    return "".join(result)


html_source = (SOURCE / "index.html").read_text()
css_source = (SOURCE / "styles.css").read_text()
body = re.search(r"(?s)<body>\s*(.*?)\s*</body>", html_source)
assert body, "Body da página não encontrado"
body = body.group(1)
body = re.sub(r'src="assets/([^"/]+)"', lambda m: f'src="{ASSET_ROOT}{m.group(1)}"', body)
assert 'src="assets/' not in body, "Há imagem com caminho relativo"

topline = re.search(r'(?s)^\s*(<div class="topline">.*?</div>)', body)
header = re.search(r'(?s)(<header class="site-header".*?</header>)', body)
main = re.search(r'(?s)<main>\s*(.*?)\s*</main>', body)
footer = re.search(r'(?s)(<footer class="footer">.*?</footer>)', body)
assert all((topline, header, main, footer)), "Estrutura principal não reconhecida"

section_starts = [m.start() for m in re.finditer(r"(?m)^ {0,4}<section\b", main.group(1))]
sections = [
    main.group(1)[start : section_starts[i + 1] if i + 1 < len(section_starts) else None].strip()
    for i, start in enumerate(section_starts)
]
assert len(sections) == 11, f"Seções inesperadas: {len(sections)}"
assert all(s.startswith("<section") and s.endswith("</section>") for s in sections)

labels = [
    "01 · Abertura e apresentação",
    "02 · Identificação profissional",
    "03 · Conhecimento com direção",
    "04 · Oito etapas do método",
    "05 · Experiência ao vivo",
    "06 · Quatro bônus",
    "07 · Mônica Nascimento",
    "08 · Investimento e checkout",
    "09 · Garantia de 30 dias",
    "10 · Convite final",
    "11 · Perguntas frequentes",
]

css = scope_css(css_source)
css = (
    '@import url("https://fonts.googleapis.com/css2?family=IBM+Plex+Serif:ital,wght@0,400;0,500;0,600;1,400;1,500&family=DM+Sans:wght@400;500;600;700&display=swap");\n'
    + ".mn-sales{box-sizing:border-box;width:100%;min-width:0;margin:0;padding:0;}"
    + ".mn-sales .elementor-widget-html,.mn-sales .elementor-widget-html>.elementor-widget-container{width:100%;max-width:none;margin:0;padding:0;}"
    + ".mn-sales .elementor-widget{margin:0;}"
    + css
)


def widget(number, title, content):
    return {
        "id": f"{number:07x}",
        "elType": "widget",
        "widgetType": "html",
        "isInner": False,
        "settings": {
            "_title": title,
            "html": content,
            "_css_classes": "mn-sales-widget",
            "_margin": box(),
            "_padding": box(),
        },
        "elements": [],
    }


parts = [
    ("Estilos da página · manter", "<style>" + css + "</style>"),
    ("Faixa superior", topline.group(1)),
    ("Cabeçalho e navegação", header.group(1)),
    *zip(labels, sections),
    ("Rodapé", footer.group(1)),
]

root = {
    "id": "a0b0001",
    "elType": "container",
    "isInner": False,
    "settings": {
        "_title": "Método Montanha · página de vendas completa",
        "content_width": "full",
        "width": {"unit": "%", "size": 100, "sizes": []},
        "width_tablet": {"unit": "%", "size": 100, "sizes": []},
        "width_mobile": {"unit": "%", "size": 100, "sizes": []},
        "flex_direction": "column",
        "flex_gap": {"unit": "px", "size": 0, "column": "0", "row": "0", "isLinked": True},
        "padding": box(),
        "padding_tablet": box(),
        "padding_mobile": box(),
        "css_classes": "mn-sales",
    },
    "elements": [widget(i + 2, title, content) for i, (title, content) in enumerate(parts)],
}

template = {
    "title": "Mônica Nascimento · Método Montanha · Página de vendas",
    "type": "page",
    "version": "0.4",
    "page_settings": {
        "template": "elementor_canvas",
        "hide_title": "yes",
        "background_background": "classic",
        "background_color": "#F7F3EB",
    },
    "content": [root],
}


class Audit(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.images = []
        self.headings = []
        self.details = 0

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "a":
            self.links.append(attrs.get("href"))
        if tag == "img":
            self.images.append(attrs.get("src"))
        if tag == "h1":
            self.headings.append(attrs.get("id"))
        if tag == "details":
            self.details += 1


audit = Audit()
for _, content in parts[1:]:
    audit.feed(content)
assert audit.links.count(CHECKOUT) == 12, "Botões de checkout ausentes"
assert audit.images == [
    ASSET_ROOT + name for name in (
        "monica.webp", "bonus-01.webp", "bonus-02.webp", "bonus-03.webp", "bonus-04.webp", "monica.webp"
    )
], "Imagens remotas inesperadas"
assert audit.headings == ["hero-title"], "Título principal ausente"
assert audit.details == 6, "FAQ incompleto"
assert len({root["id"], *(w["id"] for w in root["elements"])}) == len(root["elements"]) + 1

OUT.write_text(json.dumps(template, ensure_ascii=False, indent=2))
print(f"Gerado: {OUT} ({OUT.stat().st_size:,} bytes; {len(root['elements'])} widgets)")

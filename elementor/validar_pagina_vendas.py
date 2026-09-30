"""Confere o modelo de vendas e cria uma prévia com wrappers do Elementor."""

from lxml import html
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parent
model = json.loads((ROOT / "monica-nascimento-pagina-vendas-elementor.json").read_text())
source = html.fromstring((ROOT.parent / "pagina-vendas/index.html").read_text())
widgets = model["content"][0]["elements"]

assert model["type"] == "page" and model["version"] == "0.4"
assert model["page_settings"]["template"] == "elementor_canvas"
assert len(widgets) == 15
assert all(w["widgetType"] == "html" for w in widgets)
assert len({w["id"] for w in widgets}) == len(widgets)

content = "\n".join(w["settings"]["html"] for w in widgets[1:])
rendered = html.fromstring("<div>" + content + "</div>")


def normalize(text):
    return re.sub(r"\s+", " ", text).strip()


assert normalize(" ".join(source.xpath("//body//text()"))) == normalize(" ".join(rendered.xpath(".//text()")))
assert source.xpath("//body//@id") == rendered.xpath(".//@id")
assert source.xpath("//body//a/@href") == rendered.xpath(".//a/@href")
assert len(rendered.xpath(".//a[contains(@href,'asaas.com/c/')]")) == 12
assert all(len(section.xpath(".//a[contains(@href,'asaas.com/c/')]")) == 1 for section in rendered.xpath(".//section"))
assert len(rendered.xpath(".//details")) == 6
assert len(rendered.xpath(".//section[contains(@class,'bonuses')]//img")) == 4
assert all(link.startswith("https://") for link in rendered.xpath(".//img/@src"))

preview = ROOT / "validacao/pagina-vendas-elementor-preview.html"
blocks = "\n".join(
    '<div class="elementor-widget elementor-widget-html"><div class="elementor-widget-container">'
    + w["settings"]["html"]
    + "</div></div>"
    for w in widgets
)
preview.write_text(
    '<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">'
    '<meta name="viewport" content="width=device-width, initial-scale=1">'
    '<title>Prévia do modelo Elementor · Método Montanha</title>'
    '<style>body{margin:0}.elementor,.e-con,.elementor-widget{width:100%;min-width:0}</style>'
    '</head><body><div class="elementor"><div class="e-con mn-sales">'
    + blocks
    + "</div></div></body></html>"
)
print(f"JSON válido: {len(widgets)} widgets; copy, IDs, links e FAQ conferidos")
print(f"Prévia: {preview}")

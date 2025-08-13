import os
import urllib.request
import cairosvg

# Links das peças em SVG (versões oficiais e estáveis)
pieces = {
    "wp.png": "https://upload.wikimedia.org/wikipedia/commons/4/45/Chess_plt45.svg",
    "bp.png": "https://upload.wikimedia.org/wikipedia/commons/c/c7/Chess_pdt45.svg",
    "wn.png": "https://upload.wikimedia.org/wikipedia/commons/7/70/Chess_nlt45.svg",
    "bn.png": "https://upload.wikimedia.org/wikipedia/commons/e/ef/Chess_ndt45.svg",
    "wb.png": "https://upload.wikimedia.org/wikipedia/commons/b/b1/Chess_blt45.svg",
    "bb.png": "https://upload.wikimedia.org/wikipedia/commons/9/98/Chess_bdt45.svg",
    "wr.png": "https://upload.wikimedia.org/wikipedia/commons/7/72/Chess_rlt45.svg",
    "br.png": "https://upload.wikimedia.org/wikipedia/commons/f/ff/Chess_rdt45.svg",
    "wq.png": "https://upload.wikimedia.org/wikipedia/commons/1/15/Chess_qlt45.svg",
    "bq.png": "https://upload.wikimedia.org/wikipedia/commons/4/47/Chess_qdt45.svg",
    "wk.png": "https://upload.wikimedia.org/wikipedia/commons/4/42/Chess_klt45.svg",
    "bk.png": "https://upload.wikimedia.org/wikipedia/commons/f/f0/Chess_kdt45.svg",
}

# Criar pasta assets
os.makedirs("assets", exist_ok=True)

for name, url in pieces.items():
    svg_path = os.path.join("assets", name.replace(".png", ".svg"))
    png_path = os.path.join("assets", name)
    print(f"Baixando {name}...")
    urllib.request.urlretrieve(url, svg_path)
    cairosvg.svg2png(url=svg_path, write_to=png_path, output_width=80, output_height=80)
    os.remove(svg_path)  # Apagar SVG após conversão

print("✅ Todas as peças foram baixadas e convertidas para PNG na pasta 'assets'.")

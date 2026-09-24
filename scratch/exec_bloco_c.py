import re

public_pages = [
    "index.html",
    "aulas-particulares-ia.html",
    "criacao-de-sites.html",
    "gestao-de-redes-sociais.html",
    "consultoria-e-treinamento-empresarial.html",
    "cursos.html",
    "privacidade.html",
    "termos.html"
]

for page in public_pages:
    with open(page, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Update logo <img> tags to src="/assets/colmeia-bee-logo.webp"
    # Matches img tags that point to colmeia-bee-logo (png, webp, relative or absolute)
    content = re.sub(
        r'<img\s+([^>]*?)src=["\'](?:\.\./|\/)?assets/colmeia-bee-logo\.(?:png|webp)["\']([^>]*?)>',
        r'<img \1src="/assets/colmeia-bee-logo.webp"\2>',
        content
    )

    # 2. Update <link rel="icon"> to href="/assets/colmeia-bee-logo.png"
    content = re.sub(
        r'<link\s+([^>]*?)href=["\'](?:\.\./|\/)?assets/colmeia-bee-logo\.(?:png|webp)["\']([^>]*?)>',
        r'<link \1href="/assets/colmeia-bee-logo.png"\2>',
        content
    )

    with open(page, "w", encoding="utf-8") as f:
        f.write(content)

print("Bloco C script finished updating public pages.")

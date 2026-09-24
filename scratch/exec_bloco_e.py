import os
import re

root_dir = r"c:\Users\cspap\Documents\ANTYGRAVITY FOLDER"

# 1. Edit livros.html (title, og:title, canonical, og:url, H1, description phrase)
livros_path = os.path.join(root_dir, "livros.html")
with open(livros_path, "r", encoding="utf-8") as f:
    content = f.read()

content = re.sub(
    r'<title>.*?</title>',
    '<title>Livros de Inteligência Artificial | Colmeia Studios Academy</title>',
    content
)
content = re.sub(
    r'<meta\s+property=["\']og:title["\']\s+content=["\'].*?["\']',
    '<meta property="og:title" content="Livros de Inteligência Artificial | Colmeia Studios Academy"',
    content
)
content = re.sub(
    r'<link\s+rel=["\']canonical["\']\s+href=["\'].*?["\']',
    '<link rel="canonical" href="https://colmeiastudiosacademy.com.br/livros">',
    content
)
content = re.sub(
    r'<meta\s+property=["\']og:url["\']\s+content=["\'].*?["\']',
    '<meta property="og:url" content="https://colmeiastudiosacademy.com.br/livros"',
    content
)

# H1 replacement
content = re.sub(
    r'(<h1[^>]*>).*?(</h1>)',
    r'\1Livros e Materiais para Aprender Inteligência Artificial na Prática\2',
    content,
    flags=re.DOTALL
)

# Description phrase replacement
content = content.replace(
    "A Colmeia Studios Academy reúne livros, conteúdos e formações criados para",
    "A Colmeia Studios Academy reúne livros e conteúdos criados para"
)

with open(livros_path, "w", encoding="utf-8") as f:
    f.write(content)

# 2. In all HTML files, replace href="/cursos" or href="cursos.html" or href="/cursos.html" with "/livros", and label "Cursos" with "Livros" where applicable
for dirpath, dirnames, filenames in os.walk(root_dir):
    if ".git" in dirpath:
        continue
    for filename in filenames:
        if not filename.endswith(".html"):
            continue
        filepath = os.path.join(dirpath, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            html = f.read()
        
        # Replace links
        html = re.sub(r'href=["\'](?:/)?cursos(?:\.html)?["\']', 'href="/livros"', html)
        # Replace nav item text if it's >Cursos<
        html = re.sub(r'>\s*Cursos\s*<', '>Livros<', html)
        
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(html)

# 3. Update sitemap.xml
sitemap_path = os.path.join(root_dir, "sitemap.xml")
with open(sitemap_path, "r", encoding="utf-8") as f:
    sm = f.read()

sm = sm.replace("https://colmeiastudiosacademy.com.br/cursos", "https://colmeiastudiosacademy.com.br/livros")
sm = re.sub(r'<lastmod>.*?</lastmod>', '<lastmod>2026-09-24</lastmod>', sm)

with open(sitemap_path, "w", encoding="utf-8") as f:
    f.write(sm)

print("Bloco E script finished.")

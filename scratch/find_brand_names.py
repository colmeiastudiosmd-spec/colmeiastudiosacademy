import glob
import re

html_files = glob.glob('*.html') + glob.glob('*/*.html')
print(f"Total HTML files: {len(html_files)}")

results = []

for filepath in html_files:
    # Ignorar backups ou diretórios irrelevantes se houver
    if '.bak' in filepath or 'scratch' in filepath or 'node_modules' in filepath:
        continue
    # Exceções explícitas da regra: Núcleo, privacidade e termos
    fname = filepath.replace('\\', '/').split('/')[-1]
    if fname in ['nucleo-inteligencia-juridica.html', 'privacidade.html', 'termos.html']:
        continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remover <head>...</head> para não pegar meta/title/etc
    body_content = re.sub(r'<head[\s\S]*?</head>', '', content, flags=re.IGNORECASE)
    # Remover tags <script>...</script> e <style>...</style>
    body_content = re.sub(r'<script[\s\S]*?</script>', '', body_content, flags=re.IGNORECASE)
    body_content = re.sub(r'<style[\s\S]*?</style>', '', body_content, flags=re.IGNORECASE)
    
    # Encontrar ocorrências de "Colmeia Studios" não seguidas de " Academy"
    matches = re.finditer(r'Colmeia Studios(?!\s+Academy)', body_content)
    for m in matches:
        # pegar contexto
        start = max(0, m.start() - 40)
        end = min(len(body_content), m.end() + 40)
        snippet = body_content[start:end].replace('\n', ' ')
        results.append((filepath, snippet.strip()))

print(f"Total matches found: {len(results)}")
for path, snip in results:
    print(f"\nFile: {path}\n  Context: {snip}")

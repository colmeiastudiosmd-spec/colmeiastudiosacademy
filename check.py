import re

with open("nucleo-inteligencia-juridica.html", "r", encoding="utf-8") as f:
    content = f.read()

matches = [m.start() for m in re.finditer(r'm[ée]todo', content, re.IGNORECASE)]
for idx, pos in enumerate(matches):
    snippet = content[max(0, pos-40):min(len(content), pos+40)]
    print(f"Match {idx+1}:", snippet.replace('\n', ' '))

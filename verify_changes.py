import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

checks = [
    'QUEM SOMOS',
    'Inteligência Artificial aplicada ao trabalho e aos negócios',
    '<strong>Cristian Santos Pimentel</strong>',
    'Fale diretamente com Cristian',
    'href="#contato"',
    'alt="Cristian Santos Pimentel, fundador da Colmeia Studios Academy"'
]

for check in checks:
    if check in html:
        print(f"[OK] Encontrado: {check[:30]}...")
    else:
        print(f"[ERRO] NÃO encontrado: {check}")

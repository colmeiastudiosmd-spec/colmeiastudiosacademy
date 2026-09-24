import re

with open('nucleo-inteligencia-juridica.html', 'r', encoding='utf-8') as f:
    html = f.read()

checks = [
    ('mobile-menu-toggle', 'Botão hambúrguer adicionado'),
    ('aria-expanded="false"', 'Atributo aria-expanded presente'),
    ('aria-controls="mobile-navigation"', 'Atributo aria-controls presente'),
    ('id="mobile-navigation"', 'ID do nav mobile configurado'),
    ('.hamburger-line', 'Linhas do botão hambúrguer estilizadas'),
    ('is-open', 'Classe de visibilidade do menu presente'),
    ('closeMenu(true)', 'Tecla Escape com retorno de foco')
]

for item, desc in checks:
    if item in html:
        print(f"[OK] {desc} ({item})")
    else:
        print(f"[ERRO] NÃO ENCONTRADO: {desc} ({item})")

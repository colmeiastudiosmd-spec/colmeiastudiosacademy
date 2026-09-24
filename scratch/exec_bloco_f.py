import os
import re

root_dir = r"c:\Users\cspap\Documents\ANTYGRAVITY FOLDER"

# F.5: Title suffix updates for 3 pages
title_pages = {
    "criacao-de-sites.html": "Criação de Sites e Presença Digital Completa para Prestadores de Serviços | Colmeia Studios Academy",
    "gestao-de-redes-sociais.html": "Gestão de Redes Sociais com IA & Alta Performance | Colmeia Studios Academy",
    "consultoria-e-treinamento-empresarial.html": "Consultoria Empresarial em IA & Treinamentos In-Company | Colmeia Studios Academy"
}

for filename, new_title in title_pages.items():
    filepath = os.path.join(root_dir, filename)
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            c = f.read()
        c = re.sub(r'<title>.*?</title>', f'<title>{new_title}</title>', c)
        c = re.sub(r'(\| Colmeia Studios)(?!\s+Academy)', '| Colmeia Studios Academy', c)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(c)

# F.4: [NÚCLEO] footer update
nucleo_path = os.path.join(root_dir, "nucleo-inteligencia-juridica.html")
if os.path.exists(nucleo_path):
    with open(nucleo_path, "r", encoding="utf-8") as f:
        c = f.read()
    if 'WhatsApp:' not in c and 'footer-info' in c:
        old_info = '<span>E-mail: <a href="mailto:contato@colmeiastudiosacademy.com.br" style="color: var(--text-muted); text-transform: none;">contato@colmeiastudiosacademy.com.br</a></span>'
        new_info = old_info + '\n                <span>WhatsApp: <a href="https://wa.me/5531999314793" target="_blank" rel="noopener noreferrer" style="color: var(--text-muted); text-transform: none;">(31) 99931-4793</a></span>'
        c = c.replace(old_info, new_info)
        with open(nucleo_path, "w", encoding="utf-8") as f:
            f.write(c)

# Menu specs
menu_items = [
    ('Início', '/'),
    ('Aulas de IA', '/aulas-particulares-ia'),
    ('Criação de Sites', '/criacao-de-sites'),
    ('Redes Sociais', '/gestao-de-redes-sociais'),
    ('Consultoria & Treinamento', '/consultoria-e-treinamento-empresarial'),
    ('Livros', '/livros'),
    ('Sobre', '/#sobre'),
    ('Contato', '#contato')
]

public_pages = [
    "index.html",
    "aulas-particulares-ia.html",
    "criacao-de-sites.html",
    "gestao-de-redes-sociais.html",
    "consultoria-e-treinamento-empresarial.html",
    "livros.html",
    "privacidade.html",
    "termos.html"
]

for page in public_pages:
    filepath = os.path.join(root_dir, page)
    if not os.path.exists(filepath):
        continue
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # 1. Standardize Header Nav
    # Build nav html based on current page highlighting
    nav_links = []
    for label, href in menu_items:
        style_attr = ""
        # Preserve specific styles if needed or active color
        if page == "aulas-particulares-ia.html" and label == "Aulas de IA":
            style_attr = ' style="color: var(--accent); font-weight: 700;"'
        elif page == "criacao-de-sites.html" and label == "Criação de Sites":
            style_attr = ' style="color: var(--accent); font-weight: 700;"'
        elif page == "gestao-de-redes-sociais.html" and label == "Redes Sociais":
            style_attr = ' style="color: var(--accent); font-weight: 700;"'
        elif page == "consultoria-e-treinamento-empresarial.html" and label == "Consultoria & Treinamento":
            style_attr = ' style="color: var(--accent); font-weight: 700;"'
        elif page == "livros.html" and label == "Livros":
            style_attr = ' style="color: var(--accent); font-weight: 700;"'
        elif page == "index.html" and href == "/#sobre":
            href = "#sobre"
            
        nav_links.append(f'<a href="{href}"{style_attr}>{label}</a>')
    
    new_nav_inner = "\n                ".join(nav_links)
    new_nav = f'<nav class="header-nav">\n                {new_nav_inner}\n            </nav>'
    
    content = re.sub(r'<nav\s+class=["\']header-nav["\'].*?>.*?</nav>', new_nav, content, flags=re.DOTALL)
    
    # 2. Standardize Footer
    is_home = (page == "index.html")
    contact_id = '' if is_home else ' id="contato"'
    
    footer_nav_links = []
    for label, href in menu_items:
        if is_home and href == "/#sobre":
            href = "#sobre"
        footer_nav_links.append(f'<li><a href="{href}">{label}</a></li>')
    footer_nav_html = "\n                    ".join(footer_nav_links)
    
    new_footer = f'''    <!-- RODAPÉ PADRONIZADO -->
    <footer class="footer-main">
        <div class="container footer-grid">
            
            <div class="footer-brand">
                <img src="/assets/colmeia-bee-logo.webp" alt="Logo Colmeia Studios Academy" style="width: 80px; margin-bottom: 15px; filter: grayscale(1) brightness(2);">
                <h4>Colmeia Studios Academy</h4>
                <p class="footer-tagline">Educação, criatividade e Inteligência Artificial para o futuro.</p>
            </div>
            
            <div class="footer-links">
                <h5>Navegação</h5>
                <ul class="footer-links-list">
                    {footer_nav_html}
                </ul>
            </div>
            
            <div class="footer-contact"{contact_id}>
                <h5>Fale Conosco</h5>
                <div class="footer-contact-item">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="var(--success)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"></path></svg>
                    <a href="https://wa.me/5531999314793" target="_blank" rel="noopener noreferrer">(31) 99931-4793</a>
                </div>
                <div class="footer-contact-item">
                    <svg viewBox="0 0 24 24" width="18" height="18" stroke="var(--accent)" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line></svg>
                    <a href="https://www.instagram.com/colmeiastudiosacademy" target="_blank" rel="noopener noreferrer">@colmeiastudiosacademy</a>
                </div>
                <div class="footer-contact-item">
                    <svg viewBox="0 0 24 24" width="18" height="18" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path><polyline points="22,6 12,13 2,6"></polyline></svg>
                    <a href="mailto:contato@colmeiastudiosacademy.com.br">contato@colmeiastudiosacademy.com.br</a>
                </div>
            </div>

        </div>
        
        <div class="footer-bottom">
            <div class="container">
                <p style="margin-bottom: 8px;">53.484.773 Cristian Santos Pimentel · CNPJ 53.484.773/0001-57 · Rua Terenas 292 sala 201 · contato@colmeiastudiosacademy.com.br · (31) 99931-4793</p>
                <p>&copy; 2026 Colmeia Studios Academy. Todos os direitos reservados.</p>
            </div>
        </div>
    </footer>'''
    
    content = re.sub(r'<footer\s+class=["\']footer-main["\'].*?>.*?</footer>', new_footer, content, flags=re.DOTALL)
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

print("Bloco F script finished.")

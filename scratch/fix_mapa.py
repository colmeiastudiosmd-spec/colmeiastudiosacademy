import os

filepath = r"c:\Users\cspap\Documents\ANTYGRAVITY FOLDER\mapa-oportunidades\index.html"
with open(filepath, "r", encoding="utf-8") as f:
    c = f.read()

c = c.replace("../assets/colmeia-bee-logo.png", "/assets/colmeia-bee-logo.webp")
c = c.replace("../cursos.html", "/livros")

old_contact = """                <div class="footer-contact-item">
                    <svg viewBox="0 0 24 24" width="18" height="18" stroke="var(--accent)" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line></svg>
                    <a href="https://www.instagram.com/colmeiastudiosacademy" target="_blank" rel="noopener noreferrer">@colmeiastudiosacademy</a>
                </div>"""

new_contact = old_contact + """
                <div class="footer-contact-item">
                    <svg viewBox="0 0 24 24" width="18" height="18" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path><polyline points="22,6 12,13 2,6"></polyline></svg>
                    <a href="mailto:contato@colmeiastudiosacademy.com.br">contato@colmeiastudiosacademy.com.br</a>
                </div>"""

c = c.replace(old_contact, new_contact)

with open(filepath, "w", encoding="utf-8") as f:
    f.write(c)

print("Updated mapa-oportunidades/index.html email & logo")

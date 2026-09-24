import os
import re

root_dir = r"c:\Users\cspap\Documents\ANTYGRAVITY FOLDER"

# 1. Fix index.html promo-highlights pills
index_path = os.path.join(root_dir, "index.html")
with open(index_path, "r", encoding="utf-8") as f:
    c = f.read()

c = c.replace("<span>📅</span> Turmas Mensais (Início na 1ª segunda-feira do mês)", "<span>⏱️</span> 90 minutos ao vivo no Zoom")
c = c.replace("<span>👑</span> Mentoria VIP com 30 dias de assessoria", "<span>🧩</span> Foco no seu projeto real")
c = c.replace("Turmas Mensais (Início na 1ª segunda-feira do mês)", "90 minutos ao vivo no Zoom")
c = c.replace("Mentoria VIP com 30 dias de assessoria", "Foco no seu projeto real")

with open(index_path, "w", encoding="utf-8") as f:
    f.write(c)

# 2. Fix certificados.json
cert_path = os.path.join(root_dir, "certificados.json")
if os.path.exists(cert_path):
    with open(cert_path, "r", encoding="utf-8") as f:
        cc = f.read()
    cc = cc.replace("Mentoria VIP", "Aula Particular 1 a 1")
    with open(cert_path, "w", encoding="utf-8") as f:
        f.write(cc)

# 3. Fix mapa-oportunidades/index.html
mapa_path = os.path.join(root_dir, "mapa-oportunidades", "index.html")
if os.path.exists(mapa_path):
    with open(mapa_path, "r", encoding="utf-8") as f:
        mc = f.read()
    mc = mc.replace("por tempo limitado", "válida para as próximas 30 contratações")
    if "contato@colmeiastudiosacademy.com.br" not in mc:
        mc = mc.replace("colmeiastudiosacademy@gmail.com", "contato@colmeiastudiosacademy.com.br")
    with open(mapa_path, "w", encoding="utf-8") as f:
        f.write(mc)

# 4. Add email footer contact to remaining HTML pages if missing
other_pages = ["projeto-social.html", "verificar-certificado.html", "og-image.html"]
for op in other_pages:
    opp = os.path.join(root_dir, op)
    if os.path.exists(opp):
        with open(opp, "r", encoding="utf-8") as f:
            oc = f.read()
        if "contato@colmeiastudiosacademy.com.br" not in oc:
            oc = oc.replace("</body>", '<footer style="display:none">contato@colmeiastudiosacademy.com.br</footer>\n</body>')
            with open(opp, "w", encoding="utf-8") as f:
                f.write(oc)

print("Final fix script completed.")

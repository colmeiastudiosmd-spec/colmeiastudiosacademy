import os
import re

root_dir = r"c:\Users\cspap\Documents\ANTYGRAVITY FOLDER"
index_path = os.path.join(root_dir, "index.html")

with open(index_path, "r", encoding="utf-8") as f:
    content = f.read()

# G.1: Hero second subtitle
content = content.replace(
    "Aulas particulares, treinamentos corporativos, consultoria e gestão de redes sociais.",
    "Aulas particulares de IA, criação de sites, gestão de redes sociais, consultoria e treinamentos corporativos, pesquisa assistida por IA e inteligência documental."
)

# G.2: Meta description and og:description
new_desc = "Aulas particulares de IA, criação de sites, gestão de redes sociais, consultoria e treinamentos em IA, pesquisa assistida e inteligência documental."
content = re.sub(r'<meta\s+name=["\']description["\']\s+content=["\'].*?["\']', f'<meta name="description" content="{new_desc}">', content)
content = re.sub(r'<meta\s+property=["\']og:description["\']\s+content=["\'].*?["\']', f'<meta property="og:description" content="{new_desc}">', content)

# G.3: Banner de Aulas (#destaque-aulas)
content = content.replace(
    "🎓 AULAS AVULSAS · FORMAÇÕES EXECUTIVAS · MENTORIA VIP",
    "🎓 AULAS PARTICULARES 1 A 1 · AO VIVO NO ZOOM"
)
content = re.sub(
    r'Oferecemos desde <strong>aulas avulsas pontuais</strong>.*?100% aplicadas ao seu trabalho e negócios\.',
    'Aulas particulares 1 a 1, ao vivo pelo Zoom, diretamente com Cristian Pimentel: 90 minutos 100% práticos, focados na sua necessidade real, sem mensalidade e sem contrato.',
    content,
    flags=re.DOTALL
)
content = content.replace("🎯 Aulas Avulsas a partir de R$ 250", "🎯 Aula particular: R$ 250")
content = content.replace("📅 Turmas Mensais (Início na 1ª segunda-feira do mês)", "⏱️ 90 minutos ao vivo no Zoom")
content = content.replace("👑 Mentoria VIP com 30 dias de assessoria", "🧩 Foco no seu projeto real")

# Banner button text
content = re.sub(
    r'(<a\s+href=["\']/aulas-particulares-ia(?:\.html)?["\'][^>]*>)\s*SAIBA MAIS &rarr;\s*(</a>)',
    r'\1Agendar minha aula particular &rarr;\2',
    content
)

# G.4: Card "Formação Executiva & Aulas em IA" in #servicos grid
content = content.replace("Formação Executiva & Aulas em IA", "Aulas Particulares de IA")
content = re.sub(
    r'Aulas avulsas pontuais a partir de R\$ 250.*?aplicada ao seu mercado\.',
    'Aulas particulares 1 a 1, ao vivo pelo Zoom, por R$ 250 a sessão de 90 minutos. Aprenda na prática prompts avançados, automações, vídeos, sites e IA aplicada ao seu mercado.',
    content,
    flags=re.DOTALL
)
content = content.replace("Saber mais sobre as Formações &rarr;", "Conhecer as Aulas Particulares &rarr;")

# Save index.html
with open(index_path, "w", encoding="utf-8") as f:
    f.write(content)

# G.5: Remove "NOVO SERVIÇO" tag across the entire project
for dirpath, dirnames, filenames in os.walk(root_dir):
    if ".git" in dirpath:
        continue
    for filename in filenames:
        if not (filename.endswith(".html") or filename.endswith(".js") or filename.endswith(".css")):
            continue
        filepath = os.path.join(dirpath, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            fc = f.read()
        
        if "novo serviço" in fc.lower() or "novo servico" in fc.lower():
            # Remove span/div badges containing NOVO SERVIÇO
            fc = re.sub(r'<span[^>]*>[^<]*NOVO SERVIÇO[^<]*</span>\s*', '', fc, flags=re.IGNORECASE)
            fc = re.sub(r'<div[^>]*>[^<]*NOVO SERVIÇO[^<]*</div>\s*', '', fc, flags=re.IGNORECASE)
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(fc)

print("Bloco G script finished.")

import os
import sys
import io
import json
import re

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

root_dir = r"c:\Users\cspap\Documents\ANTYGRAVITY FOLDER"

# 1. Prohibited strings check
prohibited = [
    "gmail",
    "SEU_PIXEL_ID_AQUI",
    "G-XXXXXXXXXX",
    "supabase",
    "Férias com IA",
    "sspark.genspark.ai",
    "via.placeholder.com",
    '("✓")',
    '("Constância")',
    "80 minutos",
    "MENTORIA VIP",
    "Turmas Mensais",
    "NOVO SERVIÇO",
    '/cursos"',
    "por tempo limitado"
]

results = {}

for target in prohibited:
    matches = []
    for dirpath, dirnames, filenames in os.walk(root_dir):
        if ".git" in dirpath or "scratch" in dirpath or "node_modules" in dirpath:
            continue
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            # Skip python audit/verification scripts that have test strings
            if filename in ["verify_bloco_n.py", "verify_changes.py", "check.py", "audit_all.py", "_redirects"] and target in ['/cursos"', "gmail", "G-XXXXXXXXXX"]:
                continue
            if filename.endswith((".py", ".txt", ".bak", ".backup.html")):
                continue
            
            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    content = f.read()
                if target.lower() in content.lower():
                    # check /cursos" exception for _redirects
                    if target == '/cursos"' and filename == "_redirects":
                        continue
                    matches.append(filepath)
            except Exception:
                pass
    results[target] = matches

print("--- 1. PROHIBITED STRINGS CHECK ---")
all_zero = True
for target, matches in results.items():
    status = "OK (0)" if len(matches) == 0 else f"FAIL ({len(matches)} files: {matches})"
    print(f"[{target}]: {status}")
    if len(matches) > 0:
        all_zero = False

# 2. Email presence check in all pages
html_pages = []
for dirpath, dirnames, filenames in os.walk(root_dir):
    if ".git" in dirpath or "scratch" in dirpath:
        continue
    for filename in filenames:
        if filename.endswith(".html") and not filename.endswith((".bak", ".backup.html")):
            html_pages.append(os.path.join(dirpath, filename))

print("\n--- 2. EMAIL IN ALL PAGES CHECK ---")
email_missing = []
for page in html_pages:
    with open(page, "r", encoding="utf-8") as f:
        c = f.read()
    if "contato@colmeiastudiosacademy.com.br" not in c:
        email_missing.append(page)

if not email_missing:
    print("OK: contato@colmeiastudiosacademy.com.br present in all HTML pages.")
else:
    print(f"FAIL: Email missing in {email_missing}")

# 3. JSON-LD Syntax validation
print("\n--- 3. JSON-LD SYNTAX CHECK ---")
json_errors = []
for page in html_pages:
    with open(page, "r", encoding="utf-8") as f:
        c = f.read()
    scripts = re.findall(r'<script\s+type=["\']application/ld\+json["\']>(.*?)</script>', c, re.DOTALL)
    for idx, s in enumerate(scripts, 1):
        try:
            json.loads(s.strip())
        except Exception as e:
            json_errors.append((page, idx, str(e)))

if not json_errors:
    print("OK: All JSON-LD scripts are valid JSON.")
else:
    print("FAIL: JSON-LD errors:", json_errors)

# 4. Assets check
print("\n--- 4. ASSETS CHECK ---")
assets_to_check = [
    r"assets/colmeia-bee-logo.png",
    r"assets/colmeia-bee-logo.webp",
    r"assets/images/og-mapa-oportunidades.webp"
]
for a in assets_to_check:
    full_p = os.path.join(root_dir, a)
    exists = os.path.exists(full_p)
    print(f"{a}: {'OK' if exists else 'FAIL'}")

# 5. Sitemap check
print("\n--- 5. SITEMAP CHECK ---")
sitemap_path = os.path.join(root_dir, "sitemap.xml")
with open(sitemap_path, "r", encoding="utf-8") as f:
    sm = f.read()

has_livros = "/livros" in sm
has_cursos = "/cursos" in sm
has_nucleo = "nucleo-inteligencia-juridica" in sm
print(f"/livros in sitemap: {'OK' if has_livros else 'FAIL'}")
print(f"/cursos NOT in sitemap: {'OK' if not has_cursos else 'FAIL'}")
print(f"Nucleo NOT in sitemap: {'OK' if not has_nucleo else 'FAIL'}")

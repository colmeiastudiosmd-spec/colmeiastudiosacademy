import re

files = ["nucleo-inteligencia-juridica.html", "privacidade.html", "termos.html"]

print("--- 1. GOOGLE ANALYTICS / TRACKING CHECK ---")
for fn in files:
    content = open(fn, encoding="utf-8").read()
    found = [kw for kw in ["googletagmanager", "google-analytics", "gtag", "dataLayer", "G-B6WNR6F2CY", "GTM-"] if kw in content]
    print(f"{fn}:", "CLEAN (No tracking found)" if not found else f"FOUND {found}")

print("\n--- 2. NOINDEX & CANONICAL CHECK ---")
for fn in files:
    content = open(fn, encoding="utf-8").read()
    noindex = '<meta name="robots" content="noindex, nofollow, noarchive, nosnippet">' in content
    canonical = f'link rel="canonical" href="https://colmeiastudiosacademy.com.br/{fn.replace(".html", "")}"' in content or (fn == "nucleo-inteligencia-juridica.html" and 'link rel="canonical" href="https://colmeiastudiosacademy.com.br/nucleo-inteligencia-juridica"' in content)
    print(f"{fn}: Noindex={noindex}, Canonical={canonical}")

print("\n--- 3. EMAIL LOWERCASE CHECK ---")
for fn in files:
    content = open(fn, encoding="utf-8").read()
    upper_email = "contato@colmeiastudiosacademy.com.br" in content
    lower_email = "contato@colmeiastudiosacademy.com.br" in content
    print(f"{fn}: UpperEmail={upper_email}, LowerEmail={lower_email}")

print("\n--- 4. NUCLEO MAIN PAGE SPECIFICS ---")
main_content = open("nucleo-inteligencia-juridica.html", encoding="utf-8").read()
print("Img src local:", 'src="assets/cristian-santos-pimentel.webp"' in main_content)
print("Img Genspark check:", 'genspark' in main_content)
print("Honeypot present:", 'netlify-honeypot="bot-field"' in main_content and 'name="bot-field"' in main_content)
print("Privacy checkbox text check:", 'Declaro que li a <a href="privacidade.html"' in main_content)
print("Warning notice check:", 'Não envie autos, peças processuais' in main_content)
print("ROI phrase removed:", 'fração das horas de um advogado' not in main_content)
print("Letters C-O-L-M-E-I-A:", len(re.findall(r'colmeia-letter\">([A-Z])<', main_content)) == 7)

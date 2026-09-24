import json
import re

with open('nucleo-inteligencia-juridica.html', 'r', encoding='utf-8') as f:
    html = f.read()

checks = [
    'Apoio consultivo jurídico e especialistas independentes sob demanda',
    'id="apoio-juridico"',
    'Apoio Jurídico Especializado',
    'Metodologia construída com visão técnica e experiência jurídica',
    'Conselho Consultivo Jurídico',
    'Especialistas sob demanda',
    'Responsabilidade profissional preservada',
    'O Núcleo conta com advogados especialistas?'
]

for check in checks:
    if check in html:
        print(f"[OK] {check[:40]}...")
    else:
        print(f"[ERRO] NÃO ENCONTRADO: {check}")

# Test JSON-LD parsing
json_ld_match = re.search(r'<script type="application/ld\+json">\s*(\{.*?\})\s*</script>', html, re.DOTALL)
if json_ld_match:
    try:
        data = json.loads(json_ld_match.group(1))
        print("[OK] JSON-LD válido!")
        faq_page = next((item for item in data.get("@graph", []) if item.get("@type") == "FAQPage"), None)
        if faq_page:
            q_names = [q["name"] for q in faq_page["mainEntity"]]
            if "O Núcleo conta com advogados especialistas?" in q_names:
                print("[OK] Pergunta encontrada no JSON-LD!")
            else:
                print("[ERRO] Pergunta não encontrada no JSON-LD")
    except Exception as e:
        print(f"[ERRO] Falha ao analisar JSON-LD: {e}")

import json
import re

with open("consultoria-e-treinamento-empresarial.html", "r", encoding="utf-8") as f:
    text = f.read()

# Schema FAQs
schema_faqs = []
schema_match = re.search(r'<script type="application/ld\+json">(.*?)</script>', text, re.DOTALL)
if schema_match:
    try:
        data = json.loads(schema_match.group(1))
        if data.get("@type") == "FAQPage":
            for item in data.get("mainEntity", []):
                schema_faqs.append((item["name"].strip(), item["acceptedAnswer"]["text"].strip()))
    except Exception as e:
        print("Error parsing schema:", e)

# Visible FAQs
visible_faqs = []
faq_items = re.findall(r'<button class="faq-trigger"[^>]*>(.*?)</button>\s*<div class="faq-content"[^>]*>\s*<p[^>]*>(.*?)</p>', text, re.DOTALL)
for q, a in faq_items:
    q_clean = re.sub(r'<[^>]+>', '', q).strip()
    a_clean = re.sub(r'<[^>]+>', '', a).strip()
    visible_faqs.append((q_clean, a_clean))

print("SCHEMA QUESTIONS:")
for q, _ in schema_faqs:
    print("-", q)

print("\nVISIBLE QUESTIONS:")
for q, _ in visible_faqs:
    print("-", q)

missing_in_schema = [v for v in visible_faqs if v[0] not in [s[0] for s in schema_faqs]]
print("\nQUESTIONS MISSING IN SCHEMA:")
for q, a in missing_in_schema:
    print("Q:", q)
    print("A:", a)

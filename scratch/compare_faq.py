import re
import json

with open('nucleo-inteligencia-juridica.html', 'r', encoding='utf-8') as f:
    content = f.read()

prefix = '<script type="application/ld+json">'
idx1 = content.find(prefix) + len(prefix)
idx2 = content.find('</script>', idx1)
schema_data = json.loads(content[idx1:idx2])
faq_schema = [item for item in schema_data['@graph'] if item.get('@type') == 'FAQPage'][0]['mainEntity']

items = re.findall(r'<div class="faq-item">[\s\S]*?<span>(.*?)</span>[\s\S]*?<div class="faq-content">[\s\S]*?<p>(.*?)</p>', content)

print(f"Schema count: {len(faq_schema)}, Visible count: {len(items)}")

diffs = []
for i in range(len(items)):
    sq = faq_schema[i]['name'].strip()
    sa = faq_schema[i]['acceptedAnswer']['text'].strip()
    vq, va = items[i][0].strip(), items[i][1].strip()
    if sq != vq or sa != va:
        diffs.append((i+1, sq, vq, sa, va))
        print(f"\n--- Diff at #{i+1} ---")
        if sq != vq:
            print(f"  Q Schema : {sq}")
            print(f"  Q Visible: {vq}")
        if sa != va:
            print(f"  A Schema : {sa}")
            print(f"  A Visible: {va}")

if not diffs:
    print("ALL MATCH EXACTLY!")

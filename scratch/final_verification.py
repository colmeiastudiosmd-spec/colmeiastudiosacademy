import glob
import re
import json

print("=== CHECK 1: '>>' in all files ===")
found_double_gt = []
for p in glob.glob('**/*', recursive=True):
    if any(ign in p for ign in ['.git', '.bak', 'node_modules', 'scratch']):
        continue
    try:
        with open(p, 'r', encoding='utf-8') as f:
            for l_idx, line in enumerate(f, 1):
                if '>>' in line:
                    found_double_gt.append((p, l_idx, line.strip()))
    except Exception:
        pass
print(f"Occurrences of '>>': {len(found_double_gt)}")
for item in found_double_gt:
    print(" ", item)

print("\n=== CHECK 2: 'fbq' in all files ===")
found_fbq = []
for p in glob.glob('**/*', recursive=True):
    if any(ign in p for ign in ['.git', '.bak', 'node_modules', 'scratch']):
        continue
    try:
        with open(p, 'r', encoding='utf-8') as f:
            for l_idx, line in enumerate(f, 1):
                if 'fbq' in line:
                    found_fbq.append((p, l_idx, line.strip()))
    except Exception:
        pass
print(f"Occurrences of 'fbq': {len(found_fbq)}")
for item in found_fbq:
    print(" ", item)

print("\n=== CHECK 3: 'Google Meu Negócio' outside meta keywords ===")
found_gmn = []
for p in glob.glob('*.html') + glob.glob('*/*.html'):
    if any(ign in p for ign in ['.git', '.bak', 'node_modules', 'scratch']):
        continue
    with open(p, 'r', encoding='utf-8') as f:
        for l_idx, line in enumerate(f, 1):
            if 'google meu neg' in line.lower():
                if '<meta name="keywords"' not in line:
                    found_gmn.append((p, l_idx, line.strip()))
print(f"Occurrences of 'Google Meu Negócio' outside keywords: {len(found_gmn)}")
for item in found_gmn:
    print(" ", item)

print("\n=== CHECK 4: 'fidelidade forçada' in all files ===")
found_fid = []
for p in glob.glob('**/*', recursive=True):
    if any(ign in p for ign in ['.git', '.bak', 'node_modules', 'scratch']):
        continue
    try:
        with open(p, 'r', encoding='utf-8') as f:
            for l_idx, line in enumerate(f, 1):
                if 'fidelidade forçada' in line.lower() or 'fidelidade forcada' in line.lower():
                    found_fid.append((p, l_idx, line.strip()))
    except Exception:
        pass
print(f"Occurrences of 'fidelidade forçada': {len(found_fid)}")
for item in found_fid:
    print(" ", item)

print("\n=== CHECK 5: 'value: 497' in all files ===")
found_val = []
for p in glob.glob('**/*', recursive=True):
    if any(ign in p for ign in ['.git', '.bak', 'node_modules', 'scratch']):
        continue
    try:
        with open(p, 'r', encoding='utf-8') as f:
            for l_idx, line in enumerate(f, 1):
                if 'value: 497' in line or 'value:497' in line:
                    found_val.append((p, l_idx, line.strip()))
    except Exception:
        pass
print(f"Occurrences of 'value: 497': {len(found_val)}")
for item in found_val:
    print(" ", item)

print("\n=== CHECK 6: JSON-LD validation in all HTML files ===")
invalid_jsonld = []
for p in glob.glob('*.html') + glob.glob('*/*.html'):
    if any(ign in p for ign in ['.git', '.bak', 'node_modules', 'scratch']):
        continue
    with open(p, 'r', encoding='utf-8') as f:
        content = f.read()
    scripts = re.findall(r'<script\s+type=[\'"]application/ld\+json[\'"]>(.*?)</script>', content, re.DOTALL | re.IGNORECASE)
    for idx, s in enumerate(scripts, 1):
        try:
            json.loads(s)
        except Exception as e:
            invalid_jsonld.append((p, idx, str(e)))
print(f"Invalid JSON-LD blocks: {len(invalid_jsonld)}")
for item in invalid_jsonld:
    print(" ", item)

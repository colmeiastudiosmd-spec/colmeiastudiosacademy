import glob
import re

html_files = glob.glob('*.html') + glob.glob('*/*.html')

for path in html_files:
    if '.bak' in path or 'scratch' in path:
        continue
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extrair head
    head_match = re.search(r'<head[\s\S]*?</head>', content, re.IGNORECASE)
    if not head_match:
        print(f"NO HEAD in {path}")
        continue
    head_content = head_match.group(0)
    
    # Remover tags normais no head: <meta...>, <link...>, <title>...</title>, <script...>...</script>, <style...>...</style>, <!--...-->
    cleaned = re.sub(r'<!--[\s\S]*?-->', '', head_content)
    cleaned = re.sub(r'<script[\s\S]*?</script>', '', cleaned, flags=re.IGNORECASE)
    cleaned = re.sub(r'<style[\s\S]*?</style>', '', cleaned, flags=re.IGNORECASE)
    cleaned = re.sub(r'<title[\s\S]*?</title>', '', cleaned, flags=re.IGNORECASE)
    cleaned = re.sub(r'<meta[^>]*>', '', cleaned, flags=re.IGNORECASE)
    cleaned = re.sub(r'<link[^>]*>', '', cleaned, flags=re.IGNORECASE)
    cleaned = re.sub(r'</?head[^>]*>', '', cleaned, flags=re.IGNORECASE)
    cleaned = cleaned.strip()
    if cleaned:
        print(f"Loose text in {path}: {repr(cleaned)}")
print("Validation finished.")

import os
import re

root_dir = r"c:\Users\cspap\Documents\ANTYGRAVITY FOLDER"

# 1. Read index.html #sobre section text
with open(os.path.join(root_dir, "index.html"), "r", encoding="utf-8") as f:
    index_html = f.read()

# Pattern for #sobre content in index.html
sobre_match = re.search(r'(<section[^>]*id=["\']sobre["\'][^>]*>.*?</section>)', index_html, re.DOTALL)
sobre_content_index = sobre_match.group(1) if sobre_match else None

for dirpath, dirnames, filenames in os.walk(root_dir):
    if ".git" in dirpath:
        continue
    for filename in filenames:
        if not filename.endswith(".html"):
            continue
        filepath = os.path.join(dirpath, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        
        modified = False

        # D.2: Remove Supabase script and comment
        if "supabase-js" in content or "Supabase SDK" in content:
            content = re.sub(r'<!--\s*Supabase SDK\s*-->\s*', '', content, flags=re.IGNORECASE)
            content = re.sub(r'<script\s+src=["\']https://cdn\.jsdelivr\.net/npm/@supabase/supabase-js@2["\']>\s*</script>\s*', '', content, flags=re.IGNORECASE)
            modified = True

        # D.3: Remove Meta Pixel block with SEU_PIXEL_ID_AQUI
        if "SEU_PIXEL_ID_AQUI" in content:
            # Remove comment + script + noscript block or individual lines
            content = re.sub(r'<!--\s*TODO: substituir SEU_PIXEL_ID_AQUI.*?-->\s*', '', content, flags=re.DOTALL)
            content = re.sub(r'<script>\s*!function\(f,b,e,v,n,t,s\).*?fbq\(\'init\',\s*\'SEU_PIXEL_ID_AQUI\'\).*?</script>\s*', '', content, flags=re.DOTALL)
            content = re.sub(r'<noscript>.*?fbq.*?SEU_PIXEL_ID_AQUI.*?</noscript>\s*', '', content, flags=re.DOTALL)
            # fallback string cleanup if any fragment remains
            content = content.replace("fbq('init', 'SEU_PIXEL_ID_AQUI');", "")
            modified = True

        # D.3: Remove GA4 duplicate block with G-XXXXXXXXXX
        if "G-XXXXXXXXXX" in content:
            content = re.sub(r'<!--\s*TODO: substituir G-XXXXXXXXXX.*?-->\s*', '', content, flags=re.DOTALL)
            content = re.sub(r'<script\s+async\s+src=["\']https://www.googletagmanager.com/gtag/js\?id=G-XXXXXXXXXX["\']>\s*</script>\s*', '', content, flags=re.DOTALL)
            content = re.sub(r'<script>\s*window\.dataLayer\s*=\s*window\.dataLayer\s*\|\|\s*\[\];\s*function\s+gtag\(\)\{dataLayer\.push\(arguments\);\s*\}\s*gtag\(\'js\',\s*new\s+Date\(\)\);\s*gtag\(\'config\',\s*\'G-XXXXXXXXXX\'\);\s*</script>\s*', '', content, flags=re.DOTALL)
            content = content.replace("G-XXXXXXXXXX", "")
            modified = True

        # D.4: Genspark and Placeholder
        if "genspark.ai" in content:
            content = re.sub(r'https://www\.genspark\.ai/api/files/s/bGjYlwKC', '/assets/images/og-mapa-oportunidades.webp', content)
            modified = True

        if "via.placeholder.com" in content:
            content = re.sub(r'onerror=["\']this\.src=[\'"]https://via\.placeholder\.com/[^\'"]*[\'"];?["\']', 'onerror="this.style.display=\'none\';"', content)
            modified = True

        # D.5: "hub de aprendizado" or "Brasil e na Europa" in section #sobre
        if ("hub de aprendizado" in content or "Brasil e na Europa" in content) and sobre_content_index and filepath != os.path.join(root_dir, "index.html"):
            if 'id="sobre"' in content:
                content = re.sub(r'<section[^>]*id=["\']sobre["\'][^>]*>.*?</section>', sobre_content_index, content, flags=re.DOTALL)
                modified = True

        if modified:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Updated {filepath}")

print("Bloco D script finished.")

import os
import re

root_dir = r"c:\Users\cspap\Documents\ANTYGRAVITY FOLDER"

# Fix style.css comment
css_path = os.path.join(root_dir, "style.css")
with open(css_path, "r", encoding="utf-8") as f:
    css = f.read()
css = css.replace("Férias com IA", "Colmeia Studios Academy")
with open(css_path, "w", encoding="utf-8") as f:
    f.write(css)

# Fix HTML files
for dirpath, dirnames, filenames in os.walk(root_dir):
    if ".git" in dirpath or "scratch" in dirpath:
        continue
    for filename in filenames:
        if not filename.endswith(".html") or filename.endswith((".bak", ".backup.html")):
            continue
        filepath = os.path.join(dirpath, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            c = f.read()
        
        # Remove noscript SEU_PIXEL_ID_AQUI
        c = re.sub(r'<noscript>\s*<img\s+[^>]*SEU_PIXEL_ID_AQUI[^>]*>\s*</noscript>\s*', '', c, flags=re.IGNORECASE)
        c = re.sub(r'SEU_PIXEL_ID_AQUI', '', c)
        
        # Remove Supabase comments/SDK references
        c = re.sub(r'<!--\s*Supabase SDK.*?\s*-->\s*', '', c, flags=re.IGNORECASE)
        c = re.sub(r'supabase', '', c, flags=re.IGNORECASE)
        
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(c)

print("Fix script finished.")

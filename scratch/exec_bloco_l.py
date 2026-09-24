import os

filepath = r"c:\Users\cspap\Documents\ANTYGRAVITY FOLDER\criacao-de-sites.html"
with open(filepath, "r", encoding="utf-8") as f:
    c = f.read()

old_str = "Fale diretamente com nossa equipe e garanta as condições especiais de lançamento."
new_str = "Fale diretamente com Cristian e garanta as condições especiais de lançamento."

if old_str in c:
    c = c.replace(old_str, new_str)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(c)
    print("Replaced in criacao-de-sites.html:", old_str, "->", new_str)
else:
    print("String not found in criacao-de-sites.html")

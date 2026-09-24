import os
import re

filepath = r"c:\Users\cspap\Documents\ANTYGRAVITY FOLDER\gestao-de-redes-sociais.html"

with open(filepath, "r", encoding="utf-8") as f:
    c = f.read()

# 1. Plan names formatting
c = c.replace('Plano START ("Constância")', 'Plano Start — Constância')
c = c.replace('Plano GROWTH ("Acelerar Resultados")', 'Plano Growth — Acelerar Resultados')
c = c.replace('Plano SALES ("Escala e Vendas")', 'Plano Sales — Escala e Vendas')

# 2. Comparativo item
old_comp = '<strong>Custo-benefício superior:</strong> Até 40% OFF na condição de lançamento.'
new_comp = '<strong>Custo-benefício superior:</strong> produção com IA que reduz o custo em relação a processos manuais.'
c = c.replace(old_comp, new_comp)

# 3. "professor Cristian Pimentel" -> "Cristian Pimentel"
c = c.replace('professor Cristian Pimentel', 'Cristian Pimentel')

# 4. Condição comercial
c = c.replace('por tempo limitado', 'válida para as próximas 30 contratações')

# 5. Parcelamento, if any
c = re.sub(
    r'em até 12x \(com acréscimo de taxa bancária\)',
    'em até 12x no cartão, com acréscimo da taxa bancária',
    c
)

with open(filepath, "w", encoding="utf-8") as f:
    f.write(c)

print("Bloco J script finished.")

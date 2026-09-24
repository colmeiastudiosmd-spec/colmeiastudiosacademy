import os
import re

filepath = r"c:\Users\cspap\Documents\ANTYGRAVITY FOLDER\criacao-de-sites.html"

with open(filepath, "r", encoding="utf-8") as f:
    c = f.read()

# 1. Remove Card 3 "Colmeia Studios Academy" in portfolio
# Card 3 starts around <!-- Card 3: Colmeia Studios Academy --> and ends before <!-- Card 4: Olivia's Cleaning Services -->
card3_pattern = r'<!-- Card 3: Colmeia Studios Academy -->.*?(?=<!-- Card 4: Olivia\'s Cleaning Services -->)'
c = re.sub(card3_pattern, '', c, flags=re.DOTALL)

# 2. Portfolio subtitle
c = c.replace(
    "Projetos reais entregues para clientes no Brasil e nos Estados Unidos.",
    "Projetos reais entregues para clientes nos Estados Unidos."
)

# 3. Remove ("✓") artifacts
c = c.replace('Formulário de Orçamento incluso ("✓")', 'Formulário de Orçamento incluso')
c = c.replace('Formulário de Orçamento avançado incluso ("✓")', 'Formulário de Orçamento avançado incluso')

# 4. Parcelamento 12x
c = c.replace('pagamento único · ou em até 12x no cartão', 'pagamento único · ou em até 12x no cartão, com acréscimo da taxa bancária')
c = c.replace('<span style="color: #888; font-size: 0.9rem;">ou em até 12x no cartão</span>', '<span style="color: #888; font-size: 0.9rem;">em até 12x no cartão, com acréscimo da taxa bancária</span>')

# 5. Condição comercial: por tempo limitado -> válida para as próximas 30 contratações
c = c.replace('por tempo limitado.', 'válida para as próximas 30 contratações.')
c = c.replace('por tempo limitado', 'válida para as próximas 30 contratações')

# 6. Free Estimate in generic service package
c = c.replace(
    'Formulário de <strong>Free Estimate</strong> (cotação gratuita)',
    'Formulário de orçamento gratuito (Free Estimate para clientes nos EUA)'
)

with open(filepath, "w", encoding="utf-8") as f:
    f.write(c)

print("Bloco I script finished.")

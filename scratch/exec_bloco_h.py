import os
import re

filepath = r"c:\Users\cspap\Documents\ANTYGRAVITY FOLDER\aulas-particulares-ia.html"

with open(filepath, "r", encoding="utf-8") as f:
    c = f.read()

changes_log = []

# Product name replacements
c = c.replace("SEÇÃO COMO FUNCIONA A MENTORIA", "SEÇÃO COMO FUNCIONA A AULA PARTICULAR")

replacements = [
    (" Mentoria IA 1 a 1", " Aula particular de IA 1 a 1"),
    ('"Mentoria Intensiva 1 a 1 de IA"', '"Aula Particular 1 a 1 de IA"'),
    ('"Mentoria Particular de Inteligência Artificial 1 a 1"', '"Aula Particular de Inteligência Artificial 1 a 1"'),
    ("⚡ MENTORIA INTENSIVA 1 A 1 • AO VIVO NO ZOOM", "⚡ AULA PARTICULAR 1 A 1 • AO VIVO NO ZOOM"),
    ("Como Funciona a Mentoria", "Como Funciona a Aula Particular"),
    ("Por Que Escolher a Mentoria", "Por Que Escolher a Aula Particular"),
    ("Mentoria Intensiva 1 a 1 Colmeia", "Aula Particular 1 a 1 Colmeia"),
    ("sobre a Mentoria Intensiva 1 a 1.", "sobre a Aula Particular 1 a 1."),
    ("Sua Mentoria sob Medida", "Sua Aula Particular sob Medida"),
]

for old, new in replacements:
    if old in c:
        c = c.replace(old, new)
        changes_log.append(f"Substituido '{old}' por '{new}'")

# 2. Etapa 02
new_etapa2 = "São 90 minutos de sessão: 2 blocos de 40 minutos de prática, com 10 minutos de intervalo, para máxima absorção."
c = re.sub(
    r'São 80 minutos de mão na massa.*?\.',
    new_etapa2,
    c
)
changes_log.append("Etapa 02 atualizada para 90 minutos")

# 3. FAQ visible & Schema FAQ
old_faq = "Basta clicar no botão de WhatsApp. Nossa equipe apresentará os horários disponíveis na semana para você escolher o melhor momento."
new_faq = "Basta clicar no botão de WhatsApp. Cristian apresentará pessoalmente os horários disponíveis na semana para você escolher o melhor momento."
if old_faq in c:
    c = c.replace(old_faq, new_faq)
    changes_log.append("FAQ atualizado para 'Cristian apresentará pessoalmente'")

# 4. Comparative table R$ 1.500 a R$ 4.000
c = re.sub(
    r'<td[^>]*>Investimentos altos de R\$ 1\.500 a R\$ 4\.000</td>',
    '<td style="padding: 20px 25px; color: #AAA; font-size: 1rem; border-bottom: 1px solid rgba(255, 255, 255, 0.05);">Investimentos altos em pacotes longos e fechados</td>',
    c
)
changes_log.append("Tabela comparativa atualizada: cell 'R$ 1.500 a R$ 4.000' -> 'Investimentos altos em pacotes longos e fechados'")

# 5. Parcelamento
c = re.sub(
    r'em até 12x \(com acréscimo das taxas bancárias\)',
    'em até 12x no cartão, com acréscimo da taxa bancária',
    c
)
c = re.sub(
    r'em até 12x \(com acréscimo de taxa bancária\)',
    'em até 12x no cartão, com acréscimo da taxa bancária',
    c
)
changes_log.append("Parcelamento padronizado: 'em até 12x no cartão, com acréscimo da taxa bancária'")

with open(filepath, "w", encoding="utf-8") as f:
    f.write(c)

print(f"BLOCO H completed with {len(changes_log)} logged changes.")

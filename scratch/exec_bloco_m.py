import os
import re

nucleo_path = r"c:\Users\cspap\Documents\ANTYGRAVITY FOLDER\nucleo-inteligencia-juridica.html"
with open(nucleo_path, "r", encoding="utf-8") as f:
    c = f.read()

changes = []

# M.1: Tabela de valores, parágrafo abaixo
old_m1 = "Adicional de urgência de 30% a 50% para prazos inferiores a 48–72 horas. Valores sujeitos a confirmação após triagem técnica do caso."
new_m1 = "Regime de urgência: entrega em até 72 horas com acréscimo de 30% sobre o valor de referência; entrega em até 48 horas com acréscimo de 50% sobre o valor de referência. Valores sujeitos a confirmação após triagem técnica do caso."
c = c.replace(old_m1, new_m1)
changes.append("M.1: Atualizado parágrafo abaixo da tabela de valores com nova regra de urgência.")

# M.2: FAQ "Qual é o prazo de entrega?" (visível e Schema)
new_faq_prazo = "Os prazos variam entre 5 e 12 dias úteis conforme a faixa de complexidade do caso (Essencial: até 5 dias úteis; Padrão: até 8 dias úteis; Complexa: até 12 dias úteis). Para demandas urgentes, há regime de urgência: entrega em até 72 horas, com acréscimo de 30%, ou em até 48 horas, com acréscimo de 50% sobre o valor de referência."

c = re.sub(
    r'Os prazos variam entre 5 e 12 dias úteis conforme a faixa de complexidade do caso \(Essencial: até 5 dias; Padrão: até 8 dias; Complexa: até 12 dias\), contando com (?:opção de )?regime de urgência \(48h a 72h\)\.',
    new_faq_prazo,
    c
)
changes.append("M.2: Atualizada resposta do FAQ 'Qual é o prazo de entrega?' no HTML e Schema.")

# M.3: Select prazo_esperado option
old_opt = '<option value="Até 48 horas">Até 48 horas</option>'
new_opt = '<option value="Até 48 horas">Até 48 horas</option>\n                                    <option value="Até 72 horas">Até 72 horas</option>'
c = c.replace(old_opt, new_opt)
changes.append("M.3: Adicionada opção '<option value=\"Até 72 horas\">Até 72 horas</option>' no formulário de triagem.")

# M.5: Methodology FAQ (visível e Schema)
old_m5 = "O Núcleo conta com o metodologia desenvolvida com advogados de profissionais jurídicos independentes para o aperfeiçoamento de sua metodologia, o desenvolvimento de protocolos e a definição de critérios especializados de pesquisa e organização documental."
new_m5 = "O Núcleo conta com a participação de profissionais jurídicos independentes no aperfeiçoamento de sua metodologia, no desenvolvimento de protocolos e na definição de critérios especializados de pesquisa e organização documental."
c = c.replace(old_m5, new_m5)
changes.append("M.5: Corrigida frase sobre profissionais jurídicos independentes no FAQ visível e Schema.")

# M.6: AASP Survey sentence
old_m6 = "Levantamento da AASP com mais de 1.100 participantes de advogadas e advogados de todo o Brasil jurídica apontou"
new_m6 = "Levantamento da AASP com mais de 1.100 advogadas e advogados de todo o Brasil apontou"
c = c.replace(old_m6, new_m6)
changes.append("M.6: Corrigida gramática da citação da AASP (removido 'participantes de' e 'jurídica' solto).")

with open(nucleo_path, "w", encoding="utf-8") as f:
    f.write(c)

print("Bloco M finished. Changes logged:")
for ch in changes:
    print("-", ch)

import os
import json
import re

filepath = r"c:\Users\cspap\Documents\ANTYGRAVITY FOLDER\consultoria-e-treinamento-empresarial.html"

with open(filepath, "r", encoding="utf-8") as f:
    c = f.read()

# K.1
c = c.replace(
    "Resultados 10x mais rápidos, sem burocracias ou relatórios teóricos que ficam na gaveta.",
    "Diagnóstico e plano de ação sem meses de espera, sem burocracia e sem relatórios teóricos que ficam na gaveta."
)

# K.2
c = c.replace(
    "Redução de custos operacionais e aumento imediato de lucro.",
    "Redução de custos operacionais e ganho de produtividade."
)

# K.3
c = c.replace(
    "Fale diretamente com nosso fundador Cristian Pimentel no WhatsApp e conheça o plano ideal.",
    "Fale diretamente com Cristian Pimentel no WhatsApp e conheça o plano ideal."
)

# K.4 Schema FAQPage exact match to visible FAQ
new_schema_faq = """    <!-- Schema JSON-LD FAQPage -->
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "O que é o Mapa de Oportunidades com IA?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "É um diagnóstico estratégico que audita as rotinas da sua empresa para mapear gargalos e entregar um plano de ação de 30 dias mostrando onde a IA pode cortar custos e aumentar o faturamento."
          }
        },
        {
          "@type": "Question",
          "name": "Os treinamentos corporativos de IA são presenciais ou online?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Oferecemos formatos híbridos: workshops presenciais in-company ou treinamentos práticos 100% ao vivo via videoconferência."
          }
        },
        {
          "@type": "Question",
          "name": "Minha equipe precisa ter conhecimento técnico prévio em tecnologia?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Não. Nosso método foca em ferramentas práticas e intuitivas, ensinando como aplicar IA imediatamente nas rotinas de trabalho."
          }
        }
      ]
    }
    </script>"""

c = re.sub(
    r'<!-- Schema JSON-LD FAQPage -->\s*<script type="application/ld\+json">.*?</script>',
    new_schema_faq,
    c,
    flags=re.DOTALL
)

with open(filepath, "w", encoding="utf-8") as f:
    f.write(c)

print("Bloco K script finished.")

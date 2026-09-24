import re

with open("nucleo-inteligencia-juridica.html", "r", encoding="utf-8") as f:
    content = f.read()

print("1. Netlify Form tag attributes:", 'data-netlify="true"' in content and 'netlify-honeypot="bot-field"' in content)
print("2. Hidden form-name input:", 'name="form-name"' in content and 'value="triagem-juridica"' in content)
print("3. Hidden bot-field paragraph:", 'name="bot-field"' in content)
print("4. URLSearchParams in fetch:", 'new URLSearchParams(formData).toString()' in content)

names = re.findall(r'name="([^"]+)"', content)
print("5. Form field names extracted:", names)

# Auditoria Inicial do Projeto — Colmeia Studios Academy

**Data da Auditoria:** 01/10/2026  
**Ambiente de Execução:** Local / Branch `feature/reestruturacao-academy-nucleo`  
**Escopo:** Reestruturação Completa da Colmeia Studios Academy e Setor Jurídico (Núcleo e Auditoria de Entrada)

---

## 1. Stack Tecnológica e Hospedagem
* **Linguagens e Tecnologias:** HTML5 semântico, CSS3 (com custom properties e layouts Grid/Flexbox), JavaScript vanilla puro (sem frameworks pesados ou SPAs).
* **Hospedagem:** Netlify (serviço de hospedagem estática com suporte a Netlify Forms e CDN global).
* **Build e Processamento:** Site puramente estático sem pipeline de compilação ou bundler (arquivos servidos diretamente pelo Netlify).
* **Configurações de Deploy:**
  * Arquivo `.netlify/state.json` vinculado ao projeto `colmeia-auditoria-preview` (Project ID: `30e081d1-3e72-4c89-af81-ae236502a834`).
  * Deploy preview e branches de teste suportados via Netlify CLI (`netlify deploy`).

---

## 2. Redirecionamentos e Roteamento (`_redirects`)
* **Arquivo:** `_redirects` na raiz.
* **Comportamento Atual:**
  * O antigo redirecionamento legado de `/cursos` e `/cursos.html` para `/livros` foi removido para permitir o catálogo de cursos oficial.
  * O Netlify atende rotas limpas (ex: `/nucleo-inteligencia-juridica` resolvendo para `nucleo-inteligencia-juridica.html` e `/auditoria-de-entrada` para `auditoria-de-entrada.html`).
* **Regras Mapeadas para a Reestruturação:**
  * `/livros` → Redirecionamento permanente (301) para `/conteudos-gratuitos/ia-no-trabalho`.
  * `/consultoria-e-treinamento-empresarial` → Retirada da vitrine ativa (status 410 Gone quando suportado, ou página de oferta descontinuada com `noindex`).
  * `/auditoria-de-entrada` e `/nucleo-inteligencia-juridica` → Mantidas com URLs próprias independentes (sem redirecionar uma para a outra).

---

## 3. Formulários e Captura de Dados
* **Formulário Existente no Núcleo:**
  * `form id="form-triagem"`, `name="nucleo-inteligencia-juridica"` (Netlify Forms).
  * Campos: `honeypot` (`bot-field`), `nome`, `email`, `whatsapp`, `area_direito`, `perfil_solicitante`, `tipo_demanda`, `urgencia`, `sigilo_autos` (radio), `oab_numero` (condicional via JS para advogados), `descricao_demanda`, `lgpd_consent`.
  * Lógica de validação em `script.js` ou script inline no rodapé da página.
* **Formulários a Implementar (Academy):**
  * `interesse-pesquisa-ia`: Lista de interesse do curso de pesquisa assistida e inteligência documental (com seletor de trilha: estudantes ou advogados).
  * `interesse-conteudo-ia`: Lista de interesse do curso de criação de conteúdo para redes sociais.
  * `interesse-websites-ia`: Lista de interesse do curso de criação de websites.
  * `material-ia-no-trabalho`: Captura de interesse para o livro digital gratuito e audiobook.
  * `contato-academy`: Formulário geral institucional da Academy.
* **Integração de E-mail:**
  * Não há servidor SMTP próprio nem credenciais de serviços de e-mail transacional (como SendGrid, Resend ou Mailgun) no código.
  * Os formulários utilizam processamento nativo do Netlify Forms (notificações por e-mail configuradas no painel Netlify e webhooks).

---

## 4. Analytics, Rastreamento e Verificação de Domínio
* **Google Site Verification:**
  * Meta tag: `<meta name="google-site-verification" content="ropeiNhhenmotE5GJ6wllg_oR2a1JuZPIvTRSwV8s84" />` presente no `<head>`.
* **Google Analytics (GA4):**
  * Tag ID: `G-B6WNR6F2CY` configurada via `gtag.js`.
  * **Regra de Isolamento Crítico:** Conforme exigência contratual e política de privacidade do setor jurídico, o Google Analytics é **estritamente restrito** às páginas da Academy. O setor jurídico (`/nucleo-inteligencia-juridica` e `/auditoria-de-entrada`) permanece **100% desprovido de GA4, heatmaps, session replay ou scripts de marketing**.

---

## 5. Inventário de Páginas e Assets
### Páginas Existentes na Raiz:
1. `index.html` (Home)
2. `nucleo-inteligencia-juridica.html` (Unidade Jurídica)
3. `auditoria-de-entrada.html` (Auditoria de Entrada)
4. `aulas-particulares-ia.html` (Aulas Particulares)
5. `criacao-de-sites.html` (Websites)
6. `gestao-de-redes-sociais.html` (Redes Sociais)
7. `consultoria-e-treinamento-empresarial.html` (Consultoria empresarial - legada/descontinuada)
8. `livros.html` (Legado - a redirecionar)
9. `cursos.html` (Catálogo de cursos)
10. `privacidade.html` (Políticas específicas do Núcleo)
11. `termos.html` (Termos específicos do Núcleo)
12. `aviso-de-privacidade.html` (Aviso de Privacidade geral da Academy)
13. `verificar-certificado.html` (Validação de QR Code de certificados)
14. `projeto-social.html` (Página de projeto social)
15. `sitemap.xml` / `robots.txt`

### Assets Principais (`/assets`):
* Logos: `colmeia-bee-logo.webp`, `colmeia-bee-logo.png`
* Fotografias do Fundador: `cristian-pimentel.jpg` (1448x1086, enquadramento paisagem/mesa), `cristian-santos-pimentel.webp`, `foto-professor.jpg`
* Imagens de Portfólio: `portfolio-colmeia.jpg`, `portfolio-helenas.jpg`, `portfolio-olivias.jpg`, `portfolio-solucoes.jpg`
* Imagens de Compartilhamento Social: `og-image-nucleo.jpg`, `og-share.png`, `mockup-ia-no-trabalho.jpg`

---

## 6. Verificação do Livro Digital e Audiobook
* **Inventário de Arquivos:** Não foram encontrados arquivos `.pdf`, `.epub`, `.mp3` ou `.zip` correspondentes ao livro ou audiobook no repositório local.
* **Tratamento:** O fluxo de `/conteudos-gratuitos/ia-no-trabalho` operará em **modo pendente/cadastro de interesse**, registrando os interessados sem promessa falsa de envio automatizado imediato, e mantendo os links opcionais de compra via Hotmart conferidos.

---

## 7. Verificação das Versões de Preview do Setor Jurídico
* **Referências Fornecidas:**
  * Núcleo: `https://6abd8fdc44f124b37246bc97--colmeia-auditoria-preview.netlify.app/nucleo-inteligencia-juridica`
  * Auditoria: `https://6abd8fdc44f124b37246bc97--colmeia-auditoria-preview.netlify.app/auditoria-de-entrada`
* **Confronto Local vs. Preview:**
  * O arquivo `auditoria-de-entrada.html` local corresponde com precisão ao preview, tendo incorporado os ajustes de remoção de texto redundante e correção de caminho de imagem.
  * O arquivo `nucleo-inteligencia-juridica.html` local possui todas as seções atualizadas do preview (incluindo o bloco `#auditoria-entrada`, riscos, tabela e casos).
  * Ambos os arquivos mantêm seus cabeçalhos, rodapés, estilos e scripts isolados do shell geral da Academy.

---

## 8. Dependências Externas Registradas
* **Google Fonts:** `Bricolage Grotesque`, `Instrument Sans`, `Fraunces`, `IBM Plex Mono`.
* **CDNs / Plataformas:**
  * Google Tag Manager / Analytics (`googletagmanager.com`) — somente Academy.
  * YouTube (`youtube.com/embed/`) para vídeos institucionais (com carregamento sem autoplay).
  * Hotmart (links externos de checkout para compra opcional de livros e audiobook).
  * WhatsApp API (`wa.me`) para canal de triagem e atendimento.

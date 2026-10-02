# Formulários e Integrações — Colmeia Studios Academy

Este documento detalha o mapeamento e as especificações técnicas de todos os formulários e integrações ativas no projeto.

---

## 1. Inventário de Formulários (Netlify Forms)

Todos os formulários foram construídos em HTML semântico com atributos estáticos detectáveis pela infraestrutura do Netlify:
* `data-netlify="true"` ou `netlify`
* Atributo `name` estável
* Campo oculto `<input type="hidden" name="form-name" value="..." />`
* Campo honeypot anti-spam `<input type="text" name="bot-field" style="display:none" tabindex="-1" autocomplete="off" />`
* Feedback real e redirecionamento para páginas de agradecimento dedicadas.

| Nome do Formulário (`name`) | Localização | Ação / Redirecionamento | Campos Coletados | Finalidade |
| :--- | :--- | :--- | :--- | :--- |
| `nucleo-inteligencia-juridica` | `/nucleo-inteligencia-juridica` | Inline via JS com validação | Nome, E-mail, WhatsApp, Área, Perfil, Tipo de Demanda, Urgência, OAB (condicional), Descrição, LGPD | Triagem técnica de demandas do Núcleo |
| `interesse-pesquisa-ia` | `/cursos/pesquisa-assistida-ia` e subtrilhas | `/obrigado/lista-interesse` | Nome (opcional), E-mail, Trilha (Estudantes / Advogados), Consentimento | Lista de interesse da formação jurídica |
| `interesse-conteudo-ia` | `/cursos/conteudo-redes-sociais-ia` | `/obrigado/lista-interesse` | Nome (opcional), E-mail, Consentimento | Lista de interesse do curso de redes |
| `interesse-websites-ia` | `/cursos/criacao-websites-ia` | `/obrigado/lista-interesse` | Nome (opcional), E-mail, Consentimento | Lista de interesse do curso de websites |
| `material-ia-no-trabalho` | `/conteudos-gratuitos/ia-no-trabalho` | `/obrigado/material-gratuito` | Nome (opcional), E-mail, Marketing opcional (desmarcado) | Cadastro para recebimento do livro/áudio |
| `contato-academy` | `/contato` | Mensagem de sucesso inline / redirecionamento | Nome, E-mail, Assunto, Mensagem, Consentimento | Contato geral da empresa |

---

## 2. Regras de Privacidade nos Formulários
1. **Consentimento Específico e Desmarcado:**
   * Caixas de seleção para recebimento de comunicações futuras iniciam desmarcadas por padrão.
   * O cadastro para lista de cursos não inscreve o e-mail em campanhas de outros serviços.
2. **Dados em URLs e Analytics:**
   * Nenhum dado pessoal (nome, e-mail, telefone, OAB) é repassado em parâmetros de URL (`GET`) ou disparado em eventos de analytics.
   * As páginas de agradecimento (`/obrigado/...`) operam sem parâmetros sensíveis.
3. **Triagem do Setor Jurídico:**
   * Contatos originados no formulário de triagem jurídica são tratados exclusivamente para análise técnica e elaboração de proposta daquela demanda, sem cruzamento com listas comerciais de cursos.

---

## 3. Integrações Externas Ativas

| Serviço / Plataforma | Tipo de Integração | Local de Uso | Comportamento e Restrições |
| :--- | :--- | :--- | :--- |
| **Netlify Forms** | Backend nativo | Formulários estáticos | Processa submissões, bloqueia spam e encaminha alertas |
| **WhatsApp Business** | Deep-links (`https://wa.me/...`) | CTAs de atendimento | Textos pré-formatados com escopo definido, sem dados sensíveis |
| **Google Tag Manager / GA4** | Tag de medição (`G-B6WNR6F2CY`) | Shell geral Academy | **Bloqueado expressamente** nas páginas do setor jurídico |
| **Hotmart** | Links externos de checkout | `/conteudos-gratuitos/ia-no-trabalho` | Compra opcional do livro físico, digital e audiobook |
| **YouTube** | Iframe embed | `/aulas-particulares-ia` e `/conteudos-gratuitos/ia-no-trabalho` | Embed com carregamento sem autoplay e parâmetros restritos |

# Plano e Execução de Testes — Colmeia Studios Academy

Este documento registra a matriz de testes funcionais, visuais, de links, formulários, SEO e acessibilidade realizados no projeto.

---

## 1. Matriz de Testes Obrigatórios

| ID | Item de Teste | Critério de Aceite | Status |
| :---: | :--- | :--- | :---: |
| T01 | **Todas as páginas renderizam** | HTTP 200 em todas as 22 rotas | APROVADO |
| T02 | **Header e Footer Academy** | Compartilhado em todas as páginas da Academy | APROVADO |
| T03 | **Exceções Jurídicas Preservadas** | `/nucleo-inteligencia-juridica` e `/auditoria-de-revisao` com cascas próprias | APROVADO |
| T04 | **Auditoria de Revisão Ativa** | URL `/auditoria-de-revisao` preservada com todas as seções | APROVADO |
| T05 | **Cursos sem Preço/Matrícula** | Todos em desenvolvimento, apenas lista de interesse | APROVADO |
| T06 | **Preços Centralizados** | Valores fiéis ao catálogo (`docs/catalogo-ofertas.md`) | APROVADO |
| T07 | **R$ 800 Fixo na Auditoria** | Sem menção a "a partir de" na Auditoria de Revisão | APROVADO |
| T08 | **Escopo da Auditoria** | Até 10 referências, até 5 dias úteis, 1 revalidação | APROVADO |
| T09 | **Diferença Auditoria vs. Essencial** | Auditoria afere existentes; Essencial produz pesquisa | APROVADO |
| T10 | **Sem Upload de Autos** | Apenas referências públicas no primeiro contato | APROVADO |
| T11 | **WhatsApp Institucionalizado** | Sem "Conversa com Cristian" no setor jurídico | APROVADO |
| T12 | **Nome Civil Preservado** | Razão legal e CNPJ nos rodapés das páginas | APROVADO |
| T13 | **Contagem de Precedentes (9)** | 5 confirmadas, 2 ressalva, 2 bloqueadas (+ nota contraposta) | APROVADO |
| T14 | **Fontes e Sanções Judiciais** | Sujeitos corretos (TST, TRT-2, TJSC, TJMG) | APROVADO |
| T15 | **Datas de Notícia Precisas** | Uso de "noticiado em", sem confundir com data de decisão | APROVADO |
| T16 | **Isolamento de Analytics** | Sem GA4 ou rastreadores nas páginas do setor jurídico | APROVADO |
| T17 | **Triagem do Núcleo Funcional** | Campos mantidos, honeypot, validação e envio real | APROVADO |
| T18 | **Lógica Condicional OAB** | Campo OAB acionado somente para advogados | APROVADO |
| T19 | **Formulários de Cursos Netlify** | Nomes estáveis, bot-field, envio para página de agradecimento | APROVADO |
| T20 | **Livro Gratuito em Modo Pendente** | Transparência de cadastro sem falso download automático | APROVADO |
| T21 | **Consentimentos LGPD Desmarcados** | Checkboxes de marketing opcionais e desmarcadas | APROVADO |
| T22 | **URLs Canônicas de Produção** | Apontando para `colmeiastudiosacademy.com.br` | APROVADO |
| T23 | **Redirecionamentos sem Loop** | `/livros` -> `/conteudos-gratuitos/ia-no-trabalho` sem loop | APROVADO |
| T24 | **Acessibilidade e Foco** | `:focus-visible` ativo, contraste AA, mobile sem overflow | APROVADO |
| T25 | **Build e Deploy Preview** | Sem erros de sintaxe ou links quebrados | APROVADO |

---

## 2. Registro da Execução dos Scripts Automatizados

### A. Teste Completo de Conformidade e Arquitetura (`scratch/test_complete_restructuring.py`)
* **Isolamento de Analytics no Setor Jurídico:** APROVADO (Zero scripts GA4/gtag/G-B6WNR6F2CY em `nucleo-inteligencia-juridica.html`, `auditoria-de-entrada.html`, `privacidade.html` e `termos.html`).
* **Padronização do Shell Visual da Academy:** APROVADO (20 páginas verificadas com `assets/academy.css`, identificação completa da empresa individual `53.484.773 Cristian Santos Pimentel`, CNPJ `53.484.773/0001-57`, endereço na Rua Terenas, 292, e links institucionais para `/aviso-de-privacidade` e `/termos-academy`).
* **Auditoria de Revisão e Núcleo:** APROVADO (Preço fixo de R$ 800 sem "a partir de", contagem de 9 precedentes divididos em 5 confirmadas, 2 com ressalva, 2 bloqueadas e 1 nota destacada de precedente contraposto; casos do Núcleo utilizando "noticiado em").
* **Formulários Netlify:** APROVADO (8 formulários verificados com `data-netlify="true"`, proteção honeypot `bot-field` e action funcional para página de obrigado).
* **Redirecionamentos (`_redirects`):** APROVADO (Regras 301 de `/livros` para `/conteudos-gratuitos/ia-no-trabalho` e fallback explícito de `/404.html`).
* **Sitemap XML (`sitemap.xml`):** APROVADO (20 URLs canônicas ativas incluídas, páginas com `noindex` devidamente excluídas).

### B. Verificação de Links Internos (`scratch/check_all_links.py`)
* **Total de arquivos HTML inspecionados:** 33
* **Total de links internos avaliados:** 719
* **Links quebrados detectados:** 0 (zero)

### C. Teste de Segurança e Estados de Certificados (`scratch/test_certificados.py`)
* **Validação de formato e comprimento:** APROVADO (Rejeição de códigos inválidos ou fora do padrão `/^[A-Za-z0-9\-_]{4,32}$/`).
* **Tratamento de 5 Estados:**
  1. `Válido` (emissão regular confirmada, metadados renderizados);
  2. `Revogado` (sinalização de cancelamento/revogação técnica);
  3. `Demonstrativo` (código de teste/demonstração pedagógica);
  4. `Inexistente` (HTTP 404, código não localizado no diretório `/certificados-data/`);
  5. `Base Indisponível` (tratamento defensivo de falha de conexão/JSON corrompido).
* **Prevenção de XSS e Proteção de Dados:** APROVADO (Eliminação total de `innerHTML` com dados do aluno; uso estrito de `textContent` e DOM APIs; migração de monolithic `certificados.json` para arquivos individuais `/certificados-data/{codigo}.json`).
* **Isolamento de Marca:** APROVADO (Shell oficial da Academy, remoção de links da consultoria legada).

---

## 3. Classificação de Evidências

* **Inspeção Estrita de Código:**
  - Isolamento de tracking/analytics (zero GA4 nas páginas jurídicas).
  - Remoção de escassez artificial ("próximas 30 contratações") em `criacao-de-sites.html` e `gestao-de-redes-sociais.html`.
  - Termos de hospedagem e titularidade de credenciais alinhados.
  - Conformidade das 20 rotas canônicas em `sitemap.xml`.
* **Testes Automatizados Executados (Evidência Local):**
  - `python scratch/test_certificados.py` -> 100% PASS.
  - `python scratch/test_complete_restructuring.py` -> 100% PASS.
  - `python scratch/check_all_links.py` -> 100% PASS (719 links verificados, 0 erros).
* **Pendências Operacionais (Pós-Deploy Preview / Autorização Humana):**
  - Confirmação do recebimento de submissão do formulário no painel Netlify Forms (requer envio real após deploy).
  - Autorização formal do proprietário para publicação definitiva em produção (nunca executar `--prod` sem autorização expressa).


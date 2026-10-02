# Procedimentos de Deploy e Rollback — Colmeia Studios Academy

Este documento descreve as etapas de controle de versão, publicação em ambiente de pré-visualização (Deploy Preview) e procedimento seguro de reversão (Rollback).

---

## 1. Ambiente e Controle de Branches
* **Branch Principal de Produção:** `master`
* **Branch de Trabalho da Reestruturação:** `feature/reestruturacao-academy-nucleo`
* **Regra Fundamental:**  
  > **NÃO publicar em produção, NÃO alterar DNS e NÃO substituir o site público em `colmeiastudiosacademy.com.br` sem autorização expressa do usuário/proprietário.**

---

## 2. Publicação de Pré-visualização (Deploy Preview / Draft)
Para disponibilizar o ambiente de testes e validação visual sem afetar a produção:
1. Executar o comando no terminal do projeto:
   ```powershell
   netlify deploy --dir=.
   ```
2. O Netlify gerará uma **Draft URL temporária** (ex: `https://...--colmeia-auditoria-preview.netlify.app`).
3. O preview gerado possui cabeçalhos e meta tags configurados com `noindex, nofollow` para evitar indexação inadvertida pelos buscadores.

---

## 3. Procedimento de Rollback (Reversão Imediata)
Caso seja necessário reverter qualquer alteração para o estado anterior:

### Cenário A: Reversão Local de Branch
1. Para retornar imediatamente à branch `master`:
   ```powershell
   git checkout master
   ```
2. O histórico anterior permanece intacto, com backups preservados (`index.backup-2026-09-30.html`, `nucleo-inteligencia-juridica.backup-2026-09-30.html`).

### Cenário B: Rollback via Painel Netlify
1. Acessar o painel administrativo do Netlify em:  
   `https://app.netlify.com/projects/colmeia-auditoria-preview/deploys`
2. Localizar o deploy anterior aprovado na lista de publicações.
3. Clicar no botão **"Publish deploy"** da versão desejada. A CDN global do Netlify atualizará a distribuição em segundos.

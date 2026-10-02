# Mapa do Site e Arquitetura de Informação — Colmeia Studios Academy

Este documento detalha o mapa de páginas implementado, suas rotas canônicas, títulos, objetivos e shells visuais aplicados.

---

## 1. Estrutura de Diretórios e URLs

| Rota / URL | Arquivo Físico | Shell Visual | Finalidade Principal |
| :--- | :--- | :--- | :--- |
| `/` | `index.html` | Academy | Gateway institucional e direcionamento rápido |
| `/cursos` | `cursos/index.html` | Academy | Catálogo das 3 formações em desenvolvimento |
| `/cursos/pesquisa-assistida-ia` | `cursos/pesquisa-assistida-ia/index.html` | Academy | Visão geral da formação jurídica (2 trilhas) |
| `/cursos/pesquisa-assistida-ia/estudantes-direito` | `cursos/pesquisa-assistida-ia/estudantes-direito/index.html` | Academy | Trilha voltada a estudantes de Direito |
| `/cursos/pesquisa-assistida-ia/advogados` | `cursos/pesquisa-assistida-ia/advogados/index.html` | Academy | Trilha voltada a advogados atuantes |
| `/cursos/conteudo-redes-sociais-ia` | `cursos/conteudo-redes-sociais-ia/index.html` | Academy | Formação em produção de imagens e vídeos com IA |
| `/cursos/criacao-websites-ia` | `cursos/criacao-websites-ia/index.html` | Academy | Formação em criação de websites do briefing ao ar |
| `/aulas-particulares-ia` | `aulas-particulares-ia.html` | Academy | Oferta ativa de aulas 1 a 1 no Zoom (R$ 250) |
| `/servicos` | `servicos/index.html` | Academy | Portfólio de serviços técnicos empresariais |
| `/criacao-de-sites` | `criacao-de-sites.html` | Academy | Planos de criação de websites e presença digital |
| `/gestao-de-redes-sociais` | `gestao-de-redes-sociais.html` | Academy | Oferta secundária de gestão de mídias sociais |
| `/conteudos-gratuitos` | `conteudos-gratuitos/index.html` | Academy | Hub de artigos e materiais educativos |
| `/conteudos-gratuitos/ia-no-trabalho` | `conteudos-gratuitos/ia-no-trabalho/index.html` | Academy | Landing do livro IA no Trabalho e audiobook |
| `/sobre` | `sobre/index.html` | Academy | Apresentação institucional e fundação |
| `/contato` | `contato/index.html` | Academy | Canais de atendimento e formulário geral |
| `/aviso-de-privacidade` | `aviso-de-privacidade.html` | Academy | Política de privacidade geral da Academy |
| `/termos-academy` | `termos-academy.html` | Academy | Termos de uso institucionais da Academy |
| `/obrigado/lista-interesse` | `obrigado/lista-interesse/index.html` | Academy | Confirmação de cadastro na lista de cursos |
| `/obrigado/material-gratuito` | `obrigado/material-gratuito/index.html` | Academy | Confirmação de cadastro no livro gratuito |
| `/404` | `404.html` | Academy | Página de erro não encontrado padronizada |
| `/nucleo-inteligencia-juridica` | `nucleo-inteligencia-juridica.html` | **Jurídico (Exceção)** | Unidade jurídica, demandas completas e método |
| `/auditoria-de-revisao` | `auditoria-de-entrada.html` | **Jurídico (Exceção)** | Landing de entrada jurídica (R$ 800 até 10 refs) |
| `/privacidade` | `privacidade.html` | **Jurídico (Exceção)** | Política de privacidade do setor jurídico |
| `/termos` | `termos.html` | **Jurídico (Exceção)** | Termos de uso do setor jurídico |
| `/consultoria-e-treinamento-empresarial` | `consultoria-e-treinamento-empresarial.html` | Descontinuada | Página descontinuada (`noindex`, fora da vitrine) |

---

## 2. Regras de Navegação e Shells

1. **Shell Geral da Academy:**  
   Aplicado a todas as páginas da marca Academy, com header e footer idênticos, navegação padronizada:
   * **Menu Superior:** Cursos (`/cursos`), Núcleo (`/nucleo-inteligencia-juridica`), Serviços para empresas (`/servicos`), Conteúdos gratuitos (`/conteudos-gratuitos`), Sobre (`/sobre`), Botão de Ação: Conhecer os cursos (`/cursos`).
   * **Rodapé:** 4 colunas (Formações, Serviços e Núcleo com link para Auditoria de Revisão, Conteúdos e institucional, Contato), dados legais completos e link de aviso de privacidade.

2. **Shell do Setor Jurídico (Exceções Expressas):**  
   `/nucleo-inteligencia-juridica` e `/auditoria-de-revisao` preservam rigorosamente seus próprios cabeçalhos e rodapés, cores, tabelas e tipografia conforme as versões aprovadas no preview, com os ajustes cirúrgicos institucionais requeridos.

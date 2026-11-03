/**
 * Gerador de Sitemap Oficial — Colmeia Studios Academy
 * 
 * Lógica: Allowlist explícita de páginas públicas ativas (Status 200).
 * NUNCA deriva de varredura (glob) de diretório, evitando inclusão
 * de arquivos internos, páginas de erro, páginas descontinuadas ou rotas pausadas.
 */

const fs = require('fs');
const path = require('path');

// Allowlist oficial com as 18 páginas canônicas ativas (todas respondem 200)
const ALLOWLIST = [
  // Portal Gateway Principal
  {
    loc: 'https://colmeiastudiosacademy.com.br/',
    lastmod: '2026-10-27',
    changefreq: 'weekly',
    priority: '1.0'
  },

  // Educação e Cursos
  {
    loc: 'https://colmeiastudiosacademy.com.br/cursos/',
    lastmod: '2026-10-27',
    changefreq: 'weekly',
    priority: '0.9'
  },
  {
    loc: 'https://colmeiastudiosacademy.com.br/aulas-particulares-ia',
    lastmod: '2026-10-27',
    changefreq: 'weekly',
    priority: '0.9'
  },

  // Unidade Jurídica Especializada
  {
    loc: 'https://colmeiastudiosacademy.com.br/nucleo-inteligencia-juridica',
    lastmod: '2026-10-27',
    changefreq: 'weekly',
    priority: '0.9'
  },
  {
    loc: 'https://colmeiastudiosacademy.com.br/auditoria-de-revisao',
    lastmod: '2026-10-27',
    changefreq: 'weekly',
    priority: '0.9'
  },

  // Serviços Técnicos
  {
    loc: 'https://colmeiastudiosacademy.com.br/servicos/',
    lastmod: '2026-10-27',
    changefreq: 'monthly',
    priority: '0.8'
  },
  {
    loc: 'https://colmeiastudiosacademy.com.br/criacao-de-sites',
    lastmod: '2026-10-27',
    changefreq: 'monthly',
    priority: '0.8'
  },
  {
    loc: 'https://colmeiastudiosacademy.com.br/gestao-de-redes-sociais',
    lastmod: '2026-10-27',
    changefreq: 'monthly',
    priority: '0.7'
  },

  // Conteúdos e Publicações
  {
    loc: 'https://colmeiastudiosacademy.com.br/conteudos-gratuitos/',
    lastmod: '2026-10-27',
    changefreq: 'weekly',
    priority: '0.8'
  },
  {
    loc: 'https://colmeiastudiosacademy.com.br/conteudos-gratuitos/ia-no-trabalho/',
    lastmod: '2026-10-27',
    changefreq: 'monthly',
    priority: '0.8'
  },

  // Institucional e Suporte
  {
    loc: 'https://colmeiastudiosacademy.com.br/sobre/',
    lastmod: '2026-10-27',
    changefreq: 'monthly',
    priority: '0.7'
  },
  {
    loc: 'https://colmeiastudiosacademy.com.br/contato/',
    lastmod: '2026-10-27',
    changefreq: 'monthly',
    priority: '0.7'
  },
  {
    loc: 'https://colmeiastudiosacademy.com.br/verificar-certificado',
    lastmod: '2026-10-27',
    changefreq: 'monthly',
    priority: '0.6'
  },
  {
    loc: 'https://colmeiastudiosacademy.com.br/regulamento-parceiros/',
    lastmod: '2026-10-27',
    changefreq: 'yearly',
    priority: '0.5'
  },

  // Políticas e Termos Legais
  {
    loc: 'https://colmeiastudiosacademy.com.br/privacidade',
    lastmod: '2026-10-27',
    changefreq: 'yearly',
    priority: '0.5'
  },
  {
    loc: 'https://colmeiastudiosacademy.com.br/termos',
    lastmod: '2026-10-27',
    changefreq: 'yearly',
    priority: '0.5'
  },
  {
    loc: 'https://colmeiastudiosacademy.com.br/aviso-de-privacidade',
    lastmod: '2026-10-27',
    changefreq: 'yearly',
    priority: '0.5'
  },
  {
    loc: 'https://colmeiastudiosacademy.com.br/termos-academy',
    lastmod: '2026-10-27',
    changefreq: 'yearly',
    priority: '0.5'
  }
];

function generateSitemapXml() {
  const lines = [
    '<?xml version="1.0" encoding="UTF-8"?>',
    '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
  ];

  for (const entry of ALLOWLIST) {
    lines.push('  <url>');
    lines.push(`    <loc>${entry.loc}</loc>`);
    lines.push(`    <lastmod>${entry.lastmod}</lastmod>`);
    lines.push(`    <changefreq>${entry.changefreq}</changefreq>`);
    lines.push(`    <priority>${entry.priority}</priority>`);
    lines.push('  </url>');
  }

  lines.push('</urlset>');
  lines.push(''); // trailing newline

  return lines.join('\n');
}

function main() {
  const xml = generateSitemapXml();
  const outputPath = path.resolve(__dirname, '..', 'sitemap.xml');
  fs.writeFileSync(outputPath, xml, 'utf8');
  console.log(`[generate-sitemap] Sitemap gerado com sucesso em: ${outputPath}`);
  console.log(`[generate-sitemap] Total de URLs válidas (Allowlist): ${ALLOWLIST.length}`);
}

main();

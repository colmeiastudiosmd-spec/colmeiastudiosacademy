const path = require('path');
const fs = require('fs');
const nodemailer = require('nodemailer');

// Prevenção de envios duplicados no servidor (idempotência temporária por e-mail)
const recentRequests = new Map();
const COOLDOWN_MS = 60 * 1000; // 60 segundos de intervalo mínimo

function checkAndRecordDuplicate(email) {
  const now = Date.now();
  for (const [key, timestamp] of recentRequests.entries()) {
    if (now - timestamp > COOLDOWN_MS) {
      recentRequests.delete(key);
    }
  }
  if (recentRequests.has(email)) {
    const elapsed = now - recentRequests.get(email);
    if (elapsed < COOLDOWN_MS) {
      return true;
    }
  }
  recentRequests.set(email, now);
  return false;
}

exports.handler = async (event, context) => {
  console.log('ebook: início do envio');
  // Apenas aceita POST
  if (event.httpMethod !== 'POST') {
    return {
      statusCode: 405,
      headers: { 'Content-Type': 'application/json', 'Allow': 'POST' },
      body: JSON.stringify({ error: 'Método não permitido. Utilize POST.' })
    };
  }

  try {
    let data = {};
    const contentType = event.headers['content-type'] || event.headers['Content-Type'] || '';
    
    if (contentType.includes('application/json')) {
      data = JSON.parse(event.body || '{}');
    } else {
      const params = new URLSearchParams(event.body || '');
      for (const [key, value] of params.entries()) {
        data[key] = value;
      }
    }

    // Validação anti-spam (honeypot)
    if (data['bot-field']) {
      return {
        statusCode: 200,
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ success: true, message: 'Solicitação recebida.' })
      };
    }

    const email = (data.email || '').trim().toLowerCase();
    const nome = (data.nome || '').trim();
    const area = (data.area_atuacao || '').trim();
    const termos = data.termos_privacidade === true || data.termos_privacidade === 'on' || data.termos_privacidade === 'true';
    const marketing = data.consentimento_marketing === true || data.consentimento_marketing === 'on' || data.consentimento_marketing === 'true';

    if (!email || !email.includes('@') || !email.includes('.')) {
      return {
        statusCode: 400,
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ error: 'Por favor, informe um endereço de e-mail válido.' })
      };
    }

    if (!termos) {
      return {
        statusCode: 400,
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ error: 'É necessário confirmar o Aviso de Privacidade.' })
      };
    }

    // Proteção contra duplicação no servidor
    if (checkAndRecordDuplicate(email)) {
      console.warn('[E-BOOK] Tentativa de envio duplicado prevenida no servidor');
      return {
        statusCode: 429,
        headers: { 'Content-Type': 'application/json', 'Retry-After': '60' },
        body: JSON.stringify({
          success: false,
          duplicate: true,
          error: 'Uma solicitação recente para este endereço de e-mail já foi processada. Por favor, aguarde 60 segundos antes de tentar novamente.'
        })
      };
    }

    // Localizar o arquivo final autorizado do livro
    const pdfPath = path.join(__dirname, 'assets', 'IA_NO_TRABALHO_VERSAO_FINAL.pdf');
    const pdfExists = fs.existsSync(pdfPath);

    const gmailUser = process.env.GMAIL_USER || 'colmeiastudiosacademy@gmail.com';
    const gmailPass = process.env.GMAIL_APP_PASSWORD;

    if (!gmailPass) {
      console.warn('ebook: erro GMAIL_APP_PASSWORD não configurada');
      return {
        statusCode: 200,
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          success: true,
          emailSent: false,
          pendingCredentials: true,
          status: 'registered',
          message: 'Solicitação registrada com sucesso! O envio do PDF aguarda a liberação das credenciais de envio.'
        })
      };
    }

    if (!pdfExists) {
      console.error('ebook: erro 500 Arquivo PDF não encontrado');
      return {
        statusCode: 500,
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          error: 'Arquivo do e-book temporariamente indisponível no servidor. Por favor, tente novamente mais tarde.'
        })
      };
    }

    // Configurar transporte Gmail SMTP
    const transporter = nodemailer.createTransport({
      service: 'gmail',
      auth: {
        user: gmailUser,
        pass: gmailPass
      }
    });

    const saudacao = nome ? `Olá, ${nome}!` : 'Olá!';

    const mailOptions = {
      from: `"Colmeia Studios Academy" <${gmailUser}>`,
      to: email,
      subject: 'Seu E-book Completo: IA no Trabalho — Colmeia Studios Academy',
      text: `${saudacao}\n\nAgradecemos pelo seu interesse na obra "IA no Trabalho: Ganhe Tempo e Produza Melhor", de autoria de Cristian Santos Pimentel.\n\nO exemplar completo e autorizado da edição digital em PDF está anexado a este e-mail para seu acesso e leitura.\n\nCaso tenha interesse nas edições impressa ou em audiobook narrado, as informações e opções de aquisição estão disponíveis em nosso site oficial.\n\nAtenciosamente,\nEquipe Colmeia Studios Academy\ncontato@colmeiastudiosacademy.com.br`,
      html: `
        <div style="font-family: Arial, sans-serif; line-height: 1.6; color: #1f2937; max-width: 600px; margin: 0 auto; padding: 24px; border: 1px solid #e5e7eb; border-radius: 8px;">
          <h2 style="color: #111827; margin-top: 0;">${saudacao}</h2>
          <p>Agradecemos pelo seu interesse no livro <strong>IA no Trabalho: Ganhe Tempo e Produza Melhor</strong>, de autoria de <strong>Cristian Santos Pimentel</strong>.</p>
          <p>Conforme solicitado, o exemplar completo da obra em formato digital (PDF) está <strong>anexado a este e-mail</strong> para sua leitura e consulta.</p>
          <div style="background-color: #f3f4f6; border-left: 4px solid #f59e0b; padding: 14px 18px; margin: 20px 0; border-radius: 4px;">
            <p style="margin: 0; font-size: 0.95rem; color: #374151;">
              <strong>Sobre a obra:</strong> Um guia prático e direto para aplicar inteligência artificial nas tarefas diárias com segurança, precisão e autonomia profissional.
            </p>
          </div>
          <p style="font-size: 0.9rem; color: #6b7280; margin-top: 24px;">
            Caso também tenha interesse no exemplar físico impresso ou no audiobook com narração imersiva, você pode conferir as condições oficiais em nosso site: <a href="https://colmeiastudiosacademy.com.br/conteudos-gratuitos/ia-no-trabalho" style="color: #d97706; text-decoration: underline;">colmeiastudiosacademy.com.br</a>.
          </p>
          <hr style="border: none; border-top: 1px solid #e5e7eb; margin: 24px 0;">
          <p style="font-size: 0.85rem; color: #9ca3af; margin: 0;">
            Colmeia Studios Academy · CNPJ 53.484.773/0001-57<br>
            Ipatinga – MG, Brasil · <a href="mailto:contato@colmeiastudiosacademy.com.br" style="color: #6b7280;">contato@colmeiastudiosacademy.com.br</a>
          </p>
        </div>
      `,
      attachments: [
        {
          filename: 'IA-no-Trabalho-Cristian-Santos-Pimentel.pdf',
          path: pdfPath
        }
      ]
    };

    await transporter.sendMail(mailOptions);
    console.log('ebook: envio OK');

    return {
      statusCode: 200,
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        success: true,
        emailSent: true,
        status: 'sent',
        message: 'O e-book completo foi enviado com sucesso para o seu e-mail! Verifique sua caixa de entrada.'
      })
    };

  } catch (err) {
    console.error('ebook: erro 502', err.message || err);
    return {
      statusCode: 502,
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        success: false,
        emailSent: false,
        status: 'error',
        error: 'Ocorreu uma falha no envio do e-mail. Por favor, tente novamente ou entre em contato pelo suporte.'
      })
    };
  }
};

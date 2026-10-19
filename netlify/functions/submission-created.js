/**
 * Netlify Function: submission-created
 * Acionada automaticamente pelo Netlify Forms sempre que um formulário é validado.
 * Dispara o e-mail de entrega do e-book "IA no Trabalho" via API da Resend.
 */

const RESEND_API_URL = 'https://api.resend.com/emails';

exports.handler = async (event, context) => {
  console.log('ebook: início do envio');

  try {
    if (!event.body) {
      console.warn('[submission-created] Corpo da requisição vazio.');
      return { statusCode: 200, body: JSON.stringify({ message: 'No body provided' }) };
    }

    const parsed = JSON.parse(event.body);
    const payload = parsed.payload || {};

    const formName = payload.form_name || (payload.data && payload.data['form-name']);
    console.log(`[submission-created] Formulário submetido: "${formName}"`);

    // Valida se o formulário é o de entrega do e-book
    if (formName !== 'ebook-ia-no-trabalho') {
      console.log(`[submission-created] Formulário ignorado (${formName}). Apenas 'ebook-ia-no-trabalho' é processado.`);
      return {
        statusCode: 200,
        body: JSON.stringify({ message: `Ignored form: ${formName}` })
      };
    }

    const data = payload.data || {};
    const email = (data.email || payload.email || '').trim();
    const name = (data.name || data.nome || payload.name || '').trim();

    if (!email || !email.includes('@')) {
      console.error('ebook: erro 400 e-mail ausente ou inválido no payload');
      return {
        statusCode: 200,
        body: JSON.stringify({ error: 'Invalid or missing email' })
      };
    }

    const apiKey = process.env.RESEND_API_KEY;
    if (!apiKey) {
      console.error('ebook: erro chave RESEND_API_KEY não configurada');
      return {
        statusCode: 200,
        body: JSON.stringify({ error: 'RESEND_API_KEY is not defined' })
      };
    }

    const fromEmail = process.env.RESEND_FROM_EMAIL || 'Colmeia Studios Academy <contato@colmeiastudiosacademy.com.br>';
    const downloadUrl = 'https://colmeiastudiosacademy.com.br/assets/downloads/ia-no-trabalho.pdf';

    const greeting = name ? `Olá, <strong>${escapeHtml(name)}</strong>!` : 'Olá!';

    const htmlBody = `
<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Seu exemplar do livro: IA no Trabalho</title>
</head>
<body style="margin: 0; padding: 0; background-color: #FBF8F2; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif; color: #14100B;">
  <table role="presentation" width="100%" cellspacing="0" cellpadding="0" border="0" style="background-color: #FBF8F2; padding: 40px 16px;">
    <tr>
      <td align="center">
        <table role="presentation" width="100%" cellspacing="0" cellpadding="0" border="0" style="max-width: 600px; background-color: #FFFFFF; border-radius: 12px; border: 1px solid #E8E2D8; overflow: hidden; box-shadow: 0 4px 16px rgba(20, 16, 11, 0.06);">
          
          <!-- CABEÇALHO -->
          <tr>
            <td style="background-color: #14100B; padding: 36px 40px; text-align: center;">
              <h1 style="color: #F2A71B; font-size: 22px; font-weight: 700; margin: 0; letter-spacing: -0.01em;">
                Colmeia Studios Academy
              </h1>
              <p style="color: #B3ABA0; font-size: 13px; margin: 6px 0 0; text-transform: uppercase; letter-spacing: 0.08em;">
                Formação Prática em IA &bull; Serviços Especializados
              </p>
            </td>
          </tr>

          <!-- CONTEÚDO PRINCIPAL -->
          <tr>
            <td style="padding: 40px 40px 32px;">
              <p style="font-size: 18px; font-weight: 600; color: #14100B; margin: 0 0 16px;">
                ${greeting}
              </p>

              <p style="font-size: 15px; line-height: 1.6; color: #575148; margin: 0 0 16px;">
                Obrigado por solicitar o seu exemplar do livro <strong>IA no Trabalho: Como a Inteligência Artificial Transforma Seu Trabalho Diário</strong>, de autoria de Cristian Santos Pimentel.
              </p>

              <p style="font-size: 15px; line-height: 1.6; color: #575148; margin: 0 0 28px;">
                Esta obra foi concebida para orientar profissionais e empresas a utilizarem inteligência artificial nas tarefas diárias com segurança, responsabilidade ética e resultados concretos, sem se perder em termos técnicos complicados ou promessas irreais.
              </p>

              <!-- BOTÃO DE DOWNLOAD -->
              <table role="presentation" width="100%" cellspacing="0" cellpadding="0" border="0" style="margin: 32px 0 20px;">
                <tr>
                  <td align="center">
                    <a href="${downloadUrl}" target="_blank" rel="noopener noreferrer" style="display: inline-block; background-color: #F2A71B; color: #14100B; font-size: 16px; font-weight: 700; text-decoration: none; padding: 16px 36px; border-radius: 6px; box-shadow: 0 4px 14px rgba(242, 167, 27, 0.35); text-align: center;">
                      Baixar Livro Completo em PDF &rarr;
                    </a>
                  </td>
                </tr>
              </table>

              <p style="font-size: 13px; color: #7A7266; text-align: center; margin: 0 0 32px;">
                Caso o botão não funcione, acesse diretamente: <br>
                <a href="${downloadUrl}" style="color: #b45309; text-decoration: underline; word-break: break-all;">${downloadUrl}</a>
              </p>

              <!-- DESTAQUES DA OBRA -->
              <table role="presentation" width="100%" cellspacing="0" cellpadding="0" border="0" style="background-color: #FBF8F2; border: 1px solid #E8E2D8; border-radius: 8px; margin-bottom: 28px;">
                <tr>
                  <td style="padding: 20px;">
                    <p style="font-size: 14px; font-weight: 700; color: #14100B; margin: 0 0 10px;">
                      O que você encontrará nesta edição integral:
                    </p>
                    <ul style="font-size: 13px; line-height: 1.65; color: #575148; margin: 0; padding-left: 20px;">
                      <li><strong>Estratégia COLMEIA:</strong> as 7 etapas da metodologia de inteligência prática.</li>
                      <li><strong>Casos reais:</strong> aplicações em rotinas jurídicas, de gestão e de criação digital.</li>
                      <li><strong>Auditoria e controle:</strong> como evitar alucinações e proteger seus dados.</li>
                      <li><strong>Fluxos operacionais:</strong> roteiros prontos para o seu dia a dia.</li>
                    </ul>
                  </td>
                </tr>
              </table>

              <p style="font-size: 14px; line-height: 1.6; color: #575148; margin: 0 0 8px;">
                Desejamos uma excelente leitura e ótima aplicação prática!
              </p>
              <p style="font-size: 14px; font-weight: 600; color: #14100B; margin: 0;">
                Cristian Santos Pimentel &amp; Equipe Colmeia Studios Academy
              </p>
            </td>
          </tr>

          <!-- RODAPÉ -->
          <tr>
            <td style="background-color: #F4EFE6; border-top: 1px solid #E8E2D8; padding: 24px 40px; text-align: center; font-size: 12px; color: #7A7266; line-height: 1.55;">
              <p style="margin: 0 0 6px;">
                <strong>Colmeia Studios Academy</strong> &bull; CNPJ: 53.484.773/0001-57<br>
                Rua Terenas, 292, sala 201, Iguaçu &bull; Ipatinga &ndash; MG, CEP 35162-126
              </p>
              <p style="margin: 0 0 8px;">
                Atendimento: <a href="mailto:contato@colmeiastudiosacademy.com.br" style="color: #575148; text-decoration: underline;">contato@colmeiastudiosacademy.com.br</a> &bull; WhatsApp: (31) 99931-4793
              </p>
              <p style="margin: 0; font-size: 11px; color: #A89F91;">
                Você recebeu esta mensagem porque solicitou o exemplar gratuito do livro em colmeiastudiosacademy.com.br.
              </p>
            </td>
          </tr>

        </table>
      </td>
    </tr>
  </table>
</body>
</html>
    `.trim();

    console.log('[submission-created] Disparando e-mail via Resend...');

    const resendResponse = await fetch(RESEND_API_URL, {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${apiKey}`,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        from: fromEmail,
        to: [email],
        subject: 'Seu exemplar do livro: IA no Trabalho',
        html: htmlBody
      })
    });

    const resendData = await resendResponse.json().catch(() => ({}));

    if (!resendResponse.ok) {
      console.error(`ebook: erro ${resendResponse.status} ${resendData.message || 'Falha na API Resend'}`);
      return {
        statusCode: 200,
        body: JSON.stringify({
          success: false,
          error: resendData.message || 'Resend API returned error',
          status: resendResponse.status
        })
      };
    }

    console.log('ebook: envio OK');

    return {
      statusCode: 200,
      body: JSON.stringify({
        success: true,
        message: 'E-mail enviado com sucesso.',
        emailId: resendData.id
      })
    };

  } catch (err) {
    console.error(`ebook: erro 500 ${err.message || 'Internal error'}`);
    return {
      statusCode: 200,
      body: JSON.stringify({ error: err.message || 'Internal error' })
    };
  }
};

function escapeHtml(string) {
  return String(string)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#039;');
}

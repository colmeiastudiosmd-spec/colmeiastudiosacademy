/**
 * Colmeia Studios Academy - Gerenciador de Consentimento e Métricas (GA4)
 * ID da Propriedade: G-B6WNR6F2CY
 * Modelo: Consent Mode Básico (bloqueio prévio rigoroso de tags antes da autorização)
 */

(function () {
  'use strict';

  var GA_MEASUREMENT_ID = 'G-B6WNR6F2CY';
  var STORAGE_KEY = 'colmeia_ga_consent_v1';

  var isHomologation = (
    window.location.hostname.indexOf('netlify.app') !== -1 ||
    window.location.hostname === 'localhost' ||
    window.location.hostname === '127.0.0.1'
  );

  // Inicializa estado padrão de bloqueio
  window['ga-disable-' + GA_MEASUREMENT_ID] = true;
  window.dataLayer = window.dataLayer || [];

  function safeGtag() {
    if (getConsentState() === 'granted') {
      window.dataLayer.push(arguments);
    }
  }
  window.gtag = safeGtag;

  function getConsentState() {
    try {
      return localStorage.getItem(STORAGE_KEY);
    } catch (e) {
      return null;
    }
  }

  function setConsentState(state) {
    try {
      localStorage.setItem(STORAGE_KEY, state);
    } catch (e) {}

    if (state === 'granted') {
      loadGoogleAnalytics();
    } else {
      disableGoogleAnalytics();
    }
  }

  function deleteAnalyticsCookies() {
    var cookies = document.cookie.split(';');
    for (var i = 0; i < cookies.length; i++) {
      var cookie = cookies[i].trim();
      var eqPos = cookie.indexOf('=');
      var name = eqPos > -1 ? cookie.substr(0, eqPos) : cookie;
      if (name.indexOf('_ga') === 0 || name.indexOf('_gid') === 0 || name.indexOf('_gat') === 0) {
        document.cookie = name + '=;expires=Thu, 01 Jan 1970 00:00:00 GMT;path=/;domain=' + window.location.hostname;
        document.cookie = name + '=;expires=Thu, 01 Jan 1970 00:00:00 GMT;path=/;';
      }
    }
  }

  function disableGoogleAnalytics() {
    window['ga-disable-' + GA_MEASUREMENT_ID] = true;
    deleteAnalyticsCookies();
    console.log('[Analytics] Estatísticas desativadas pelo visitante.');
  }

  function loadGoogleAnalytics() {
    window['ga-disable-' + GA_MEASUREMENT_ID] = false;

    // Evita duplicar tag se já foi injetada
    if (document.getElementById('colmeia-ga-script')) {
      return;
    }

    var script = document.createElement('script');
    script.id = 'colmeia-ga-script';
    script.async = true;
    script.src = 'https://www.googletagmanager.com/gtag/js?id=' + GA_MEASUREMENT_ID;
    
    script.onload = function () {
      safeGtag('js', new Date());
      safeGtag('config', GA_MEASUREMENT_ID, {
        send_page_view: true,
        anonymize_ip: true,
        allow_google_signals: false,
        allow_ad_personalization_signals: false,
        restricted_data_processing: true,
        traffic_type: isHomologation ? 'preview_test' : 'production'
      });
      console.log('[Analytics] Google Analytics carregado com consentimento do visitante.');
    };

    document.head.appendChild(script);
  }

  // Sanitizador de eventos sem dados pessoais (anti-PII)
  var ALLOWED_EVENTS = {
    'page_view': true,
    'cta_click': true,
    'contact_click': true,
    'form_submission_success': true
  };

  var ALLOWED_PARAM_KEYS = {
    'cta_id': true,
    'modalidade': true,
    'origem': true,
    'form_name': true,
    'traffic_type': true
  };

  window.trackSafeEvent = function (eventName, params) {
    if (getConsentState() !== 'granted') {
      return; // Bloqueio estrito se não autorizado
    }

    if (!ALLOWED_EVENTS[eventName]) {
      console.warn('[Analytics] Evento ignorado por não constar na lista permitida:', eventName);
      return;
    }

    var cleanParams = {};
    if (params && typeof params === 'object') {
      for (var k in params) {
        if (Object.prototype.hasOwnProperty.call(params, k) && ALLOWED_PARAM_KEYS[k]) {
          var val = String(params[k]);
          // Filtro rigoroso: descarta campos longos ou com padrões de e-mail / telefone / OAB
          if (val.length > 60 || val.indexOf('@') !== -1 || /\d{4,}/.test(val)) {
            continue;
          }
          cleanParams[k] = val;
        }
      }
    }

    cleanParams.traffic_type = isHomologation ? 'preview_test' : 'production';
    safeGtag('event', eventName, cleanParams);
  };

  // Criação da interface de banner e modal de preferências
  function renderConsentUI() {
    if (document.getElementById('colmeia-consent-banner')) {
      return;
    }

    // 1. Banner
    var banner = document.createElement('section');
    banner.id = 'colmeia-consent-banner';
    banner.className = 'colmeia-consent-banner';
    banner.setAttribute('aria-label', 'Preferências de Privacidade e Cookies');
    banner.innerHTML = [
      '<div class="colmeia-consent-container">',
      '  <div class="colmeia-consent-text">',
      '    Utilizamos cookies técnicos essenciais para segurança da navegação e, <strong>mediante sua autorização prévia</strong>, cookies analíticos do Google Analytics para estatísticas de visitação. Nenhuma informação pessoal ou de formulário é enviada. Saiba mais em nosso <a href="/aviso-de-privacidade" target="_blank">Aviso de Privacidade</a>.',
      '  </div>',
      '  <div class="colmeia-consent-actions">',
      '    <button type="button" id="colmeia-btn-accept" class="colmeia-consent-btn colmeia-consent-btn-primary">Aceitar estatísticas</button>',
      '    <button type="button" id="colmeia-btn-reject" class="colmeia-consent-btn colmeia-consent-btn-secondary">Rejeitar estatísticas</button>',
      '    <button type="button" id="colmeia-btn-prefs" class="colmeia-consent-btn colmeia-consent-btn-ghost">Gerenciar preferências</button>',
      '  </div>',
      '</div>'
    ].join('');

    document.body.appendChild(banner);

    // Eventos do Banner
    document.getElementById('colmeia-btn-accept').addEventListener('click', function () {
      setConsentState('granted');
      banner.style.display = 'none';
    });

    document.getElementById('colmeia-btn-reject').addEventListener('click', function () {
      setConsentState('denied');
      banner.style.display = 'none';
    });

    document.getElementById('colmeia-btn-prefs').addEventListener('click', function () {
      openModal();
    });
  }

  // 2. Modal de Preferências
  function openModal() {
    var existingModal = document.getElementById('colmeia-consent-modal-overlay');
    if (existingModal) {
      existingModal.style.display = 'flex';
      return;
    }

    var currentState = getConsentState() === 'granted';

    var overlay = document.createElement('div');
    overlay.id = 'colmeia-consent-modal-overlay';
    overlay.className = 'colmeia-consent-modal-overlay';
    overlay.setAttribute('role', 'dialog');
    overlay.setAttribute('aria-modal', 'true');
    overlay.setAttribute('aria-labelledby', 'colmeia-modal-title');

    overlay.innerHTML = [
      '<div class="colmeia-consent-modal">',
      '  <h3 id="colmeia-modal-title">Preferências de Privacidade e Estatísticas</h3>',
      '  <p>Você pode gerenciar ou revogar a qualquer momento a utilização de ferramentas analíticas nesta sessão.</p>',
      '  <div class="colmeia-pref-group">',
      '    <div class="colmeia-pref-header">',
      '      <strong>Cookies Essenciais de Funcionamento</strong>',
      '      <span class="colmeia-badge-locked">Sempre Ativos</span>',
      '    </div>',
      '    <p class="colmeia-pref-desc">Necessários para segurança, balanceamento de carga e prevenção contra ataques cibernéticos. Não coletam dados para perfil comportamental.</p>',
      '  </div>',
      '  <div class="colmeia-pref-group">',
      '    <div class="colmeia-pref-header">',
      '      <label for="colmeia-pref-analytics" style="cursor:pointer; display:flex; align-items:center; gap:8px;">',
      '        <input type="checkbox" id="colmeia-pref-analytics"' + (currentState ? ' checked' : '') + ' style="width:16px; height:16px;">',
      '        <strong>Estatísticas de Navegação (Google Analytics)</strong>',
      '      </label>',
      '    </div>',
      '    <p class="colmeia-pref-desc">Métricas agregadas (visualizações de página e navegação geral) para melhoria contínua das páginas. Nenhum formulário ou dado confidencial é repassado ao Analytics.</p>',
      '  </div>',
      '  <div class="colmeia-consent-modal-actions">',
      '    <button type="button" id="colmeia-modal-close" class="colmeia-consent-btn colmeia-consent-btn-secondary">Fechar</button>',
      '    <button type="button" id="colmeia-modal-save" class="colmeia-consent-btn colmeia-consent-btn-primary">Salvar preferências</button>',
      '  </div>',
      '</div>'
    ].join('');

    document.body.appendChild(overlay);

    document.getElementById('colmeia-modal-close').addEventListener('click', function () {
      overlay.style.display = 'none';
    });

    document.getElementById('colmeia-modal-save').addEventListener('click', function () {
      var isChecked = document.getElementById('colmeia-pref-analytics').checked;
      setConsentState(isChecked ? 'granted' : 'denied');
      overlay.style.display = 'none';
      var banner = document.getElementById('colmeia-consent-banner');
      if (banner) banner.style.display = 'none';
    });

    overlay.addEventListener('click', function (e) {
      if (e.target === overlay) {
        overlay.style.display = 'none';
      }
    });
  }

  window.openCookiePreferences = openModal;

  // Inicialização na carga da página
  document.addEventListener('DOMContentLoaded', function () {
    var state = getConsentState();
    if (state === 'granted') {
      loadGoogleAnalytics();
    } else if (state === 'denied') {
      disableGoogleAnalytics();
    } else {
      renderConsentUI();
    }

    // Vincula gatilhos no rodapé para reabrir preferências
    document.addEventListener('click', function (e) {
      if (e.target && (e.target.matches('.cookie-pref-trigger') || e.target.closest('.cookie-pref-trigger'))) {
        e.preventDefault();
        openModal();
      }
    });
  });

})();

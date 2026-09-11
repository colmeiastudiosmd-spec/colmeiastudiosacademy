/**
 * Colmeia Studios Academy - Férias com IA
 * Comportamentos e Funcionalidades Dinâmicas da Landing Page
 */

// Inicialização do Supabase (Preparado para uso futuro)
if (typeof supabase !== 'undefined') {
    const supabaseUrl = 'https://ehxibsyifaolrdozqklk.supabase.co';
    const supabaseKey = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImVoeGlic3lpZmFvbHJkb3pxa2xrIiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODAxNjEwNzksImV4cCI6MjA5NTczNzA3OX0.jTk3iBhaGrS_srkLgGZFq0dVJudSjC4HyMWCP78eDLQ';
    window.supabaseClient = supabase.createClient(supabaseUrl, supabaseKey);
}

document.addEventListener("DOMContentLoaded", () => {
    
    /* -------------------------------------------------------------
       1. CABEÇALHO FIXO COM EFEITO DE ROLAGEM (STICKY HEADER)
       ------------------------------------------------------------- */
    const header = document.getElementById("headerMain");
    
    const handleHeaderScroll = () => {
        if (window.scrollY > 30) {
            header.classList.add("scrolled");
        } else {
            header.classList.remove("scrolled");
        }
    };
    
    window.addEventListener("scroll", handleHeaderScroll);
    // Executa uma vez no início para caso a página inicie já com scroll
    handleHeaderScroll();


    /* -------------------------------------------------------------
       2. CRONÔMETRO CONTADOR REGRESSIVO DINÂMICO
       ------------------------------------------------------------- */
    // Alvo: 1 de Julho de 2026 à meia-noite (Horário de Brasília: -03:00)
    const targetDateString = "2026-07-01T00:00:00-03:00";
    const targetTime = new Date(targetDateString).getTime();
    
    const daysEl = document.getElementById("days");
    const hoursEl = document.getElementById("hours");
    const minutesEl = document.getElementById("minutes");
    const secondsEl = document.getElementById("seconds");
    const countdownEl = document.getElementById("countdown");
    
    const updateCountdown = () => {
        if (!daysEl || !hoursEl || !minutesEl || !secondsEl) return;
        
        const now = new Date().getTime();
        const difference = targetTime - now;
        
        if (difference <= 0) {
            // Se o contador expirar
            daysEl.textContent = "00";
            hoursEl.textContent = "00";
            minutesEl.textContent = "00";
            secondsEl.textContent = "00";
            
            // Opcional: Alterar texto do banner de urgência
            const urgencyBanners = document.querySelectorAll(".hero-urgency span, .form-urgency-banner span");
            urgencyBanners.forEach(banner => {
                banner.textContent = "⏳ Inscrições Encerradas!";
            });
            return;
        }
        
        // Cálculos de tempo
        const msPerSecond = 1000;
        const msPerMinute = msPerSecond * 60;
        const msPerHour = msPerMinute * 60;
        const msPerDay = msPerHour * 24;
        
        const days = Math.floor(difference / msPerDay);
        const hours = Math.floor((difference % msPerDay) / msPerHour);
        const minutes = Math.floor((difference % msPerHour) / msPerMinute);
        const seconds = Math.floor((difference % msPerMinute) / msPerSecond);
        
        // Exibição com dois dígitos (ex: 09 ao invés de 9)
        daysEl.textContent = String(days).padStart(2, "0");
        hoursEl.textContent = String(hours).padStart(2, "0");
        minutesEl.textContent = String(minutes).padStart(2, "0");
        secondsEl.textContent = String(seconds).padStart(2, "0");
    };
    
    // Inicia e roda a cada segundo
    updateCountdown();
    setInterval(updateCountdown, 1000);


    /* -------------------------------------------------------------
       3. ACORDEÃO INTERATIVO DO FAQ
       ------------------------------------------------------------- */
    const faqTriggers = document.querySelectorAll(".faq-trigger");
    
    faqTriggers.forEach(trigger => {
        trigger.addEventListener("click", () => {
            const item = trigger.parentElement;
            const content = trigger.nextElementSibling;
            const isCurrentlyActive = item.classList.contains("active");
            
            // Fecha todos os outros itens abertos (efeito sanfona único)
            document.querySelectorAll(".faq-item").forEach(otherItem => {
                if (otherItem !== item && otherItem.classList.contains("active")) {
                    otherItem.classList.remove("active");
                    otherItem.querySelector(".faq-trigger").setAttribute("aria-expanded", "false");
                    otherItem.querySelector(".faq-content").style.maxHeight = "0px";
                }
            });
            
            // Alterna o estado do item clicado
            if (!isCurrentlyActive) {
                item.classList.add("active");
                trigger.setAttribute("aria-expanded", "true");
                content.style.maxHeight = content.scrollHeight + "px";
            } else {
                item.classList.remove("active");
                trigger.setAttribute("aria-expanded", "false");
                content.style.maxHeight = "0px";
            }
        });
    });


    /* -------------------------------------------------------------
       4. MÁSCARA DINÂMICA DE TELEFONE (WHATSAPP BRASILEIRO)
       ------------------------------------------------------------- */
    const whatsappInput = document.getElementById("parentWhatsapp");
    
    if (whatsappInput) {
        whatsappInput.addEventListener("input", (e) => {
            let value = e.target.value.replace(/\D/g, ""); // Remove tudo que não for dígito
            
            // Limita a 11 dígitos
            if (value.length > 11) {
                value = value.slice(0, 11);
            }
            
            // Aplica a formatação em tempo real
            if (value.length > 10) {
                // Celular: (XX) XXXXX-XXXX
                value = `(${value.slice(0, 2)}) ${value.slice(2, 7)}-${value.slice(7)}`;
            } else if (value.length > 6) {
                // Fixo ou celular incompleto: (XX) XXXX-XXXX
                value = `(${value.slice(0, 2)}) ${value.slice(2, 6)}-${value.slice(6)}`;
            } else if (value.length > 2) {
                // DDD e começo: (XX) XXX
                value = `(${value.slice(0, 2)}) ${value.slice(2)}`;
            } else if (value.length > 0) {
                // Apenas DDD: (XX
                value = `(${value}`;
            }
            
            e.target.value = value;
        });
    }


    /* -------------------------------------------------------------
       5. VALIDAÇÃO DO FORMULÁRIO E MENSAGEM DE SUCESSO
       ------------------------------------------------------------- */
    const form = document.getElementById("enrollmentForm");
    const formContainer = document.getElementById("formContainer");
    const successContainer = document.getElementById("successContainer");
    
    // Função auxiliar para exibir/ocultar erros
    const setError = (element, hasError) => {
        const group = element.closest(".form-group") || element.parentElement;
        if (hasError) {
            group.classList.add("has-error");
            if (element.classList.contains("form-input")) {
                element.classList.add("input-error");
            } else if (element.classList.contains("checkbox-input")) {
                group.classList.add("has-error");
            }
        } else {
            group.classList.remove("has-error");
            if (element.classList.contains("form-input")) {
                element.classList.remove("input-error");
            }
        }
    };
    
    if (form) {
        form.addEventListener("submit", (e) => {
            e.preventDefault();
        
        let isValid = true;
        let firstErrorElement = null;
        
        // 1. Validação: Nome do Responsável (Não pode ser vazio e deve ter pelo menos duas palavras)
        const parentName = document.getElementById("parentName");
        const nameVal = parentName.value.trim();
        if (nameVal === "" || nameVal.split(/\s+/).length < 2) {
            setError(parentName, true);
            isValid = false;
            if (!firstErrorElement) firstErrorElement = parentName;
        } else {
            setError(parentName, false);
        }
        
        // 2. Validação: WhatsApp (Deve ter a máscara preenchida com 10 ou 11 números)
        const whatsappDigits = whatsappInput.value.replace(/\D/g, "");
        if (whatsappDigits.length < 10 || whatsappDigits.length > 11) {
            setError(whatsappInput, true);
            isValid = false;
            if (!firstErrorElement) firstErrorElement = whatsappInput;
        } else {
            setError(whatsappInput, false);
        }
        
        // 3. Validação: E-mail (Regex de validação de e-mail comum)
        const emailInput = document.getElementById("parentEmail");
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(emailInput.value.trim())) {
            setError(emailInput, true);
            isValid = false;
            if (!firstErrorElement) firstErrorElement = emailInput;
        } else {
            setError(emailInput, false);
        }
        
        // 4. Validação: Estado UF
        const stateSelect = document.getElementById("parentState");
        if (stateSelect.value === "") {
            setError(stateSelect, true);
            isValid = false;
            if (!firstErrorElement) firstErrorElement = stateSelect;
        } else {
            setError(stateSelect, false);
        }
        
        // 5. Validação: Nome da Criança/Adolescente
        const childName = document.getElementById("childName");
        if (childName.value.trim() === "") {
            setError(childName, true);
            isValid = false;
            if (!firstErrorElement) firstErrorElement = childName;
        } else {
            setError(childName, false);
        }
        
        // 6. Validação: Idade da Criança (Número inteiro entre 8 e 17)
        const childAge = document.getElementById("childAge");
        const ageVal = parseInt(childAge.value, 10);
        if (isNaN(ageVal) || ageVal < 8 || ageVal > 17) {
            setError(childAge, true);
            isValid = false;
            if (!firstErrorElement) firstErrorElement = childAge;
        } else {
            setError(childAge, false);
        }
        
        // 7. Validação: Experiência anterior com IA
        const experienceSelect = document.getElementById("childExperience");
        if (experienceSelect.value === "") {
            setError(experienceSelect, true);
            isValid = false;
            if (!firstErrorElement) firstErrorElement = experienceSelect;
        } else {
            setError(experienceSelect, false);
        }
        
        // 8. Validação: Dispositivo de Assistência
        const deviceSelect = document.getElementById("childDevice");
        if (deviceSelect.value === "") {
            setError(deviceSelect, true);
            isValid = false;
            if (!firstErrorElement) firstErrorElement = deviceSelect;
        } else {
            setError(deviceSelect, false);
        }
        
        // 9. Validação: Checkboxes obrigatórios
        const termsCheck = document.getElementById("termsCheck");
        const supervisorCheck = document.getElementById("supervisorCheck");
        const consentCheck = document.getElementById("consentCheck");
        
        const checks = [
            { el: termsCheck, lbl: document.getElementById("lblTermsCheck") },
            { el: supervisorCheck, lbl: document.getElementById("lblSupervisorCheck") },
            { el: consentCheck, lbl: document.getElementById("lblConsentCheck") }
        ];
        
        checks.forEach(check => {
            if (!check.el.checked) {
                check.lbl.classList.add("has-error");
                isValid = false;
                if (!firstErrorElement) firstErrorElement = check.el;
            } else {
                check.lbl.classList.remove("has-error");
            }
        });
        
        // Execução se for válido
        if (isValid) {
            // Transição suave para tela de sucesso
            formContainer.style.transition = "opacity 0.4s ease";
            formContainer.style.opacity = "0";
            
            setTimeout(() => {
                formContainer.style.display = "none";
                successContainer.style.display = "block";
                
                // Rola a página suavemente até o topo do card de sucesso
                successContainer.scrollIntoView({ behavior: "smooth", block: "center" });
            }, 400);
            
            // Estruturação dos dados coletados para o Netlify Forms
            const dadosInscricao = {
                "form-name": "inscricao-projeto",
                responsavel_nome: parentName.value.trim(),
                responsavel_whatsapp: whatsappDigits,
                responsavel_email: emailInput.value.trim(),
                responsavel_estado: stateSelect.value,
                aluno_nome: childName.value.trim(),
                aluno_idade: ageVal,
                aluno_experiencia_ia: experienceSelect.value,
                aluno_dispositivo: deviceSelect.value,
                termo_responsavel: termsCheck.checked ? "aceito" : "nao_aceito",
                termo_supervisao: supervisorCheck.checked ? "aceito" : "nao_aceito",
                termo_consentimento: consentCheck.checked ? "aceito" : "nao_aceito",
                data_cadastro: new Date().toISOString()
            };
            
            // Converte os dados em formato x-www-form-urlencoded para o Netlify Forms
            const encodedBody = Object.keys(dadosInscricao)
                .map(key => encodeURIComponent(key) + "=" + encodeURIComponent(dadosInscricao[key]))
                .join("&");

            // Disparo de envio em segundo plano para o Netlify Forms
            fetch("/", {
                method: "POST",
                headers: { "Content-Type": "application/x-www-form-urlencoded" },
                body: encodedBody
            })
            .then(response => {
                if (response.ok) {
                    console.log("Inscrição enviada com sucesso para o Netlify Forms!");
                } else {
                    console.error("Falha no envio para o Netlify Forms:", response.statusText);
                }
            })
            .catch(error => {
                console.error("Erro técnico no envio para o Netlify Forms:", error);
            });
        } else if (firstErrorElement) {
            // Foco e rolagem até o primeiro campo com erro
            firstErrorElement.focus();
            firstErrorElement.scrollIntoView({ behavior: "smooth", block: "center" });
        }
    });
    }


    /* -------------------------------------------------------------
       6. ANIMAÇÃO DE ENTRADA AO ROLAR A PÁGINA (SCROLL REVEAL LEVE)
       ------------------------------------------------------------- */
    const revealElements = document.querySelectorAll(".reveal-element");
    
    const revealOnScroll = () => {
        const windowHeight = window.innerHeight;
        
        revealElements.forEach(element => {
            const elementTop = element.getBoundingClientRect().top;
            const revealPoint = 80; // Ponto de trigger (pixels acima do fundo da tela)
            
            if (elementTop < windowHeight - revealPoint) {
                element.classList.add("revealed");
            }
        });
    };
    
    // Criação de IntersectionObserver para performance e precisão modernas
    if ("IntersectionObserver" in window) {
        const revealObserver = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add("revealed");
                    observer.unobserve(entry.target); // Deixa de observar após animar uma vez
                }
            });
        }, {
            root: null, // viewport
            threshold: 0.1, // 10% do elemento visível
            rootMargin: "0px 0px -50px 0px" // Dispara um pouco antes de entrar totalmente
        });
        
        revealElements.forEach(element => {
            revealObserver.observe(element);
        });
    } else {
        // Fallback para navegadores sem suporte a IntersectionObserver
        window.addEventListener("scroll", revealOnScroll);
        revealOnScroll();
    }


    /* -------------------------------------------------------------
       7. AJUSTE DE ROLAGEM SUAVE NO BOTÃO DO HERO "VER AS AULAS"
       ------------------------------------------------------------- */
    const btnScrollCalendar = document.getElementById("btnScrollCalendar");
    
    if (btnScrollCalendar) {
        btnScrollCalendar.addEventListener("click", (e) => {
            e.preventDefault();
            const targetSection = document.getElementById("calendario");
            if (targetSection) {
                targetSection.scrollIntoView({ behavior: "smooth" });
            }
        });
    }

});

/* -------------------------------------------------------------
   8. TRACKING - MAPA DE OPORTUNIDADES
   ------------------------------------------------------------- */
window.trackMapaConversao = function(origem) {
    if (typeof fbq !== 'undefined') {
        fbq('track', 'Lead', {
            content_name: 'Mapa de Oportunidades com IA',
            content_category: 'Diagnóstico IA',
            value: 497.00,
            currency: 'BRL',
            origem_botao: origem
        });
    }
    if (typeof gtag !== 'undefined') {
        gtag('event', 'generate_lead', {
            event_category: 'CTA',
            event_label: 'Mapa de Oportunidades - ' + origem,
            value: 497,
            currency: 'BRL',
            origem_botao: origem
        });
        gtag('event', 'conversion_mapa_ia', {
            send_to: 'G-XXXXXXXXXX', // TODO: substituir G-XXXXXXXXXX pelo ID real do GA4
            origem_botao: origem,
            page_location: window.location.href
        });
    }
    console.log('[Tracking] Conversão Mapa IA registrada:', origem);
};

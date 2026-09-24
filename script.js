/**
 * Colmeia Studios Academy
 * Comportamentos e Funcionalidades Dinâmicas da Landing Page
 */

document.addEventListener("DOMContentLoaded", () => {
    
    /* -------------------------------------------------------------
       1. CABEÇALHO FIXO COM EFEITO DE ROLAGEM (STICKY HEADER)
       ------------------------------------------------------------- */
    const header = document.getElementById("headerMain");
    
    if (header) {
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
    }

    /* -------------------------------------------------------------
       2. ACORDEÃO INTERATIVO DO FAQ
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
       3. ANIMAÇÃO DE ENTRADA AO ROLAR A PÁGINA (SCROLL REVEAL LEVE)
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

});

/* -------------------------------------------------------------
   4. TRACKING - MAPA DE OPORTUNIDADES
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
    }
    console.log('[Tracking] Conversão Mapa IA registrada:', origem);
};

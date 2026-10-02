/**
 * Colmeia Studios Academy - Shared JavaScript Utilities
 * - Responsive mobile navigation toggle
 * - Sticky header elevation on scroll
 * - Accessible keyboard navigation (Esc to close menu)
 */

document.addEventListener('DOMContentLoaded', () => {
  document.documentElement.classList.add('js-ready');

  // 1. Mobile Menu Toggle
  const menuBtn = document.querySelector('.mobile-menu-btn');
  const navMenu = document.querySelector('.header-nav');

  if (menuBtn && navMenu) {
    menuBtn.addEventListener('click', () => {
      const isExpanded = menuBtn.getAttribute('aria-expanded') === 'true';
      menuBtn.setAttribute('aria-expanded', !isExpanded);
      navMenu.classList.toggle('is-open');
    });

    // Close on ESC
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && navMenu.classList.contains('is-open')) {
        menuBtn.setAttribute('aria-expanded', 'false');
        navMenu.classList.remove('is-open');
        menuBtn.focus();
      }
    });

    // Close when clicking outside
    document.addEventListener('click', (e) => {
      if (!navMenu.contains(e.target) && !menuBtn.contains(e.target) && navMenu.classList.contains('is-open')) {
        menuBtn.setAttribute('aria-expanded', 'false');
        navMenu.classList.remove('is-open');
      }
    });
  }

  // 2. Header shadow on scroll
  const header = document.querySelector('.academy-header');
  if (header) {
    const handleScroll = () => {
      if (window.scrollY > 20) {
        header.classList.add('scrolled');
      } else {
        header.classList.remove('scrolled');
      }
    };
    window.addEventListener('scroll', handleScroll, { passive: true });
    handleScroll();
  }

  // 3. Highlight current page in nav if matching
  const currentPath = window.location.pathname.replace(/\/index\.html$/, '').replace(/\/$/, '');
  const navLinks = document.querySelectorAll('.header-nav .nav-link');
  navLinks.forEach(link => {
    const linkPath = link.getAttribute('href').replace(/\/index\.html$/, '').replace(/\/$/, '');
    if (linkPath && (linkPath === currentPath || (linkPath !== '' && currentPath.startsWith(linkPath)))) {
      link.classList.add('active');
    }
  });
});

// Smooth scroll + nav highlight
document.querySelectorAll('a[href^="#"]').forEach(a => {
  a.addEventListener('click', e => {
    const target = document.querySelector(a.getAttribute('href'));
    if (target) { e.preventDefault(); target.scrollIntoView({ behavior: 'smooth' }); }
  });
});

// Nav scroll effect
const nav = document.querySelector('.nav');
window.addEventListener('scroll', () => {
  nav.style.background = window.scrollY > 50
    ? 'rgba(8,8,16,0.95)' : 'rgba(8,8,16,0.8)';
});

// Fade-in on scroll
const observer = new IntersectionObserver(entries => {
  entries.forEach(e => {
    if (e.isIntersecting) {
      e.target.classList.add('visible');
      observer.unobserve(e.target);
    }
  });
}, { threshold: 0.05, rootMargin: '0px 0px -40px 0px' });

document.querySelectorAll('.project-card, .stat, .about-text, .terminal').forEach(el => {
  el.classList.add('fade-init');
  observer.observe(el);
});

// CSS for fade animation injected via style tag
const style = document.createElement('style');
style.textContent = `
  .fade-init { opacity: 0; transform: translateY(24px); transition: opacity 0.6s ease, transform 0.6s ease; }
  .fade-init.visible { opacity: 1; transform: translateY(0); }
`;
document.head.appendChild(style);

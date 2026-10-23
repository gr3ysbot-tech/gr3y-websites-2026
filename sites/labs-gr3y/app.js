// Native anchor navigation preserves keyboard focus and URL history.
const nav = document.querySelector('.nav');
if (nav) {
  const updateNav = () => {
    nav.style.background = window.scrollY > 50
      ? 'rgba(8,8,16,0.95)' : 'rgba(8,8,16,0.8)';
  };
  window.addEventListener('scroll', updateNav, { passive: true });
  updateNav();
}
// Content stays visible by default; no scroll-triggered hiding.

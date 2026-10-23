const trigger = document.querySelector('.menu-button');
const navigation = document.getElementById('site-navigation');
function closeMenu(returnFocus = false) {
  navigation.classList.remove('open');
  trigger.setAttribute('aria-expanded', 'false');
  trigger.textContent = 'Menu';
  if (returnFocus) trigger.focus();
}
trigger.addEventListener('click', () => {
  const open = navigation.classList.toggle('open');
  trigger.setAttribute('aria-expanded', String(open));
  trigger.textContent = open ? 'Close' : 'Menu';
});
navigation.addEventListener('click', event => {
  if (event.target.closest('a')) closeMenu();
});
document.addEventListener('keydown', event => {
  if (event.key === 'Escape' && navigation.classList.contains('open')) closeMenu(true);
});
// Family links stay within the preview when served together on this computer.
if (['localhost', '127.0.0.1'].includes(location.hostname)) {
  const family = {'gr3ycapital.com': 'gr3ycapital', 'gr3ylabs.com': 'gr3ylabs', 'gr3y.io': 'gr3y-io'};
  document.querySelectorAll('a[href]').forEach(anchor => {
    const url = new URL(anchor.href);
    if (family[url.hostname]) anchor.href = `/${family[url.hostname]}/${url.hash}`;
  });
}

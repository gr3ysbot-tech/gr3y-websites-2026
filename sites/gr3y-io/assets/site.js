document.querySelectorAll('.mobile-toggle').forEach(button=>{button.addEventListener('click',()=>{const nav=document.getElementById('navigation');const open=nav.classList.toggle('open');button.setAttribute('aria-expanded',String(open));button.textContent=open?'Close':'Menu'});});document.querySelectorAll('#navigation a').forEach(a=>a.addEventListener('click',()=>{document.getElementById('navigation').classList.remove('open');const button=document.querySelector('.mobile-toggle');button.setAttribute('aria-expanded','false');button.textContent='Menu';}));
// Return focus to the menu trigger when dismissing with the keyboard.
document.addEventListener('keydown', event => {
  const nav = document.getElementById('navigation');
  const button = document.querySelector('.mobile-toggle');
  if (event.key === 'Escape' && nav?.classList.contains('open') && button) {
    nav.classList.remove('open');
    button.setAttribute('aria-expanded', 'false');
    button.textContent = 'Menu';
    button.focus();
  }
});

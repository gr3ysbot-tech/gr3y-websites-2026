/* Static-only interactions. No analytics, accounts, execution, or data collection. */
document.querySelectorAll('[data-year]').forEach(node => { node.textContent = new Date().getFullYear(); });
const menuButton = document.querySelector('.menu-toggle');
const navigation = document.querySelector('#nav');
menuButton?.addEventListener('click', () => {
 const open = menuButton.getAttribute('aria-expanded') !== 'true';
 menuButton.setAttribute('aria-expanded', String(open));
 navigation.classList.toggle('open', open);
});
navigation?.querySelectorAll('a').forEach(link => link.addEventListener('click', () => { navigation.classList.remove('open'); menuButton.setAttribute('aria-expanded', 'false'); }));
document.addEventListener('keydown', event => {
 if (event.key === 'Escape' && navigation?.classList.contains('open')) { navigation.classList.remove('open'); menuButton.setAttribute('aria-expanded', 'false'); menuButton.focus(); }
});
document.querySelectorAll('[data-filter]').forEach(button => button.addEventListener('click', () => {
 const category = button.dataset.filter;
 let shown = 0;
 document.querySelectorAll('.project').forEach(project => { project.hidden = category !== 'all' && project.dataset.category !== category; if (!project.hidden) shown++; });
 document.querySelectorAll('[data-filter]').forEach(item => { const active = item === button; item.classList.toggle('active', active); item.setAttribute('aria-pressed', String(active)); });
 const status = document.querySelector('#filter-status');
 if (status) status.textContent = `Showing ${shown} ${shown === 1 ? 'project' : 'projects'}`;
}));
let dialogTrigger;
document.querySelectorAll('[data-dialog]').forEach(button => button.addEventListener('click', () => { dialogTrigger = button; document.getElementById(button.dataset.dialog)?.showModal(); }));
document.querySelectorAll('dialog').forEach(dialog => {
 dialog.querySelector('.dialog-close')?.addEventListener('click', () => dialog.close());
 dialog.addEventListener('click', event => { if (event.target === dialog) { const rect = dialog.getBoundingClientRect(); if (event.clientX < rect.left || event.clientX > rect.right || event.clientY < rect.top || event.clientY > rect.bottom) dialog.close(); } });
 dialog.addEventListener('close', () => dialogTrigger?.focus());
});

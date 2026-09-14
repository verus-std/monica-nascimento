const form = document.querySelector('#capture-form');
form.addEventListener('submit', (event) => {
  event.preventDefault();
  const status = document.querySelector('#form-status');
  status.textContent = 'Protótipo visual: os dados não foram enviados.';
  status.hidden = false;
});
document.querySelectorAll('a[href="#inscricao"]').forEach(link => {
  link.addEventListener('click', () => {
    window.setTimeout(() => document.querySelector('#email').focus({ preventScroll: true }), 450);
  });
});

const form = document.querySelector('#capture-form');
form.addEventListener('submit', (event) => {
  event.preventDefault();
  window.location.assign(form.getAttribute('action'));
});
document.querySelectorAll('a[href="#inscricao"]').forEach(link => {
  link.addEventListener('click', () => {
    window.setTimeout(() => document.querySelector('#email').focus({ preventScroll: true }), 450);
  });
});

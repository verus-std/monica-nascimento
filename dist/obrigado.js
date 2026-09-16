const countdown = document.querySelector('[data-event-start]');
const eventTime = Date.parse(countdown.dataset.eventStart);
const units = Object.fromEntries(
  [...countdown.querySelectorAll('[data-unit]')].map(node => [node.dataset.unit, node])
);
let interval;
function updateCountdown() {
  const remaining = Math.max(0, Math.floor((eventTime - Date.now()) / 1000));
  const values = {
    days: Math.floor(remaining / 86400),
    hours: Math.floor(remaining / 3600) % 24,
    minutes: Math.floor(remaining / 60) % 60,
    seconds: remaining % 60
  };
  for (const [key, value] of Object.entries(values)) {
    units[key].textContent = String(value).padStart(2, '0');
  }
  if (remaining === 0) {
    clearInterval(interval);
    countdown.querySelector('.countdown-ended').hidden = false;
  }
}
interval = setInterval(updateCountdown, 1000);
updateCountdown();

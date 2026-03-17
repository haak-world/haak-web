const btn = document.getElementById('theme-toggle');
const html = document.documentElement;

function applyTheme(light) {
  if (light) {
    html.setAttribute('data-theme', 'light');
    btn.textContent = '\u263E';
  } else {
    html.removeAttribute('data-theme');
    btn.textContent = '\u2600';
  }
  localStorage.setItem('haak-theme', light ? 'light' : 'dark');
}

const saved = localStorage.getItem('haak-theme');
applyTheme(saved === 'light');

btn.addEventListener('click', () => {
  applyTheme(html.getAttribute('data-theme') !== 'light');
});

/* Persist the selected theme across all pages; works on GitHub Pages and locally. */
(function () {
  const themes = ['gold', 'glitch', 'zetsieri', 'gruvbox', 'monokai', 'solarized-light', 'oblivion', 'github-light', 'nord-light'];
  let saved = 'gold';
  try { saved = localStorage.getItem('henosis-theme') || 'gold'; } catch (_) {}
  if (!themes.includes(saved)) saved = 'gold';
  document.documentElement.dataset.theme = saved;
  function setup() {
    const select = document.getElementById('theme-select');
    if (!select) return;
    select.value = saved;
    select.addEventListener('change', function () {
      if (!themes.includes(select.value)) return;
      saved = select.value;
      document.documentElement.dataset.theme = saved;
      try { localStorage.setItem('henosis-theme', saved); } catch (_) {}
    });
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', setup);
  else setup();
})();

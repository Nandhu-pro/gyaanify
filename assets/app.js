document.addEventListener('DOMContentLoaded', function () {
  const body = document.body;
  const savedTheme = localStorage.getItem('gyaanify-theme') || 'light';
  const applyTheme = (theme) => {
    body.setAttribute('data-theme', theme);
    const toggle = document.querySelector('.theme-toggle');
    if (toggle) {
      toggle.textContent = theme === 'dark' ? '☀️' : '🌙';
      toggle.setAttribute('aria-label', theme === 'dark' ? 'Switch to light mode' : 'Switch to dark mode');
    }
  };
  applyTheme(savedTheme);

  const themeToggle = document.querySelector('.theme-toggle');
  if (themeToggle) {
    themeToggle.addEventListener('click', function () {
      const next = body.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
      localStorage.setItem('gyaanify-theme', next);
      applyTheme(next);
    });
  }

  const menuToggle = document.getElementById('site-menu-toggle');
  const mobileNav = document.getElementById('site-mobile-nav');
  if (menuToggle && mobileNav) {
    menuToggle.addEventListener('click', function () {
      const isOpen = !mobileNav.hidden;
      mobileNav.hidden = isOpen;
      menuToggle.setAttribute('aria-expanded', String(!isOpen));
      menuToggle.textContent = isOpen ? '☰' : '✕';
    });
  }

  const pageName = location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('.site-menu a, .site-mobile-nav a').forEach(function (link) {
    const href = link.getAttribute('href');
    const active = href === pageName || (pageName === '' && href === 'index.html');
    if (active) {
      link.setAttribute('aria-current', 'page');
    } else {
      link.removeAttribute('aria-current');
    }
  });

  const tips = [
    ['Security', 'Your UPI PIN is only for sending money. Never for receiving it.', 'If anyone asks you to scan a QR code or enter your PIN to receive money, it is a scam.'],
    ['Security', 'New number plus an urgent money request? Call the old number first.', 'Scammers pretend to be family on WhatsApp. One call to the saved number ends the scam.'],
    ['AI', 'Agree on a family code word.', 'AI can copy a voice from a few seconds of audio. It cannot copy a secret only your family knows.'],
    ['Cloud', 'Start with the official free learning paths.', 'Microsoft Learn offers beginner-friendly paths for Azure and cloud fundamentals.'],
    ['Careers', 'Show your work, not just your certificates.', 'One small project on GitHub with a short write-up says more than a list of badges.'],
    ['Security', 'Police never arrest anyone over a video call.', 'There is no “digital arrest”. Hang up, tell your family and report it immediately.'],
    ['Learning', 'Teach what you learn.', 'Explaining an idea to someone else is the fastest way to understand it yourself.']
  ];
  const tipTopic = document.getElementById('tipTopic');
  const tipText = document.getElementById('tipText');
  const tipWhy = document.getElementById('tipWhy');
  const tipCount = document.getElementById('tipCount');
  if (tipTopic && tipText && tipWhy && tipCount) {
    let index = 0;
    const renderTip = (nextIndex) => {
      index = (nextIndex + tips.length) % tips.length;
      const [topic, text, why] = tips[index];
      tipTopic.textContent = topic;
      tipText.textContent = text;
      tipWhy.textContent = why;
      tipCount.textContent = String(index + 1).padStart(2, '0') + ' / ' + String(tips.length).padStart(2, '0');
    };
    const prev = document.getElementById('tipPrev');
    const next = document.getElementById('tipNext');
    if (prev) prev.addEventListener('click', () => renderTip(index - 1));
    if (next) next.addEventListener('click', () => renderTip(index + 1));
    renderTip(Math.floor(Date.now() / 86400000) % tips.length);
  }

  function makeSearch(searchId) {
    const input = document.getElementById(searchId);
    const results = document.getElementById(searchId + '-results');
    if (!input || !results || !window.GY_INDEX) return;
    const render = () => {
      const query = input.value.trim().toLowerCase();
      results.innerHTML = '';
      if (query.length < 2) {
        results.hidden = true;
        return;
      }
      const terms = query.split(/\s+/).filter(Boolean);
      const hits = window.GY_INDEX.filter((row) => {
        const haystack = `${row.t || ''} ${row.s || ''} ${row.k || ''}`.toLowerCase();
        return terms.every((term) => haystack.includes(term));
      }).slice(0, 7);
      if (!hits.length) {
        const empty = document.createElement('p');
        empty.className = 'noresult';
        empty.textContent = 'No lessons match your search.';
        results.appendChild(empty);
      } else {
        hits.forEach((row) => {
          const link = document.createElement('a');
          link.href = row.u;
          const title = document.createElement('b');
          title.textContent = row.t;
          const meta = document.createElement('span');
          meta.textContent = row.s;
          link.appendChild(title);
          link.appendChild(meta);
          results.appendChild(link);
        });
      }
      results.hidden = false;
    };
    input.addEventListener('input', render);
    input.addEventListener('focus', render);
    input.addEventListener('keydown', function (event) {
      if (event.key === 'Escape') {
        results.hidden = true;
      }
      if (event.key === 'Enter') {
        const firstLink = results.querySelector('a');
        if (firstLink) {
          window.location.href = firstLink.href;
        }
      }
    });
    document.addEventListener('click', function (event) {
      if (event.target && !event.target.closest('.search')) {
        results.hidden = true;
      }
    });
  }
  makeSearch('homeSearch');
  makeSearch('pathSearch');

  const certGrid = document.getElementById('certGrid');
  const certSearch = document.getElementById('certSearch');
  const certFilters = document.querySelectorAll('.cert-filter');
  if (certGrid && certSearch && certFilters.length) {
    let currentFilter = 'all';
    const cards = Array.from(certGrid.querySelectorAll('.cert-card'));
    const applyFilters = () => {
      const query = certSearch.value.trim().toLowerCase();
      let visible = 0;
      cards.forEach((card) => {
        const categoryMatch = currentFilter === 'all' || card.dataset.category === currentFilter;
        const text = (card.textContent || '').toLowerCase();
        const inputMatch = !query || text.includes(query);
        const show = categoryMatch && inputMatch;
        card.hidden = !show;
        if (show) visible += 1;
      });
      const count = document.getElementById('certCount');
      if (count) count.textContent = visible + (visible === 1 ? ' certification' : ' certifications');
    };
    certSearch.addEventListener('input', applyFilters);
    certFilters.forEach((button) => {
      button.addEventListener('click', function () {
        currentFilter = button.dataset.filter || 'all';
        certFilters.forEach((item) => item.classList.toggle('is-active', item === button));
        applyFilters();
      });
    });
    applyFilters();
  }

  const skeletonSection = document.querySelector('.cert-skeletons');
  if (skeletonSection) {
    window.setTimeout(function () {
      document.querySelector('.cert-section')?.classList.add('is-loaded');
    }, 650);
  }

  const grid = document.getElementById('pathGrid');
  if (grid) {
    const state = { topic: 'all', level: 'all' };
    const apply = () => {
      let count = 0;
      grid.querySelectorAll('.pcard').forEach((card) => {
        const topicOK = state.topic === 'all' || card.dataset.topic === state.topic;
        const levelOK = state.level === 'all' || card.dataset.level === state.level;
        const visible = topicOK && levelOK;
        card.hidden = !visible;
        if (visible) count += 1;
      });
      const countNode = document.getElementById('pathCount');
      if (countNode) countNode.textContent = count + (count === 1 ? ' path' : ' paths');
    };
    const topicWrap = document.getElementById('fTopic');
    const levelWrap = document.getElementById('fLevel');
    if (topicWrap) {
      topicWrap.addEventListener('click', function (event) {
        const button = event.target.closest('.f');
        if (!button) return;
        topicWrap.querySelectorAll('.f').forEach((item) => item.classList.toggle('on', item === button));
        state.topic = button.dataset.v || 'all';
        apply();
      });
    }
    if (levelWrap) {
      levelWrap.addEventListener('click', function (event) {
        const button = event.target.closest('.f');
        if (!button) return;
        levelWrap.querySelectorAll('.f').forEach((item) => item.classList.toggle('on', item === button));
        state.level = button.dataset.v || 'all';
        apply();
      });
    }
    apply();
  }
});

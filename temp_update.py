from pathlib import Path
import re

root = Path(r'C:\Users\lakshmi\gyaanify')

css = '''
:root {
  --ms-primary: #0078D4;
  --ms-primary-dark: #106EBE;
  --ms-bg: #F3F2F1;
  --ms-bg-alt: #FFFFFF;
  --ms-surface: #FFFFFF;
  --ms-surface-soft: #F5F7FB;
  --ms-line: #D9D9D9;
  --ms-text: #1b1a19;
  --ms-muted: #4f4f4f;
  --ms-muted-soft: #6f7278;
  --ms-ink: #0f172a;
  --shadow-soft: 0 12px 28px -24px rgba(16, 110, 190, 0.45);
  --shadow-lg: 0 28px 56px -28px rgba(16, 110, 190, 0.35);
  --wrap: 1180px;
  --sans: 'Segoe UI', 'Segoe UI Variable', system-ui, -apple-system, BlinkMacSystemFont, sans-serif;
}
body[data-theme='dark'] {
  --ms-primary: #4da3ff;
  --ms-primary-dark: #8bc3ff;
  --ms-bg: #0b1220;
  --ms-bg-alt: #111b2b;
  --ms-surface: #121d2d;
  --ms-surface-soft: #172538;
  --ms-line: #2e3f59;
  --ms-text: #edf4ff;
  --ms-muted: #bfd3ee;
  --ms-muted-soft: #9db5d7;
  --ms-ink: #f4f8ff;
  --shadow-soft: 0 12px 28px -20px rgba(77, 163, 255, 0.4);
  --shadow-lg: 0 28px 56px -28px rgba(77, 163, 255, 0.26);
}
* { box-sizing: border-box; }
html { scroll-behavior: smooth; scroll-padding-top: 88px; }
body { margin: 0; background: var(--ms-bg); color: var(--ms-text); font-family: var(--sans); -webkit-font-smoothing: antialiased; text-rendering: optimizeLegibility; transition: background .25s ease, color .25s ease; }
a { color: inherit; text-decoration: none; }
img { max-width: 100%; display: block; }
main { display: block; }
button, input { font: inherit; }
[hidden] { display: none !important; }
:focus-visible { outline: 3px solid rgba(0,120,212,.35); outline-offset: 3px; }
.wrap { width: min(var(--wrap), calc(100% - 32px)); margin: 0 auto; }
.skip { position: absolute; left: -9999px; top: 12px; z-index: 100; background: var(--ms-primary-dark); color: white; padding: 10px 16px; border-radius: 10px; }
.skip:focus { left: 16px; }
.eyebrow { display: inline-block; font-size: 12px; font-weight: 700; letter-spacing: .12em; text-transform: uppercase; color: var(--ms-primary-dark); }
.lede { font-size: 1.08rem; line-height: 1.7; color: var(--ms-muted); max-width: 65ch; }
.site-header { position: sticky; top: 0; z-index: 60; background: rgba(255,255,255,.7); backdrop-filter: blur(14px); border-bottom: 1px solid rgba(217,217,217,.9); }
body[data-theme='dark'] .site-header { background: rgba(11,18,32,.7); border-bottom-color: rgba(46,63,89,.9); }
.site-nav { display: flex; align-items: center; justify-content: space-between; gap: 16px; min-height: 74px; }
.site-logo { display: inline-flex; align-items: center; gap: 12px; font-size: 1.32rem; font-weight: 700; letter-spacing: -0.04em; color: var(--ms-text); }
.site-logo-mark { width: 36px; height: 36px; display: grid; place-items: center; border-radius: 12px; background: linear-gradient(135deg, var(--ms-primary) 0%, var(--ms-primary-dark) 100%); color: white; font-size: 1rem; box-shadow: var(--shadow-soft); }
.site-menu { display: flex; align-items: center; gap: 8px; }
.site-menu a { display: inline-flex; align-items: center; justify-content: center; min-height: 40px; padding: 9px 14px; border-radius: 10px; font-weight: 600; color: var(--ms-muted); transition: .2s ease; }
.site-menu a:hover, .site-menu a[aria-current='page'] { background: rgba(0,120,212,.08); color: var(--ms-primary-dark); }
.site-header-actions { display: flex; align-items: center; gap: 12px; }
.site-profile { display: inline-flex; align-items: center; gap: 10px; padding: 6px 12px 6px 8px; border-radius: 999px; background: rgba(255,255,255,.72); border: 1px solid rgba(217,217,217,.9); box-shadow: var(--shadow-soft); }
body[data-theme='dark'] .site-profile { background: rgba(18,29,45,.7); border-color: var(--ms-line); }
.site-avatar { width: 32px; height: 32px; display: grid; place-items: center; border-radius: 50%; background: linear-gradient(135deg, #D9EEFF 0%, #C4E0FF 100%); color: var(--ms-primary-dark); font-weight: 700; font-size: .72rem; }
.site-profile-name { font-size: .84rem; font-weight: 700; }
.site-menu-toggle, .theme-toggle { display: grid; place-items: center; width: 42px; height: 42px; border-radius: 12px; border: 1px solid var(--ms-line); background: rgba(255,255,255,.75); color: var(--ms-text); cursor: pointer; transition: transform .2s ease, border-color .2s ease, background .2s ease; }
body[data-theme='dark'] .site-menu-toggle, body[data-theme='dark'] .theme-toggle { background: rgba(18,29,45,.75); }
.site-menu-toggle:hover, .theme-toggle:hover { transform: translateY(-1px); border-color: rgba(0,120,212,.45); }
.site-mobile-nav { display: none; gap: 8px; padding: 0 16px 14px; }
.site-mobile-nav a { display: block; padding: 12px 14px; border-radius: 10px; background: rgba(255,255,255,.7); border: 1px solid var(--ms-line); color: var(--ms-muted); font-weight: 600; }
body[data-theme='dark'] .site-mobile-nav a { background: rgba(18,29,45,.7); }
.site-mobile-nav a[aria-current='page'] { background: rgba(0,120,212,.08); color: var(--ms-primary-dark); }
.site-footer { margin-top: 40px; background: linear-gradient(180deg, #0F172A 0%, #0B1220 100%); color: rgba(255,255,255,.78); border-top: 1px solid rgba(255,255,255,.06); }
.site-footer-inner { padding: 56px 0 26px; }
.site-footer-grid { display: grid; grid-template-columns: 1.2fr repeat(3, minmax(0, 1fr)); gap: 26px; }
.site-footer-brand { max-width: 320px; }
.site-footer-brand p { margin-top: 14px; line-height: 1.7; color: rgba(255,255,255,.7); }
.site-footer h4 { margin: 0 0 12px; color: white; font-size: 1rem; letter-spacing: -0.02em; }
.site-footer ul { list-style: none; padding: 0; margin: 0; display: grid; gap: 10px; }
.site-footer li a { color: rgba(255,255,255,.72); }
.site-footer li a:hover { color: white; }
.site-footer-bottom { margin-top: 30px; padding-top: 20px; border-top: 1px solid rgba(255,255,255,.1); display: flex; align-items: center; justify-content: space-between; gap: 16px; flex-wrap: wrap; font-size: .9rem; color: rgba(255,255,255,.68); }
.site-social { display: flex; align-items: center; gap: 10px; flex-wrap: wrap; }
.site-social a { width: 34px; height: 34px; display: grid; place-items: center; border-radius: 50%; background: rgba(255,255,255,.06); border: 1px solid rgba(255,255,255,.08); color: white; font-weight: 700; }
.hero { padding: 54px 0 46px; background: radial-gradient(circle at top left, rgba(0,120,212,.12), transparent 26%), radial-gradient(circle at bottom right, rgba(16,110,190,.08), transparent 26%), linear-gradient(180deg, rgba(255,255,255,.35) 0%, var(--ms-bg) 100%); }
body[data-theme='dark'] .hero { background: radial-gradient(circle at top left, rgba(77,163,255,.20), transparent 24%), radial-gradient(circle at bottom right, rgba(16,110,190,.20), transparent 23%), linear-gradient(180deg, rgba(16,27,42,.00) 0%, var(--ms-bg) 100%); }
.hero-grid { display: grid; grid-template-columns: minmax(0, 1.5fr) minmax(280px, .8fr); gap: 38px; align-items: center; }
.hero-copy { max-width: 620px; }
.hero h1 { margin-top: 16px; font-size: clamp(2.7rem, 5vw, 4.3rem); line-height: 1.03; letter-spacing: -.06em; }
.hero-actions { display: flex; flex-wrap: wrap; gap: 14px; margin-top: 24px; }
.primary-btn, .secondary-btn { display: inline-flex; align-items: center; justify-content: center; gap: 8px; min-height: 48px; padding: 0 22px; border-radius: 12px; font-weight: 700; transition: transform .2s ease, box-shadow .2s ease; }
.primary-btn:hover, .secondary-btn:hover { transform: translateY(-1px); }
.primary-btn { background: linear-gradient(180deg, var(--ms-primary) 0%, var(--ms-primary-dark) 100%); color: white; box-shadow: var(--shadow-lg); }
.secondary-btn { background: rgba(255,255,255,.8); color: var(--ms-text); border: 1px solid var(--ms-line); box-shadow: var(--shadow-soft); }
body[data-theme='dark'] .secondary-btn { background: rgba(18,29,45,.8); }
.hero-search { margin-top: 26px; max-width: 620px; }
.search { position: relative; display: flex; align-items: center; gap: 10px; height: 58px; padding: 0 16px 0 14px; border-radius: 14px; background: rgba(255,255,255,.84); border: 1px solid var(--ms-line); box-shadow: var(--shadow-soft); }
body[data-theme='dark'] .search { background: rgba(18,29,45,.75); }
.search:focus-within { border-color: rgba(0,120,212,.55); box-shadow: 0 0 0 4px rgba(0,120,212,.08); }
.search .i { width: 18px; height: 18px; color: var(--ms-muted-soft); }
.search input { flex: 1; min-width: 0; border: 0; background: transparent; color: var(--ms-text); font-size: 1rem; outline: none; height: 100%; }
.results { position: absolute; left: 0; right: 0; top: calc(100% + 10px); background: rgba(255,255,255,.97); border: 1px solid var(--ms-line); border-radius: 14px; box-shadow: 0 24px 50px -30px rgba(15,23,42,.45); padding: 8px; z-index: 30; max-height: 320px; overflow: auto; }
body[data-theme='dark'] .results { background: rgba(11,18,32,.98); }
.results a { display: block; padding: 10px 12px; border-radius: 10px; }
.results a:hover { background: var(--ms-surface-soft); }
.results b { display: block; font-weight: 700; }
.results span { display: block; color: var(--ms-muted); font-size: .8rem; margin-top: 2px; }
.noresult { padding: 12px; color: var(--ms-muted); }
.hero-tags { display: flex; flex-wrap: wrap; gap: 10px; margin-top: 18px; }
.hero-tag { display: inline-flex; align-items: center; justify-content: center; padding: 8px 12px; border-radius: 999px; background: rgba(0,120,212,.08); border: 1px solid rgba(0,120,212,.12); color: var(--ms-primary-dark); font-size: .8rem; font-weight: 700; }
.insight-card { background: rgba(255,255,255,.82); border: 1px solid var(--ms-line); border-radius: 22px; box-shadow: var(--shadow-soft); padding: 22px; }
body[data-theme='dark'] .insight-card { background: rgba(18,29,45,.75); }
.insight-meta { display: flex; align-items: center; justify-content: space-between; gap: 12px; margin-bottom: 10px; }
.insight-topic { display: inline-flex; padding: 6px 10px; border-radius: 999px; background: rgba(0,120,212,.08); border: 1px solid rgba(0,120,212,.12); color: var(--ms-primary-dark); font-size: .7rem; font-weight: 700; letter-spacing: .1em; text-transform: uppercase; }
.insight-count { font-size: .72rem; font-weight: 700; color: var(--ms-muted); }
.insight-text { margin-top: 12px; font-size: clamp(1.8rem, 2.3vw, 2.3rem); line-height: 1.25; letter-spacing: -.04em; color: var(--ms-text); }
.insight-why { margin-top: 12px; line-height: 1.7; color: var(--ms-muted); }
.insight-nav { display: flex; justify-content: flex-end; gap: 10px; margin-top: 18px; }
.insight-nav button { width: 40px; height: 40px; display: grid; place-items: center; border: 1px solid var(--ms-line); border-radius: 12px; background: rgba(255,255,255,.82); color: var(--ms-text); cursor: pointer; }
body[data-theme='dark'] .insight-nav button { background: rgba(18,29,45,.8); }
.stats { border-top: 1px solid rgba(217,217,217,.8); border-bottom: 1px solid rgba(217,217,217,.8); background: rgba(255,255,255,.3); }
body[data-theme='dark'] .stats { background: rgba(18,29,45,.2); }
.stat-grid { display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); }
.stat-grid div { padding: 28px 0; }
.stat-grid b { display: block; font-size: clamp(1.9rem, 2.8vw, 2.6rem); letter-spacing: -.05em; margin-bottom: 8px; }
.stat-grid span { color: var(--ms-muted); }
.sec { padding: 72px 0; }
.sec.alt { background: rgba(255,255,255,.45); border-top: 1px solid rgba(217,217,217,.8); border-bottom: 1px solid rgba(217,217,217,.8); }
body[data-theme='dark'] .sec.alt { background: rgba(18,29,45,.2); }
.sec-head { display: flex; align-items: end; justify-content: space-between; gap: 18px; flex-wrap: wrap; margin-bottom: 26px; }
.sec-head h2 { margin-top: 10px; font-size: clamp(2rem, 3vw, 2.9rem); letter-spacing: -.05em; }
.more { display: inline-flex; align-items: center; gap: 8px; color: var(--ms-primary-dark); font-weight: 700; }
.cards { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 24px; }
.cards.two { grid-template-columns: repeat(2, minmax(0, 1fr)); }
.pcard { display: flex; flex-direction: column; background: rgba(255,255,255,.86); border: 1px solid var(--ms-line); border-radius: 22px; overflow: hidden; box-shadow: var(--shadow-soft); transition: transform .2s ease, box-shadow .2s ease, border-color .2s ease; opacity: 0; animation: fadeUp .5s ease forwards; }
body[data-theme='dark'] .pcard { background: rgba(18,29,45,.7); }
.pcard:hover { transform: translateY(-4px); border-color: rgba(0,120,212,.35); box-shadow: var(--shadow-lg); }
.thumb { position: relative; min-height: 160px; display: grid; place-items: center; color: white; background: linear-gradient(135deg, #0F172A 0%, #0E5EA8 55%, #12395A 100%); }
.thumb-topic { position: absolute; left: 18px; top: 16px; font-size: .7rem; font-weight: 700; letter-spacing: .1em; text-transform: uppercase; color: rgba(255,255,255,.8); }
.thumb-i { width: 62px; height: 62px; }
.p-grid { background-image: linear-gradient(rgba(255,255,255,.08) 1px, transparent 1px), linear-gradient(90deg, rgba(255,255,255,.08) 1px, transparent 1px); background-size: 22px 22px; }
.p-dots { background-image: radial-gradient(rgba(255,255,255,.38) 1.5px, transparent 1.6px); background-size: 12px 12px; }
.p-diag { background-image: linear-gradient(45deg, rgba(255,255,255,.08) 0 1px, transparent 1px 18px), linear-gradient(-45deg, rgba(255,255,255,.08) 0 1px, transparent 1px 18px); }
.p-rings { background-image: radial-gradient(circle at center, rgba(255,255,255,.08) 0 18%, transparent 18.5%); }
.pbody { display: grid; gap: 12px; padding: 22px 22px 20px; }
.level { display: inline-flex; justify-self: start; padding: 5px 9px; border-radius: 999px; background: rgba(0,120,212,.08); border: 1px solid rgba(0,120,212,.12); color: var(--ms-primary-dark); font-size: .72rem; font-weight: 700; letter-spacing: .08em; text-transform: uppercase; }
.pbody h3 { font-size: 1.4rem; }
.pbody p { color: var(--ms-muted); line-height: 1.65; }
.meta { display: flex; flex-wrap: wrap; align-items: center; gap: 8px; color: var(--ms-muted); font-size: .82rem; }
.meta .i { width: 15px; height: 15px; }
.steps { list-style: none; margin: 0; padding: 0; display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 22px; }
.steps li { display: block; background: rgba(255,255,255,.86); border: 1px solid var(--ms-line); border-radius: 20px; padding: 26px; box-shadow: var(--shadow-soft); }
body[data-theme='dark'] .steps li { background: rgba(18,29,45,.7); }
.steps .n { width: 38px; height: 38px; display: grid; place-items: center; margin-bottom: 14px; border-radius: 50%; background: linear-gradient(180deg, var(--ms-primary) 0%, var(--ms-primary-dark) 100%); color: white; font-weight: 700; }
.steps h3 { margin-bottom: 8px; font-size: 1.2rem; }
.steps p { color: var(--ms-muted); line-height: 1.7; }
.band { background: linear-gradient(135deg, #0F172A 0%, #0D4B74 54%, #0F6BAA 100%); color: white; padding: 58px 0; }
.band-in { display: flex; align-items: center; justify-content: space-between; gap: 24px; flex-wrap: wrap; }
.band h2 { color: white; font-size: clamp(2rem, 3vw, 3rem); letter-spacing: -.05em; }
.band p { color: rgba(255,255,255,.74); margin-top: 8px; }
.band-cta { display: flex; flex-wrap: wrap; gap: 12px; }
.btn-light, .btn-outline { display: inline-flex; align-items: center; justify-content: center; min-height: 46px; padding: 0 20px; border-radius: 12px; font-weight: 700; }
.btn-light { background: white; color: #0F172A; }
.btn-outline { border: 1px solid rgba(255,255,255,.2); color: white; }
.page-head { padding: 32px 0 10px; }
.page-head h1 { margin-top: 10px; font-size: clamp(2.4rem, 4vw, 3.7rem); letter-spacing: -.05em; }
.page-head .lede { margin-top: 12px; }
.crumbs { display: flex; align-items: center; flex-wrap: wrap; gap: 8px; color: var(--ms-muted); font-size: .9rem; }
.crumbs a:hover { color: var(--ms-primary-dark); }
.page-head .search { margin-top: 24px; }
.catalog { display: grid; grid-template-columns: 220px minmax(0, 1fr); gap: 32px; align-items: start; }
.filters { position: sticky; top: 92px; padding: 18px; border: 1px solid var(--ms-line); border-radius: 18px; background: rgba(255,255,255,.7); box-shadow: var(--shadow-soft); }
body[data-theme='dark'] .filters { background: rgba(18,29,45,.7); }
.filters h4 { margin: 12px 0 8px; font-size: .72rem; letter-spacing: .1em; text-transform: uppercase; color: var(--ms-muted); }
.filters h4:first-child { margin-top: 0; }
.fgroup { display: grid; gap: 8px; }
.f { width: 100%; text-align: left; border-radius: 10px; padding: 10px 12px; border: 1px solid transparent; background: transparent; color: var(--ms-muted); font-weight: 600; cursor: pointer; }
.f:hover { background: rgba(0,120,212,.05); color: var(--ms-primary-dark); }
.f.on { background: linear-gradient(180deg, var(--ms-primary) 0%, var(--ms-primary-dark) 100%); color: white; border-color: transparent; }
.resultcount { color: var(--ms-muted); margin-bottom: 14px; }
.empty { padding: 32px 0; color: var(--ms-muted); }
.certify-toolbar { display: flex; flex-wrap: wrap; align-items: center; gap: 12px; margin-bottom: 20px; }
.certify-toolbar .search { max-width: 420px; flex: 1 1 260px; }
.cert-filter-bar { display: flex; flex-wrap: wrap; gap: 10px; }
.cert-filter { display: inline-flex; align-items: center; justify-content: center; min-height: 38px; padding: 0 14px; border-radius: 999px; border: 1px solid var(--ms-line); background: rgba(255,255,255,.72); color: var(--ms-muted); cursor: pointer; font-weight: 600; }
body[data-theme='dark'] .cert-filter { background: rgba(18,29,45,.7); }
.cert-filter.is-active { background: rgba(0,120,212,.08); border-color: rgba(0,120,212,.2); color: var(--ms-primary-dark); }
.cert-grid { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 24px; }
.cert-card { display: flex; flex-direction: column; height: 100%; background: rgba(255,255,255,.86); border: 1px solid var(--ms-line); border-radius: 22px; box-shadow: var(--shadow-soft); overflow: hidden; transition: transform .22s ease, box-shadow .22s ease, border-color .22s ease; opacity: 0; animation: fadeUp .5s ease forwards; }
body[data-theme='dark'] .cert-card { background: rgba(18,29,45,.7); }
.cert-card:hover { transform: translateY(-4px); box-shadow: var(--shadow-lg); border-color: rgba(0,120,212,.3); }
.cert-card[hidden] { display: none !important; }
.cert-card .thumb { min-height: 140px; }
.cert-body { padding: 20px 20px 22px; display: grid; gap: 12px; }
.cert-body h3 { font-size: 1.3rem; }
.cert-meta { color: var(--ms-muted); font-size: .82rem; }
.cert-progress { display: grid; gap: 8px; }
.cert-progress .bar { height: 8px; background: rgba(217,217,217,.9); border-radius: 999px; overflow: hidden; }
.cert-progress .bar span { display: block; width: var(--value, 50%); height: 100%; background: linear-gradient(90deg, var(--ms-primary) 0%, var(--ms-primary-dark) 100%); }
.cert-skeletons { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 24px; }
.cert-skeleton { min-height: 250px; border-radius: 22px; background: rgba(255,255,255,.7); border: 1px solid var(--ms-line); position: relative; overflow: hidden; box-shadow: var(--shadow-soft); }
body[data-theme='dark'] .cert-skeleton { background: rgba(18,29,45,.7); }
.cert-skeleton::after { content: ''; position: absolute; inset: 0; transform: translateX(-100%); background: linear-gradient(90deg, transparent, rgba(255,255,255,.45), transparent); animation: shimmer 1.25s infinite; }
body[data-theme='dark'] .cert-skeleton::after { background: linear-gradient(90deg, transparent, rgba(255,255,255,.12), transparent); }
.is-loaded .cert-skeletons { display: none; }
@keyframes fadeUp { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }
@keyframes shimmer { 100% { transform: translateX(100%); } }
@media (max-width: 980px) {
  .site-menu { display: none; }
  .site-menu-toggle { display: grid; }
  .site-mobile-nav { display: grid; }
  .site-profile-name { display: none; }
  .hero-grid, .path-hero-grid, .catalog, .path-layout { grid-template-columns: 1fr; }
  .cards, .cert-grid, .cert-skeletons { grid-template-columns: repeat(2, minmax(0, 1fr)); }
  .steps { grid-template-columns: 1fr; }
  .site-footer-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); }
  .stat-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); }
}
@media (max-width: 640px) {
  .cards, .cards.two, .cert-grid, .cert-skeletons, .stat-grid, .site-footer-grid { grid-template-columns: 1fr; }
  .hero { padding-top: 40px; }
  .hero-actions, .band-cta { width: 100%; }
  .hero-actions a, .band-cta a { flex: 1 1 100%; }
  .site-footer-bottom { flex-direction: column; align-items: flex-start; }
  .site-nav { min-height: 68px; }
  .row { grid-template-columns: 1fr; }
  .wrap { width: min(var(--wrap), calc(100% - 24px)); }
  .certify-toolbar { align-items: stretch; }
  .certify-toolbar .search { max-width: none; }
}
'''
(root / 'assets' / 'style.css').write_text(css.strip() + '\n', encoding='utf-8')

js = '''document.addEventListener('DOMContentLoaded', function () {
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
'''
(root / 'assets' / 'app.js').write_text(js, encoding='utf-8')

index = root / 'index.html'
text = index.read_text(encoding='utf-8')
needle = '<section class="sec alt">'
replacement = '''<section class="sec cert-section"><div class="wrap"><div class="sec-head"><div><span class="eyebrow">Career roadmap</span><h2>Certifications built for real growth</h2></div><a class="more" href="azure.html">Explore all certifications →</a></div><div class="certify-toolbar"><div class="search" role="search"><svg class="i" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="M20 20L16.5 16.5"/></svg><input id="certSearch" type="search" placeholder="Search certifications" aria-label="Search certifications"></div><div class="cert-filter-bar" aria-label="Certification filters"><button type="button" class="cert-filter is-active" data-filter="all">All</button><button type="button" class="cert-filter" data-filter="fundamentals">Fundamentals</button><button type="button" class="cert-filter" data-filter="associate">Associate</button><button type="button" class="cert-filter" data-filter="ai">AI</button></div></div><p class="resultcount" id="certCount">4 certifications</p><div class="cert-skeletons" aria-hidden="true"><div class="cert-skeleton"></div><div class="cert-skeleton"></div><div class="cert-skeleton"></div></div><div class="cert-grid" id="certGrid"><a class="cert-card" href="cert-az-900.html" data-category="fundamentals"><div class="thumb p-grid"><span class="thumb-topic">AZ-900</span><svg class="thumb-i" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 11.5l5.5 5.5L20 1"/></svg></div><div class="cert-body"><span class="level">Fundamentals</span><h3>Azure Fundamentals</h3><p>Learn cloud concepts, governance, pricing, and core Azure services.</p><div class="cert-progress"><div class="meta">Completion: 72%</div><div class="bar"><span style="--value:72%"></span></div></div></div></a><a class="cert-card" href="cert-ai-901.html" data-category="ai"><div class="thumb p-rings"><span class="thumb-topic">AI-900</span><svg class="thumb-i" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="5" y="5" width="14" height="14" rx="3"/><path d="M9 9h6v6H9z"/></svg></div><div class="cert-body"><span class="level">AI</span><h3>Azure AI Fundamentals</h3><p>Understand AI workloads, ML foundations, and responsible AI practices.</p><div class="cert-progress"><div class="meta">Completion: 58%</div><div class="bar"><span style="--value:58%"></span></div></div></div></a><a class="cert-card" href="cert-az-104.html" data-category="associate"><div class="thumb p-dots"><span class="thumb-topic">AZ-104</span><svg class="thumb-i" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 18V6h16v12M8 10h8M8 14h5"/></svg></div><div class="cert-body"><span class="level">Associate</span><h3>Azure Administrator</h3><p>Build operational confidence across Azure networking, identity, and compute.</p><div class="cert-progress"><div class="meta">Completion: 46%</div><div class="bar"><span style="--value:46%"></span></div></div></div></a><a class="cert-card" href="cert-az-400.html" data-category="associate"><div class="thumb p-diag"><span class="thumb-topic">AZ-400</span><svg class="thumb-i" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="5" cy="12" r="2.5"/><circle cx="19" cy="6" r="2.5"/><circle cx="19" cy="18" r="2.5"/><path d="M7.5 12h4l5-6M11.5 12l5 6"/></svg></div><div class="cert-body"><span class="level">Associate</span><h3>Azure DevOps Engineer</h3><p>Master continuous delivery, automation, and secure development workflows.</p><div class="cert-progress"><div class="meta">Completion: 35%</div><div class="bar"><span style="--value:35%"></span></div></div></div></a></div></div></section><section class="sec alt">'''
if 'certify-toolbar' not in text:
    text = text.replace(needle, replacement)
if 'theme-toggle' not in text:
    text = text.replace('<div class="site-header-actions">', '<div class="site-header-actions">\n      <button class="theme-toggle" type="button" aria-label="Switch to dark mode" title="Toggle color mode">🌙</button>')
text = text.replace('href="src/style.css"', 'href="assets/style.css"')
if '<script src="assets/app.js"></script>' not in text:
    text = text.replace('</body>', '<script src="assets/app.js"></script>\n</body>')
index.write_text(text, encoding='utf-8')

for html in root.glob('*.html'):
    text = html.read_text(encoding='utf-8')
    if 'theme-toggle' not in text:
        text = text.replace('<div class="site-header-actions">', '<div class="site-header-actions">\n      <button class="theme-toggle" type="button" aria-label="Switch to dark mode" title="Toggle color mode">🌙</button>')
    text = text.replace('href="src/style.css"', 'href="assets/style.css"')
    if '<script src="assets/app.js"></script>' not in text:
        text = text.replace('</body>', '<script src="assets/app.js"></script>\n</body>')
    html.write_text(text, encoding='utf-8')

print('Done')

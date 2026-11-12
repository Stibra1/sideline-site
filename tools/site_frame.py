"""The site's frame (Nov 2026), shared by the front pages (make_home.py) and the support and privacy
pages (make_shared_pages.py): skip link, header with a short menu and a menu button on phones, the
phone menu, and the footer in columns. The same design rules as spons.sideline.no; styles in
assets/site.css, behaviour in assets/site.js."""

from __future__ import annotations

SPONS = "https://spons.sideline.no"
YEAR = 2026
COMPANY = "Braastad Software &amp; App Utvikling"
ORG_NO = "938 698 503"
ADDRESS = "Brokvollveien 12, 3032 Drammen"

APP_STORE = {
    "spons": "6824289338",
    "insights": "6818266063",
    "handball": "6817756823",
    "football": "6816678735",
    "basketball": "6819058783",
}
GOOGLE_PLAY_SPONS = "https://play.google.com/store/apps/details?id=no.braastad.sideline.spons"

T = {
    "nb": {
        "home": "/", "other": "en", "other_home": "/en/", "other_label": "English", "here_label": "Norsk",
        "spons": SPONS, "spons_how": f"{SPONS}/slik-fungerer-det", "spons_price": f"{SPONS}/pris",
        "spons_join": f"{SPONS}/bli-med", "spons_login": f"{SPONS}/login", "spons_new": f"{SPONS}/new",
        "spons_vipps": f"{SPONS}/spons-og-vipps",
        "skip": "Hopp til innhold", "menu": "Meny", "close": "Lukk meny", "main_nav": "Hovedmeny",
        "nav_spons": "Spons", "nav_apps": "Appene", "nav_about": "Om oss", "nav_support": "Støtte",
        "have_code": "Har du lagkode?", "login": "Logg inn", "start": "Prøv Spons gratis",
        "tagline": "Apper for trenere, lagledere og foreldre. Fra benken til lagkassa.",
        "col_spons": "Sideline Spons", "col_apps": "Apper", "col_company": "Sideline",
        "how": "Slik fungerer det", "pricing": "Pris", "vipps": "Spons og Vipps",
        "support": "Støtte", "privacy": "Personvern", "contact": "Kontakt", "cookies": "Informasjonskapsler",
        "langs": "Språk", "org": "Org.nr.", "store_country": "no",
    },
    "en": {
        "home": "/en/", "other": "nb", "other_home": "/", "other_label": "Norsk", "here_label": "English",
        "spons": f"{SPONS}/en", "spons_how": f"{SPONS}/en/how-it-works", "spons_price": f"{SPONS}/en/pricing",
        "spons_join": f"{SPONS}/en/join-a-team", "spons_login": f"{SPONS}/login", "spons_new": f"{SPONS}/new",
        "spons_vipps": None,
        "skip": "Skip to content", "menu": "Menu", "close": "Close menu", "main_nav": "Main menu",
        "nav_spons": "Spons", "nav_apps": "Apps", "nav_about": "About us", "nav_support": "Support",
        "have_code": "Got a team code?", "login": "Sign in", "start": "Try Spons for free",
        "tagline": "Apps for coaches, team managers and parents. From the bench to the team kitty.",
        "col_spons": "Sideline Spons", "col_apps": "Apps", "col_company": "Sideline",
        "how": "How it works", "pricing": "Pricing", "vipps": None,
        "support": "Support", "privacy": "Privacy", "contact": "Contact", "cookies": "Cookies",
        "langs": "Language", "org": "Org. no.", "store_country": "gb",
    },
}

MENU_ICON = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16"/></svg>'
CLOSE_ICON = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 6l12 12M18 6 6 18"/></svg>'


def app_store(app: str, lang: str) -> str:
    return f"https://apps.apple.com/{T[lang]['store_country']}/app/id{APP_STORE[app]}"


def logo(lang: str) -> str:
    return f'<a class="mark" href="{T[lang]["home"]}"><span class="mark__sideline">Sideline</span></a>'


def nav_items(lang: str) -> list[tuple[str, str]]:
    t = T[lang]
    return [
        (t["spons"], t["nav_spons"]),
        (f"{t['home']}#apper", t["nav_apps"]),
        (f"{t['home']}#om", t["nav_about"]),
        ("/support/" if lang == "nb" else "/support/en/", t["nav_support"]),
    ]


def langs(lang: str, here: str, there: str) -> str:
    t = T[lang]
    a = f'<a href="{there}" hreflang="{t["other"]}" lang="{t["other"]}">{t["other_label"]}</a>'
    s = f"<span>{t['here_label']}</span>"
    return f'<nav class="langs" aria-label="{t["langs"]}">' + (s + a if lang == "nb" else a + s) + "</nav>"


def header(lang: str, here: str, there: str) -> str:
    """Skip link, header and phone menu. `here`/`there`: this page and the same page in the other language."""
    t = T[lang]
    items = nav_items(lang)
    nav = "".join(f'<li><a href="{h}">{label}</a></li>' for h, label in items)
    menu = "".join(f'<li><a href="{h}">{label}</a></li>' for h, label in items)
    menu += f'<li><a href="{t["spons_join"]}">{t["have_code"]}</a></li><li><a href="{t["spons_login"]}">{t["login"]}</a></li>'
    return f"""<a class="skiplink" href="#innhold">{t['skip']}</a>
<header class="sitebar"><div class="sitebar__inner">
{logo(lang)}
<nav class="sitebar__nav" aria-label="{t['main_nav']}"><ul>{nav}</ul></nav>
<div class="sitebar__end">
<a class="sitebar__text" href="{t['spons_join']}">{t['have_code']}</a>
<a class="sitebar__text" href="{t['spons_login']}">{t['login']}</a>
<a class="btn btn--primary sitebar__cta" href="{t['spons_new']}">{t['start']}</a>
<button type="button" class="sitebar__menu" aria-expanded="false" aria-controls="sitemenu" aria-label="{t['menu']}" data-menu-toggle>{MENU_ICON}</button>
</div>
</div></header>
<div class="sitemenu" id="sitemenu-wrap" hidden>
<div class="sitemenu__panel" id="sitemenu" role="dialog" aria-modal="true" aria-label="{t['menu']}">
<div class="sitemenu__head">{logo(lang)}<button type="button" class="sitebar__menu" aria-label="{t['close']}" data-menu-close>{CLOSE_ICON}</button></div>
<nav aria-label="{t['main_nav']}"><ul class="sitemenu__list">{menu}</ul></nav>
<a class="btn btn--primary btn--block" href="{t['spons_new']}">{t['start']}</a>
<div class="sitemenu__lang">{langs(lang, here, there)}</div>
</div>
</div>"""


def footer(lang: str, here: str, there: str) -> str:
    t = T[lang]
    spons = [(t["spons_how"], t["how"]), (t["spons_price"], t["pricing"]), (t["spons_join"], t["have_code"])]
    if t["spons_vipps"]:
        spons.append((t["spons_vipps"], t["vipps"]))
    apps = [(app_store(a, lang), f"Sideline: {a.capitalize()}") for a in ("insights", "football", "handball", "basketball")]
    support = "/support/" if lang == "nb" else "/support/en/"
    privacy = "/privacy/" if lang == "nb" else "/privacy/en/"
    company = [(support, t["support"]), (privacy, t["privacy"]), ("mailto:support@sideline.no", t["contact"])]

    def col(title, links, extra=""):
        lis = "".join(f'<li><a href="{h}">{label}</a></li>' for h, label in links)
        return f'<nav class="sitefoot__col" aria-label="{title}"><h2 class="sitefoot__title">{title}</h2><ul>{lis}{extra}</ul></nav>'

    return f"""<footer class="sitefoot">
<div class="sitefoot__grid">
<div class="sitefoot__brand">{logo(lang)}<p>{t['tagline']}</p></div>
{col(t['col_spons'], spons)}
{col(t['col_apps'], apps)}
{col(t['col_company'], company, f'<li><a href="#" data-consent-settings>{t["cookies"]}</a></li>')}
</div>
<div class="sitefoot__bottom">
{langs(lang, here, there)}
<p>© {YEAR} {COMPANY} · {t['org']} {ORG_NO} · {ADDRESS} · <a href="mailto:support@sideline.no">support@sideline.no</a></p>
</div>
</footer>
<script src="/assets/site.js" defer></script>"""


FONT_PRELOAD = ('<link rel="preload" href="/assets/fonts/plus-jakarta-sans-latin-wght-normal.woff2" as="font" type="font/woff2" crossorigin>\n'
                '<link rel="preload" href="/assets/fonts/oswald-latin-wght-normal.woff2" as="font" type="font/woff2" crossorigin>')


def modern_head(html_head: str) -> str:
    """Light by default, dark on dark devices; the fonts early."""
    return (html_head
            .replace('<meta name="theme-color" content="#000000">',
                     '<meta name="theme-color" content="#F3F2EE" media="(prefers-color-scheme: light)">\n'
                     '<meta name="theme-color" content="#000000" media="(prefers-color-scheme: dark)">')
            .replace('<meta name="color-scheme" content="dark">', '<meta name="color-scheme" content="light dark">'))

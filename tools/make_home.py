#!/usr/bin/env python3
"""Writes the front pages, / (NB) and /en/ (EN), in the design of spons.sideline.no (Nov 2026).

    python3 tools/make_home.py

The head (meta, structured data) comes from tools/home_head_{nb,en}.html; the frame from site_frame.py.
Spons first (the main offering, everything links to spons.sideline.no), then the other Sideline apps.
"""

from __future__ import annotations

from pathlib import Path

from site_frame import (ADDRESS, COMPANY, FONT_PRELOAD, GOOGLE_PLAY_SPONS, ORG_NO, T, app_store, footer,
                        header, modern_head)

ROOT = Path(__file__).resolve().parents[1]
TOOLS = Path(__file__).resolve().parent

C = {
    "nb": {
        "photo_alt": "Jentelag i Sideline-drakter foran fotballmålet",
        "kicker": "Sideline",
        "h1": "Apper for trenere, lagledere og foreldre",
        "lead": "Nyest fra oss er Sideline Spons: familie og venner sponser hvert mål, og pengene går rett til lagkassa.",
        "note": "30 dager gratis · Ingen kort",
        "more": "Se alle appene fra Sideline ↓",
        "phone_alt": "Lagets side i Spons-appen: det laget har samlet inn, hva du skal betale og betalingsknappen",
        "trust_label": "Om Sideline",
        "trust": ["Vipps rett til lagkassa", f"{COMPANY}, org.nr. {ORG_NO}", "iPhone, Android og nett"],
        "s_kicker": "Sideline Spons",
        "s_title": "Hvert mål gir penger i lagkassa",
        "s_lead": 'Målspons og digital dugnad for idrettslaget. Familie og venner velger selv beløp per mål, per seier og når laget holder nullen. Spons regner ut og minner på, og pengene går rett til laget, aldri via oss.',
        "steps": [
            ("Laget opprettes på 5 min", "Laglederen eller dugnadsansvarlig oppretter Sponsen i appen eller på nett, legger inn kampene og deler lagkoden."),
            ("Familie og venner velger kr per mål", "Hver støttespiller velger beløp per mål, seier eller holdt null, med et maksbeløp så ingen får overraskelser."),
            ("Vipps etter kampen", "Laglederen legger inn resultatet. Alle får varsel om hva de skal gi, og betaler rett til lagkassa med Vipps."),
        ],
        "how": "Slik fungerer det", "pricing": "Se priser",
        "topics_label": "Les mer om Spons",
        "topics": [("/malspons", "Målspons for idrettslag"), ("/alternativ-til-dugnad", "Alternativ til dugnad"), ("/digital-dugnad", "Digital dugnad")],
        "film": "Ta kontakt og vi hjelper deg med å komme i gang:",
        "film_label": "Slik kommer laget i gang med Spons, film på 45 sekunder",
        "vipps_title": "Betal med Vipps – rett til lagkassa",
        "vipps_text": "Sideline Spons er godkjent Vipps-partner. Supporterne trykker «Betal» i appen og betaler med Vipps rett til lagets Vipps boks. Sideline rører aldri pengene.",
        "vipps_more": "Les om Spons og Vipps",
        "a_title": "Flere apper fra Sideline",
        "a_lead": "Vi lager også apper for treneren på sidelinjen: kamptavle, laguttak, bytter, spilletid og statistikk.",
        "apps": [
            ("insights", "nb-football_overview.jpg", "Sideline: Insights", "Kampstatistikk og heatmaps for fotball og håndball.", "Spillerkort med heatmap over skudd på fotballbanen"),
            ("football", "nb-football_app.jpg", "Sideline: Football", "Kamptavle for fotball: laguttak, bytter og spilletid.", "Fotballbane med laguttak, kampklokke og benk"),
            ("handball", "nb-handball_app.jpg", "Sideline: Handball", "Kamptavle for håndball: laguttak, bytter og spilletid.", "Håndballbane med spillere, kampklokke og benk"),
            ("basketball", "nb-basketball_app.jpg", "Sideline: Basketball", "Skudd, fouls og spillerstatistikk for basketballtrenere.", "Heatmap over skudd på basketballbanen"),
        ],
        "store_alt": "Last ned i App Store", "gp_alt": "Last ned på Google Play", "badge": "nb",
        "o_title": "Om Sideline",
        "o_text": [
            f"Sideline lages av {COMPANY} i Drammen. Appene utvikles og driftes av Stian Braastad, en ivrig fotball- og håndballpappa som lager det han selv savnet på sidelinjen.",
            "Spørsmål eller ønsker? Skriv til <a href=\"mailto:support@sideline.no\">support@sideline.no</a>, så svarer vi.",
        ],
        "f_title": "Klar for en enklere dugnad?",
        "f_text": "Opprett laget i Spons på noen minutter. 30 dager gratis, ingen kort.",
    },
    "en": {
        "photo_alt": "Girls' football team in Sideline shirts in front of the goal",
        "kicker": "Sideline",
        "h1": "Apps for coaches, team managers and parents",
        "lead": "Our newest is Sideline Spons: family and friends sponsor every goal, and the money goes straight to the team.",
        "note": "30 days free · No card",
        "more": "See all the Sideline apps ↓",
        "phone_alt": "The team's page in the Spons app: what the team has raised, what you owe and the pay button",
        "trust_label": "About Sideline",
        "trust": ["Payments go straight to the team", f"{COMPANY}, org. no. {ORG_NO}", "iPhone, Android and web"],
        "s_kicker": "Sideline Spons",
        "s_title": "Every goal fills the team kitty",
        "s_lead": "Per-goal pledges and online fundraising for your team. Family and friends choose an amount per goal, per win and for a clean sheet. Spons does the maths and the reminders, and the money goes straight to the team, never through us.",
        "steps": [
            ("Set up the team in 5 minutes", "The team leader or fundraising lead sets up Spons in the app or on the web, adds the matches and shares the team code."),
            ("Family and friends choose an amount per goal", "Each supporter picks an amount per goal, win or clean sheet, with a cap so nobody gets a surprise."),
            ("Pay after the match", "The team leader enters the result. Everyone is told what they give and pays the team directly."),
        ],
        "how": "How it works", "pricing": "See pricing",
        "topics_label": "More about Spons",
        "topics": [("/en/sponsor-a-goal", "Sponsor a goal"), ("/en/fundraising-without-raffles", "Fundraising without raffles"), ("/en/online-fundraising", "Online fundraising")],
        "film": None, "film_label": None,
        "vipps_title": None,
        "a_title": "More apps from Sideline",
        "a_lead": "We also make apps for the coach on the sideline: match board, line-ups, substitutions, playing time and stats.",
        "apps": [
            ("insights", "en-football_overview.jpg", "Sideline: Insights", "Match stats and heat maps for football and handball.", "Player card with a shot heat map on the football pitch"),
            ("football", "en-football_app.jpg", "Sideline: Football", "Match board for football: line-ups, subs and playing time.", "Football pitch with line-up, match clock and bench"),
            ("handball", "en-handball_app.jpg", "Sideline: Handball", "Match board for handball: line-ups, subs and court time.", "Handball court with players, match clock and bench"),
            ("basketball", "en-basketball_app.jpg", "Sideline: Basketball", "Shots, fouls and player stats for basketball coaches.", "Shot heat map on the basketball court"),
        ],
        "store_alt": "Download on the App Store", "gp_alt": "Get it on Google Play", "badge": "en",
        "o_title": "About Sideline",
        "o_text": [
            f"Sideline is made by {COMPANY} in Drammen, Norway. The apps are built and run by Stian Braastad, a keen football and handball dad who makes what he missed on the sideline himself.",
            "Questions or ideas? Write to <a href=\"mailto:support@sideline.no\">support@sideline.no</a> and we will answer.",
        ],
        "f_title": "Ready for an easier fundraiser?",
        "f_text": "Set up your team in Spons in a few minutes. 30 days free, no card.",
    },
}

ICONS = {
    "pay": '<rect x="3.5" y="6" width="17" height="12" rx="2"/><path d="M3.5 10h17M7 14.5h3"/>',
    "company": '<path d="M12 3 4.5 6v5.5c0 4.6 3.2 8.4 7.5 9.5 4.3-1.1 7.5-4.9 7.5-9.5V6z"/><path d="m8.8 12 2.2 2.2 4.4-4.4"/>',
    "devices": '<rect x="7" y="2.5" width="10" height="19" rx="2.2"/><path d="M11 18.5h2"/>',
}


def page(lang: str) -> str:
    t, c = T[lang], C[lang]
    here, there = t["home"], t["other_home"]
    head = modern_head((TOOLS / f"home_head_{lang}.html").read_text())
    # Safari's App Store banner for Spons, the main offering.
    head = head.replace('content="app-id=6818266063"', 'content="app-id=6824289338"')
    head = head.replace("Braastad Software og App Utvikling", COMPANY)
    head += f"\n{FONT_PRELOAD}\n<link rel=\"stylesheet\" href=\"/assets/site.css\">\n</head>"
    badge = c["badge"]
    store = f'<a class="badge" href="{app_store("spons", lang)}"><img src="/assets/badges/app-store-{badge}.svg" width="150" height="50" alt="{c["store_alt"]}" loading="lazy"></a>'
    gp = f'<a class="badge gp" href="{GOOGLE_PLAY_SPONS}&amp;hl={"no" if lang == "nb" else "en"}"><img src="/assets/badges/google-play-{badge}.png" width="168" height="65" alt="{c["gp_alt"]}" loading="lazy"></a>'

    steps = "".join(f'<li><span class="steps__n" aria-hidden="true">{i}</span><h3>{h}</h3><p>{p}</p></li>'
                    for i, (h, p) in enumerate(c["steps"], 1))
    topics = "".join(f'<li><a href="https://spons.sideline.no{p}">{label}</a></li>' for p, label in c["topics"])
    if c["film"]:
        film = f"""<figure class="spons__film">
<div class="phone"><video src="/assets/video/spons-howto-nb.mp4" poster="/assets/video/spons-howto-nb.jpg" width="720" height="1280" autoplay muted loop playsinline controls preload="metadata" aria-label="{c['film_label']}"></video></div>
<figcaption>{c['film']} <a href="mailto:support@sideline.no">support@sideline.no</a></figcaption>
</figure>"""
    else:
        film = f"""<figure class="spons__film"><div class="phone"><img src="/assets/img/spons-home-en.webp" width="540" height="1108" alt="{c['phone_alt']}" loading="lazy"></div></figure>"""
    vipps = ""
    if c["vipps_title"]:
        vipps = f"""<div class="vipps"><img src="/assets/img/vipps-paymark.svg" width="104" height="65" alt="Vipps">
<div><h3>{c['vipps_title']}</h3><p>{c['vipps_text']}</p><p><a class="homelink" href="{t['spons_vipps']}">{c['vipps_more']} →</a></p></div></div>"""

    apps = "".join(f"""<article class="app">
<img class="app__shot" src="/assets/img/{shot}" width="600" height="1298" alt="{alt}" loading="lazy">
<div><h3>{name}</h3><p>{text}</p>
<p class="badges"><a class="badge" href="{app_store(app, lang)}"><img src="/assets/badges/app-store-{badge}.svg" width="150" height="50" alt="{c['store_alt']}" loading="lazy"></a></p></div>
</article>""" for app, shot, name, text, alt in c["apps"])
    trust = "".join(f'<li><svg viewBox="0 0 24 24" aria-hidden="true">{ICONS[k]}</svg><span>{v}</span></li>'
                    for k, v in zip(("pay", "company", "devices"), c["trust"]))
    about = "".join(f"<p>{p}</p>" for p in c["o_text"])

    return f"""{head}
<body class="site">
{header(lang, here, there)}
<main id="innhold" tabindex="-1">
<section class="hero" aria-labelledby="hero-title">
<picture class="hero__photo"><source type="image/webp" srcset="/assets/photos/team-sideline-800.webp 800w, /assets/photos/team-sideline-1600.webp 1600w" sizes="100vw"><img src="/assets/photos/team-sideline-800.jpg" width="2210" height="900" alt="{c['photo_alt']}" fetchpriority="high"></picture>
<div class="hero__inner">
<div>
<p class="hero__kicker">{c['kicker']}</p>
<h1 id="hero-title" class="hero__title">{c['h1']}</h1>
<p class="hero__lead">{c['lead']}</p>
<a class="btn btn--primary btn--lg hero__cta" href="{t['spons_new']}">{t['start']}</a>
<p class="hero__note">{c['note']}</p>
<p class="hero__more"><a href="#apper">{c['more']}</a></p>
</div>
<div class="hero__visual"><div class="phone"><img src="/assets/img/spons-home-{lang}.webp" width="540" height="1108" alt="{c['phone_alt']}" fetchpriority="high"></div></div>
</div>
</section>
<ul class="trust" aria-label="{c['trust_label']}">{trust}</ul>
<div class="home">
<section class="spons" aria-labelledby="spons-title">
<div>
<p class="kicker">{c['s_kicker']}</p>
<h2 id="spons-title" class="section-title">{c['s_title']}</h2>
<p class="section-lead">{c['s_lead']}</p>
<ol class="steps">{steps}</ol>
<div class="spons__actions" style="margin-top:24px"><a class="btn btn--primary" href="{t['spons_new']}">{t['start']}</a><a class="btn btn--ghost" href="{t['spons_price']}">{c['pricing']}</a><a class="homelink" href="{t['spons_how']}">{c['how']} →</a></div>
<p class="badges" style="margin-top:18px">{store}{gp}</p>
<ul class="topics" style="margin-top:14px" aria-label="{c['topics_label']}">{topics}</ul>
{vipps and '<div style="margin-top:28px">' + vipps + '</div>'}
</div>
{film}
</section>
<section id="apper" aria-labelledby="apps-title">
<h2 id="apps-title" class="section-title">{c['a_title']}</h2>
<p class="section-lead">{c['a_lead']}</p>
<div class="apps">{apps}</div>
</section>
<section id="om" class="about" aria-labelledby="about-title">
<h2 id="about-title" class="section-title">{c['o_title']}</h2>
{about}
</section>
<section class="finalcta" aria-labelledby="final-title">
<h2 id="final-title">{c['f_title']}</h2>
<p>{c['f_text']}</p>
<a class="btn btn--primary btn--lg" href="{t['spons_new']}">{t['start']}</a>
</section>
</div>
</main>
{footer(lang, here, there)}
</body>
</html>
"""


def main():
    (ROOT / "index.html").write_text(page("nb"))
    (ROOT / "en" / "index.html").write_text(page("en"))
    print("Front pages written.")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Writes the shared privacy and support pages for all Sideline apps.

    python3 tools/make_shared_pages.py

Outputs /privacy/, /privacy/en/, /support/, /support/en/ and turns the old
/handball/privacy|support pages into redirects to the shared ones (the
Handball App Store listing points there).
"""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
UPDATED = {"nb": "8. oktober 2026", "en": "8 October 2026"}

LOGO = ('<svg class="logo" viewBox="0 0 48 32" width="48" height="32" '
        'aria-hidden="true" focusable="false"><g fill="none" stroke="#FF6100" '
        'stroke-width="1.4" stroke-linejoin="round"><rect x="1.5" y="1.5" '
        'width="45" height="29" rx="3"/><line x1="24" y1="1.5" x2="24" '
        'y2="30.5"/><circle cx="24" cy="16" r="5"/></g><g fill="#FF6100">'
        '<rect x="8" y="18" width="3" height="7" rx=".6"/><rect x="13" y="13" '
        'width="3" height="12" rx=".6"/><rect x="33" y="15" width="3" '
        'height="10" rx=".6"/><rect x="38" y="9" width="3" height="16" '
        'rx=".6"/></g></svg>')

APPS = [
    # name, App Store id (None = not out yet), nb, en
    ("Sideline: Football", "6816678735",
     "Kamptavle for fotball: laguttak, bytter, spilletid og statistikk for "
     "3er- til 11er-fotball.",
     "Match board for football: line-ups, substitutions, playing time and "
     "stats for 3- to 11-a-side."),
    ("Sideline: Handball", "6817756823",
     "Kamptavle for håndball: laguttak, bytter, spilletid, 2 minutters "
     "utvisninger og statistikk.",
     "Match board for handball: line-ups, substitutions, playing time, "
     "2-minute suspensions and stats."),
    ("Sideline: Insights", "6818266063",
     "Kampstatistikk for fotball og håndball: heatmaps, spillerkort og "
     "utvikling over tid.",
     "Match stats for football and handball: heat maps, player cards and "
     "development over time."),
    ("Sideline: Basketball", None,
     "Skudd, fouls og spillerstatistikk for basketballtrenere.",
     "Shots, fouls and player stats for basketball coaches."),
    ("Sideline: Playbook", None,
     "Taktikktavle og øvelsesbank for fotball: tegn trekk, spill dem av og "
     "del dem som bilder.",
     "Tactics board and drill library for football: draw plays, animate "
     "them and share them as pictures."),
]

T = {
    "nb": dict(
        support="Støtte", privacy="Personvern", other="en", other_label="EN",
        here_label="NO", menu="Meny", langs="Språk",
        privacy_title="Personvernerklæring – Sideline-appene",
        privacy_desc="Personvern i Sideline-appene: ingen konto, ingen "
                     "sporing og ingen reklame. Alt lagres kun på din iPhone, "
                     "og ingenting sendes til utvikleren.",
        support_title="Støtte – Sideline-appene",
        support_desc="Hjelp og vanlige spørsmål for Sideline: Football, "
                     "Handball, Insights, Basketball og Playbook.",
        coming="Kommer snart", store="App Store",
        updated="Sist oppdatert",
        copyright="© 2026 Stian Braastad",
        no_cookies="Denne siden bruker ingen informasjonskapsler, sporing "
                   "eller analyseverktøy.",
        footer_other="English",
    ),
    "en": dict(
        support="Support", privacy="Privacy", other="nb", other_label="NO",
        here_label="EN", menu="Menu", langs="Language",
        privacy_title="Privacy Policy – the Sideline apps",
        privacy_desc="Privacy in the Sideline apps: no account, no tracking "
                     "and no ads. Everything stays on your iPhone, and nothing "
                     "is sent to the developer.",
        support_title="Support – the Sideline apps",
        support_desc="Help and FAQ for Sideline: Football, Handball, "
                     "Insights, Basketball and Playbook.",
        coming="Coming soon", store="App Store",
        updated="Last updated",
        copyright="© 2026 Stian Braastad",
        no_cookies="This site uses no cookies, tracking or analytics.",
        footer_other="Norsk",
    ),
}

PRIVACY = {
    "nb": """
<section class="hero policy"><p class="eyebrow">Personvern</p><h1>Personvernerklæring for Sideline-appene</h1><p class="meta">{updated}: {date}</p></section>
<div class="card summary policy"><p style="margin:0"><strong>Kort fortalt:</strong> Ingen av Sideline-appene samler inn personopplysninger. Alt lagres kun på enheten din, og ingenting sendes til utvikleren.</p></div>
<article class="policy">
<h2>Hvem står bak</h2>
<p>Sideline-appene er Sideline: Football, Sideline: Handball, Sideline: Insights, Sideline: Basketball og Sideline: Playbook, apper for trenere, lagledere og foreldre. De er utviklet av Stian Braastad (privatperson, Oslo, Norge). Denne erklæringen gjelder alle appene og forklarer hvordan de behandler opplysninger.</p>
<h2>1. Kort oppsummert</h2>
<p>Appene samler ikke inn personopplysninger. Alt du legger inn lagres kun lokalt på enheten din. Ingenting sendes til utvikleren eller til tredjeparter. Appene har ingen konto, ingen innlogging, ingen reklame fra andre, ingen analyseverktøy og ingen sporing.</p>
<h2>2. Hvilke opplysninger lagres, og hvor</h2>
<p>Appene lagrer bare det du selv legger inn, i appens egen lagringsplass på enheten din:</p>
<ul>
<li><strong>Sideline: Football, Handball og Basketball</strong> (kamptavler): lagnavn, motstander, spillernavn og draktnummer, formasjoner og laguttak, kamper, spilletid, bytter og hendelser (for eksempel mål, skudd, redninger, utvisninger, fouls og kort).</li>
<li><strong>Sideline: Insights</strong> (statistikk): lag og spillere (navn og draktnummer), kamper og motstandere, og hendelser med posisjon på banen og i målet. Statistikk, heatmaps og grafer regnes ut på enheten.</li>
<li><strong>Sideline: Playbook</strong> (taktikktavle): tavlene du lager, med navn, brikker og draktnummer eller initialer, streker og kommentarer.</li>
</ul>
<p>I tillegg lagres innstillinger som idrett og språk. Appene sender ikke disse dataene noe sted.</p>
<h2>3. Deling av bilder og filer</h2>
<p>Noen av appene lar deg selv dele et bilde (for eksempel et kampsammendrag eller en tavle) eller eksportere en kamprapport som CSV-fil. Filen lages på enheten og overlates til delingsmenyen i iOS, der du velger mottaker eller app (for eksempel e-post, meldinger, Spond eller Filer). Dette skjer bare når du selv starter det. Det du deler kan inneholde spillernavn og statistikk, og videre behandling styres av appen eller mottakeren du deler med. Utvikleren mottar ingenting.</p>
<h2>4. Opplysninger om andre, for eksempel barn</h2>
<p>Spillernavn du legger inn, kan gjelde andre personer, også barn. Disse opplysningene blir liggende på din enhet og er under din kontroll. Vi anbefaler at du bare legger inn det du trenger, for eksempel fornavn og draktnummer, at du er varsom med hva du deler, og at du følger retningslinjene i klubben din.</p>
<h2>5. Sletting</h2>
<p>Du kan slette og endre det du har lagt inn, i appene. Sletter du en app fra enheten, slettes alle data som den appen har lagret. Hvis du har slått på sikkerhetskopi av enheten (for eksempel iCloud-sikkerhetskopi eller kopi på datamaskin), kan appdata være med i denne kopien. Det styres av deg og Apple, ikke av utvikleren.</p>
<h2>6. Tillatelser</h2>
<p>Appene ber ikke om tilgang til kamera, kontakter, posisjon, mikrofon eller sporing, og ingen av dem leser bildene dine. Velger du «Arkiver bilde» i delingsmenyen i Sideline: Playbook, spør iOS om appen kan legge til et bilde i bildebiblioteket ditt. Appen kan da bare legge til bilder, ikke se dem du har.</p>
<h2>7. Lenker til App Store</h2>
<p>Sideline: Playbook viser et lite banner om de andre Sideline-appene. Trykker du på det, åpnes App Store. Banneret samler ikke inn noe og sender ingenting til utvikleren.</p>
<h2>8. Apple</h2>
<p>Nedlasting fra App Store skjer via Apple og følger Apples egen personvernerklæring. Apple kan gi utviklere anonymiserte, samlede tall (for eksempel antall nedlastinger) og krasjrapporter fra brukere som selv har valgt å dele dem med utviklere. Utvikleren kan ikke bruke dette til å identifisere deg. Testversjoner via TestFlight følger Apples vilkår for TestFlight.</p>
<h2>9. Kontakt med utvikleren</h2>
<p>Hvis du sender en e-post til <a href="mailto:support@sideline.no">support@sideline.no</a>, bruker jeg e-postadressen din og innholdet i meldingen bare til å svare deg. E-posten slettes når saken er avsluttet, med mindre du ønsker noe annet. Behandlingsgrunnlaget er berettiget interesse i å svare på henvendelsen (personvernforordningen art. 6 nr. 1 bokstav f).</p>
<h2>10. Dine rettigheter</h2>
<p>Etter personvernregelverket (GDPR) har du blant annet rett til innsyn, retting og sletting. Fordi utvikleren ikke har tilgang til dataene i appene, utøver du disse rettighetene direkte i appen eller ved å slette den. For henvendelser som gjelder e-post du har sendt, kontakt <a href="mailto:support@sideline.no">support@sideline.no</a>. Du kan klage til Datatilsynet (<a href="https://www.datatilsynet.no">www.datatilsynet.no</a>).</p>
<h2>11. Nettsiden</h2>
<p>Denne nettsiden er publisert med GitHub Pages. GitHub registrerer IP-adressen til besøkende av sikkerhetshensyn, i henhold til GitHubs personvernerklæring. Nettsiden bruker ikke egne informasjonskapsler (cookies), sporing eller analyseverktøy, og laster ingen eksterne skrifttyper.</p>
<h2>12. Endringer</h2>
<p>Hvis en app endres slik at den behandler opplysninger på en annen måte, oppdateres denne erklæringen før endringen tas i bruk, og datoen øverst endres.</p>
<h2>Kontakt</h2>
<p>Stian Braastad, <a href="mailto:support@sideline.no">support@sideline.no</a></p>
</article>
""",
    "en": """
<section class="hero policy"><p class="eyebrow">Privacy</p><h1>Privacy Policy for the Sideline apps</h1><p class="meta">{updated}: {date}</p></section>
<div class="card summary policy"><p style="margin:0"><strong>In short:</strong> None of the Sideline apps collect personal data. Everything stays on your device, and nothing is sent to the developer.</p></div>
<article class="policy">
<h2>Who we are</h2>
<p>The Sideline apps are Sideline: Football, Sideline: Handball, Sideline: Insights, Sideline: Basketball and Sideline: Playbook, apps for coaches, team managers and parents. They are developed by Stian Braastad (private individual, Oslo, Norway). This policy covers all of the apps and explains how they handle information.</p>
<h2>1. Summary</h2>
<p>The apps do not collect personal data. Everything you enter is stored only on your device. Nothing is sent to the developer or to any third party. The apps have no account, no sign-in, no third-party ads, no analytics and no tracking.</p>
<h2>2. What is stored, and where</h2>
<p>The apps store only what you enter yourself, in the app's own storage on your device:</p>
<ul>
<li><strong>Sideline: Football, Handball and Basketball</strong> (match boards): team name, opponent, player names and shirt numbers, formations and line-ups, matches, playing time, substitutions and events (such as goals, shots, saves, suspensions, fouls and cards).</li>
<li><strong>Sideline: Insights</strong> (stats): teams and players (names and shirt numbers), matches and opponents, and events with their position on the pitch or court and in the goal. Stats, heat maps and charts are calculated on your device.</li>
<li><strong>Sideline: Playbook</strong> (tactics board): the plays you create, with their names, pieces and shirt numbers or initials, lines and notes.</li>
</ul>
<p>Settings such as sport and language are stored too. The apps do not send this data anywhere.</p>
<h2>3. Sharing pictures and files</h2>
<p>Some of the apps let you share a picture (such as a match summary or a play) or export a match report as a CSV file. The file is created on your device and handed to the iOS share sheet, where you choose the recipient or app (for example email, Messages, Spond or Files). This only happens when you start it yourself. What you share may contain player names and stats, and how it is handled afterwards is up to the app or recipient you share it with. The developer receives nothing.</p>
<h2>4. Information about other people, including children</h2>
<p>Player names you enter may relate to other people, including children. This information stays on your device and under your control. We recommend entering only what you need, for example first names and shirt numbers, being careful about what you share, and following your club's guidelines.</p>
<h2>5. Deletion</h2>
<p>You can delete and edit what you have entered in the apps. Deleting an app from your device deletes all data that app has stored. If you use device backups (for example iCloud Backup or a backup on a computer), app data may be included in that backup. This is controlled by you and Apple, not by the developer.</p>
<h2>6. Permissions</h2>
<p>The apps do not ask for access to your camera, contacts, location or microphone, or for permission to track you, and none of them read your photos. If you choose “Save Image” in the share sheet in Sideline: Playbook, iOS asks whether the app may add a picture to your photo library. The app can then only add pictures, not see the ones you have.</p>
<h2>7. Links to the App Store</h2>
<p>Sideline: Playbook shows a small banner about the other Sideline apps. Tapping it opens the App Store. The banner collects nothing and sends nothing to the developer.</p>
<h2>8. Apple</h2>
<p>Downloads from the App Store are handled by Apple under Apple's own privacy policy. Apple may give developers anonymised, aggregated figures (such as download numbers) and crash reports from users who have chosen to share them with developers. The developer cannot use these to identify you. Test versions through TestFlight follow Apple's TestFlight terms.</p>
<h2>9. Contacting the developer</h2>
<p>If you email <a href="mailto:support@sideline.no">support@sideline.no</a>, I use your email address and message only to reply to you. The email is deleted once the matter is closed, unless you ask otherwise. The legal basis is legitimate interest in answering your enquiry (GDPR Article 6(1)(f)).</p>
<h2>10. Your rights</h2>
<p>Under data protection law (GDPR) you have rights including access, rectification and erasure. Because the developer has no access to the data in the apps, you exercise these rights directly in the app or by deleting it. For questions about email you have sent, contact <a href="mailto:support@sideline.no">support@sideline.no</a>. You can complain to the Norwegian Data Protection Authority, Datatilsynet (<a href="https://www.datatilsynet.no">www.datatilsynet.no</a>).</p>
<h2>11. This website</h2>
<p>This website is published with GitHub Pages. GitHub logs visitors' IP addresses for security purposes, under GitHub's privacy statement. The website sets no cookies of its own, uses no tracking or analytics, and loads no external fonts.</p>
<h2>12. Changes</h2>
<p>If an app changes how it handles information, this policy is updated before the change takes effect, and the date at the top changes.</p>
<h2>Contact</h2>
<p>Stian Braastad, <a href="mailto:support@sideline.no">support@sideline.no</a></p>
</article>
""",
}

FAQ = {
    "nb": [
        ("Trenger jeg en konto?", "Nei. Ingen av appene har konto eller innlogging."),
        ("Hvor lagres dataene mine?", "Kun lokalt på din iPhone. Ingenting sendes til utvikleren eller til andre, og appene fungerer uten nett."),
        ("Kan jeg flytte data mellom appene?", "Nei, hver app har sine egne data på telefonen. De deler ingenting med hverandre."),
        ("Hva skjer når jeg deler et bilde eller eksporterer CSV?", "Bildet eller filen lages på enheten din og deles bare når du selv velger det, via delingsmenyen i iOS (for eksempel e-post, meldinger, Spond eller Filer). Appene sender ingenting på egen hånd."),
        ("Hvordan sletter jeg noe?", "På listene i appene: sveip mot venstre og trykk Slett, eller hold fingeren på elementet og velg Slett. Bekreft i dialogen. Det kan ikke angres."),
        ("Hva skjer hvis jeg sletter en app?", "Da slettes alle data som den appen har lagret på enheten. Hvis du bruker sikkerhetskopi av telefonen (for eksempel iCloud-sikkerhetskopi), kan appdata være med i den kopien."),
        ("Hvilke språk finnes appene på?", "Appene følger språket på telefonen og har en språkknapp. Alle finnes på norsk, engelsk, tysk, fransk, spansk og portugisisk. Sideline: Playbook finnes også på dansk og svensk."),
        ("Hvordan melder jeg fra om en feil?", 'Send en e-post til <a href="mailto:support@sideline.no">support@sideline.no</a>. Skriv hvilken app det gjelder, hva du gjorde og hva som skjedde, hvilken iPhone-modell og iOS-versjon du har, og legg ved et skjermbilde hvis du kan.'),
    ],
    "en": [
        ("Do I need an account?", "No. None of the apps have an account or sign-in."),
        ("Where is my data stored?", "Only on your iPhone. Nothing is sent to the developer or anyone else, and the apps work offline."),
        ("Can I move data between the apps?", "No, each app keeps its own data on your phone. They don't share anything with each other."),
        ("What happens when I share a picture or export a CSV?", "The picture or file is created on your device and only shared when you choose to, through the iOS share sheet (for example email, Messages, Spond or Files). The apps never send anything on their own."),
        ("How do I delete something?", "In the lists in the apps: swipe left and tap Delete, or press and hold the item and choose Delete. Confirm in the dialog. This can't be undone."),
        ("What happens if I delete an app?", "All data that app has stored on your device is deleted. If you use device backups (for example iCloud Backup), app data may be included in that backup."),
        ("Which languages are available?", "The apps follow your phone's language and have a language button. All are available in Norwegian, English, German, French, Spanish and Portuguese. Sideline: Playbook is also available in Danish and Swedish."),
        ("How do I report a problem?", 'Email <a href="mailto:support@sideline.no">support@sideline.no</a>. Please say which app, what you did and what happened, your iPhone model and iOS version, and attach a screenshot if you can.'),
    ],
}

SUPPORT_INTRO = {
    "nb": ("Støtte", "Hjelp til Sideline-appene",
           "Apper for trenere, lagledere og foreldre. Her finner du alle "
           "appene, svar på vanlige spørsmål og hvordan du kontakter meg."),
    "en": ("Support", "Help with the Sideline apps",
           "Apps for coaches, team managers and parents. Here you'll find "
           "all the apps, answers to common questions and how to reach me."),
}

HEADINGS = {
    "nb": dict(apps="Appene", faq="Vanlige spørsmål", contact="Kontakt",
               privacy="Personvern", email="E-post", dev="Utvikler",
               dev_who="Stian Braastad, Oslo, Norge",
               privacy_text='Ingen av Sideline-appene samler inn '
                            'personopplysninger. Les '
                            '<a href="/privacy/">personvernerklæringen</a> '
                            '(<a href="/privacy/en/" hreflang="en">English</a>).'),
    "en": dict(apps="The apps", faq="FAQ", contact="Contact",
               privacy="Privacy", email="Email", dev="Developer",
               dev_who="Stian Braastad, Oslo, Norway",
               privacy_text='None of the Sideline apps collect personal data. '
                            'Read the <a href="/privacy/en/">privacy policy</a> '
                            '(<a href="/privacy/" hreflang="nb">norsk</a>).'),
}


def url(kind, lang):
    return f"/{kind}/" if lang == "nb" else f"/{kind}/en/"


def head(lang, kind, title, desc):
    t = T[lang]
    canonical = f"https://sideline.no{url(kind, lang)}"
    locale = "nb_NO" if lang == "nb" else "en_GB"
    alt_locale = "en_GB" if lang == "nb" else "nb_NO"
    return f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#000000">
<meta name="color-scheme" content="dark">
<meta name="referrer" content="no-referrer">
<link rel="canonical" href="{canonical}">
<link rel="alternate" hreflang="nb" href="https://sideline.no{url(kind, 'nb')}">
<link rel="alternate" hreflang="en" href="https://sideline.no{url(kind, 'en')}">
<link rel="alternate" hreflang="x-default" href="https://sideline.no{url(kind, 'nb')}">
<meta property="og:site_name" content="Sideline">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canonical}">
<meta property="og:type" content="website">
<meta property="og:locale" content="{locale}">
<meta property="og:locale:alternate" content="{alt_locale}">
<meta property="og:image" content="https://sideline.no/assets/og/{'sideline-og.jpg' if lang == 'nb' else 'sideline-og-en.jpg'}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="https://sideline.no/assets/og/{'sideline-og.jpg' if lang == 'nb' else 'sideline-og-en.jpg'}">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="/assets/icons/favicon-32.png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="stylesheet" href="/assets/style.css">
</head>
<body>
<header><div class="wrap bar">
<a class="brand" href="{'/' if lang == 'nb' else '/en/'}">{LOGO}<span>Sideline</span></a>
<div class="right"><nav class="links" aria-label="{t['menu']}"><a href="{url('support', lang)}">{t['support']}</a><a href="{url('privacy', lang)}">{t['privacy']}</a></nav>
<nav class="lang" aria-label="{t['langs']}">""" + (
        f"<span>{t['here_label']}</span><a href=\"{url(kind, t['other'])}\" hreflang=\"{t['other']}\" lang=\"{t['other']}\">{t['other_label']}</a>"
        if lang == "nb" else
        f"<a href=\"{url(kind, t['other'])}\" hreflang=\"{t['other']}\" lang=\"{t['other']}\">{t['other_label']}</a><span>{t['here_label']}</span>"
    ) + """</nav></div>
</div></header>
<main class="wrap">"""


def foot(lang, kind):
    t = T[lang]
    return f"""</main>
<footer><div class="wrap">
<nav><a href="{'/' if lang == 'nb' else '/en/'}">Sideline</a><a href="{url('support', lang)}">{t['support']}</a><a href="{url('privacy', lang)}">{t['privacy']}</a><a href="{url(kind, t['other'])}" hreflang="{t['other']}">{t['footer_other']}</a></nav>
<p>{t['copyright']}</p>
<p>{t['no_cookies']}</p>
</div></footer>
</body>
</html>
"""


def privacy(lang):
    t = T[lang]
    body = PRIVACY[lang].format(updated=t["updated"], date=UPDATED[lang])
    return (head(lang, "privacy", t["privacy_title"], t["privacy_desc"])
            + body + foot(lang, "privacy"))


def support(lang):
    t, h = T[lang], HEADINGS[lang]
    eyebrow, title, lead = SUPPORT_INTRO[lang]
    parts = [f"""
<section class="hero">
<p class="eyebrow">{eyebrow}</p>
<h1>{title}</h1>
<p class="lead">{lead}</p>
</section>
<h2>{h['apps']}</h2>
<div class="apps">"""]
    for name, store_id, nb, en in APPS:
        text = nb if lang == "nb" else en
        if store_id:
            country = "no" if lang == "nb" else "gb"
            link = (f'<a href="https://apps.apple.com/{country}/app/id{store_id}">'
                    f'{t["store"]}</a>')
        else:
            link = f'<span style="color:var(--muted)">{t["coming"]}</span>'
        parts.append(f"""<div class="app-card"><h3>{name}</h3><p>{text}</p><nav>{link}</nav></div>""")
    parts.append(f"""</div>
<h2>{h['faq']}</h2>
<div class="faq">""")
    for question, answer in FAQ[lang]:
        parts.append(f"""<div class="card"><h3>{question}</h3><p>{answer}</p></div>""")
    parts.append(f"""</div>
<h2>{h['contact']}</h2>
<div class="card contact"><p style="margin:0">{h['email']}: <a href="mailto:support@sideline.no">support@sideline.no</a><br>{h['dev']}: {h['dev_who']}</p></div>
<h2>{h['privacy']}</h2>
<p>{h['privacy_text']}</p>
""")
    return (head(lang, "support", t["support_title"], t["support_desc"])
            + "\n".join(parts) + foot(lang, "support"))


def redirect(target, title):
    return (f'<!doctype html><html><head><meta charset="utf-8"><title>{title}</title>'
            f'<meta name="robots" content="noindex">'
            f'<meta http-equiv="refresh" content="0; url={target}">'
            f'<link rel="canonical" href="https://sideline.no{target}"></head>'
            f'<body><a href="{target}">{title}</a></body></html>\n')


def main():
    for lang in ("nb", "en"):
        for kind, render in (("privacy", privacy), ("support", support)):
            out = ROOT / url(kind, lang).strip("/") / "index.html"
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text(render(lang))
    for kind, nb_title, en_title in (
        ("privacy", "Personvern – Sideline", "Privacy – Sideline"),
        ("support", "Støtte – Sideline", "Support – Sideline"),
    ):
        (ROOT / f"handball/{kind}/index.html").write_text(
            redirect(f"/{kind}/", nb_title))
        (ROOT / f"handball/{kind}/en/index.html").write_text(
            redirect(f"/{kind}/en/", en_title))
    (ROOT / "handball/index.html").write_text(redirect("/support/", "Sideline"))
    print("Shared privacy and support pages written.")


if __name__ == "__main__":
    main()

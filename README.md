# sideline.no

Static site for https://sideline.no (GitHub Pages, custom domain). Plain HTML/CSS, no build step, self-hosted fonts (Plus Jakarta Sans and Oswald, OFL, `assets/fonts/`). Since November 2026 in the design of spons.sideline.no: `assets/site.css` (the same tokens; light, dark on dark devices) and `assets/site.js` (header shadow, phone menu). The front pages are written by `tools/make_home.py` (head from `tools/home_head_{nb,en}.html`), the support and privacy pages by `tools/make_shared_pages.py`; both use the shared header and footer in `tools/site_frame.py`. Edit those and re-run, not the HTML. Google tag (Google Ads AW-18545227066) with a consent banner: `assets/consent.js`, included high in every page's `<head>` (Consent Mode v2, nothing set before Accept; only runs on sideline.no).

| Path | Content |
|---|---|
| `/` · `/en/` | Front page (NB · EN): photo hero with one message and «Prøv Spons gratis», a trust strip, Sideline Spons in depth (three steps, the 45-second film on the NB page, store badges, the Vipps band in NB), the other apps (Insights, Football, Handball, Basketball, Playbook), about, a last call. Everything about Spons links to spons.sideline.no |
| `/support/` · `/support/en/` | Support for all Sideline apps |
| `/privacy/` · `/privacy/en/` | Privacy policy for all Sideline apps |
| `/handball/support/…`, `/handball/privacy/…`, `/handball/` | Redirect to the shared pages |

Contact: support@sideline.no

## App Store links

The badges are the `<a class="badge" data-app="...">` elements in `index.html` and `en/index.html`:

- `spons`: https://apps.apple.com/no/app/sideline-spons/id6824289338 (Spons block; English page without /no/) and Google Play https://play.google.com/store/apps/details?id=no.braastad.sideline.spons
- `insights`: https://apps.apple.com/no/app/sideline-insights/id6818266063
- `handball`: https://apps.apple.com/no/app/sideline-handball/id6817756823
- `football`: https://apps.apple.com/no/app/sideline-football/id6816678735
- `basketball`: https://apps.apple.com/no/app/sideline-basketball/id6819058783
- `playbook`: https://apps.apple.com/no/app/sideline-playbook/id6820581905 (free; card image from the app's 1.0.4 store screenshots, 04-drill)

Badges are official Apple artwork from Apple Marketing Tools (`assets/badges/app-store-nb.svg` = NO, `app-store-en.svg` = US/UK).
`/b/` and `/b/en/` redirect to `/` and `/en/`.

Photos: `assets/photos/*-{800,1600}.{webp,jpg}` (WebP with JPEG fallback).


On wide screens the five app cards stand in one row; the text column runs to the card's foot so every badge sits at the same height.

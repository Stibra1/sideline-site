# sideline.no

Static site for https://sideline.no (GitHub Pages, custom domain). Plain HTML/CSS, no build step, no external fonts. Google tag (Google Ads AW-18545227066) with a consent banner: `assets/consent.js`, included high in every page's `<head>` (Consent Mode v2, nothing set before Accept; only runs on sideline.no).

| Path | Content |
|---|---|
| `/` · `/en/` | Landing page (NB · EN): Sideline wordmark over a photo hero, a feature card for Sideline: Spons (the main offering, links to spons.sideline.no; animated illustration `assets/img/spons-{nb,en}.svg` from `tools/make_spons_art.py`), then four app cards with App Store badges (Insights, Handball, Football, Basketball) |
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

Badges are official Apple artwork from Apple Marketing Tools (`assets/badges/app-store-nb.svg` = NO, `app-store-en.svg` = US/UK).
`/b/` and `/b/en/` redirect to `/` and `/en/`.

Photos: `assets/photos/*-{800,1600}.{webp,jpg}` (WebP with JPEG fallback).


`data-app="basketball"` on the landing badges is still `href="#"` until Sideline: Basketball is live on the App Store.

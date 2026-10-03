# sideline.no

Static site for https://sideline.no (GitHub Pages, custom domain). Plain HTML/CSS, no build step, no trackers, no external fonts.

| Path | Content |
|---|---|
| `/` · `/en/` | Landing page (NB · EN): Sideline wordmark over a photo hero, three app cards with App Store badges |
| `/support/` · `/support/en/` | Sideline: Insights support |
| `/privacy/` · `/privacy/en/` | Sideline: Insights privacy policy |
| `/handball/support/` · `/handball/support/en/` | Sideline: Håndball support |
| `/handball/privacy/` · `/handball/privacy/en/` | Sideline: Håndball privacy policy |

Contact: support@sideline.no

## App Store links

The badges are the `<a class="badge" data-app="...">` elements in `index.html` and `en/index.html`:

- `insights`: https://apps.apple.com/no/app/sideline-insights/id6818266063
- `handball`: https://apps.apple.com/no/app/sideline-handball/id6817756823
- `football`: https://apps.apple.com/no/app/sideline-football/id6816678735

Badges are official Apple artwork from Apple Marketing Tools (`assets/badges/app-store-nb.svg` = NO, `app-store-en.svg` = US/UK).
`/b/` and `/b/en/` redirect to `/` and `/en/`.

Photos: `assets/photos/*-{800,1600}.{webp,jpg}` (WebP with JPEG fallback).

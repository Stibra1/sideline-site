# sideline.no

Static site for https://sideline.no (GitHub Pages, custom domain). Plain HTML/CSS, no build step, no trackers, no external fonts.

| Path | Content |
|---|---|
| `/` · `/en/` | Landing page, option 1 (NB · EN): wordmark, lifestyle photos, intro text, three app cards with App Store badges |
| `/b/` · `/b/en/` | Landing page, option 2 (noindex): same content with the photos as faded backgrounds |
| `/support/` · `/support/en/` | Sideline: Insights support |
| `/privacy/` · `/privacy/en/` | Sideline: Insights privacy policy |
| `/handball/support/` · `/handball/support/en/` | Sideline: Håndball support |
| `/handball/privacy/` · `/handball/privacy/en/` | Sideline: Håndball privacy policy |

Contact: support@sideline.no

## App Store links

The badges are the `<a class="badge" data-app="...">` elements in `index.html`, `en/index.html`, `b/index.html` and `b/en/index.html`.
`data-app="insights"` is still `href="#"` (marked with an HTML comment). Replace it with the apps.apple.com URL when Sideline: Insights is live.
Badges are official Apple artwork from Apple Marketing Tools (`assets/badges/app-store-nb.svg` = NO, `app-store-en.svg` = US/UK).

Photos: `assets/photos/*-{800,1600}.{webp,jpg}` (WebP with JPEG fallback).

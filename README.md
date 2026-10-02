# sideline.no

Static site for https://sideline.no (GitHub Pages, custom domain). Plain HTML/CSS, no build step, no trackers, no external fonts.

| Path | Content |
|---|---|
| `/` · `/en/` | Landing page (NB · EN): the three Sideline apps with App Store badges |
| `/support/` · `/support/en/` | Sideline: Insights support |
| `/privacy/` · `/privacy/en/` | Sideline: Insights privacy policy |
| `/handball/support/` · `/handball/support/en/` | Sideline: Håndball support |
| `/handball/privacy/` · `/handball/privacy/en/` | Sideline: Håndball privacy policy |

Contact: support@sideline.no

## App Store links

The badges live in `index.html` (NB) and `en/index.html` (EN), on the `<a class="badge" data-app="...">` elements.
`data-app="insights"` is still `href="#"` (marked with an HTML comment). Replace it with the apps.apple.com URL when Sideline: Insights is live.
Badges: official Apple artwork from Apple Marketing Tools (`assets/badges/app-store-nb.svg` = NO, `app-store-en.svg` = US/UK).

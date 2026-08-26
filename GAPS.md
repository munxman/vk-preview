# VK Mirror — Known Gaps & Static Limitations

**Mirror created:** 2026-08-26  
**Source:** https://valvekliinik.ee/  
**Mirror type:** wget full-site mirror (page-requisites + convert-links)  
**Deployed to:** https://munxman.github.io/vk-preview/

---

## Assets Loading from Live Domain

**Status:** By design — visual appearance is identical  
All CSS, JS, and font files in HTML `<link>/<script>` tags use absolute `https://valvekliinik.ee/` URLs. The `<base href="https://valvekliinik.ee/">` tag injected into every page ensures root-absolute paths (`/wp-content/`, `/wp-includes/`) also resolve to the live domain.

Result: Visual appearance is pixel-identical to the live site. The preview is functionally self-contained for visual inspection.

## WordPress Dynamic Features (Non-Functional in Static Preview)

1. **Contact/appointment forms** — CF7 forms render but submit to live WP (may work or 403)
2. **Search (`?s=query`)** — Excluded from mirror; search form will attempt live submission
3. **WordPress REST API** — Excluded (`/wp-json/`); no dynamic content loading
4. **ConnectedOnlineX booking iframe** — Embeds external iframe; loads from live booking system ✅ (works as-is)
5. **WooCommerce / shop features** — Not present on this site
6. **User login/account** — Not applicable for patient-facing pages
7. **Comments** — Feed excluded; static HTML shows comment forms but submit to live WP

## Pages Excluded from Mirror

- `/wp-admin/` — Admin interface (excluded intentionally)
- `/feed/`, `/comments/feed/` — RSS feeds (excluded intentionally)  
- `/wp-json/` — REST API (excluded intentionally; caused infinite crawl)
- `/?s=` — Search results (dynamic, excluded)
- `/?p=NNN` — WP post ID redirects (downloaded as redirect artifacts, serve no purpose in preview)

## Navigation in Preview

Navigation links in the preview work as follows:
- Links with `<base>` tag redirect to the **live valvekliinik.ee** site when clicked
- This is intentional for the preview — individual pages are opened by direct URL
- Within-page functionality (accordions, tabs, popups) works normally via the live JS

## File Count

- **HTML pages:** ~985
- **Total files:** ~1858
- **Mirror size:** ~557 MB

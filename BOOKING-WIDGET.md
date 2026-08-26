# Valvekliinik – Booking Widget Documentation
**Provider:** ConnectedOnlineX (ConnectedServer EU)  
**Crawled:** 2026-08-26  
**Pages crawled:** /broneerimine/, /toendid/, /en/booking/, /fi/varaaminen/, /ru/бронирование/

---

## Widget Embed Code

### Exact iframe URL (from live WordPress site)
```
https://connectedserver.eu/ConnectedOnlineX/default.aspx?key=XxX0j1C0&lang=et
```

### Parameters
| Parameter | Value | Notes |
|---|---|---|
| `key` | `XxX0j1C0` | Clinic's unique identifier — **DO NOT CHANGE** |
| `lang` | `et` | Language. All pages (ET/EN/FI/RU) use `lang=et`. Widget handles language internally via its own UI. |

### As extracted from /broneerimine/ (WordPress raw HTML)
```html
<iframe src="https://connectedserver.eu/ConnectedOnlineX/default.aspx?key=XxX0j1C0&lang=et"; style='height:800px;width:100%;' frameBorder='0' ></iframe>
```
Note: The semicolon after the URL (`;`) is a quirk in the WordPress Elementor HTML widget. It is harmless — browsers ignore it. Static rebuild uses clean HTML without the semicolon.

### As used in static rebuild (clean, valid HTML5)
```html
<iframe
  src="https://connectedserver.eu/ConnectedOnlineX/default.aspx?key=XxX0j1C0&amp;lang=et"
  title="Broneerige vastuvõtuaeg – Valvekliinik"
  style="height:800px;width:100%;border:none;display:block;"
  frameborder="0"
  allowfullscreen
  loading="lazy"
></iframe>
```

---

## Pages Using the Widget

| Page (live) | Static file | Widget present | Notes |
|---|---|---|---|
| /broneerimine/ | broneerimine/index.html | ✅ Added Phase 1 | Primary booking page |
| /toendid/ | toendid/index.html | ✅ Added Phase 1 | Certificate/driver license page |
| /en/booking/ | (Phase 2 – not built yet) | — | EN version |
| /fi/varaaminen/ | (Phase 2 – not built yet) | — | FI version |
| /ru/бронирование/ | (Phase 2 – not built yet) | — | RU version |

---

## Pages WITHOUT the Widget (confirmed)

| Page | Notes |
|---|---|
| /teenused/gunekoloogia/ | Service page – no widget |
| /teenused/vastuvott/ | Service page – no widget |
| /teenused/analuusid/ | Service page – no widget |
| /teenused/ultraheliuuringud/ | Service page – no widget |
| /teenused/tervisetoendid/ | Service page – no widget |
| /teenused/retsepti-pikendamine/ | Service page – no widget |
| /teenused/concierge/ | Service page – no widget |
| /teenused/raseduskeskus/ | Service page – no widget |
| /teenused/protseduurid/ | Service page – no widget |
| /teenused/vaimne-tervis/ | Service page – no widget |

---

## Widget Configuration

### Service Selection
The ConnectedOnlineX widget renders a **"Valige teenus" dropdown** that lists all available services offered by Valvekliinik. The service list is defined on the ConnectedServer side (not in the embed code). No service pre-selection parameters were observed in any of the embed codes.

### Language Note
All 4 language versions of the booking page (/broneerimine/, /en/booking/, /fi/varaaminen/, /ru/бронирование/) use **identical embed code** with `lang=et`. The widget appears to present its UI in Estonian regardless of the page language. This is consistent across the live site.

If language-specific variants need to be supported in Phase 2, check if ConnectedOnlineX supports `lang=en`, `lang=fi`, `lang=ru` parameters — but do **not** change `lang=et` without confirming with Ingmar first.

### Dimensions
- **Standard:** `height:800px; width:100%`
- **English/Finnish live site variant:** `height:800px; width:90%` (narrower — may be intentional for those layouts)
- **Static rebuild:** Uses `width:100%` (matches ET live site) for all

---

## Analytics / Tracking
The live site has two GTM containers:
- `GTM-WHSVMBD`
- `GTM-TGC548C8`

Also uses Plausible Analytics (`mango.dignicy.com/js/script.js` with `data-domain="valvekliinik.ee"`).

These are **not** included in the static rebuild. Add in Phase 3 deploy step after owner confirmation.

---

## How to Update in Future

To change booking system:
1. Replace `src` URL in `broneerimine/index.html` → `<iframe src>` attribute
2. Replace `src` URL in `toendid/index.html` → `<iframe src>` attribute
3. Update this file

To change widget height: adjust `height:800px` in the `style` attribute of both pages.

---

## Verified Working (live site cross-check)
✅ Widget loads on `https://valvekliinik.ee/broneerimine/` — "Valige teenus" dropdown visible  
✅ Same `key=XxX0j1C0` across all 5 booking-capable pages  
✅ No service-specific parameters; widget provides full service list internally  
✅ No authentication or cookie requirements for the embed  

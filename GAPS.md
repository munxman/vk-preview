# GAPS.md – Content Not Extracted / Missing

**Created:** 2026-08-26  
**Purpose:** Items from the live valvekliinik.ee that could not be confirmed from crawl or were omitted from Phase 1 build.

---

## 🔴 Critical Gaps

### Doctor Photos
- **Issue:** No doctor photos could be extracted. The live site uses Elementor image widgets.
- **Impact:** arstid/index.html uses placeholder emoji avatars instead of real photos.
- **Action needed:** Download doctor photos from live site or request from Ingmar.
- **URL pattern on live site:** wp-content/uploads/... (various)

### Booking System
- **Resolved in Phase 1.** ConnectedOnlineX (connectedserver.eu) iframe with key=XxX0j1C0 embedded on broneerimine/index.html and toendid/index.html.
- Full documentation: BOOKING-WIDGET.md

### Veebivastuvõtt Chat Widget
- **Issue:** The live online consultation is a chat widget, provider unknown.
- **Impact:** veebivestlus/index.html links to live site for actual consultation.
- **Action needed:** Identify chat widget provider and embed in Phase 2.

### Contact Form
- **Issue:** Live site has a contact form (likely WP plugin). Not replicated.
- **Impact:** kontakt/index.html shows contact info only, no form.
- **Action needed:** Use Formspree, Netlify Forms, or equivalent in Phase 2.

---

## 🟡 Content Gaps (partial information)

### Doctor Profiles – Incomplete
- **Dr Elise Keskpaik** (Naistearst, languages: ET, EN) — no bio extracted from live site. Placeholder used.
- **Dr Maria Pintsaar** (Perearst / Concierge) — only role and price extracted, no education/bio.
- **Lastearsti meeskond** — no individual lastearst names extracted. Live site has filtered tabs but no separate URL per doctor.
- **Sisehaiguste arstid** — no individual doctor names extracted.
- **Ultraheliarstid** — no individual names extracted.
- **Õed ja administratsioon** — no names extracted.

### Töötervishoiu Pricing
- **Issue:** Töötervishoiu (occupational health) pricing not listed on live site. Only general info available.
- **Action needed:** Request price list from Ingmar.

### Veebivastuvõtu Pricing – Discrepancy
- **Issue:** Different pages mention different prices: live site says "Konsultatsiooni hind 20 EUR" on /veebivestlus/ page, but /hinnakiri/ does not list this separately.
- **Status:** Used 20 € in static site based on /veebivestlus/ page content.

### Blog/Article Content (kasulikku/)
- **Issue:** 12+ blog posts not included in Phase 1.
- **Posts identified (3 recent):**
  - "Dr Anastassia Schults alustab Valvekliinikus pisikirurgiliste protseduuridega" (2026-08-24)
  - "D-vitamiin: millal on vereanalüüs tegelikult vajalik?" (2026-08-04)
  - "Kõrvad lukus suvel: põhjused, esmaabi ja millal pöörduda arsti poole" (2026-07-13)
- **Action needed:** Crawl and build all blog posts in Phase 2.

### Multilingual Content – Phase 2A Status

✅ BUILT IN PHASE 2A:
- /en/ → en/index.html
- /en/booking/ → en/booking/index.html
- /en/services/ → en/services/index.html (archive)
- /fi/ → fi/index.html
- /fi/varaaminen/ → fi/varaaminen/index.html
- /fi/palvelut/ → fi/palvelut/index.html (archive)
- /ru/ → ru/index.html
- /ru/бронирование/ → ru/бронирование/index.html
- /ru/servisy/ → ru/servisy/index.html (archive)
- /toendid-en/ → toendid-en/index.html
- /toendid-ru/ → toendid-ru/index.html
- /toendid-fi/ → toendid-fi/index.html
- /toendid-uk/ → toendid-uk/index.html

❌ DISCOVERED BUT NOT YET BUILT (Phase 2B):
- /en/services/gynaecology/ (confirmed 200, has full EN content)
- /en/services/doctor-appointment/ (inferred from archive)
- /en/services/pregnancy-centre/ (inferred from archive)
- /en/services/ultrasound/ (inferred from archive)
- /en/services/lab-tests/ (inferred from archive)
- /en/services/procedures/ (inferred from archive)
- /en/services/health-certificates/ (inferred from archive)
- /en/services/prescription-renewal/ (inferred from archive)
- /en/services/concierge/ (inferred from archive)
- /en/services/mental-health/ (inferred from archive)
- /fi/palvelut/* — 10 individual FI service sub-pages (inferred, URLs not confirmed)
- /ru/servisy/* — 10 individual RU service sub-pages (inferred, URLs not confirmed)
- /en/2026/08/24/, /en/2026/08/04/, /en/2026/07/13/ — EN blog posts (Phase 3)
- /fi/2026/08/24/, /fi/2026/08/04/, /fi/2026/07/13/ — FI blog posts (Phase 3)
- /ru/2026/08/24/, /ru/2026/08/04/, /ru/2026/07/13/ — RU blog posts (Phase 3)
- **Action needed:** Build individual EN/FI/RU service sub-pages in Phase 2B.

### Tervisetõend for Weapons License
- **Issue:** The live site mentions "relvaloa taotlemine" (weapons license) as a use case for health certificates but no separate page or detailed process.
- **Status:** Mentioned in tervisetoendid page but not expanded.

### Retsepti uuendamine – Online Form
- **Issue:** The live site has a web form (ankeet) for prescription renewal. The form URL/provider is not known.
- **Action needed:** Identify form provider and embed in Phase 2.

### Map / Directions
- **Issue:** No embedded map in Phase 1. Live site likely has Google Maps or similar.
- **Action needed:** Add embedded map (OSM or Google) in Phase 2.

---

## 🟢 Content Confirmed from Live Site (no gaps)

- ✅ Full price list (all categories, all prices)
- ✅ Clinic address: Sepapaja 12/1, 3. korrus, Ülemiste Tervisemaja 2, Tallinn
- ✅ Phone: +372 5911 0909
- ✅ Email: info@valvekliinik.ee
- ✅ Opening hours: E–R 09:00–18:00, L 12:00–16:00, Riigipühad 12:00–16:00*
- ✅ Company: Valvekliinik OÜ, registrikood 11576944
- ✅ IBAN: EE797700771006197042 (AS LHV Pank)
- ✅ Brand colors: #BE1E2D (red), #414042 (dark gray)
- ✅ Logo: SVG downloaded, in assets/
- ✅ 6 named naistearstid with bios
- ✅ Dr Ingmar Lindström full bio and concierge pricing
- ✅ All core service descriptions
- ✅ Veebivastuvõtt pricing and process
- ✅ Juhiloa tervisetõend full process and pricing
- ✅ Retsepti pikendamise process and pricing
- ✅ Concierge service description and pricing
- ✅ Töötervishoid service description (pricing TBD)

---

## Statistics Not Verified / Potentially Problematic

| Claim | Source | Status |
|---|---|---|
| "üle viie aasta tegutsenud" | Live site multiple pages | ✅ Direct copy |
| "rohkem kui 12 000 patsienti" | Live site contact/hinnakiri | ✅ Direct copy |
| "enam kui sajast riigist" | Live site contact | ✅ Direct copy |
| "üle 3500 tunni" (Lindström valvetöö) | Live site arstid | ✅ Direct copy from bio |
| "üle 1500 tunni" (Lindström haiglad) | Live site arstid | ✅ Direct copy from bio |

**All statistics are verbatim copies from the live site.** None are invented by the static build process.

# Valvekliinik Static Site – Page Inventory
**Crawl date:** 2026-08-26  
**Source:** valvekliinik.ee (live WordPress+Elementor site)

---

## Core Pages – BUILT ✅

| URL (live) | File (static) | Title | Priority | Status |
|---|---|---|---|---|
| / | index.html | Avaleht – Kiire arstiabi Tallinnas | 1.0 | ✅ Built |
| /millega-saame-aidata/ | millega-saame-aidata/index.html | Millega saame aidata? | 0.9 | ✅ Built |
| /hinnakiri/ | hinnakiri/index.html | Hinnakiri | 0.9 | ✅ Built |
| /arstid/ | arstid/index.html | Meie meeskond | 0.8 | ✅ Built |
| /broneerimine/ | broneerimine/index.html | Aja broneerimine | 0.9 | ✅ Built |
| /kontakt/ | kontakt/index.html | Kontakt | 0.8 | ✅ Built |
| /veebivestlus/ | veebivestlus/index.html | Veebivastuvõtt | 0.85 | ✅ Built |
| /toendid/ | toendid/index.html | Juhiloa tervisetõend (detailed) | 0.85 | ✅ Built |
| /tootervishoid-ja-tootajate-tervisekontroll/ | tootervishoid-ja-tootajate-tervisekontroll/index.html | Töötervishoid | 0.8 | ✅ Built |

## Service Subpages – BUILT ✅

| URL (live) | File (static) | Title | Status |
|---|---|---|---|
| /teenused/vastuvott/ | teenused/vastuvott/index.html | Arsti vastuvõtt | ✅ Built |
| /teenused/gunekoloogia/ | teenused/gunekoloogia/index.html | Naistearsti vastuvõtt / Günekoloogia | ✅ Built |
| /teenused/analuusid/ | teenused/analuusid/index.html | Analüüsid | ✅ Built |
| /teenused/ultraheliuuringud/ | teenused/ultraheliuuringud/index.html | Ultraheliuuringud | ✅ Built |
| /teenused/tervisetoendid/ | teenused/tervisetoendid/index.html | Tervisetõendid | ✅ Built |
| /teenused/retsepti-pikendamine/ | teenused/retsepti-pikendamine/index.html | Retsepti uuendamine | ✅ Built |
| /teenused/concierge/ | teenused/concierge/index.html | Concierge – Isiklik arst | ✅ Built |
| /teenused/raseduskeskus/ | teenused/raseduskeskus/index.html | Raseduskeskus | ✅ Built |
| /teenused/protseduurid/ | teenused/protseduurid/index.html | Protseduurid | ✅ Built |
| /teenused/vaimne-tervis/ | teenused/vaimne-tervis/index.html | Vaimne tervis | ✅ Built |

## Phase 2A – Multilingual Pages – BUILT ✅

| URL (live) | File (static) | Lang | Status |
|---|---|---|---|
| /toendid-en/ | toendid-en/index.html | EN | ✅ Built |
| /toendid-ru/ | toendid-ru/index.html | RU | ✅ Built |
| /toendid-fi/ | toendid-fi/index.html | FI | ✅ Built |
| /toendid-uk/ | toendid-uk/index.html | UK | ✅ Built |
| /toendid/ | toendid/index.html | ET | ✅ Hreflang cluster updated |
| /en/ | en/index.html | EN | ✅ Built |
| /en/booking/ | en/booking/index.html | EN | ✅ Built |
| /en/services/ | en/services/index.html | EN | ✅ Built (archive) |
| /fi/ | fi/index.html | FI | ✅ Built |
| /fi/varaaminen/ | fi/varaaminen/index.html | FI | ✅ Built |
| /fi/palvelut/ | fi/palvelut/index.html | FI | ✅ Built (archive) |
| /ru/ | ru/index.html | RU | ✅ Built |
| /ru/бронирование/ | ru/бронирование/index.html | RU | ✅ Built |
| /ru/servisy/ | ru/servisy/index.html | RU | ✅ Built (archive) |

## Not Built – TODO (Phase 2B+)

| URL (live) | Category | Notes |
|---|---|---|
| /privaatsuspoliitika/ | Legal | ✅ Built (Phase 2B) |
| /liitu-uudiskirjaga/ | Marketing | ✅ Built (Phase 3) – form disabled, owner decision needed |
| /tagasiside/ | Marketing | ✅ Built (Phase 3) – form disabled, owner decision needed |
| /arve/ | Admin | ✅ Built (Phase 3) – form disabled, owner decision needed |
| /arst-ilma-jarjekorrata/ | SEO landing page | Redirect target – needs content |
| /aitah/ | Conversion | Thank-you page post-booking |
| /retseptide-uuendamine/ | Service | Alternate URL for prescription renewal |
| /en/services/gynaecology/ | Multilingual | EN individual service page (confirmed 200) |
| /en/services/* (9 more) | Multilingual | EN individual service sub-pages |
| /fi/palvelut/* (10) | Multilingual | FI individual service sub-pages |
| /ru/servisy/* (10) | Multilingual | RU individual service sub-pages |
| /ru/домашняя-страница-2/ | Multilingual | Russian homepage (alt slug – may redirect) |
| /teenus/spirograafia-koos-bronhodilataatortestiga/ | Service | ✅ Built (Phase 3) → teenus/spirograafia/index.html |
| /en/2026/08/24/, /fi/2026/08/24/, /ru/2026/08/24/ | Blog | EN/FI/RU translated blog posts |
| /category/kasulikku/ | Blog | Blog category page |

## Phase 3 – BUILT ✅ (2026-08-26)

| URL (live) | Static File | Notes |
|---|---|---|
| /teenus/spirograafia-koos-bronhodilataatortestiga/ | teenus/spirograafia/index.html | Full service content; MedicalTest schema |
| /tagasiside/ | tagasiside/index.html | Form disabled; tel/mailto interim |
| /arve/ | arve/index.html | Form disabled; billing details shown |
| /liitu-uudiskirjaga/ | liitu-uudiskirjaga/index.html | Form disabled; mailto interim |

---

## Discovered but excluded (system URLs)

- /feed/, /comments/feed/ – RSS feeds
- /wp-json/* – WordPress REST API
- /xmlrpc.php – WordPress XML-RPC
- /wp-content/* – WordPress media
- jet-menu-sitemap, jet-theme-core-sitemap – JetEngine artifacts

---

## Live Site Statistics

- **Core pages:** 9
- **Service subpages (ET):** 10
- **Service subpages (EN):** 10 (palvelut/*, services/*, servisy/* variants)
- **Multilingual pages:** 4 main + 4 certificate variants  
- **Blog posts:** 12+ (crawled 3 recent)
- **Team profiles:** ~20+ individual doctor pages (via Elementor tabs, not separate URLs)
- **TOTAL distinct content URLs:** ~50+

## Phase 1 Build Statistics

- **Pages built:** 19
- **Coverage:** All critical patient-facing pages (homepage, services, prices, team, contact, booking, certificates)
- **Remaining after Phase 1:** ~31 pages (multilingual, blog, legal, forms)

## Phase 2A Build Statistics

- **New pages built:** 13 (multilingual)
- **Pages updated:** 1 (toendid/index.html – hreflang cluster)
- **Languages covered:** ET (updated), EN, FI, RU, UK
- **Hreflang clusters:** Tõendid (5-lang: et/en/fi/ru/uk/x-default) ✅; Booking (4-lang: et/en/fi/ru) ✅; Homepages (4-lang: et/en/fi/ru) ✅; Services (4-lang: et/en/fi/ru) ✅
- **Total pages after Phase 2A:** 32 (plus 12 artiklid built by parallel session)

---

## Phase 2B – BUILT ✅ (2026-08-26)

### Blog Articles (35 total)

| URL (live) | Static File | Status |
|---|---|---|
| /kasulikku/ | artiklid/index.html | ✅ Built (index) |
| /kasulikku/pisikirurgia-valvekliinikus-dr-anastassia-schults/ | artiklid/pisikirurgia-valvekliinikus-dr-anastassia-schults/index.html | ✅ Built |
| /kasulikku/d-vitamiin-millal-on-vereanaluus-vajalik/ | artiklid/d-vitamiin-millal-on-vereanaluus-vajalik/index.html | ✅ Built |
| /kasulikku/korvad-lukus-suvel-kas-laheb-ise-ule-ja-millal-poorduda-arsti-poole/ | artiklid/korvad-lukus-suvel.../index.html | ✅ Built |
| /kasulikku/kuumarabandus-ja-ulekuumenemine-.../ | artiklid/kuumarabandus.../index.html | ✅ Built |
| /kasulikku/puugihammustus-mida-teha-ja-millal-poorduda-arsti-poole/ | artiklid/puugihammustus.../index.html | ✅ Built |
| /kasulikku/bppv/ | artiklid/bppv/index.html | ✅ Built |
| /kasulikku/korvapoletik/ | artiklid/korvapoletik/index.html | ✅ Built |
| /kasulikku/gripi-haigusnahud-diagnoosimine-ja-ravi/ | artiklid/gripi-haigusnahud.../index.html | ✅ Built |
| /kasulikku/nutikael-kui-moodsa-inimese-kaelavalude-pohjustaja/ | artiklid/nutikael.../index.html | ✅ Built |
| /kasulikku/millal-voib-kasutada-sos-pille-.../ | artiklid/sos-pillid.../index.html | ✅ Built |
| /kasulikku/kuidas-hoiduda-puukidest-.../ | artiklid/puugid-hoidumine.../index.html | ✅ Built |
| /kasulikku/gunekoloog-ivi-saar-selgitab-.../ | artiklid/vererohke-menstruatsioon.../index.html | ✅ Built |
| /kasulikku/vahene-fuusiline-liikumine-.../ | artiklid/vahene-fuusiline.../index.html | ✅ Built |
| /kasulikku/kuidas-toimida-et-paike-meile-liiga-ei-teeks/ | artiklid/kuidas-toimida-paike.../index.html | ✅ Built |
| /kasulikku/mahetoit-pole-tavatoidust-tervislikum/ | artiklid/mahetoit.../index.html | ✅ Built |
| /kasulikku/sugelev-saasehammustus/ | artiklid/sugelev-saasehammustus/index.html | ✅ Built |
| /kasulikku/koharavimid-mojuvad-peamiselt-rahakotile-.../ | artiklid/koharavimid.../index.html | ✅ Built |
| /kasulikku/psuhholoog-psuhhiaater-vastuvott/ | artiklid/psuhholoog-psuhhiaater-vastuvott/index.html | ✅ Built |
| /kasulikku/sotsiaalne-arevus/ | artiklid/sotsiaalne-arevus/index.html | ✅ Built |
| /kasulikku/labipolemine/ | artiklid/labipolemine/index.html | ✅ Built |
| /kasulikku/kuseteedepoletik/ | artiklid/kuseteedepoletik/index.html | ✅ Built |
| /kasulikku/valvekliinik-kolib-ulemiste-tervisemajja/ | artiklid/valvekliinik-kolib.../index.html | ✅ Built |
| /kasulikku/tootervishoiuteenus-tooandjale/ | artiklid/tootervishoiuteenus.../index.html | ✅ Built |
| /kasulikku/sisehaiguste-arst-maria-pintsaar/ | artiklid/sisehaiguste-arst-maria-pintsaar/index.html | ✅ Built |
| /kasulikku/narkootilise-retsepti-uuendamine/ | artiklid/narkootilise-retsepti-uuendamine/index.html | ✅ Built |
| /kasulikku/lastearsti-vastuvotud/ | artiklid/lastearsti-vastuvotud/index.html | ✅ Built |
| /kasulikku/naomaskid-aitavad-immuunsusteemi-kaitsta/ | artiklid/naomaskid.../index.html | ✅ Built |
| /kasulikku/perearstide-kumme-kasku-koroonaviiruse-kohta/ | artiklid/perearstide-kumme-kasku.../index.html | ✅ Built |
| /kasulikku/laste-nahaloobed-ning-ennetusmeetmed/ | artiklid/laste-nahaloobed.../index.html | ✅ Built |
| /kasulikku/valvekliinik-uued-lahtiolekuajad/ | artiklid/valvekliinik-uued-lahtiolekuajad/index.html | ✅ Built |
| /kasulikku/juhiloa-tervisetoend-kiirelt-katte-tallinnas/ | artiklid/juhiloa-tervisetoend.../index.html | ✅ Built |
| /kasulikku/kas-korvavalu-viitab-keskkorvapoletikule/ | artiklid/kas-korvavalu.../index.html | ✅ Built |
| /kasulikku/ettevaatust-paike/ | artiklid/ettevaatust-paike/index.html | ✅ Built |
| /kasulikku/koolikiusamine/ | artiklid/koolikiusamine/index.html | ✅ Built |
| /viimased-uudised/laste-hingamisteede-poletike-.../ | artiklid/laste-hingamisteede.../index.html | ✅ Built |

### Utility Pages

| URL (live) | Static File | Status |
|---|---|---|
| /privaatsuspoliitika/ | privaatsuspoliitika/index.html | ✅ Built |
| /arst-ilma-jarjekorrata/ | arst-ilma-jarjekorrata/index.html | ✅ Built (SEO landing) |
| /aitah/ | aitah/index.html | ✅ Built (thank-you) |

### Images Downloaded (Phase 2B)

- Dr_Ingmar_Lindstrom.jpg (used in arstid/index.html, replacing emoji)
- grete-raag.jpg
- d-vitamiini-kapslid.jpg
- korvad-lukus-suvel.webp
- puuk.webp
- kuumarabandus-ulekuumenemine.jpg
- bppv.png
- VALVEKLIINIK-26.-veebruar-2021-S7_-0360-scaled.jpg (clinic photo)

### Still Not Built (Phase 3)

- /en/, /fi/, /ru/ – Multilingual (another agent's scope)
- /toendid-en/, /toendid-fi/, /toendid-ru/, /toendid-uk/ – Multilingual certificates
- /tagasiside/ – Feedback form (needs third-party integration)
- /liitu-uudiskirjaga/ – Newsletter signup
- /arve/ – Invoice request form
- /retseptide-uuendamine/ – Alternate URL
- /teenus/spirograafia-koos-bronhodilataatortestiga/ – Spirography page

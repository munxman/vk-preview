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
| /privaatsuspoliitika/ | Legal | Privacy policy – low priority |
| /liitu-uudiskirjaga/ | Marketing | Newsletter signup – needs third-party form |
| /tagasiside/ | Marketing | Feedback form – needs third-party integration |
| /arve/ | Admin | Invoice request form |
| /arst-ilma-jarjekorrata/ | SEO landing page | Redirect target – needs content |
| /aitah/ | Conversion | Thank-you page post-booking |
| /retseptide-uuendamine/ | Service | Alternate URL for prescription renewal |
| /en/services/gynaecology/ | Multilingual | EN individual service page (confirmed 200) |
| /en/services/* (9 more) | Multilingual | EN individual service sub-pages |
| /fi/palvelut/* (10) | Multilingual | FI individual service sub-pages |
| /ru/servisy/* (10) | Multilingual | RU individual service sub-pages |
| /ru/домашняя-страница-2/ | Multilingual | Russian homepage (alt slug – may redirect) |
| /teenus/spirograafia-koos-bronhodilataatortestiga/ | Service | Spirography – single service page |
| /en/2026/08/24/, /fi/2026/08/24/, /ru/2026/08/24/ | Blog | EN/FI/RU translated blog posts |
| /category/kasulikku/ | Blog | Blog category page |

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

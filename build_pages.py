#!/usr/bin/env python3
"""Generate all static HTML pages for valvekliinik.ee static site."""

import os

BASE = os.path.dirname(os.path.abspath(__file__))

def header(title, desc, canonical, depth=1, current_page=""):
    prefix = "../" * depth
    nav_links = [
        ("Millega saame aidata?", f"{prefix}millega-saame-aidata/index.html"),
        ("Hinnakiri", f"{prefix}hinnakiri/index.html"),
        ("Meeskond", f"{prefix}arstid/index.html"),
        ("Kontakt", f"{prefix}kontakt/index.html"),
    ]
    mobile_links = nav_links + [
        ("Broneeri aeg", f"{prefix}broneerimine/index.html"),
        ("Veebivastuvõtt", f"{prefix}veebivestlus/index.html"),
    ]
    nav_items = ""
    for name, href in nav_links:
        aria = ' aria-current="page"' if name == current_page else ""
        nav_items += f'          <li><a href="{href}"{aria}>{name}</a></li>\n'
    mob_items = ""
    for name, href in mobile_links:
        mob_items += f'        <li><a href="{href}">{name}</a></li>\n'

    return f'''<!DOCTYPE html>
<html lang="et">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <meta name="robots" content="noindex,nofollow">
  <link rel="canonical" href="{canonical}">
  <link rel="alternate" hreflang="et" href="{canonical}">
  <link rel="alternate" hreflang="x-default" href="{canonical}">
  <meta property="og:type" content="website">
  <meta property="og:url" content="{canonical}">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:locale" content="et_EE">
  <meta property="og:site_name" content="Valvekliinik">
  <meta name="twitter:card" content="summary">
  <meta name="twitter:title" content="{title}">
  <meta name="twitter:description" content="{desc}">
  <link rel="stylesheet" href="{prefix}assets/style.css">
</head>
<body>
  <a class="skip-link" href="#main-content">Hüppa põhisisu juurde</a>
  <div class="draft-notice">⚠ MUSTAND – mitte avalikustada</div>

  <header class="site-header" role="banner">
    <div class="header-top">
      <a href="tel:+37259110909">📞 +372 5911 0909</a>
      &nbsp;·&nbsp; E–R 09–18 &nbsp;·&nbsp; L 12–16
      &nbsp;·&nbsp; <a href="{prefix}veebivestlus/index.html">Veebivastuvõtt – 20 €</a>
    </div>
    <div class="header-inner">
      <a class="site-logo" href="{prefix}index.html" aria-label="Valvekliinik – avaleht">
        <img src="{prefix}assets/vk-logo.svg" alt="Valvekliinik" width="180" height="50">
      </a>
      <nav class="primary-nav" aria-label="Peamine navigatsioon">
        <ul>
{nav_items}        </ul>
      </nav>
      <a class="header-cta btn btn-primary" href="{prefix}broneerimine/index.html">Broneeri aeg</a>
      <button class="nav-toggle" aria-label="Ava menüü" aria-expanded="false" onclick="this.setAttribute('aria-expanded', this.getAttribute('aria-expanded')==='true'?'false':'true'); document.getElementById('mobile-menu').classList.toggle('is-open');">
        <span></span><span></span><span></span>
      </button>
    </div>
    <nav class="mobile-menu" id="mobile-menu" aria-label="Mobiilmenüü">
      <ul>
{mob_items}      </ul>
    </nav>
  </header>
  <main id="main-content">'''


def footer(depth=1):
    prefix = "../" * depth
    return f'''  </main>

  <footer class="site-footer" role="contentinfo">
    <div class="footer-inner">
      <div class="footer-brand">
        <div class="site-logo">
          <img src="{prefix}assets/vk-logo.svg" alt="Valvekliinik" width="160" height="44">
        </div>
        <p>Kiire ja kvaliteetne arstiabi Tallinnas. Sepapaja 12/1, Ülemiste Tervisemaja 2, 3. korrus.</p>
        <p style="margin-top:12px;">Valvekliinik OÜ · Registrikood: 11576944</p>
      </div>
      <div class="footer-col">
        <h4>Teenused</h4>
        <ul>
          <li><a href="{prefix}teenused/vastuvott/index.html">Arsti vastuvõtt</a></li>
          <li><a href="{prefix}teenused/gunekoloogia/index.html">Günekoloogia</a></li>
          <li><a href="{prefix}teenused/raseduskeskus/index.html">Raseduskeskus</a></li>
          <li><a href="{prefix}teenused/ultraheliuuringud/index.html">Ultraheliuuringud</a></li>
          <li><a href="{prefix}teenused/analuusid/index.html">Analüüsid</a></li>
          <li><a href="{prefix}teenused/protseduurid/index.html">Protseduurid</a></li>
          <li><a href="{prefix}teenused/concierge/index.html">Concierge</a></li>
          <li><a href="{prefix}teenused/tervisetoendid/index.html">Tervisetõendid</a></li>
          <li><a href="{prefix}teenused/retsepti-pikendamine/index.html">Retsepti uuendamine</a></li>
          <li><a href="{prefix}tootervishoid-ja-tootajate-tervisekontroll/index.html">Töötervishoid</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>Kiirlingid</h4>
        <ul>
          <li><a href="{prefix}broneerimine/index.html">Broneeri aeg</a></li>
          <li><a href="{prefix}veebivestlus/index.html">Veebivastuvõtt</a></li>
          <li><a href="{prefix}hinnakiri/index.html">Hinnakiri</a></li>
          <li><a href="{prefix}arstid/index.html">Meie meeskond</a></li>
          <li><a href="{prefix}kontakt/index.html">Kontakt</a></li>
          <li><a href="{prefix}toendid/index.html">Juhiloa tervisetõend</a></li>
        </ul>
      </div>
      <div class="footer-col footer-contact">
        <h4>Kontakt</h4>
        <p>📍 Sepapaja 12/1, 3. korrus<br>Tallinn</p>
        <p>📞 <a href="tel:+37259110909">+372 5911 0909</a></p>
        <p>✉️ <a href="mailto:info@valvekliinik.ee">info@valvekliinik.ee</a></p>
      </div>
    </div>
    <div class="footer-bottom">
      <p>2021 © Kõik õigused kaitstud · Valvekliinik OÜ · <a href="#">Privaatsuspoliitika</a></p>
    </div>
  </footer>
</body>
</html>'''


def breadcrumb(items, depth=1):
    prefix = "../" * depth
    lis = f'<li><a href="{prefix}index.html">Avaleht</a></li>\n'
    for i, (name, href) in enumerate(items):
        if i == len(items) - 1:
            lis += f'          <li><span aria-current="page">{name}</span></li>\n'
        else:
            lis += f'          <li><a href="{href}">{name}</a></li>\n'
    return f'''    <nav class="breadcrumb" aria-label="Navigatsiooniraja">
      <div class="container">
        <ol>
          {lis}        </ol>
      </div>
    </nav>'''


def page_hero(h1, p=""):
    ptext = f'<p>{p}</p>' if p else ""
    return f'''    <div class="page-hero">
      <h1>{h1}</h1>
      {ptext}
    </div>'''


def schema_webpage(name, url, desc, breadcrumbs):
    blist = [{"@type":"ListItem","position":1,"name":"Avaleht","item":"https://valvekliinik.ee/"}]
    for i, (bname, burl) in enumerate(breadcrumbs):
        blist.append({"@type":"ListItem","position":i+2,"name":bname,"item":f"https://valvekliinik.ee{burl}"})
    import json
    schema = {
        "@context": "https://schema.org",
        "@type": "WebPage",
        "name": name,
        "url": url,
        "description": desc,
        "isPartOf": {"@id": "https://valvekliinik.ee/#clinic"},
        "breadcrumb": {
            "@type": "BreadcrumbList",
            "itemListElement": blist
        }
    }
    return f'<script type="application/ld+json">\n{json.dumps(schema, indent=2, ensure_ascii=False)}\n</script>'


def write(path, content):
    full = os.path.join(BASE, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"✓ {path}")


# ── KONTAKT ─────────────────────────────────────────────────────────────────
kontakt_schema = '''<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "WebPage",
  "name": "Kontakt – Valvekliinik",
  "url": "https://valvekliinik.ee/kontakt/",
  "isPartOf": {"@id": "https://valvekliinik.ee/#clinic"},
  "breadcrumb": {"@type":"BreadcrumbList","itemListElement":[
    {"@type":"ListItem","position":1,"name":"Avaleht","item":"https://valvekliinik.ee/"},
    {"@type":"ListItem","position":2,"name":"Kontakt","item":"https://valvekliinik.ee/kontakt/"}
  ]}
}
</script>'''

write("kontakt/index.html",
header("Kontakt – Valvekliinik | Aadress, telefon, lahtiolekuajad",
       "Valvekliinik asub Ülemiste Tervisemaja 2-s, Sepapaja 12/1, Tallinn. Telefon +372 5911 0909. E–R 09–18, L 12–16.",
       "https://valvekliinik.ee/kontakt/", depth=1, current_page="Kontakt") +
kontakt_schema + '''
''' + breadcrumb([("Kontakt","")], depth=1) + '''
''' + page_hero("Kontakt", "Kiire ja kvaliteetne arstiabi ka töövälisel ajal ja laupäeviti!") + '''
    <section>
      <div class="container">
        <div class="two-col">
          <div>
            <div class="contact-box">
              <h2>Aadress ja kontaktandmed</h2>
              <div class="contact-item">
                <span class="icon">📍</span>
                <div>
                  <strong>Aadress</strong>
                  Sepapaja 12/1, 3. korrus<br>
                  Ülemiste Tervisemaja 2<br>
                  Tallinn 11415
                </div>
              </div>
              <div class="contact-item">
                <span class="icon">📞</span>
                <div>
                  <strong>Telefon</strong>
                  <a href="tel:+37259110909">+372 5911 0909</a>
                </div>
              </div>
              <div class="contact-item">
                <span class="icon">✉️</span>
                <div>
                  <strong>E-post</strong>
                  <a href="mailto:info@valvekliinik.ee">info@valvekliinik.ee</a>
                </div>
              </div>
              <div class="contact-item">
                <span class="icon">🕐</span>
                <div>
                  <strong>Lahtiolekuajad</strong>
                  <table class="hours-table">
                    <tr><td>Esmaspäev–Reede</td><td>09:00 – 18:00</td></tr>
                    <tr><td>Laupäev</td><td>12:00 – 16:00</td></tr>
                    <tr><td>Riigipühad</td><td>12:00 – 16:00*</td></tr>
                    <tr><td>Pühapäev</td><td>Suletud</td></tr>
                  </table>
                  <small style="color:#888;font-size:0.8rem;">* Pühapäevale langevatel pühadel suletud</small>
                </div>
              </div>
              <div class="contact-item">
                <span class="icon">🏦</span>
                <div>
                  <strong>Pangaandmed</strong>
                  Valvekliinik OÜ<br>
                  Registrikood: 11576944<br>
                  IBAN: EE797700771006197042 (AS LHV Pank)
                </div>
              </div>
              <div class="contact-item">
                <span class="icon">🅿️</span>
                <div>Meie juures on parkimine kellaga 2 tundi tasuta.</div>
              </div>
            </div>
          </div>
          <div>
            <h2 class="section-title">Kuidas meieni jõuda?</h2>
            <p style="margin-bottom:16px;">Asume <strong>Ülemiste Tervisemaja 2-s</strong>, aadressil Sepapaja 12/1, 3. korrus. Ülemiste linnaosa, Tallinn.</p>
            <p style="margin-bottom:24px;">Parkimine kellaga 2 tundi tasuta.</p>

            <div class="highlight-box">
              <h3>Kirjuta meile</h3>
              <p>Küsimuste korral saatke e-kiri aadressile <strong>info@valvekliinik.ee</strong> või helistage +372 5911 0909.</p>
              <a href="mailto:info@valvekliinik.ee" class="btn btn-white">Saada e-kiri</a>
            </div>

            <div style="margin-top:24px;">
              <h3 style="margin-bottom:12px;">Valvekliinikust</h3>
              <p>Valvekliinik on tegutsenud üle viie aasta ning selle aja jooksul on abi saanud rohkem kui 12&nbsp;000 patsienti enam kui sajast riigist. Meie missioon on olla kättesaadav igale abivajajale ja pakkuda patsiendikeskset raviteenust just sellel hetkel, kui seda kõige enam vajatakse.</p>
            </div>
          </div>
        </div>
      </div>
    </section>
''' + footer(depth=1))


# ── MILLEGA SAAME AIDATA ────────────────────────────────────────────────────
write("millega-saame-aidata/index.html",
header("Millega saame aidata? – Valvekliinik | Arstiabi Tallinnas",
       "Valvekliinik pakub valvearsti, naistearsti, lastearsti vastuvõttu ja mitmeid uuringuid ning protseduure. Kiire arstiabi Tallinnas samal päeval.",
       "https://valvekliinik.ee/millega-saame-aidata/", depth=1, current_page="Millega saame aidata?") + '''
''' + breadcrumb([("Millega saame aidata?","")], depth=1) + '''
''' + page_hero("Millega saame aidata?",
   "Valvekliiniku pikaaegse kogemusega arstide ja õdede vastuvõtule võite pöörduda nii ägedate tervisemurede kui ka krooniliste haiguste korral.") + '''
    <section>
      <div class="container">
        <div class="two-col">
          <div>
            <h2 class="section-title">Arsti vastuvõtt</h2>
            <p style="margin-bottom:16px;">Vastuvõtule on oodatud nii täiskasvanud kui ka lapsed. Meie pakutava ravi hulka jäävad kõik tavapärased perearsti ravitavad, aga ka kiiremat ravi vajavad juhud, nagu kõrvavalu, hingamisteede põletikud, seljavalu, nahapõletikud, haavasidumine.</p>
            <p style="margin-bottom:16px;">Valvekliinikus pakume laia valikut uuringuid, protseduure ja analüüse, et selgitada välja Teie tervisemure olemus. Analüüsitulemused saab kätte samal päeval.</p>
            <p style="margin-bottom:16px;">Valvekliinikus on eraldi <strong>Günekoloogia- ja Raseduskeskus</strong>, kuhu on oodatud kõik naised günekoloogiliste vaevuste ja tervist puudutavate küsimustega.</p>
            <p style="margin-bottom:24px;color:#BE1E2D;font-weight:600;">NB! Valvekliinikus ei ole kohapeal röntgenit ning eluohtlike vigastuste ja haigusseisundite puhul soovitame pöörduda erakorralise meditsiini keskuse poole.</p>

            <h2 class="section-title">Kiire arstiabi samal päeval</h2>
            <p style="margin-bottom:16px;">Pakume arsti ja õe vastuvõttu samal päeval. Valveõe vastuvõtule võite pöörduda aega broneerimata. Valvearsti- ja eriarstide vastuvõtule soovitame aja broneerida meie kodulehel või helistada.</p>
            <a href="../broneerimine/index.html" class="btn btn-primary" style="margin-bottom:32px;">Broneeri vastuvõtt</a>
          </div>
          <div>
            <div class="contact-box">
              <h2>Kontakt</h2>
              <div class="contact-item">
                <span class="icon">📍</span>
                <div>Sepapaja 12/1, 3. korrus<br>Ülemiste Tervisemaja 2, Tallinn</div>
              </div>
              <div class="contact-item">
                <span class="icon">📞</span>
                <div><a href="tel:+37259110909">+372 5911 0909</a></div>
              </div>
              <div class="contact-item">
                <span class="icon">🕐</span>
                <div>E–R 09:00–18:00<br>L 12:00–16:00</div>
              </div>
            </div>
          </div>
        </div>

        <div class="category-header">Teenused</div>
        <div class="services-grid">
          <div class="service-card">
            <div class="service-card-icon">🩺</div>
            <h3>Valvearsti vastuvõtt</h3>
            <p>Pere- ja üldarsti tasemel arstiabi kiiret lahendamist vajavatele terviseprobleemidele. Samal päeval.</p>
            <div class="price">75 €</div>
            <a href="../teenused/vastuvott/index.html" class="card-link">Loe lähemalt →</a>
          </div>
          <div class="service-card">
            <div class="service-card-icon">👶</div>
            <h3>Lastearsti vastuvõtt</h3>
            <p>Kiire lastearsti vastuvõtt. Abiks nii ootamatute tervisemurede kui ka lapse arenguküsimuste korral.</p>
            <div class="price">90 €</div>
            <a href="../teenused/vastuvott/index.html" class="card-link">Loe lähemalt →</a>
          </div>
          <div class="service-card">
            <div class="service-card-icon">👩‍⚕️</div>
            <h3>Naistearsti vastuvõtt</h3>
            <p>Günekoloogilised probleemid, rasedusaegsed vaevused, rasestumisvastased vahendid.</p>
            <div class="price">90 €</div>
            <a href="../teenused/gunekoloogia/index.html" class="card-link">Loe lähemalt →</a>
          </div>
          <div class="service-card">
            <div class="service-card-icon">🤰</div>
            <h3>Raseduskeskus</h3>
            <p>Kõik vajalikud rasedusuuringud ning raseduse jälgimine alates I trimestrist.</p>
            <div class="price">alates 90 €</div>
            <a href="../teenused/raseduskeskus/index.html" class="card-link">Loe lähemalt →</a>
          </div>
          <div class="service-card">
            <div class="service-card-icon">🔬</div>
            <h3>Analüüsid</h3>
            <p>Vere-, uriini- ja kiiranalüüsid. Tulemused samal päeval.</p>
            <div class="price">alates 15 €</div>
            <a href="../teenused/analuusid/index.html" class="card-link">Loe lähemalt →</a>
          </div>
          <div class="service-card">
            <div class="service-card-icon">🔊</div>
            <h3>Ultraheliuuringud</h3>
            <p>Kilpnäärme, kõhu- ja vaagnapiirkonna, liigeste ja veenide ultraheli.</p>
            <div class="price">alates 40 €</div>
            <a href="../teenused/ultraheliuuringud/index.html" class="card-link">Loe lähemalt →</a>
          </div>
          <div class="service-card">
            <div class="service-card-icon">🧪</div>
            <h3>Protseduurid</h3>
            <p>EKG, vaktsineerimine, haavahooldus, kõrvavaigu eemaldamine, pisikirurgia.</p>
            <div class="price">alates 25 €</div>
            <a href="../teenused/protseduurid/index.html" class="card-link">Loe lähemalt →</a>
          </div>
          <div class="service-card">
            <div class="service-card-icon">💬</div>
            <h3>Veebivastuvõtt</h3>
            <p>Arstiabi veebivestluse kaudu. E–R 9–18, L 12–16.</p>
            <div class="price">20 €</div>
            <a href="../veebivestlus/index.html" class="card-link">Loe lähemalt →</a>
          </div>
          <div class="service-card">
            <div class="service-card-icon">📋</div>
            <h3>Retsepti uuendamine</h3>
            <p>Kordusretsepti pikendamine kodust lahkumata. Kiirretsept 2 tunni jooksul.</p>
            <div class="price">alates 15 €</div>
            <a href="../teenused/retsepti-pikendamine/index.html" class="card-link">Loe lähemalt →</a>
          </div>
          <div class="service-card">
            <div class="service-card-icon">📄</div>
            <h3>Tervisetõendid</h3>
            <p>Mootorsõidukijuhi tervisetõend, tõend tööle asumiseks jne. Samal päeval.</p>
            <div class="price">alates 25 €</div>
            <a href="../teenused/tervisetoendid/index.html" class="card-link">Loe lähemalt →</a>
          </div>
          <div class="service-card">
            <div class="service-card-icon">⭐</div>
            <h3>Concierge – isiklik arst</h3>
            <p>Oma isiklik arst ööpäevaringselt kättesaadav.</p>
            <div class="price">alates 250 €/kuus</div>
            <a href="../teenused/concierge/index.html" class="card-link">Loe lähemalt →</a>
          </div>
          <div class="service-card">
            <div class="service-card-icon">🏢</div>
            <h3>Töötervishoid</h3>
            <p>Töötajate tervisekontroll ettevõtetele. Litsentseeritud töötervishoiuarstid.</p>
            <div class="price">Küsi pakkumist</div>
            <a href="../tootervishoid-ja-tootajate-tervisekontroll/index.html" class="card-link">Loe lähemalt →</a>
          </div>
        </div>
      </div>
    </section>
''' + footer(depth=1))


# ── BRONEERIMINE ────────────────────────────────────────────────────────────
write("broneerimine/index.html",
header("Aja broneerimine – Valvekliinik | Broneeri vastuvõtt veebis",
       "Broneerige Valvekliiniku vastuvõtt veebis või helistage +372 5911 0909. Valvearst ja õde samal päeval. E–R 9–18, L 12–16.",
       "https://valvekliinik.ee/broneerimine/", depth=1) + '''
''' + breadcrumb([("Broneerimine","")], depth=1) + '''
''' + page_hero("Aja broneerimine", "Broneerige vastuvõtt mugavalt veebis. Valvearst ja õde samal päeval.") + '''
    <section>
      <div class="container">
        <div class="two-col">
          <div>
            <div class="info-box">
              <strong>Lahtiolekuajad</strong>
              E–R 09:00–18:00 · Laupäev 12:00–16:00 · Riigipühad 12:00–16:00 · Pühapäeval suletud
            </div>

            <h2 class="section-title" style="margin-top:24px;">Kuidas broneerida?</h2>
            <div class="steps">
              <div class="step">
                <div class="step-num">1</div>
                <div class="step-content">
                  <h3>Valige teenus</h3>
                  <p>Valige vajalik teenus (nt valvearsti vastuvõtt, naistearsti vastuvõtt, ultraheliuuring vms).</p>
                </div>
              </div>
              <div class="step">
                <div class="step-num">2</div>
                <div class="step-content">
                  <h3>Valige sobiv aeg</h3>
                  <p>Valige teile sobiv vastuvõtuaeg online broneerimissüsteemist. Pakume üldarsti ja õe vastuvõttu alati samal päeval.</p>
                </div>
              </div>
              <div class="step">
                <div class="step-num">3</div>
                <div class="step-content">
                  <h3>Tulge vastuvõtule</h3>
                  <p>Tulge õigel ajal vastuvõtule. Parkimine kellaga 2 tundi tasuta.</p>
                </div>
              </div>
            </div>

            <div class="info-box" style="margin-top:24px;">
              <strong>Broneermisreeglid</strong>
              Vastuvõtule mitteilmumise või vähem kui 24 h etteteatamise korral on kliinikul õigus esitada arve 50% ulatuses visiiditasust. Eriarstid töötavad vastavalt graafikule ning vajalik on eelnev broneerimine.
            </div>

            <div style="margin-top:32px;text-align:center;">
              <a href="https://valvekliinik.ee/broneerimine/" class="btn btn-primary" target="_blank" rel="noopener noreferrer">
                Broneeri aeg veebis (live sait) ↗
              </a>
              <p style="margin-top:12px;font-size:0.85rem;color:#888;">
                Märkus: Broneerimine toimub Valvekliiniku ametlikul veebilehel.
              </p>
            </div>
          </div>
          <div>
            <div class="contact-box">
              <h2>Kontakt</h2>
              <div class="contact-item">
                <span class="icon">📍</span>
                <div>Sepapaja 12/1, 3. korrus<br>Ülemiste Tervisemaja 2, Tallinn</div>
              </div>
              <div class="contact-item">
                <span class="icon">📞</span>
                <div>
                  <strong>Telefon</strong>
                  <a href="tel:+37259110909">+372 5911 0909</a>
                </div>
              </div>
              <div class="contact-item">
                <span class="icon">🕐</span>
                <div>
                  <strong>Lahtiolekuajad</strong>
                  E–R 09–18<br>L 12–16
                </div>
              </div>
            </div>

            <div class="highlight-box" style="margin-top:24px;">
              <h3>Veebivastuvõtt</h3>
              <p>Ei soovi kliinikusse tulla? Kasutage Veebivastuvõttu – arstiabi veebivestluse teel. 20 €.</p>
              <a href="../veebivestlus/index.html" class="btn btn-white">Alusta veebivastuvõttu</a>
            </div>
          </div>
        </div>
      </div>
    </section>
''' + footer(depth=1))


print("\n✅ Pages generated successfully!")

if __name__ == "__main__":
    pass

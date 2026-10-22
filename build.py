"""Static site generator for rbfconstruction.com.

Edit the BUSINESS facts or page content below, then run:
    python build.py            # writes the site into ./site
    python build.py --serve    # builds, then previews at http://localhost:8000
"""
import json
import os
import sys
from datetime import date
from html import escape

from PIL import Image

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from content import ARTICLES, COUNTIES, GROUPS, OTHER_AREAS, SERVICES as SVC  # noqa: E402

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "site")
IMG = os.path.join(OUT, "img")
TODAY = date.today().isoformat()


def ver(rel):
    import hashlib
    with open(os.path.join(OUT, rel), "rb") as fh:
        return hashlib.md5(fh.read()).hexdigest()[:8]

# --------------------------------------------------------------------------
# Business facts — the single source of truth for every page, schema, and llms.txt
# --------------------------------------------------------------------------
SITE = "https://rbfconstruction.com"
BIZ = {
    "name": "RBF Construction, Inc.",
    "short": "RBF Construction",
    "slogan": "A Rather Be Fishing Company",
    "phone": "810-938-8498",
    "phone_e164": "+18109388498",
    "email": "info@rbfconstruction.com",
    "street": "1411 W Hill Rd",
    "city": "Flint",
    "region": "MI",
    "region_name": "Michigan",
    "zip": "48507",
    "county": "Genesee County",
    "lat": 42.944206,
    "lng": -83.706416,
    "hours_text": "Monday–Friday, 9:00 AM – 5:00 PM",
    "facebook": "https://facebook.com/rbfconstructioninc/",
}
# Service area lives in content.py (COUNTIES) — CONFIRM WITH OWNER before launch (see README)
TOWNS = ["Flint", "Burton", "Grand Blanc", "Flushing", "Fenton", "Davison",
         "Swartz Creek", "Clio", "Mt. Morris", "Linden", "Holly", "Lapeer",
         "Owosso", "Saginaw"]
FORM_ACTION = "https://formsubmit.co/" + BIZ["email"]

MAP_EMBED = ("https://www.google.com/maps?q=RBF+Construction,+1411+W+Hill+Rd,"
             "+Flint,+MI+48507&output=embed")
MAP_LINK = "https://www.google.com/maps/search/?api=1&query=1411+W+Hill+Rd,+Flint,+MI+48507"

# --------------------------------------------------------------------------
# Photos (filename stem -> descriptive alt text / caption)
# --------------------------------------------------------------------------
PHOTOS = {
    "retail-plaza-jimmy-johns-pizza-hut-smoothie-king": "Completed multi-tenant retail building with Jimmy John's, Pizza Hut and Smoothie King storefronts built by RBF Construction",
    "commercial-renovation-before": "Before: aging single-story commercial building with a cracked, flooded parking lot",
    "commercial-renovation-after": "After: RBF Construction's renovated commercial building with stone facade, new awnings and a freshly paved, striped parking lot",
    "commercial-site-excavation-grading": "Excavators grading and excavating a commercial building site",
    "underground-utility-trench-excavation": "Crew installing manholes and pipe in an underground utility trench",
    "storm-sewer-pipe-installation-crew": "RBF crew connecting large-diameter storm sewer pipe deep in an excavation",
    "manhole-water-valve-installation": "RBF team member installing a water valve inside a precast manhole",
    "precast-structure-crane-set": "Excavator setting a precast concrete structure on a prepared base",
    "concrete-road-curb-gutter-construction": "New concrete road with curb and gutter at a commercial development",
    "steel-frame-commercial-building": "Structural steel frame of a commercial building under construction",
    "foundation-walls-excavation": "Insulated foundation walls being formed in an excavation with an excavator on site",
    "pump-station-tank-installation": "Above-ground tank with ladder, piping and bollards installed at a pump station",
    "pump-room-piping-installation": "New pumps and blue piping installed in a pump room",
    "large-water-valve-installation": "Worker rigging and installing a large blue water valve",
    "industrial-pump-room-upgrade": "Row of large industrial pumps and motors in an upgraded pump room",
}
CLIENTS = [("client-jimmy-johns", "Jimmy John's"), ("client-pizza-hut", "Pizza Hut"),
           ("client-smoothie-king", "Smoothie King"), ("client-taco-bell", "Taco Bell"),
           ("client-dollar-tree", "Dollar Tree"), ("client-biggby-coffee", "Biggby Coffee"),
           ("client-cottage-inn-pizza", "Cottage Inn Pizza"), ("client-athletico", "Athletico Physical Therapy")]


def dims(stem):
    with Image.open(os.path.join(IMG, stem + ".webp")) as im:
        return im.size


def img(stem, cls="", lazy=True, sizes=None, alt=None, priority=False):
    w, h = dims(stem)
    alt = PHOTOS.get(stem, "") if alt is None else alt
    srcset = ""
    if os.path.exists(os.path.join(IMG, stem + "-800.webp")):
        srcset = f' srcset="/img/{stem}-800.webp 800w, /img/{stem}.webp {w}w" sizes="{sizes or "100vw"}"'
    attrs = ' loading="lazy" decoding="async"' if lazy else ""
    if priority:
        attrs += ' fetchpriority="high"'
    c = f' class="{cls}"' if cls else ""
    return f'<img src="/img/{stem}.webp"{srcset} width="{w}" height="{h}" alt="{escape(alt)}"{c}{attrs}>'


# --------------------------------------------------------------------------
# Icons (inline SVG, stroke = currentColor)
# --------------------------------------------------------------------------
def icon(name):
    p = {
        "phone": '<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z"/>',
        "mail": '<rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-10 6L2 7"/>',
        "pin": '<path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0z"/><circle cx="12" cy="10" r="3"/>',
        "clock": '<circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/>',
        "check": '<path d="M20 6 9 17l-5-5"/>',
        "arrow": '<path d="M5 12h14M13 6l6 6-6 6"/>',
        "menu": '<path d="M3 6h18M3 12h18M3 18h18"/>',
        "doc": '<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6M9 13h6M9 17h6"/>',
        "excavator": '<path d="M2 20h14M4 20v-4h9v4M6 16v-3h5l1 3"/><path d="M11 13 15 5l5 3-2 5"/><path d="M18 13l2 3h-4"/>',
        "demo": '<path d="M3 21h18M5 21V9l7-5 7 5v12"/><path d="m9 13 6 6M15 13l-6 6"/>',
        "road": '<path d="M4 21 8 3M20 21 16 3M12 5v2M12 11v2M12 17v2"/>',
        "curb": '<path d="M2 18h20M2 14h8v4M10 14l4-6h8"/>',
        "pipe": '<path d="M2 8h8a4 4 0 0 1 4 4v10M2 4h8a8 8 0 0 1 8 8v10"/>',
        "grade": '<path d="M2 20h20M2 20l6-8 4 4 4-6 6 10"/>',
        "building": '<rect x="4" y="2" width="16" height="20" rx="1"/><path d="M9 22v-4h6v4M8 6h.01M12 6h.01M16 6h.01M8 10h.01M12 10h.01M16 10h.01M8 14h.01M12 14h.01M16 14h.01"/>',
        "home": '<path d="m3 10 9-7 9 7v10a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><path d="M9 22V12h6v10"/>',
        "clipboard": '<rect x="8" y="2" width="8" height="4" rx="1"/><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2M9 12l2 2 4-4"/>',
        "people": '<path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.9M16 3.1a4 4 0 0 1 0 7.8"/>',
    }
    if name == "facebook":
        return '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M14 8h3V4h-3a5 5 0 0 0-5 5v2H7v4h2v7h4v-7h3l1-4h-4V9a1 1 0 0 1 1-1z"/></svg>'
    return ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
            'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">' + p[name] + "</svg>")


# --------------------------------------------------------------------------
# Navigation
# --------------------------------------------------------------------------
# Hub pages (existing URLs kept from the old site). Detailed service pages live in content.py.
SERVICES = [
    ("/general-contracting", "General Contracting"),
    ("/residential-general-contracting", "Residential Construction"),
    ("/commercial-general-contracting", "Commercial Construction"),
    ("/site-development", "Site Development"),
]
SVC_BY_GROUP = {g: [s for s in SVC if s["group"] == g] for g in GROUPS}
ALL_SERVICE_LINKS = SERVICES + [("/" + s["slug"], s["nav"]) for s in SVC]


def header(path):
    def cur(p):
        return ' aria-current="page"' if p == path else ""
    cols = []
    for g, (label, hub) in GROUPS.items():
        items = "".join(f'<a href="/{s["slug"]}"{cur("/" + s["slug"])}>{s["nav"]}</a>' for s in SVC_BY_GROUP[g])
        cols.append(f'<div><a class="grp" href="{hub}"{cur(hub)}>{label}</a>{items}</div>')
    mega = "".join(cols)
    areas = "".join(f'<a href="/{c["slug"]}"{cur("/" + c["slug"])}>{c["name"]}</a>' for c in COUNTIES)
    return f"""<a class="skip" href="#main">Skip to content</a>
<div class="topbar"><div class="wrap">
  <span class="slogan">&ldquo;{BIZ['slogan']}&rdquo; &mdash; Serving Genesee, Oakland &amp; Southeast Michigan</span>
  <span><a class="tl" href="/careers">Careers</a><a class="tl" href="/bidding-list">Subcontractors</a>{icon('phone')} <a href="tel:{BIZ['phone_e164']}">{BIZ['phone']}</a></span>
</div></div>
<header class="site-header"><div class="wrap">
  <a class="brand" href="/" aria-label="{BIZ['short']} home">
    <img src="/img/rbf-construction-logo.webp" width="480" height="480" alt="{BIZ['short']} logo">
    <span class="brand-text"><strong>RBF CONSTRUCTION</strong><em>Genesee &middot; Oakland &middot; SE Michigan</em></span>
  </a>
  <button class="menu-toggle" aria-controls="nav" aria-expanded="false" aria-label="Open menu">{icon('menu')}</button>
  <nav id="nav" class="nav" aria-label="Main">
    <a href="/"{cur('/')}>Home</a>
    <div class="has-sub"><a href="/general-contracting"{cur('/general-contracting')}>Services</a><div class="sub mega">{mega}</div></div>
    <div class="has-sub"><a href="/service-areas"{cur('/service-areas')}>Service Areas</a><div class="sub">{areas}</div></div>
    <a href="/projects"{cur('/projects')}>Projects</a>
    <a href="/resources/"{cur('/resources/')}>Resources</a>
    <a href="/construction-contact"{cur('/construction-contact')}>Contact</a>
    <a class="btn btn-amber" href="/construction-contact#quote">Request a Bid</a>
  </nav>
</div></header>"""


def footer():
    res = "".join(f'<li><a href="/{s["slug"]}">{s["nav"]}</a></li>' for s in SVC_BY_GROUP["residential"])
    com = "".join(f'<li><a href="/{s["slug"]}">{s["nav"]}</a></li>' for s in SVC_BY_GROUP["commercial"])
    site = "".join(f'<li><a href="/{s["slug"]}">{s["nav"]}</a></li>' for s in SVC_BY_GROUP["site"])
    areas = "".join(f'<li><a href="/{c["slug"]}">{c["name"]}</a></li>' for c in COUNTIES)
    return f"""<section class="cta-band"><div class="wrap">
  <div><h2>We&rsquo;d rather be fishing.</h2><p>That&rsquo;s why we build it right the first time. Tell us about your project and get a straight answer on scope, schedule and budget.</p></div>
  <div class="actions"><a class="btn btn-amber" href="/construction-contact#quote">Request a Bid {icon('arrow')}</a><a class="btn btn-ghost" href="tel:{BIZ['phone_e164']}">{icon('phone')} {BIZ['phone']}</a></div>
</div></section>
<footer class="site-footer"><div class="wrap">
  <div class="foot-grid">
    <div>
      <img class="logo" src="/img/rbf-construction-logo.webp" width="480" height="480" alt="{BIZ['short']} logo" loading="lazy">
      <p>{BIZ['name']} is a general contractor serving Genesee County, Oakland County and all of Southeast Michigan: kitchen and bath remodeling, custom homes, commercial construction and complete site work.</p>
      <address><a href="{MAP_LINK}" rel="noopener" target="_blank">{BIZ['street']}, {BIZ['city']}, {BIZ['region']} {BIZ['zip']}</a><br>
      <a href="tel:{BIZ['phone_e164']}">{BIZ['phone']}</a> &middot; <a href="mailto:{BIZ['email']}">{BIZ['email']}</a><br>{BIZ['hours_text']}</address>
      <div class="social"><a href="{BIZ['facebook']}" rel="noopener" target="_blank" aria-label="RBF Construction on Facebook">{icon('facebook')}</a></div>
    </div>
    <div><h2><a href="/residential-general-contracting">Residential</a></h2><ul>{res}</ul>
      <h2 style="margin-top:22px"><a href="/site-development">Site Work</a></h2><ul>{site}</ul></div>
    <div><h2><a href="/commercial-general-contracting">Commercial</a></h2><ul>{com}<li><a href="/general-contracting">General Contracting</a></li></ul></div>
    <div><h2><a href="/service-areas">Service Areas</a></h2><ul>{areas}</ul></div>
    <div><h2>Company</h2><ul>
      <li><a href="/projects">Projects</a></li><li><a href="/resources/">Resources</a></li><li><a href="/careers">Careers</a></li>
      <li><a href="/bidding-list">Subcontractor Bid List</a></li><li><a href="/construction-contact">Contact</a></li>
      <li><a href="/privacy-policy">Privacy Policy</a></li></ul></div>
  </div>
  <div class="foot-bottom"><span>&copy; <span id="year">{date.today().year}</span> {BIZ['name']} &mdash; &ldquo;{BIZ['slogan']}.&rdquo; All rights reserved.</span><span>General contractor serving Genesee, Oakland &amp; Southeast Michigan</span></div>
</div></footer>
<nav class="callbar" aria-label="Quick contact"><a href="tel:{BIZ['phone_e164']}">{icon('phone')} Call Now</a><a href="/construction-contact#quote">{icon('doc')} Get a Bid</a></nav>
<script src="/js/main.js?v={ver('js/main.js')}" defer></script>"""


# --------------------------------------------------------------------------
# Structured data
# --------------------------------------------------------------------------
BIZ_ID = SITE + "/#business"


def area_served(cities=True):
    out = [{"@type": "AdministrativeArea", "name": f"{c['name']}, Michigan"} for c in COUNTIES]
    if cities:
        for c in COUNTIES[:2]:
            out += [{"@type": "City", "name": f"{t}, MI"} for t in c["cities"]]
    out += [{"@type": "Place", "name": "Southeast Michigan"}, {"@type": "State", "name": "Michigan"}]
    return out


def business_schema():
    return {
        "@type": ["GeneralContractor", "LocalBusiness"],
        "@id": BIZ_ID,
        "name": BIZ["name"],
        "alternateName": [BIZ["short"], "RBF Construction Inc", "RBF"],
        "slogan": BIZ["slogan"],
        "description": ("RBF Construction, Inc. is a general contractor headquartered in Flint, Michigan serving all of "
                        "Genesee County, Oakland County and Southeast Michigan. Services include custom homes, kitchen and bathroom "
                        "remodeling, pole barns and additions, commercial construction of office buildings, restaurants, "
                        "medical and dental offices and retail, construction management, design-build, and complete site work: "
                        "excavation, grading, underground utilities, parking lots, concrete and demolition."),
        "url": SITE + "/",
        "logo": {"@type": "ImageObject", "url": SITE + "/img/rbf-construction-logo.png"},
        "image": [SITE + "/img/og-image.jpg", SITE + "/img/commercial-renovation-after.webp",
                  SITE + "/img/commercial-site-excavation-grading.webp"],
        "telephone": BIZ["phone_e164"],
        "email": BIZ["email"],
        "address": {"@type": "PostalAddress", "streetAddress": BIZ["street"], "addressLocality": BIZ["city"],
                    "addressRegion": BIZ["region"], "postalCode": BIZ["zip"], "addressCountry": "US"},
        "geo": {"@type": "GeoCoordinates", "latitude": BIZ["lat"], "longitude": BIZ["lng"]},
        "hasMap": MAP_LINK,
        "openingHoursSpecification": [{"@type": "OpeningHoursSpecification",
                                       "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
                                       "opens": "09:00", "closes": "17:00"}],
        "areaServed": area_served(),
        "sameAs": [BIZ["facebook"]],
        "knowsAbout": ["General contracting", "Custom home building", "Kitchen remodeling", "Bathroom remodeling", "Pole barns", "Post-frame buildings",
                       "Home additions", "Commercial construction", "Office building construction", "Tenant build-outs",
                       "Restaurant construction", "Drive-thru construction", "Medical office construction",
                       "Dental office construction", "Retail construction", "Construction management", "Design-build",
                       "Design-bid-build", "Value engineering", "Site development", "Excavation", "Grading",
                       "Land balancing", "Demolition", "Parking lot construction", "Concrete curbs and gutters",
                       "Storm sewer installation", "Sanitary sewer installation", "Water line installation",
                       "Retention ponds", "Pump stations"],
        "hasOfferCatalog": {
            "@type": "OfferCatalog", "name": "Construction services",
            "itemListElement": [{"@type": "Offer", "itemOffered": {"@type": "Service", "name": t, "url": SITE + u}}
                                for u, t in ALL_SERVICE_LINKS]},
        "contactPoint": [{"@type": "ContactPoint", "telephone": BIZ["phone_e164"], "email": BIZ["email"],
                          "contactType": "sales", "areaServed": "US-MI", "availableLanguage": "English"}],
    }


def website_schema():
    return {"@type": "WebSite", "@id": SITE + "/#website", "url": SITE + "/", "name": BIZ["short"],
            "alternateName": BIZ["name"], "publisher": {"@id": BIZ_ID}, "inLanguage": "en-US"}


def crumbs_schema(trail):
    return {"@type": "BreadcrumbList", "@id": None, "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": SITE + u} for i, (n, u) in enumerate(trail)]}


def faq_schema(faqs):
    return {"@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": strip_tags(a)}}
        for q, a in faqs]}


def strip_tags(s):
    import re
    from html import unescape
    return unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", s)).strip())


def service_schema(name, path, desc, types, area=None):
    return {"@type": "Service", "@id": SITE + path + "#service", "name": name, "serviceType": types,
            "description": desc, "url": SITE + path, "provider": {"@id": BIZ_ID},
            "areaServed": area or area_served(cities=False)}


# --------------------------------------------------------------------------
# Page shell
# --------------------------------------------------------------------------
def page(path, title, desc, body, trail, extra_schema=(), page_type="WebPage", preload=None, og_image="og-image.jpg"):
    url = SITE + (path if path != "/" else "/")
    bc = crumbs_schema(trail)
    bc["@id"] = url + "#breadcrumb"
    webpage = {"@type": page_type, "@id": url + "#webpage", "url": url, "name": title, "description": desc,
               "isPartOf": {"@id": SITE + "/#website"}, "about": {"@id": BIZ_ID},
               "breadcrumb": {"@id": url + "#breadcrumb"}, "inLanguage": "en-US", "dateModified": TODAY,
               "primaryImageOfPage": {"@type": "ImageObject", "url": SITE + "/img/" + og_image}}
    graph = [business_schema(), website_schema(), webpage, bc] + list(extra_schema)
    ld = json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, separators=(",", ":"))
    pre = ""
    if preload:
        first = HERO_SLIDES[0][0]
        pre = (f'<link rel="preload" as="image" href="/img/{first}-hero.webp" '
               f'imagesrcset="/img/{first}-hero-960.webp 960w, /img/{first}-hero.webp 1920w" imagesizes="100vw" fetchpriority="high">')
    og_img = SITE + "/img/" + og_image
    return f"""<!doctype html>
<html lang="en-US">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(title)}</title>
<meta name="description" content="{escape(desc)}">
<link rel="canonical" href="{url}">
<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1">
<meta name="author" content="{BIZ['name']}">
<meta name="theme-color" content="#0b1726">
<meta name="geo.region" content="US-MI">
<meta name="geo.placename" content="{BIZ['city']}, Michigan">
<meta name="geo.position" content="{BIZ['lat']};{BIZ['lng']}">
<meta name="ICBM" content="{BIZ['lat']}, {BIZ['lng']}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{BIZ['short']}">
<meta property="og:locale" content="en_US">
<meta property="og:title" content="{escape(title)}">
<meta property="og:description" content="{escape(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{og_img}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Retail building built by RBF Construction in Michigan">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{escape(title)}">
<meta name="twitter:description" content="{escape(desc)}">
<meta name="twitter:image" content="{og_img}">
<link rel="icon" href="/favicon.ico" sizes="48x48">
<link rel="icon" href="/img/icon-192.png" type="image/png" sizes="192x192">
<link rel="apple-touch-icon" href="/img/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<link rel="alternate" type="text/plain" href="/llms.txt" title="LLM-readable summary">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@600;700&family=Barlow:wght@400;500;600;700&display=swap">
{pre}
<link rel="stylesheet" href="/css/style.css?v={ver('css/style.css')}">
<script type="application/ld+json">{ld}</script>
</head>
<body>
{header(path)}
<main id="main">
{body}
</main>
{footer()}
</body>
</html>
"""


def page_hero(h1, lead, trail, bg):
    items = "".join(
        f'<li><a href="{u}">{escape(n)}</a></li>' if i < len(trail) - 1 else f'<li aria-current="page">{escape(n)}</li>'
        for i, (n, u) in enumerate(trail))
    pic = img(bg, 'bg', lazy=False, alt='', priority=True) if bg else ""
    cls = "page-hero" if bg else "page-hero plain"
    return f"""<section class="{cls}">{pic}
<div class="wrap"><nav class="crumbs" aria-label="Breadcrumb"><ol>{items}</ol></nav>
<h1>{h1}</h1><p>{lead}</p></div></section>"""


def faq_html(faqs, heading="Frequently Asked Questions", sub=""):
    items = "".join(f"<details><summary>{escape(q)}</summary><div><p>{a}</p></div></details>" for q, a in faqs)
    return f"""<section class="alt" id="faq"><div class="wrap">
<div class="section-head center"><span class="eyebrow">FAQ</span><h2>{heading}</h2>{f'<p>{sub}</p>' if sub else ''}</div>
<div class="faq">{items}</div></div></section>"""


def aside(path, group=None):
    if group:
        label, hub = GROUPS[group]
        links = [(hub, f"All {label} Services")] + [("/" + s["slug"], s["nav"]) for s in SVC_BY_GROUP[group]]
        title = f"{label} Services"
    else:
        links, title = SERVICES, "Our Services"
    lis = "".join(f'<li><a href="{u}"{" aria-current=\"page\"" if u == path else ""}>{t}</a></li>' for u, t in links)
    areas = "".join(f'<li><a href="/{c["slug"]}">{c["name"]}</a></li>' for c in COUNTIES)
    return f"""<aside class="aside">
<div class="box"><h3>Get a Bid</h3><p>Talk directly with our team about your project&rsquo;s scope, schedule and budget.</p>
<a class="btn btn-amber" href="/construction-contact#quote">Request a Bid</a>
<a class="btn btn-ghost" href="tel:{BIZ['phone_e164']}">{icon('phone')} {BIZ['phone']}</a></div>
<div class="links"><h3>{title}</h3><ul>{lis}</ul></div>
<div class="links"><h3>Service Areas</h3><ul>{areas}</ul></div>
</aside>"""


# --------------------------------------------------------------------------
# Shared content
# --------------------------------------------------------------------------
HOME_FAQ = [
    ("What does RBF Construction do?",
     "RBF Construction, Inc. is a full-service general contractor serving Genesee County, Oakland County and Southeast Michigan. "
     "We build <a href=\"/custom-home-builder\">custom homes and additions</a>, do <a href=\"/kitchen-remodeling\">kitchen</a> "
     "and <a href=\"/bathroom-remodeling\">bathroom remodeling</a>, build <a href=\"/pole-barns\">pole barns</a>, and handle commercial construction of "
     "<a href=\"/office-building-construction\">office buildings</a>, <a href=\"/restaurant-construction\">restaurants</a>, "
     "<a href=\"/medical-office-construction\">medical and dental offices</a> and <a href=\"/retail-construction\">retail</a>, "
     "plus complete <a href=\"/site-development\">site work</a>: excavation, grading, underground utilities, parking lots, "
     "concrete and demolition."),
    ("What areas do you serve?",
     "We serve <a href=\"/genesee-county-general-contractor\">Genesee County</a>, <a href=\"/oakland-county-general-contractor\">Oakland County</a> "
     "and all of Southeast Michigan, including <a href=\"/livingston-county-general-contractor\">Livingston</a>, "
     "<a href=\"/macomb-county-general-contractor\">Macomb</a>, <a href=\"/wayne-county-general-contractor\">Wayne</a>, "
     "<a href=\"/lapeer-county-general-contractor\">Lapeer</a> and <a href=\"/washtenaw-county-general-contractor\">Washtenaw</a> "
     "counties. See all <a href=\"/service-areas\">service areas</a>."),
    ("Where is RBF Construction located?",
     f"Our office is at {BIZ['street']}, {BIZ['city']}, {BIZ['region']} {BIZ['zip']}, just off I-75 between Genesee and Oakland counties. "
     f"We&rsquo;re open {BIZ['hours_text']}. Call <a href=\"tel:{BIZ['phone_e164']}\">{BIZ['phone']}</a> or email "
     f"<a href=\"mailto:{BIZ['email']}\">{BIZ['email']}</a>."),
    ("Do you do kitchen and bathroom remodels?",
     "Yes. We remodel kitchens and bathrooms throughout Genesee County, Oakland County and Southeast Michigan, from cabinet and countertop "
     "updates to full remodels with layout changes, walk-in showers and accessible, aging-in-place bathrooms. We handle "
     "the trades, permits and inspections."),
    ("What types of commercial buildings do you build?",
     "Office buildings and tenant build-outs, restaurants including drive-thrus, medical, dental and physical therapy "
     "offices, retail stores and multi-tenant buildings. We&rsquo;ve built for brands such as Jimmy John&rsquo;s, Pizza Hut, "
     "Smoothie King, Taco Bell, Dollar Tree, Biggby Coffee, Cottage Inn Pizza and Athletico Physical Therapy."),
    ("Can RBF take a project from raw land to a finished building?",
     "Yes. Our in-house <a href=\"/site-development\">site development division</a> handles demolition, excavation, grading, "
     "utilities, paving and concrete, and we build the building too &mdash; one contractor from groundbreaking to completion."),
    ("What’s the difference between design-build and design-bid-build?",
     "In design-build, one team handles design and construction under a single contract, which simplifies communication and "
     "can shorten schedules. In design-bid-build, an architect completes the design first and contractors bid on it. RBF does "
     "both. Read our <a href=\"/resources/design-build-vs-design-bid-build\">design-build vs. design-bid-build guide</a>."),
    ("How do I get a bid or estimate?",
     f"Call <a href=\"tel:{BIZ['phone_e164']}\">{BIZ['phone']}</a> or send project details through our "
     "<a href=\"/construction-contact#quote\">bid request form</a>. Plans, photos, the site address and your target timeline "
     "help us respond faster."),
    ("I’m a subcontractor. How do I get on your bid list?",
     "Submit your company information on our <a href=\"/bidding-list\">subcontractor bidding list</a> page and we&rsquo;ll "
     "reach out when projects in your trade and area come up for bid."),
]

PROJECTS = [
    ("retail-plaza-jimmy-johns-pizza-hut-smoothie-king", "Multi-tenant retail building", "wide"),
    ("commercial-site-excavation-grading", "Commercial site excavation & grading", "wide"),
    ("storm-sewer-pipe-installation-crew", "Storm sewer installation", "tall"),
    ("concrete-road-curb-gutter-construction", "Concrete road, curb & gutter", "tall"),
    ("underground-utility-trench-excavation", "Underground utilities", ""),
    ("precast-structure-crane-set", "Setting precast structures", ""),
    ("foundation-walls-excavation", "Foundation walls", "tall"),
    ("steel-frame-commercial-building", "Structural steel erection", "tall"),
    ("manhole-water-valve-installation", "Water valve & manhole work", "tall"),
    ("pump-station-tank-installation", "Pump station tank installation", ""),
    ("industrial-pump-room-upgrade", "Industrial pump room upgrade", ""),
    ("pump-room-piping-installation", "Pump room piping", "tall"),
    ("large-water-valve-installation", "Large water valve installation", "tall"),
]


def gallery(items):
    figs = []
    for stem, cap, cls in items:
        c = f' class="{cls}"' if cls else ""
        figs.append(f'<figure{c}><button type="button" data-caption="{escape(cap)}" aria-label="Enlarge photo: {escape(cap)}">'
                    f'{img(stem, sizes="(max-width:860px) 50vw, 25vw")}</button><figcaption>{escape(cap)}</figcaption></figure>')
    return ('<div class="gallery">' + "".join(figs) + '</div>'
            '<dialog class="lightbox" aria-label="Photo viewer"><button class="close" aria-label="Close">&times;</button>'
            '<img src="" alt=""><p></p></dialog>')


def before_after():
    return f"""<div class="ba reveal">
  {img('commercial-renovation-before', sizes='(max-width:1240px) 100vw, 1200px')}
  {img('commercial-renovation-after', 'after', sizes='(max-width:1240px) 100vw, 1200px')}
  <span class="lbl b">Before</span><span class="lbl a">After</span>
  <span class="handle"></span>
  <input type="range" min="0" max="100" value="50" aria-label="Drag to compare before and after renovation">
</div>
<div class="ba-labels"><span>&larr; Drag to compare</span><span>Commercial renovation</span></div>"""


def clients_strip():
    lis = "".join(f'<li><img src="/img/{s}.webp" width="{dims(s)[0]}" height="{dims(s)[1]}" alt="{escape(n)} logo" loading="lazy"></li>'
                  for s, n in CLIENTS)
    dup = "".join(f'<li aria-hidden="true"><img src="/img/{s}.webp" width="{dims(s)[0]}" height="{dims(s)[1]}" alt="" loading="lazy"></li>'
                  for s, n in CLIENTS)
    return f"""<section class="clients" aria-label="Brands we have built for"><div class="wrap">
<p>Trusted by national brands &amp; local businesses</p>
<div class="marquee"><ul>{lis}{dup}</ul></div></div></section>"""


def area_section():
    counties = "".join(f'<li><a href="/{c["slug"]}">{c["name"]}</a></li>' for c in COUNTIES)
    return f"""<section id="service-area"><div class="wrap area">
<div>
  <span class="eyebrow">Service Area</span>
  <h2>Serving Genesee, Oakland &amp; Southeast Michigan</h2>
  <p>RBF Construction works throughout <strong>Genesee County, Oakland County</strong> and all of Southeast Michigan, from our headquarters on W Hill Rd in Flint, just off I-75. Choose your county to see the communities we serve:</p>
  <ul class="towns">{counties}</ul>
  <div class="nap"><dl>
    <dt>Address</dt><dd><a href="{MAP_LINK}" rel="noopener" target="_blank">{BIZ['street']}, {BIZ['city']}, {BIZ['region']} {BIZ['zip']}</a></dd>
    <dt>Phone</dt><dd><a href="tel:{BIZ['phone_e164']}">{BIZ['phone']}</a></dd>
    <dt>Email</dt><dd><a href="mailto:{BIZ['email']}">{BIZ['email']}</a></dd>
    <dt>Hours</dt><dd>{BIZ['hours_text']}</dd>
  </dl></div>
</div>
<div class="map"><iframe src="{MAP_EMBED}" title="Map to RBF Construction, 1411 W Hill Rd, Flint, MI" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe></div>
</div></section>"""


def child_cards(group):
    out = []
    for s in SVC_BY_GROUP[group]:
        stem = s["bg"] or (s["photos"][0] if s["photos"] else None)
        pic = (f'<div class="img">{img(stem, sizes="(max-width:640px) 100vw, 25vw")}</div>' if stem
               else f'<div class="img noimg">{icon("home" if group == "residential" else "building")}</div>')
        out.append(f'<a class="card reveal" href="/{s["slug"]}">{pic}<div class="body"><h3>{s["nav"]}</h3>'
                   f'<p>{s["lead"]}</p><span class="more">Learn more {icon("arrow")}</span></div></a>')
    return f'<div class="cards cards-{len(out)}">' + "".join(out) + "</div>"


def svc_groups():
    cols = []
    for g, (label, hub) in GROUPS.items():
        lis = "".join(f'<li><a href="/{s["slug"]}">{s["nav"]}</a></li>' for s in SVC_BY_GROUP[g])
        ic = {"residential": "home", "commercial": "building", "site": "excavator"}[g]
        cols.append(f'<div class="grp reveal">{icon(ic)}<h3><a href="{hub}">{label}</a></h3><ul>{lis}</ul>'
                    f'<a class="more" href="{hub}">All {label.lower()} services {icon("arrow")}</a></div>')
    return '<div class="svc-groups">' + "".join(cols) + "</div>"


# --------------------------------------------------------------------------
# Pages
# --------------------------------------------------------------------------
HERO_SLIDES = [
    ("retail-plaza-jimmy-johns-pizza-hut-smoothie-king", "Multi-tenant retail building &mdash; Jimmy John&rsquo;s, Pizza Hut &amp; Smoothie King", "center 65%"),
    ("commercial-renovation-after", "Commercial renovation &mdash; new facade, paving &amp; striping", "center 60%"),
    ("commercial-site-excavation-grading", "Commercial site excavation &amp; grading", "center 55%"),
    ("precast-structure-crane-set", "Setting precast structures", "center 60%"),
    ("underground-utility-trench-excavation", "Underground utility installation", "center 50%"),
    ("industrial-pump-room-upgrade", "Pump station upgrade", "center 50%"),
]


def unescape_html(t):
    from html import unescape
    return unescape(t)


def hero_slides():
    figs, dots = [], []
    for i, (stem, cap, pos) in enumerate(HERO_SLIDES):
        w, h = dims(stem + "-hero")
        first = i == 0
        load = ' fetchpriority="high"' if first else ' loading="lazy"'
        figs.append(
            f'<figure class="slide{" is-active" if first else ""}" data-caption="{escape(unescape_html(cap), quote=True)}"{"" if first else " aria-hidden=\"true\""}>'
            f'<img src="/img/{stem}-hero.webp" srcset="/img/{stem}-hero-960.webp 960w, /img/{stem}-hero.webp 1920w" sizes="100vw" '
            f'width="{w}" height="{h}" alt="{escape(PHOTOS[stem])}" style="object-position:{pos}"{load}></figure>')
        dots.append(f'<button type="button" class="dot{" is-active" if first else ""}" aria-label="Show slide {i + 1}"></button>')
    return (f'<div class="slides">{"".join(figs)}</div>',
            f'<div class="slide-bar"><div class="wrap"><p class="slide-cap" aria-live="polite">{HERO_SLIDES[0][1]}</p>'
            f'<div class="slide-nav"><button type="button" class="prev" aria-label="Previous slide">{icon("arrow")}</button>'
            f'{"".join(dots)}<button type="button" class="next" aria-label="Next slide">{icon("arrow")}</button></div></div></div>')


def home():
    caps = [
        ("building", "Commercial Site Development", "Complete site packages for office, restaurant, medical and retail projects."),
        ("grade", "Excavation &amp; Grading", "Mass excavation, land balancing, building pads and basements."),
        ("demo", "Demolition", "Building, interior and pavement demolition to clear the way for what&rsquo;s next."),
        ("road", "Parking Lots &amp; Roads", "Base preparation and construction of lots, drives and drive-thru lanes."),
        ("curb", "Curbs, Sidewalks &amp; Slabs", "Durable concrete flatwork built for Michigan freeze-thaw cycles."),
        ("pipe", "Underground Utilities", "Storm and sanitary sewers, water lines, retention ponds and pump stations."),
    ]
    links = ["/site-development", "/excavation-grading", "/demolition", "/parking-lot-paving-concrete",
             "/parking-lot-paving-concrete", "/underground-utilities"]
    caps_html = "".join(f'<a class="cap reveal" href="{l}">{icon(i)}<h3>{t}</h3><p>{d}</p></a>' for (i, t, d), l in zip(caps, links))
    cards = [
        ("/residential-general-contracting", "Residential", "Custom homes and additions, kitchen &amp; bath remodels, and pole barns &mdash; with personal on-site supervision.", "foundation-walls-excavation"),
        ("/commercial-general-contracting", "Commercial", "Office buildings, restaurants, medical and dental offices, retail and tenant build-outs.", "retail-plaza-jimmy-johns-pizza-hut-smoothie-king"),
        ("/site-development", "Site Work", "Excavation, grading, demolition, parking lots, concrete and underground utilities.", "commercial-site-excavation-grading"),
        ("/general-contracting", "General Contracting", "Construction management, design-build and design-bid-build delivered on time and on budget.", "steel-frame-commercial-building"),
    ]
    cards_html = "".join(
        f'<a class="card reveal" href="{u}"><div class="img">{img(s, sizes="(max-width:640px) 100vw, (max-width:1060px) 50vw, 25vw")}</div>'
        f'<div class="body"><h3>{t}</h3><p>{d}</p><span class="more">Learn more {icon("arrow")}</span></div></a>'
        for u, t, d, s in cards)
    steps = [
        ("Consult &amp; Site Review", "We walk the site or home, review plans and goals, and give expert technical advice from day one."),
        ("Budget &amp; Value Engineering", "We price the work, find savings without cutting corners, and select the right trades."),
        ("Build with On-Site Supervision", "Our crews and trusted trades execute while we manage scheduling, permits and logistics in person."),
        ("Close Out &amp; Hand Over", "Final inspections, punch list and a finished project delivered to your exact specifications."),
    ]
    steps_html = "".join(f'<li class="reveal"><h3>{t}</h3><p>{d}</p></li>' for t, d in steps)

    body = f"""
<section class="hero hero-slides" aria-label="Featured projects">
  {hero_slides()[0]}
  <div class="wrap">
    <span class="eyebrow">&ldquo;{BIZ['slogan']}&rdquo;</span>
    <h1>Genesee, Oakland &amp; <span>Southeast Michigan</span> General Contractor</h1>
    <p class="lead">Custom homes, remodels and pole barns. Offices, restaurants, medical and retail buildings. Plus all the site work underneath them &mdash; from the first shovel of dirt to the final walkthrough.</p>
    <div class="actions">
      <a class="btn btn-amber" href="/construction-contact#quote">Request a Bid {icon('arrow')}</a>
      <a class="btn btn-ghost" href="tel:{BIZ['phone_e164']}">{icon('phone')} Call {BIZ['phone']}</a>
    </div>
  </div>
  {hero_slides()[1]}
</section>
{clients_strip()}
<section><div class="wrap split">
  <div class="media reveal"><div class="collage">
    {img('storm-sewer-pipe-installation-crew', sizes='(max-width:860px) 50vw, 300px')}
    {img('commercial-site-excavation-grading', sizes='(max-width:860px) 50vw, 300px')}
    {img('concrete-road-curb-gutter-construction', sizes='(max-width:860px) 50vw, 300px')}
    <div class="badge-card"><strong>Ground-up builder</strong><span>Site work, utilities &amp; buildings under one contract</span></div>
  </div></div>
  <div class="reveal">
    <span class="eyebrow">Who We Are</span>
    <h2>Your Vision, Our Expertise in Construction</h2>
    <p><strong>RBF Construction</strong> is a full-service general contractor serving Genesee County, Oakland County and all of Southeast Michigan. We build custom homes and pole barns, remodel kitchens and bathrooms, construct offices, restaurants, medical and retail buildings, and handle every phase of site work with our own crews.</p>
    <p>We pair a trusted network of skilled tradesmen, subcontractors and architects with personal on-site supervision, so every project is streamlined for efficiency and cost-effectiveness &mdash; whether it&rsquo;s one bathroom or a ground-up commercial site.</p>
    <ul class="checks">
      <li>{icon('check')}<span><strong>On time and on budget.</strong> Schedules and budgets are managed from preconstruction through closeout.</span></li>
      <li>{icon('check')}<span><strong>Built to your exact specifications.</strong> Your goals drive every project decision.</span></li>
      <li>{icon('check')}<span><strong>One accountable team.</strong> Site work, building and finishes under one roof.</span></li>
    </ul>
    <a class="btn btn-navy" href="/general-contracting">Our Approach {icon('arrow')}</a>
  </div>
</div></section>

<section class="alt"><div class="wrap">
  <div class="section-head center"><span class="eyebrow">Our Services</span><h2>Residential, Commercial &amp; Site Work</h2>
  <p>Everything from a kitchen remodel to a ground-up medical building &mdash; and the site work underneath it.</p></div>
  <div class="cards">{cards_html}</div>
  {svc_groups()}
</div></section>

<section><div class="wrap">
  <div class="section-head center"><span class="eyebrow">Recent Work</span><h2>Before &amp; After: Commercial Renovation</h2>
  <p>Drag the slider to see how RBF transformed a tired storefront and failing parking lot into a modern commercial building with new paving and striping.</p></div>
  {before_after()}
</div></section>

<section class="dark"><div class="wrap">
  <div class="section-head"><span class="eyebrow">Site Development Division</span><h2>Earthwork &amp; Civil, Done In-House</h2>
  <p>A successful project starts with a solid foundation. Our full-service earthwork division handles everything from initial site review to the critical groundwork.</p></div>
  <div class="caps">{caps_html}</div>
  <p style="margin-top:34px"><a class="btn btn-amber" href="/site-development">Explore Site Development {icon('arrow')}</a></p>
</div></section>

<section class="alt"><div class="wrap">
  <div class="section-head center"><span class="eyebrow">How We Work</span><h2>A Clear Process From Start to Finish</h2>
  <p>As part of your project team from the start, we provide budgeting, value engineering, scheduling and logistics support.</p></div>
  <ol class="steps">{steps_html}</ol>
</div></section>

<section><div class="wrap">
  <div class="section-head"><span class="eyebrow">Project Gallery</span><h2>From the Job Site</h2>
  <p>Real photos from RBF Construction projects &mdash; utilities, earthwork, concrete, steel and finished buildings.</p></div>
  {gallery(PROJECTS[:8])}
  <p style="margin-top:30px"><a class="btn btn-navy" href="/projects">View All Projects {icon('arrow')}</a></p>
</div></section>

{faq_html(HOME_FAQ, "Questions About Working With RBF", "Quick answers about our services, service area and how to get a bid.")}
{area_section()}
"""
    title = "General Contractor | Genesee, Oakland & SE Michigan | RBF"
    desc = ("Genesee, Oakland & SE Michigan general contractor: custom homes, remodels, pole barns, offices, restaurants, "
            "medical & retail builds, site work.")
    return page("/", title, desc, body, [("Home", "/")], [faq_schema(HOME_FAQ)],
                preload="hero")


def service_page(path, crumb, title, desc, h1, lead, bg, content, faqs, svc_name, svc_types, photos, group=None, trail=None):
    if trail is None:
        if group:
            trail = [("Home", "/"), (GROUPS[group][0], GROUPS[group][1]), (crumb, path)]
        elif path == "/general-contracting":
            trail = [("Home", "/"), (crumb, path)]
        else:
            trail = [("Home", "/"), ("Services", "/general-contracting"), (crumb, path)]
    row = "".join(img(p, sizes="(max-width:640px) 50vw, 250px") for p in photos)
    content = content.replace('<!--PHOTOS-->', f'<div class="photo-row">{row}</div>' if photos else "")
    body = f"""{page_hero(h1, lead, trail, bg)}
<section><div class="wrap content-grid">
  <article class="prose">{content}</article>
  {aside(path, group or {"/residential-general-contracting": "residential", "/commercial-general-contracting": "commercial", "/site-development": "site"}.get(path))}
</div></section>
{faq_html(faqs, "Common Questions") if faqs else ''}"""
    extra = [service_schema(svc_name, path, desc, svc_types)]
    if faqs:
        extra.append(faq_schema(faqs))
    return page(path, title, desc, body, trail, extra, og_image="og-image.jpg")


def detail_service(s):
    return service_page("/" + s["slug"], s["nav"], s["title"], s["desc"], s["h1"], s["lead"], s["bg"], s["body"],
                        s["faqs"], s["name"], s["types"], s["photos"], group=s["group"])


def general_contracting():
    all_svcs = "".join(f'<li><a href="/{s["slug"]}">{s["nav"]}</a></li>' for s in SVC)
    content = f"""
<h2>Comprehensive Construction Solutions</h2>
<p>At RBF Construction, Inc. we deliver outstanding results for projects of all sizes across <strong>Genesee County, Oakland County and Southeast Michigan</strong>. As a full-service construction company, we provide general contracting, construction management, design-build and construction consulting services for residential and commercial clients. Our team manages every detail to ensure your complete satisfaction.</p>
<ul class="tick-list"><li>General contracting</li><li>Construction management</li><li>Design-build</li><li>Design-bid-build</li><li>Construction consulting</li><li>Value engineering</li></ul>
<h2>Design-Bid-Build Expertise</h2>
<p>We specialize in traditional design-bid-build projects for commercial facilities, working closely with architects to deliver on time and within budget. When the drawings are done, we bring accurate pricing, a realistic schedule and the right subcontractors to the table.</p>
<h2>Design-Build: One Team, One Contract</h2>
<p>Prefer a single point of responsibility? With design-build, RBF coordinates design and construction together, which simplifies communication and keeps decisions moving. Learn more in our <a href="/resources/design-build-vs-design-bid-build">design-build vs. design-bid-build guide</a>.</p>
<h2>Comprehensive Construction Management</h2>
<p>As part of your project team from the start, we provide critical support in <strong>budgeting, value engineering, scheduling and logistics</strong> &mdash; ensuring seamless execution and optimal contractor selection.</p>
<!--PHOTOS-->
<h2>Everything We Build</h2>
<ul class="tick-list">{all_svcs}</ul>
<h2>Why Choose RBF?</h2>
<ul>
<li><strong>Tailored solutions:</strong> services customized to meet your unique needs.</li>
<li><strong>Collaborative approach:</strong> integrated teamwork from planning to completion.</li>
<li><strong>Client-focused:</strong> your goals and expectations drive every project decision.</li>
<li><strong>Site work in-house:</strong> our own <a href="/site-development">site development division</a> means fewer handoffs and tighter schedules.</li>
<li><strong>Personal on-site supervision</strong> backed by a trusted network of tradesmen, subcontractors and architects.</li>
</ul>
<p>Discover the RBF difference &mdash; where your vision becomes our mission. <a href="/construction-contact#quote">Request a bid</a>.</p>"""
    faqs = [
        ("What does a general contractor do?",
         "A general contractor manages a construction project from start to finish: pricing and budgeting, scheduling, hiring and coordinating subcontractors, ordering materials, pulling permits, managing the job site, and making sure the work meets the plans, codes and your expectations."),
        ("Does RBF offer construction management services?",
         "Yes. RBF provides construction management including budgeting, value engineering, scheduling, logistics and contractor selection, starting early in the project."),
        ("Do you work with my architect?",
         "Yes. We regularly work with owners' architects on design-bid-build projects, and we also have a network of architects for design-build projects."),
    ]
    return service_page(
        "/general-contracting", "General Contracting",
        "General Contracting & Design-Build | SE Michigan | RBF",
        "Full-service general contractor for Genesee, Oakland & Southeast Michigan: construction management, design-build, design-bid-build and consulting.",
        "General Contracting in Genesee, Oakland &amp; Southeast Michigan",
        "General contracting, construction management, design-build and consulting &mdash; managed in person, delivered on time and on budget.",
        "steel-frame-commercial-building", content, faqs, "General Contracting",
        ["General contracting", "Construction management", "Design-build", "Design-bid-build", "Construction consulting"],
        ["steel-frame-commercial-building", "foundation-walls-excavation", "concrete-road-curb-gutter-construction"])


def commercial():
    content = f"""
<h2>Commercial General Contractor for Southeast Michigan Businesses</h2>
<p>RBF Construction builds and renovates commercial properties of all kinds for owners, developers and national brands across Genesee County, Oakland County and Southeast Michigan &mdash; <strong>office buildings, restaurants, medical and dental offices, retail stores and multi-tenant buildings</strong>. Our work includes projects for Jimmy John&rsquo;s, Pizza Hut, Smoothie King, Taco Bell, Dollar Tree, Biggby Coffee, Cottage Inn Pizza and Athletico Physical Therapy.</p>
{child_cards('commercial')}
<p>Because we also run our own <a href="/site-development">site development division</a>, we can take a commercial project from raw ground &mdash; demolition, excavation, utilities, parking lot and concrete &mdash; all the way through the finished building.</p>
<h2>Featured: Commercial Renovation</h2>
<p>An aging storefront with a failing, flooded parking lot became a modern commercial building with a stone facade, new awnings and a freshly paved, striped lot.</p>
{before_after()}
<h2>Design-Bid-Build &amp; Design-Build</h2>
<p>We specialize in traditional design-bid-build projects for commercial facilities, working closely with architects to deliver on time and within budget. For owners who want a single point of responsibility, we also offer design-build.</p>
<h2>Construction Management From Day One</h2>
<p>We join your project team early to provide budgeting, value engineering, scheduling and logistics support &mdash; and to select the right subcontractors for each scope.</p>
<p>Ready to talk about your next location or renovation? <a href="/construction-contact#quote">Request a commercial bid</a> or call <a href="tel:{BIZ['phone_e164']}">{BIZ['phone']}</a>.</p>"""
    faqs = [
        ("What types of commercial projects does RBF build?",
         "Office buildings and tenant build-outs, restaurants and drive-thrus, medical, dental and physical therapy offices, retail stores and multi-tenant buildings, commercial renovations, facility upgrades such as pump stations, and the site work that goes with them."),
        ("Can you handle the site work and the building on a commercial project?",
         "Yes. RBF has an in-house site development division for demolition, excavation, grading, utilities, paving and concrete, and we serve as the general contractor for the building."),
        ("Have you built for national brands?",
         "Yes. Our work includes projects for brands such as Jimmy John's, Pizza Hut, Smoothie King, Taco Bell, Dollar Tree, Biggby Coffee, Cottage Inn Pizza and Athletico Physical Therapy."),
        ("Do you build commercial projects in Oakland County?",
         "Yes. We build throughout Oakland County, including Troy, Southfield, Auburn Hills, Novi, Rochester Hills and Waterford, and across Southeast Michigan."),
    ]
    return service_page(
        "/commercial-general-contracting", "Commercial Construction",
        "Commercial Construction | Genesee, Oakland & SE MI | RBF",
        "Commercial contractor for Genesee, Oakland & Southeast Michigan: office buildings, restaurants, medical offices, retail and tenant build-outs.",
        "Commercial Construction in Genesee, Oakland &amp; Southeast Michigan",
        "Office buildings, restaurants, medical facilities and retail &mdash; from site work to ribbon cutting, for local owners and national brands.",
        "retail-plaza-jimmy-johns-pizza-hut-smoothie-king", content, faqs, "Commercial General Contracting",
        ["Commercial construction", "Office construction", "Restaurant construction", "Medical office construction",
         "Retail construction", "Tenant build-out", "Commercial renovation"], [], trail=[("Home", "/"), ("Commercial", "/commercial-general-contracting")])


def residential():
    content = f"""
<h2>Residential Construction With Personal Supervision</h2>
<p>RBF Construction brings the discipline of a commercial contractor to homes across <strong>Genesee County, Oakland County and Southeast Michigan</strong>. Whether you&rsquo;re building a new home from the ground up, adding on, remodeling a kitchen or bathroom, or putting up a pole barn, you get one accountable contractor, personal on-site supervision and a trusted network of skilled tradesmen.</p>
{child_cards('residential')}
<h2>Built Right From the Ground Up</h2>
<p>Many residential headaches start below grade or behind the walls. Because RBF runs its own <a href="/site-development">site development and earthwork division</a>, we handle excavation, grading, drainage, foundations and utility work with the same team that manages your build &mdash; so nothing falls through the cracks between contractors.</p>
<h2>How We Work With Homeowners</h2>
<ul>
<li><strong>Tailored solutions:</strong> we listen first, then scope the work to your needs and budget.</li>
<li><strong>Clear budgeting and scheduling:</strong> we plan the work in detail and order long-lead items before demolition.</li>
<li><strong>Permits and inspections handled:</strong> we pull permits and schedule inspections.</li>
<li><strong>Clean, respectful job sites:</strong> dust control and daily cleanup in occupied homes.</li>
</ul>
<p>Planning a project? Read our <a href="/resources/kitchen-bathroom-remodel-planning-guide">kitchen and bath remodel planning guide</a>, then <a href="/construction-contact#quote">tell us about it</a> or call <a href="tel:{BIZ['phone_e164']}">{BIZ['phone']}</a>.</p>"""
    faqs = [
        ("What residential services does RBF Construction offer?",
         "Custom homes and additions, kitchen remodeling, bathroom remodeling, pole barns and garages, and residential site work such as excavation, foundations, grading, drainage, driveways and utility connections."),
        ("Do you do residential work in Oakland County?",
         "Yes. We remodel and build homes throughout Oakland County, including Clarkston, Waterford, Rochester Hills, Troy, Novi, Milford, Holly and Oxford, and across Southeast Michigan."),
    ]
    return service_page(
        "/residential-general-contracting", "Residential",
        "Residential Contractor | Genesee, Oakland & SE MI | RBF",
        "Custom homes, kitchen & bath remodels and pole barns in Genesee, Oakland & Southeast Michigan, with in-house site work and on-site supervision.",
        "Custom Homes, Remodels &amp; Pole Barns",
        "Custom homes and additions, kitchen and bath remodels, and pole barns across Genesee County, Oakland County and Southeast Michigan.",
        "foundation-walls-excavation", content, faqs, "Residential General Contracting",
        ["Residential construction", "Custom home building", "Home additions", "Kitchen remodeling", "Bathroom remodeling", "Pole barns"],
        [], trail=[("Home", "/"), ("Residential", "/residential-general-contracting")])


def site_development():
    content = f"""
<h2>Site Development &amp; Earthwork Contractor for Southeast Michigan</h2>
<p>We believe a successful project starts with a solid foundation. Our experienced crews provide comprehensive <strong>site development and earthwork services</strong> across Genesee County, Oakland County and Southeast Michigan, ensuring your project gets off to the right start. We handle everything from initial site review and expert technical advice to the critical groundwork.</p>
{child_cards('site')}
<h2>Our Full-Service Earthwork Division</h2>
<ul class="tick-list">
<li>Commercial site development</li><li>Land balancing &amp; excavation</li><li>Demolition</li><li>Road &amp; parking lot construction</li>
<li>Curbs, gutters, sidewalks &amp; slabs</li><li>Grading &amp; drainage</li><li>Storm sewers &amp; retention ponds</li><li>Sanitary sewers &amp; water lines</li></ul>
<h2>Projects of All Sizes</h2>
<p>We&rsquo;re equipped to handle projects of all sizes, from a residential lot to a multi-acre commercial development. Pair our site work with RBF&rsquo;s <a href="/general-contracting">general contracting</a> services and get one team from bare ground to finished building. New to commercial site work? Read our <a href="/resources/commercial-site-work-guide">commercial site work guide</a>.</p>
<p><a href="/construction-contact#quote">Request a site development bid</a> or call <a href="tel:{BIZ['phone_e164']}">{BIZ['phone']}</a>.</p>"""
    faqs = [
        ("What site development services does RBF offer?",
         "Commercial and residential site development, land balancing and excavation, demolition, road and parking lot construction, curbs, gutters, sidewalks and slabs, grading and drainage, and underground utilities including storm sewers, retention ponds, sanitary sewers and water lines."),
        ("What is land balancing?",
         "Land balancing means moving soil on a site so the amount cut from high areas matches the fill needed in low areas, reaching plan grades while minimizing the cost of hauling dirt on or off the site."),
        ("Do you do site work in Oakland County?",
         "Yes. We provide site development, excavation, utilities, paving and demolition throughout Genesee County, Oakland County and Southeast Michigan."),
    ]
    return service_page(
        "/site-development", "Site Work",
        "Site Development & Excavation | SE Michigan | RBF",
        "Site development contractor for Genesee, Oakland & Southeast Michigan: excavation, grading, demolition, parking lots, concrete and underground utilities.",
        "Site Development, Excavation &amp; Utilities",
        "Earthwork, demolition, paving, concrete and underground utilities &mdash; the solid foundation every successful project needs.",
        "commercial-site-excavation-grading", content, faqs, "Site Development and Earthwork",
        ["Site development", "Excavation", "Land balancing", "Demolition", "Parking lot construction",
         "Concrete curbs and gutters", "Storm sewer installation", "Sanitary sewer installation", "Water line installation"],
        [], trail=[("Home", "/"), ("Site Work", "/site-development")])


# --------------------------------------------------------------------------
# Service areas
# --------------------------------------------------------------------------
def county_page(c):
    path = "/" + c["slug"]
    trail = [("Home", "/"), ("Service Areas", "/service-areas"), (c["name"], path)]
    cities = "".join(f"<li>{t}</li>" for t in c["cities"])
    others = "".join(f'<li><a href="/{o["slug"]}">{o["name"]}</a></li>' for o in COUNTIES if o is not c)
    body = f"""{page_hero(c['h1'], c['lead'], trail, c['bg'])}
<section><div class="wrap content-grid">
  <article class="prose">{c['intro']}{c['focus']}
  <h2>{c['name']} Communities We Serve</h2>
  <ul class="city-list">{cities}</ul>
  <p>Don&rsquo;t see your community? We work throughout {c['name']} and the rest of Southeast Michigan &mdash; <a href="/construction-contact#quote">ask us about your project</a>.</p>
  <h2>Other Areas We Serve</h2><ul class="city-list">{others}</ul>
  </article>
  {aside(path)}
</div></section>
{faq_html(c['faqs'], f"{c['name']} FAQ")}"""
    area = [{"@type": "AdministrativeArea", "name": f"{c['name']}, Michigan"}] + \
           [{"@type": "City", "name": f"{t}, MI"} for t in c["cities"]]
    svc = service_schema(f"General contracting in {c['name']}, Michigan", path, strip_tags(c["desc"]),
                         ["General contracting", "Remodeling", "Commercial construction", "Site development"], area)
    return page(path, c["title"], c["desc"], body, trail, [svc, faq_schema(c["faqs"])])


def service_areas():
    trail = [("Home", "/"), ("Service Areas", "/service-areas")]
    cards = "".join(
        f'<a class="county reveal" href="/{c["slug"]}"><h3>{c["name"]}</h3><p>{", ".join(c["cities"][:7])} and more</p>'
        f'<span class="more">View {c["name"]} {icon("arrow")}</span></a>' for c in COUNTIES)
    body = f"""{page_hero("Service Areas: Genesee, Oakland &amp; Southeast Michigan", "RBF Construction serves Genesee County, Oakland County and the surrounding Southeast Michigan counties from our headquarters in Flint.", trail, "commercial-site-excavation-grading")}
<section><div class="wrap">
  <div class="section-head"><span class="eyebrow">Where We Work</span><h2>Counties We Serve</h2>
  <p>We take on residential remodeling, new homes, commercial construction and site work in each of these counties. Select yours to see the communities we serve.</p></div>
  <div class="county-grid">{cards}</div>
  <p style="margin-top:30px">We also take projects in {", ".join(OTHER_AREAS[:-1])} and {OTHER_AREAS[-1]}. <a href="/construction-contact#quote">Contact us</a> about your location.</p>
</div></section>
{area_section()}"""
    return page("/service-areas", "Service Areas | Genesee, Oakland & SE MI | RBF",
                "RBF Construction serves Genesee and Oakland counties plus Livingston, Lapeer, Macomb, Wayne and Washtenaw counties in Southeast Michigan.",
                body, trail, [{"@type": "ItemList", "name": "RBF Construction service areas",
                               "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": c["name"], "url": f"{SITE}/{c['slug']}"}
                                                   for i, c in enumerate(COUNTIES)]}])


# --------------------------------------------------------------------------
# Resources
# --------------------------------------------------------------------------
def article_page(a):
    path = "/resources/" + a["slug"]
    trail = [("Home", "/"), ("Resources", "/resources/"), (strip_tags(a["h1"]).split(":")[0], path)]
    lead = a["summary"]
    body = f"""{page_hero(a['h1'], lead, trail, a['bg'])}
<section><div class="wrap content-grid">
  <article class="prose"><p class="byline">By the RBF Construction team &middot; Updated <time datetime="{TODAY}">{date.today().strftime('%B %d, %Y')}</time></p>{a['body']}</article>
  {aside(path)}
</div></section>"""
    art = {"@type": "Article", "@id": SITE + path + "#article", "headline": strip_tags(a["h1"]), "description": a["desc"],
           "abstract": a["summary"], "datePublished": TODAY, "dateModified": TODAY,
           "author": {"@id": BIZ_ID}, "publisher": {"@id": BIZ_ID}, "mainEntityOfPage": SITE + path,
           "image": SITE + "/img/" + (a["bg"] + ".webp" if a["bg"] else "og-image.jpg"), "inLanguage": "en-US"}
    return page(path, a["title"], a["desc"], body, trail, [art])


def resources():
    trail = [("Home", "/"), ("Resources", "/resources/")]
    cards = "".join(f'<a class="county reveal" href="/resources/{a["slug"]}"><h3>{a["h1"]}</h3><p>{a["summary"]}</p>'
                    f'<span class="more">Read the guide {icon("arrow")}</span></a>' for a in ARTICLES)
    body = f"""{page_hero("Construction Guides &amp; Resources", "Straight answers to common questions about remodeling, building and site work in Southeast Michigan.", trail, None)}
<section><div class="wrap"><div class="county-grid">{cards}</div></div></section>"""
    return page("/resources/", "Construction Guides & Resources | RBF Construction",
                "Guides from RBF Construction on design-build vs. design-bid-build, planning a kitchen or bath remodel, and commercial site work in Michigan.",
                body, trail, page_type="CollectionPage")


def projects():
    trail = [("Home", "/"), ("Projects", "/projects")]
    body = f"""{page_hero("Construction Projects by RBF", "A look at our work across commercial buildings, renovations, site development, underground utilities and pump station upgrades.", trail, "commercial-renovation-after")}
<section><div class="wrap feature">
  <div class="reveal">{img('retail-plaza-jimmy-johns-pizza-hut-smoothie-king', sizes='(max-width:860px) 100vw, 680px')}</div>
  <div class="reveal"><span class="eyebrow">Featured Project</span><h2>Multi-Tenant Retail Building</h2>
  <p>A ground-up retail building with storefronts for Jimmy John&rsquo;s (with drive-thru), Pizza Hut and Smoothie King, finished with stone veneer, metal panel accents and a new concrete parking area.</p>
  <a class="btn btn-navy" href="/commercial-general-contracting">Commercial Services {icon('arrow')}</a></div>
</div></section>
<section class="alt"><div class="wrap">
  <div class="section-head center"><span class="eyebrow">Renovation</span><h2>Before &amp; After</h2><p>Drag to compare.</p></div>
  {before_after()}
</div></section>
<section><div class="wrap">
  <div class="section-head"><span class="eyebrow">Gallery</span><h2>On the Job Site</h2><p>Select any photo to enlarge it.</p></div>
  {gallery(PROJECTS[1:])}
</div></section>"""
    gal = {"@type": "ImageGallery", "@id": SITE + "/projects#gallery", "name": "RBF Construction project photos",
           "about": {"@id": BIZ_ID},
           "image": [{"@type": "ImageObject", "contentUrl": f"{SITE}/img/{s}.webp", "caption": PHOTOS[s],
                      "creator": {"@id": BIZ_ID}, "copyrightHolder": {"@id": BIZ_ID}} for s in PHOTOS]}
    return page("/projects", "Construction Projects & Gallery | RBF Construction",
                "See RBF Construction's commercial buildings, renovations, site development and underground utility projects in the Flint, Michigan area.",
                body, trail, [gal], page_type="CollectionPage")


def field(label, name, kind="text", req=True, full=False, auto=None, rows=None):
    r = ' required' if req else ''
    star = ' <span class="req" aria-hidden="true">*</span>' if req else ''
    ac = f' autocomplete="{auto}"' if auto else ''
    c = ' full' if full else ''
    if kind == "textarea":
        ctl = f'<textarea id="{name}" name="{name}"{r}></textarea>'
    elif isinstance(kind, list):
        opts = "".join(f"<option>{o}</option>" for o in kind)
        ctl = f'<select id="{name}" name="{name}"{r}><option value="">Select&hellip;</option>{opts}</select>'
    else:
        ctl = f'<input id="{name}" name="{name}" type="{kind}"{r}{ac}>'
    return f'<div class="field{c}"><label for="{name}">{label}{star}</label>{ctl}</div>'


def form(subject, fields, button):
    return f"""<form class="card-form" action="{FORM_ACTION}" method="POST">
<input type="hidden" name="_subject" value="{subject}">
<input type="hidden" name="_next" value="{SITE}/thank-you">
<input type="hidden" name="_template" value="table">
<input type="text" name="_honey" class="hp" tabindex="-1" autocomplete="off" aria-hidden="true">
<div class="fields">{''.join(fields)}</div>
<p style="margin-top:22px"><button class="btn btn-amber" type="submit">{button} {icon('arrow')}</button></p>
<p class="form-note">We&rsquo;ll only use your information to respond to you. See our <a href="/privacy-policy">privacy policy</a>.</p>
</form>"""


def contact():
    trail = [("Home", "/"), ("Contact", "/construction-contact")]
    f = form("New bid request — rbfconstruction.com", [
        field("Your name", "name", auto="name"),
        field("Company (optional)", "company", req=False, auto="organization"),
        field("Phone number", "phone", "tel", auto="tel"),
        field("Email address", "email", "email", auto="email"),
        field("Project type", "project_type", ["Kitchen remodel", "Bathroom remodel", "Custom home / addition",
                                               "Office building / build-out", "Restaurant", "Medical / dental office",
                                               "Retail / commercial business", "Excavation / grading", "Underground utilities",
                                               "Parking lot / concrete", "Demolition", "Construction management / consulting", "Other"]),
        field("Project location (city)", "location", req=False, auto="address-level2"),
        field("Tell us about your project", "message", "textarea", full=True),
    ], "Submit Your Inquiry")
    body = f"""{page_hero("Contact RBF Construction", "Get in touch for reliable construction services anywhere in Genesee County, Oakland County and Southeast Michigan. Call, email or send your project details for a bid.", trail, "precast-structure-crane-set")}
<section id="quote"><div class="wrap form-wrap">
  <div><span class="eyebrow">Request a Bid</span><h2>Tell Us About Your Project</h2>
  <p>Share a few details and our team will follow up. Plans, photos, the address and your target timeline help us respond faster.</p>{f}</div>
  <div class="nap" style="position:sticky;top:110px">
    <h3>Talk to Us Directly</h3>
    <dl>
      <dt>Office</dt><dd><a href="tel:{BIZ['phone_e164']}">{BIZ['phone']}</a></dd>
      <dt>Email</dt><dd><a href="mailto:{BIZ['email']}">{BIZ['email']}</a></dd>
      <dt>Address</dt><dd><a href="{MAP_LINK}" rel="noopener" target="_blank">{BIZ['street']}<br>{BIZ['city']}, {BIZ['region']} {BIZ['zip']}</a></dd>
      <dt>Hours</dt><dd>{BIZ['hours_text']}</dd>
      <dt>Serving</dt><dd><a href="/service-areas">Genesee, Oakland &amp; Southeast Michigan</a></dd>
    </dl>
    <p style="margin:18px 0 0"><a class="btn btn-navy" href="tel:{BIZ['phone_e164']}" style="width:100%">{icon('phone')} Call Now</a></p>
  </div>
</div></section>
{area_section()}"""
    return page("/construction-contact", "Contact RBF Construction | 810-938-8498",
                "Contact RBF Construction for a bid anywhere in Genesee, Oakland & Southeast Michigan. Call 810-938-8498 or email info@rbfconstruction.com.",
                body, trail, page_type="ContactPage")


def careers():
    trail = [("Home", "/"), ("Careers", "/careers")]
    f = form("New job application — rbfconstruction.com", [
        field("Full name", "name", auto="name"),
        field("Phone number", "phone", "tel", auto="tel"),
        field("Email", "email", "email", auto="email"),
        field("Position of interest", "position", ["Laborer", "Equipment operator", "Pipe layer", "Concrete / flatwork",
                                                    "CDL driver", "Foreman / supervisor", "Project manager / estimator", "Other"], req=False),
        field("Previous experience", "experience", "textarea", full=True),
        field("Additional information", "additional", "textarea", req=False, full=True),
    ], "Submit Your Application")
    body = f"""{page_hero("Construction Jobs in Flint, MI", "Join the RBF Construction team. Reach out to us about career opportunities in construction, site development and underground utilities.", trail, "storm-sewer-pipe-installation-crew")}
<section><div class="wrap form-wrap">
  <div><span class="eyebrow">Join Our Team</span><h2>Apply to Work at RBF</h2>
  <p>We&rsquo;re always interested in hearing from hard-working people in the trades. Tell us about yourself and the kind of work you do.</p>{f}</div>
  <div>{img('manhole-water-valve-installation', sizes='(max-width:860px) 100vw, 460px')}
  <h3 style="margin-top:20px">Why work with RBF?</h3>
  <ul class="checks">
    <li>{icon('check')}<span>Variety of work: commercial buildings, site development and underground utilities.</span></li>
    <li>{icon('check')}<span>Local projects in Flint and Genesee County.</span></li>
    <li>{icon('check')}<span>A team that takes pride in building it right the first time.</span></li>
  </ul></div>
</div></section>"""
    return page("/careers", "Careers at RBF Construction | Construction Jobs in Flint, MI",
                "Construction jobs in Flint, MI. Apply to join RBF Construction's team in general contracting, site development and underground utilities.",
                body, trail)


def bidding():
    trail = [("Home", "/"), ("Subcontractors", "/bidding-list")]
    f = form("New subcontractor bid list submission — rbfconstruction.com", [
        field("Company name", "company", auto="organization"),
        field("Contact person / title", "contact"),
        field("Phone number", "phone", "tel", auto="tel"),
        field("Email address", "email", "email", auto="email"),
        field("Trade(s) / services offered", "services", "textarea", full=True),
        field("Geographic service area", "service_area", full=True),
    ], "Join the Bid List")
    body = f"""{page_hero("Subcontractor Bidding List", "Join our network of trusted subcontractors and suppliers. Submit your details to be considered for upcoming bidding opportunities.", trail, "underground-utility-trench-excavation")}
<section><div class="wrap form-wrap">
  <div><span class="eyebrow">Subcontractor Information</span><h2>Get on Our Bid List</h2>
  <p>RBF Construction relies on a trusted network of skilled tradesmen and subcontractors. Tell us about your company and we&rsquo;ll reach out when projects in your trade and area come up for bid.</p>{f}</div>
  <div>{img('steel-frame-commercial-building', sizes='(max-width:860px) 100vw, 460px')}</div>
</div></section>"""
    return page("/bidding-list", "Subcontractor Bidding List | RBF Construction, Flint MI",
                "Subcontractors and suppliers: join RBF Construction's bid list for upcoming commercial, residential and site development projects near Flint, MI.",
                body, trail)


def simple(path, crumb, title, desc, h1, lead, html, bg, noindex=False):
    trail = [("Home", "/"), (crumb, path)]
    out = page(path, title, desc, f'{page_hero(h1, lead, trail, bg)}<section><div class="wrap prose">{html}</div></section>', trail)
    if noindex:
        out = out.replace('content="index, follow, max-image-preview:large, max-snippet:-1"', 'content="noindex, follow"')
    return out


def privacy():
    html = f"""<p><em>Last updated: {date.today().strftime('%B %d, %Y')}</em></p>
<h2>Information we collect</h2><p>When you submit a form on this website (bid request, job application or subcontractor bid list), we collect the information you provide, such as your name, company, phone number, email address and message.</p>
<h2>How we use it</h2><p>We use this information only to respond to your inquiry, evaluate applications and contact subcontractors about bidding opportunities. We do not sell your information.</p>
<h2>Form processing</h2><p>Form submissions are delivered to our email through a third-party form service, which processes the data on our behalf.</p>
<h2>Contact</h2><p>Questions? Email <a href="mailto:{BIZ['email']}">{BIZ['email']}</a> or call <a href="tel:{BIZ['phone_e164']}">{BIZ['phone']}</a>.</p>"""
    return simple("/privacy-policy", "Privacy Policy", "Privacy Policy | RBF Construction",
                  "How RBF Construction collects and uses information submitted through rbfconstruction.com.",
                  "Privacy Policy", "How we handle the information you share with us.", html, "pump-room-piping-installation")


def thanks():
    html = f"""<h2>Thank you &mdash; we received your message.</h2><p>A member of the RBF Construction team will be in touch soon. If your project is time-sensitive, call us at <a href="tel:{BIZ['phone_e164']}">{BIZ['phone']}</a> ({BIZ['hours_text']}).</p>
<p><a class="btn btn-navy" href="/">Back to Home</a> <a class="btn btn-amber" href="/projects">See Our Projects</a></p>"""
    return simple("/thank-you", "Thank You", "Thank You | RBF Construction", "Thanks for contacting RBF Construction.",
                  "Thanks for Reaching Out", "We&rsquo;ll be in touch shortly.", html, "commercial-renovation-after", noindex=True)


def not_found():
    html = f"""<h2>Sorry, we couldn&rsquo;t find that page.</h2><p>It may have moved when we updated our site. Try one of these:</p>
<ul><li><a href="/">Home</a></li>{''.join(f'<li><a href="{u}">{t}</a></li>' for u, t in SERVICES)}<li><a href="/projects">Projects</a></li><li><a href="/construction-contact">Contact</a></li></ul>"""
    return simple("/404", "Page Not Found", "Page Not Found | RBF Construction", "The page you requested could not be found.",
                  "Page Not Found", "Let&rsquo;s get you back on solid ground.", html, "commercial-site-excavation-grading", noindex=True)


# --------------------------------------------------------------------------
# Crawl & AI files
# --------------------------------------------------------------------------
def indexed():
    return (["/", "/general-contracting", "/residential-general-contracting", "/commercial-general-contracting",
             "/site-development"] + ["/" + s["slug"] for s in SVC] + ["/service-areas"] +
            ["/" + c["slug"] for c in COUNTIES] + ["/projects", "/resources/"] +
            ["/resources/" + a["slug"] for a in ARTICLES] +
            ["/construction-contact", "/careers", "/bidding-list", "/privacy-policy"])


def sitemap():
    pri = {"/": "1.0", "/construction-contact": "0.9", "/oakland-county-general-contractor": "0.9", "/privacy-policy": "0.2"}
    urls = []
    for u in indexed():
        imgs = ""
        if u == "/projects":
            imgs = "".join(f"<image:image><image:loc>{SITE}/img/{s}.webp</image:loc></image:image>" for s in PHOTOS)
        urls.append(f"<url><loc>{SITE}{u}</loc><lastmod>{TODAY}</lastmod><priority>{pri.get(u, '0.8')}</priority>{imgs}</url>")
    return ('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
            'xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">\n' + "\n".join(urls) + "\n</urlset>\n")


def robots():
    ai = ["GPTBot", "OAI-SearchBot", "ChatGPT-User", "ClaudeBot", "Claude-SearchBot", "Claude-User", "PerplexityBot",
          "Perplexity-User", "Google-Extended", "Applebot-Extended", "Bingbot", "DuckAssistBot", "Meta-ExternalAgent", "CCBot"]
    lines = ["# RBF Construction — search engines and AI assistants are welcome", "User-agent: *", "Allow: /",
             "Disallow: /thank-you", ""]
    for b in ai:
        lines += [f"User-agent: {b}", "Allow: /", "Disallow: /thank-you", ""]
    lines.append(f"Sitemap: {SITE}/sitemap.xml")
    return "\n".join(lines) + "\n"


def llms_txt():
    def sec(items):
        return "\n".join(f"- [{strip_tags(t)}]({SITE}{u}): {strip_tags(d)}" for u, t, d in items)
    hubs = sec([("/general-contracting", "General Contracting", "construction management, design-build, design-bid-build, consulting"),
                ("/residential-general-contracting", "Residential", "custom homes and additions, kitchen and bath remodeling, pole barns"),
                ("/commercial-general-contracting", "Commercial", "offices, restaurants, medical, retail, tenant build-outs"),
                ("/site-development", "Site Work", "excavation, grading, utilities, paving, concrete, demolition")])
    svcs = sec([("/" + s["slug"], s["nav"], s["desc"]) for s in SVC])
    areas = "\n".join(f"- [{c['name']}]({SITE}/{c['slug']}): {', '.join(c['cities'])}" for c in COUNTIES)
    arts = sec([("/resources/" + a["slug"], a["h1"], a["summary"]) for a in ARTICLES])
    faq = "\n".join(f"### {strip_tags(q)}\n{strip_tags(a)}\n" for q, a in HOME_FAQ)
    return f"""# {BIZ['name']}

> {BIZ['name']} ("{BIZ['slogan']}") is a general contractor headquartered in Flint, Michigan that serves Genesee County, Oakland County and all of Southeast Michigan. It builds custom homes and additions, does kitchen and bathroom remodeling, builds pole barns, commercial construction (office buildings, restaurants, medical and dental offices, retail), construction management and design-build, and complete site work: excavation, grading, underground utilities, parking lots, concrete and demolition.

## Key facts
- Legal name: {BIZ['name']}
- Also known as: RBF Construction, RBF
- Tagline: "{BIZ['slogan']}"
- Business type: General contractor (residential and commercial); site development contractor
- Headquarters: {BIZ['street']}, {BIZ['city']}, {BIZ['region']} {BIZ['zip']}, USA
- Phone: {BIZ['phone']}
- Email: {BIZ['email']}
- Hours: {BIZ['hours_text']}
- Service area: Genesee County, Oakland County and all of Southeast Michigan, including {", ".join(c['name'] for c in COUNTIES)} counties
- Brands built for: {", ".join(n for _, n in CLIENTS)}
- Facebook: {BIZ['facebook']}

## Service categories
{hubs}

## Services
{svcs}

## Service areas
{areas}

## Guides
{arts}

## Other pages
- [Projects and photo gallery]({SITE}/projects)
- [Contact / request a bid]({SITE}/construction-contact)
- [Careers]({SITE}/careers)
- [Subcontractor bidding list]({SITE}/bidding-list)

## FAQ
{faq}"""


def manifest():
    return json.dumps({"name": BIZ["name"], "short_name": "RBF", "start_url": "/", "display": "browser",
                       "background_color": "#ffffff", "theme_color": "#0b1726",
                       "icons": [{"src": "/img/icon-192.png", "sizes": "192x192", "type": "image/png"},
                                 {"src": "/img/icon-512.png", "sizes": "512x512", "type": "image/png"}]}, indent=2)


HTACCESS = """# Apache (Hostinger, cPanel, etc.)
Options -MultiViews
RewriteEngine On

# Force HTTPS + non-www
RewriteCond %{HTTPS} off [OR]
RewriteCond %{HTTP_HOST} ^www\\. [NC]
RewriteRule ^ https://rbfconstruction.com%{REQUEST_URI} [L,R=301]

# Strip .html from URLs
RewriteCond %{THE_REQUEST} \\s/+(.+?)\\.html[\\s?] [NC]
RewriteRule ^ /%1 [R=301,L]
RewriteCond %{REQUEST_FILENAME} !-d
RewriteCond %{REQUEST_FILENAME}.html -f
RewriteRule ^(.+?)/?$ $1.html [L]

ErrorDocument 404 /404.html

<IfModule mod_expires.c>
  ExpiresActive On
  ExpiresByType image/webp "access plus 1 year"
  ExpiresByType image/png "access plus 1 year"
  ExpiresByType image/jpeg "access plus 1 year"
  ExpiresByType text/css "access plus 1 month"
  ExpiresByType application/javascript "access plus 1 month"
  ExpiresByType text/html "access plus 0 seconds"
</IfModule>
<IfModule mod_deflate.c>
  AddOutputFilterByType DEFLATE text/html text/css application/javascript application/json image/svg+xml text/plain application/xml
</IfModule>
<IfModule mod_headers.c>
  Header always set X-Content-Type-Options "nosniff"
  Header always set Referrer-Policy "strict-origin-when-cross-origin"
  Header always set X-Frame-Options "SAMEORIGIN"
</IfModule>
"""

VERCEL = json.dumps({
    "cleanUrls": True, "trailingSlash": False,
    "redirects": [{"source": "/:path*", "has": [{"type": "host", "value": "www.rbfconstruction.com"}],
                   "destination": "https://rbfconstruction.com/:path*", "permanent": True}],
    "headers": [{"source": "/img/(.*)", "headers": [{"key": "Cache-Control", "value": "public, max-age=31536000, immutable"}]}],
}, indent=2)

NETLIFY = """# Netlify: pretty URLs are on by default; force non-www
https://www.rbfconstruction.com/* https://rbfconstruction.com/:splat 301!
"""


# --------------------------------------------------------------------------
def build():
    pages = {
        "index.html": home(),
        "general-contracting.html": general_contracting(),
        "commercial-general-contracting.html": commercial(),
        "residential-general-contracting.html": residential(),
        "site-development.html": site_development(),
        "service-areas.html": service_areas(),
        "projects.html": projects(),
        "resources/index.html": resources(),
        "construction-contact.html": contact(),
        "careers.html": careers(),
        "bidding-list.html": bidding(),
        "privacy-policy.html": privacy(),
        "thank-you.html": thanks(),
        "404.html": not_found(),
        "sitemap.xml": sitemap(),
        "robots.txt": robots(),
        "llms.txt": llms_txt(),
        "site.webmanifest": manifest(),
        ".htaccess": HTACCESS,
        "vercel.json": VERCEL,
        "_redirects": NETLIFY,
    }
    for s in SVC:
        pages[s["slug"] + ".html"] = detail_service(s)
    for c in COUNTIES:
        pages[c["slug"] + ".html"] = county_page(c)
    os.makedirs(os.path.join(OUT, "resources"), exist_ok=True)
    for a in ARTICLES:
        pages["resources/" + a["slug"] + ".html"] = article_page(a)
    for name, content in pages.items():
        with open(os.path.join(OUT, name), "w", encoding="utf-8", newline="\n") as fh:
            fh.write(content)
    print(f"Built {len(pages)} files into {OUT}")


def serve(port=8000):
    import http.server
    import functools

    class H(http.server.SimpleHTTPRequestHandler):
        def send_head(self):
            p = self.path.split("?")[0]
            if os.path.isdir(os.path.join(OUT, p.strip("/"))):
                return super().send_head()  # folder: redirect to "/" and serve its index.html, like Apache
            if p != "/" and "." not in p.rsplit("/", 1)[-1]:
                cand = os.path.join(OUT, p.strip("/") + ".html")
                self.path = p + ".html" if os.path.exists(cand) else "/404.html"
            return super().send_head()

    print(f"Preview: http://localhost:{port}")
    http.server.ThreadingHTTPServer(("", port), functools.partial(H, directory=OUT)).serve_forever()


if __name__ == "__main__":
    build()
    if "--serve" in sys.argv:
        serve()

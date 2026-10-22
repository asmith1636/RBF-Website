"""Page content for rbfconstruction.com — services, service areas and resource articles.

Each service: slug, group, nav (menu label), name (schema), title (<=60 chars), desc (<=155 chars),
h1, lead, bg (hero photo stem or None), photos (photo row), body (HTML; <!--PHOTOS--> marks the photo row),
faqs [(q, a)], types (schema serviceType list).
"""

PHONE = "810-938-8498"
TEL = "+18109388498"

# --------------------------------------------------------------------------
# Service areas (counties -> real communities). CONFIRM WITH OWNER.
# --------------------------------------------------------------------------
COUNTIES = [
    {
        "slug": "oakland-county-general-contractor", "name": "Oakland County",
        "cities": ["Troy", "Southfield", "Auburn Hills", "Rochester Hills", "Rochester", "Pontiac", "Bloomfield Hills",
                   "Birmingham", "West Bloomfield", "Farmington Hills", "Novi", "Wixom", "Commerce Township", "Milford",
                   "Highland", "White Lake", "Waterford", "Clarkston", "Independence Township", "Lake Orion",
                   "Orion Township", "Oxford", "Ortonville", "Holly", "Royal Oak", "Ferndale", "Madison Heights"],
        "title": "General Contractor in Oakland County, MI | RBF Construction",
        "desc": "Oakland County general contractor for kitchen & bath remodels, custom homes, office, restaurant, medical and retail construction, plus site work.",
        "h1": "General Contractor Serving All of Oakland County",
        "lead": "Kitchen and bath remodels, new homes, commercial buildings and full site work &mdash; from Holly and Clarkston to Troy, Novi and Royal Oak.",
        "bg": "retail-plaza-jimmy-johns-pizza-hut-smoothie-king",
        "intro": """<p>RBF Construction works throughout <strong>all of Oakland County</strong>, from the northern townships along I-75 &mdash; Holly, Groveland, Springfield, Independence and Orion &mdash; down through the business corridors of Auburn Hills, Troy and Southfield and into the established neighborhoods of Birmingham, Bloomfield, Royal Oak and Ferndale. Our Flint headquarters sits just up I-75, so Oakland County job sites are a short drive for our crews and equipment.</p>
<p>Oakland County has some of Michigan&rsquo;s most active construction demand: office and professional buildings along the I-75 and M-59 corridors, medical offices and clinics serving a large and growing population, restaurants and retail along Telegraph, Woodward, Novi Road and Rochester Road, and homeowners investing in kitchens, baths and new custom homes on lake lots and acreage in the northern and western townships.</p>""",
        "focus": """<h2>What We Build in Oakland County</h2>
<ul class="tick-list"><li><a href="/kitchen-remodeling">Kitchen remodeling</a></li><li><a href="/bathroom-remodeling">Bathroom remodeling</a></li>
<li><a href="/custom-home-builder">Custom homes &amp; additions</a></li><li><a href="/office-building-construction">Office buildings &amp; build-outs</a></li>
<li><a href="/restaurant-construction">Restaurants &amp; drive-thrus</a></li><li><a href="/medical-office-construction">Medical &amp; dental offices</a></li>
<li><a href="/retail-construction">Retail &amp; multi-tenant</a></li><li><a href="/site-development">Site development &amp; utilities</a></li></ul>
<h2>Residential Remodeling and New Homes</h2>
<p>For Oakland County homeowners we handle kitchen and bathroom remodels, additions and ground-up custom homes. Because we have our own excavation and site work division, we&rsquo;re a strong fit for new homes on rural and lake lots in places like Clarkston, Holly, Highland, Milford, Oxford and White Lake, where clearing, grading, driveways and utility connections are a big part of the job.</p>
<h2>Commercial Construction</h2>
<p>For businesses and developers we build and renovate offices, restaurants, medical facilities and retail space &mdash; from a tenant build-out in a Southfield or Troy office building to a ground-up quick-service restaurant with a drive-thru. We work with your architect on design-bid-build projects or deliver the whole project through design-build.</p>""",
        "faqs": [
            ("Does RBF Construction work in Oakland County?",
             "Yes. RBF Construction serves all of Oakland County, including Troy, Southfield, Auburn Hills, Rochester Hills, Novi, Farmington Hills, Birmingham, Bloomfield Hills, West Bloomfield, Waterford, Clarkston, Lake Orion, Oxford, Holly, Milford and Royal Oak."),
            ("What kinds of projects do you take on in Oakland County?",
             "Kitchen and bathroom remodels, custom homes and additions, office buildings and tenant build-outs, restaurants, medical and dental offices, retail buildings, and site work including excavation, grading, utilities, parking lots and demolition."),
            ("Is your office close to Oakland County?",
             "Our headquarters is at 1411 W Hill Rd in Flint, just off I-75, a short drive north of Oakland County. We meet clients on site anywhere in the county."),
        ],
    },
    {
        "slug": "genesee-county-general-contractor", "name": "Genesee County",
        "cities": ["Flint", "Flint Township", "Burton", "Grand Blanc", "Grand Blanc Township", "Fenton", "Fenton Township",
                   "Flushing", "Davison", "Swartz Creek", "Clio", "Mt. Morris", "Linden", "Montrose", "Goodrich",
                   "Gaines", "Genesee Township", "Mundy Township"],
        "title": "Genesee County General Contractor | Flint, MI | RBF",
        "desc": "Flint-based general contractor serving all of Genesee County: remodeling, custom homes, commercial construction and site development.",
        "h1": "Genesee County&rsquo;s Hometown General Contractor",
        "lead": "Headquartered on W Hill Rd in Flint, RBF builds, remodels and develops sites across every corner of Genesee County.",
        "bg": "commercial-renovation-after",
        "intro": """<p>Genesee County is home base for RBF Construction. Our office and crews are based at 1411 W Hill Rd in Flint, which means fast response times and personal on-site supervision on projects in Flint, Burton, Grand Blanc, Fenton, Flushing, Davison, Swartz Creek, Clio and the surrounding townships.</p>
<p>We&rsquo;ve built commercial buildings, renovated storefronts, installed underground utilities and upgraded pump stations in the region, and we bring the same team to homeowners planning a remodel or a new home.</p>""",
        "focus": """<h2>Services Across Genesee County</h2>
<ul class="tick-list"><li><a href="/kitchen-remodeling">Kitchen remodeling</a></li><li><a href="/bathroom-remodeling">Bathroom remodeling</a></li>
<li><a href="/custom-home-builder">New homes &amp; additions</a></li><li><a href="/commercial-general-contracting">Commercial construction</a></li>
<li><a href="/restaurant-construction">Restaurant construction</a></li><li><a href="/medical-office-construction">Medical offices</a></li>
<li><a href="/underground-utilities">Underground utilities</a></li><li><a href="/parking-lot-paving-concrete">Parking lots &amp; concrete</a></li></ul>
<h2>Commercial Renovation and Redevelopment</h2>
<p>Many Genesee County properties have good bones and dated buildings. We specialize in turning tired commercial properties into modern, leasable space &mdash; new facades, interiors, parking lots and utilities &mdash; as you can see in our <a href="/projects">before-and-after renovation</a>.</p>""",
        "faqs": [
            ("Where is RBF Construction located in Genesee County?",
             "Our office is at 1411 W Hill Rd, Flint, MI 48507, open Monday through Friday, 8 AM to 5 PM."),
            ("Which Genesee County communities do you serve?",
             "All of them, including Flint, Burton, Grand Blanc, Fenton, Flushing, Davison, Swartz Creek, Clio, Mt. Morris, Linden, Montrose and Goodrich."),
        ],
    },
    {
        "slug": "livingston-county-general-contractor", "name": "Livingston County",
        "cities": ["Brighton", "Howell", "Hartland", "Fowlerville", "Pinckney", "Genoa Township", "Green Oak Township",
                   "Hamburg Township", "Oceola Township", "Tyrone Township"],
        "title": "Livingston County General Contractor | RBF Construction",
        "desc": "General contractor for Brighton, Howell, Hartland and all of Livingston County: remodels, custom homes, commercial buildings and site work.",
        "h1": "General Contractor for Livingston County",
        "lead": "Custom homes, remodels, commercial buildings and site development in Brighton, Howell, Hartland and beyond.",
        "bg": "foundation-walls-excavation",
        "intro": """<p>Livingston County is one of Southeast Michigan&rsquo;s fastest-growing areas, with new homes going up on acreage and lake lots and new businesses following along the US-23 and I-96 corridors. RBF Construction serves Brighton, Howell, Hartland, Fowlerville, Pinckney and the surrounding townships, reachable from our Flint headquarters via US-23.</p>""",
        "focus": """<h2>Popular Projects in Livingston County</h2>
<ul class="tick-list"><li><a href="/custom-home-builder">Custom homes on acreage &amp; lake lots</a></li><li><a href="/excavation-grading">Excavation, clearing &amp; grading</a></li>
<li><a href="/kitchen-remodeling">Kitchen remodels</a></li><li><a href="/bathroom-remodeling">Bathroom remodels</a></li>
<li><a href="/retail-construction">Retail &amp; commercial buildings</a></li><li><a href="/office-building-construction">Professional offices</a></li></ul>
<h2>Site Work for Rural and Semi-Rural Lots</h2>
<p>New construction in Livingston County often starts with raw land. Our in-house earthwork crews handle clearing, excavation, grading, drainage, driveways and utility trenching, so your home or commercial building starts on properly prepared ground.</p>""",
        "faqs": [
            ("Do you build custom homes in Livingston County?",
             "Yes. We build ground-up homes and additions in Brighton, Howell, Hartland, Fowlerville, Pinckney and surrounding townships, including the site work."),
        ],
    },
    {
        "slug": "macomb-county-general-contractor", "name": "Macomb County",
        "cities": ["Sterling Heights", "Warren", "Shelby Township", "Macomb Township", "Clinton Township", "Utica",
                   "Washington Township", "Romeo", "Chesterfield Township", "New Baltimore", "Roseville", "St. Clair Shores"],
        "title": "Macomb County General Contractor | RBF Construction",
        "desc": "General contractor for Sterling Heights, Shelby Township, Macomb Township and all of Macomb County: remodels, commercial construction, site work.",
        "h1": "General Contractor for Macomb County",
        "lead": "Commercial construction, remodeling and site development from Sterling Heights and Warren to Shelby, Macomb and Washington Townships.",
        "bg": "steel-frame-commercial-building",
        "intro": """<p>RBF Construction serves Macomb County businesses and homeowners with commercial construction, residential remodeling and complete site development. From restaurant and retail sites along Hall Road (M-59) and Van Dyke to new homes in the growing northern townships, we bring one accountable team to every phase.</p>""",
        "focus": """<h2>Macomb County Services</h2>
<ul class="tick-list"><li><a href="/restaurant-construction">Restaurant construction</a></li><li><a href="/retail-construction">Retail construction</a></li>
<li><a href="/office-building-construction">Office construction &amp; build-outs</a></li><li><a href="/medical-office-construction">Medical facilities</a></li>
<li><a href="/kitchen-remodeling">Kitchen remodeling</a></li><li><a href="/bathroom-remodeling">Bathroom remodeling</a></li>
<li><a href="/parking-lot-paving-concrete">Parking lots &amp; concrete</a></li><li><a href="/demolition">Demolition</a></li></ul>""",
        "faqs": [
            ("Does RBF Construction work in Macomb County?",
             "Yes. We serve Sterling Heights, Warren, Shelby Township, Macomb Township, Clinton Township, Utica, Washington Township, Romeo, Chesterfield and the rest of Macomb County."),
        ],
    },
    {
        "slug": "wayne-county-general-contractor", "name": "Wayne County",
        "cities": ["Detroit", "Livonia", "Dearborn", "Dearborn Heights", "Canton", "Plymouth", "Northville", "Westland",
                   "Redford", "Taylor", "Grosse Pointe", "Romulus"],
        "title": "Wayne County & Detroit General Contractor | RBF",
        "desc": "General contractor serving Detroit, Livonia, Dearborn, Canton, Plymouth and Wayne County: commercial construction, remodels and site work.",
        "h1": "General Contractor for Detroit &amp; Wayne County",
        "lead": "Commercial buildings, renovations, remodels and site work in Detroit, Livonia, Dearborn, Canton, Plymouth and Northville.",
        "bg": "commercial-renovation-after",
        "intro": """<p>RBF Construction takes on commercial, residential and site development projects across Wayne County, including Detroit, Livonia, Dearborn, Canton, Plymouth, Northville and Westland. Much of Wayne County&rsquo;s building stock is ready for reinvestment, and renovation and redevelopment &mdash; new facades, interiors, parking and utilities &mdash; is one of our strengths.</p>""",
        "focus": """<h2>Wayne County Services</h2>
<ul class="tick-list"><li><a href="/retail-construction">Commercial renovation</a></li><li><a href="/restaurant-construction">Restaurant build-outs</a></li>
<li><a href="/office-building-construction">Office construction</a></li><li><a href="/medical-office-construction">Medical offices</a></li>
<li><a href="/demolition">Demolition</a></li><li><a href="/underground-utilities">Underground utilities</a></li>
<li><a href="/kitchen-remodeling">Kitchen remodels</a></li><li><a href="/bathroom-remodeling">Bathroom remodels</a></li></ul>""",
        "faqs": [
            ("Do you take projects in Detroit?",
             "Yes. RBF Construction serves Detroit and communities throughout Wayne County for commercial construction, renovation, remodeling and site work."),
        ],
    },
    {
        "slug": "lapeer-county-general-contractor", "name": "Lapeer County",
        "cities": ["Lapeer", "Imlay City", "Almont", "Metamora", "Dryden", "Columbiaville", "North Branch", "Attica",
                   "Hadley", "Elba Township"],
        "title": "Lapeer County General Contractor | RBF Construction",
        "desc": "General contractor for Lapeer, Imlay City, Almont, Metamora and all of Lapeer County: new homes, remodels, commercial buildings and site work.",
        "h1": "General Contractor for Lapeer County",
        "lead": "New homes, remodels, agricultural-area site work and commercial buildings in Lapeer, Imlay City, Almont and Metamora.",
        "bg": "commercial-site-excavation-grading",
        "intro": """<p>Just east of our Flint headquarters, Lapeer County combines small-town business districts with wide-open rural land. RBF Construction builds new homes and additions, remodels kitchens and baths, constructs commercial buildings and handles the excavation, grading, driveways and utilities that rural sites require.</p>""",
        "focus": """<h2>Lapeer County Services</h2>
<ul class="tick-list"><li><a href="/custom-home-builder">Custom homes</a></li><li><a href="/excavation-grading">Excavation &amp; grading</a></li>
<li><a href="/kitchen-remodeling">Kitchen remodeling</a></li><li><a href="/bathroom-remodeling">Bathroom remodeling</a></li>
<li><a href="/commercial-general-contracting">Commercial construction</a></li><li><a href="/parking-lot-paving-concrete">Driveways, lots &amp; concrete</a></li></ul>""",
        "faqs": [
            ("Do you serve Lapeer County?",
             "Yes. We work in Lapeer, Imlay City, Almont, Metamora, Dryden, Columbiaville, North Branch and the surrounding townships."),
        ],
    },
    {
        "slug": "washtenaw-county-general-contractor", "name": "Washtenaw County",
        "cities": ["Ann Arbor", "Ypsilanti", "Saline", "Dexter", "Chelsea", "Pittsfield Township", "Scio Township",
                   "Superior Township", "Ypsilanti Township", "Milan"],
        "title": "Washtenaw County General Contractor | RBF Construction",
        "desc": "General contractor for Ann Arbor, Ypsilanti, Saline, Dexter and Washtenaw County: medical and office construction, remodels and site work.",
        "h1": "General Contractor for Ann Arbor &amp; Washtenaw County",
        "lead": "Medical and professional offices, restaurants, remodels and site development in Ann Arbor, Ypsilanti, Saline and Dexter.",
        "bg": "steel-frame-commercial-building",
        "intro": """<p>With a major university and health system at its center, Washtenaw County has steady demand for medical offices, professional space, restaurants and high-quality residential remodeling. RBF Construction serves Ann Arbor, Ypsilanti, Saline, Dexter, Chelsea and the surrounding townships.</p>""",
        "focus": """<h2>Washtenaw County Services</h2>
<ul class="tick-list"><li><a href="/medical-office-construction">Medical &amp; dental offices</a></li><li><a href="/office-building-construction">Professional offices</a></li>
<li><a href="/restaurant-construction">Restaurants</a></li><li><a href="/retail-construction">Retail</a></li>
<li><a href="/kitchen-remodeling">Kitchen remodels</a></li><li><a href="/bathroom-remodeling">Bathroom remodels</a></li></ul>""",
        "faqs": [
            ("Do you work in Ann Arbor?",
             "Yes. RBF Construction serves Ann Arbor and all of Washtenaw County, including Ypsilanti, Saline, Dexter and Chelsea."),
        ],
    },
]
OTHER_AREAS = ["St. Clair County", "Shiawassee County", "Monroe County", "Saginaw County", "Tuscola County"]

# --------------------------------------------------------------------------
# Services
# --------------------------------------------------------------------------
GROUPS = {
    "residential": ("Residential", "/residential-general-contracting"),
    "commercial": ("Commercial", "/commercial-general-contracting"),
    "site": ("Site Work", "/site-development"),
}

SERVICES = [
    # ---------------- Residential ----------------
    {
        "slug": "kitchen-remodeling", "group": "residential", "nav": "Kitchen Remodeling", "name": "Kitchen Remodeling",
        "title": "Kitchen Remodeling | Oakland County & SE Michigan | RBF",
        "desc": "Kitchen remodeling contractor for Oakland County and Southeast Michigan: layout changes, cabinets, countertops, tile, lighting and permits handled.",
        "h1": "Kitchen Remodeling in Oakland County &amp; Southeast Michigan",
        "lead": "From a cabinet-and-countertop refresh to a full gut with a new layout &mdash; one contractor managing design, trades, permits and schedule.",
        "bg": None, "photos": [],
        "body": """<h2>A Kitchen Remodel Managed Like a Construction Project</h2>
<p>Kitchens are the most complex room in a house: plumbing, electrical, ventilation, structure, cabinetry and finishes all have to come together in the right order. RBF Construction manages your kitchen remodel the same way we manage commercial projects &mdash; with a clear scope, a realistic schedule, licensed trades and personal on-site supervision.</p>
<h2>What&rsquo;s Included</h2>
<ul class="tick-list"><li>Layout changes &amp; wall removal</li><li>Cabinets &amp; islands</li><li>Countertops &amp; backsplashes</li><li>Tile, flooring &amp; trim</li>
<li>Lighting &amp; electrical upgrades</li><li>Plumbing &amp; fixture relocation</li><li>Range hood ventilation</li><li>Permits &amp; inspections</li></ul>
<h2>Opening Up Your Kitchen</h2>
<p>Many Southeast Michigan homeowners want to open the kitchen to the living space. When a wall is load-bearing, we coordinate the engineering and install the beam and supports properly &mdash; then patch, finish and blend the floors and ceilings so it looks like it was always that way.</p>
<h2>Our Kitchen Remodeling Process</h2>
<ol><li><strong>Consultation:</strong> we visit your home, measure, and talk through how you use the kitchen and your budget.</li>
<li><strong>Design &amp; selections:</strong> layout, cabinets, counters, fixtures and finishes, with pricing tied to your choices.</li>
<li><strong>Permits &amp; ordering:</strong> we pull required permits and order long-lead items like cabinets before demolition starts, so your kitchen is out of service for as little time as possible.</li>
<li><strong>Construction:</strong> demolition, rough-ins, inspections, installation and finishes, with dust control and daily cleanup.</li>
<li><strong>Walkthrough:</strong> a final punch list so every detail is right.</li></ol>
<p>We remodel kitchens throughout <a href="/oakland-county-general-contractor">Oakland County</a>, <a href="/genesee-county-general-contractor">Genesee County</a> and the rest of <a href="/service-areas">Southeast Michigan</a>. Pair your kitchen with a <a href="/bathroom-remodeling">bathroom remodel</a> to save on mobilization, or <a href="/construction-contact#quote">request a kitchen remodeling estimate</a>.</p>""",
        "faqs": [
            ("How long does a kitchen remodel take?",
             "It depends on scope. A cosmetic update with new counters and fixtures is much quicker than a full remodel that moves walls, plumbing and electrical. We provide a project schedule with your estimate and order cabinets and other long-lead items before demolition to minimize the time your kitchen is out of service."),
            ("Do I need a permit to remodel my kitchen in Michigan?",
             "Most Michigan municipalities require permits when a remodel changes plumbing, electrical, mechanical or structural elements. RBF Construction handles permit applications and schedules the required inspections."),
            ("Can you remove a wall to open up my kitchen?",
             "Yes. If the wall is load-bearing, we coordinate the engineering and install a properly sized beam and supports, then finish the floors and ceilings to blend in."),
            ("Do you remodel kitchens in Oakland County?",
             "Yes. We remodel kitchens throughout Oakland County, including Troy, Rochester Hills, Clarkston, Waterford, Novi, Birmingham, Bloomfield Hills and Holly, as well as across Genesee County and Southeast Michigan."),
        ],
        "types": ["Kitchen remodeling", "Kitchen renovation", "Home remodeling"],
    },
    {
        "slug": "bathroom-remodeling", "group": "residential", "nav": "Bathroom Remodeling", "name": "Bathroom Remodeling",
        "title": "Bathroom Remodeling | Oakland County & SE Michigan | RBF",
        "desc": "Bathroom remodeling in Oakland County and Southeast Michigan: walk-in showers, tub conversions, tile, vanities and accessible, aging-in-place baths.",
        "h1": "Bathroom Remodeling in Oakland County &amp; Southeast Michigan",
        "lead": "Walk-in showers, tub-to-shower conversions, accessible baths and complete primary suite remodels &mdash; waterproofed and built to last.",
        "bg": None, "photos": [],
        "body": """<h2>Bathrooms Built Right Behind the Walls</h2>
<p>A beautiful bathroom only lasts if what&rsquo;s behind the tile is done right. RBF Construction focuses on the parts you don&rsquo;t see &mdash; proper waterproofing, sloped shower pans, correctly vented exhaust fans, solid subfloors and code-compliant plumbing and electrical &mdash; along with the finishes you do.</p>
<h2>Bathroom Remodeling Services</h2>
<ul class="tick-list"><li>Primary bathroom remodels</li><li>Walk-in &amp; curbless showers</li><li>Tub-to-shower conversions</li><li>Tile floors &amp; walls</li>
<li>Vanities, tops &amp; fixtures</li><li>Accessible &amp; aging-in-place baths</li><li>Exhaust ventilation</li><li>Hall &amp; guest baths</li></ul>
<h2>Accessible and Aging-in-Place Bathrooms</h2>
<p>Planning to stay in your home for the long run? We build bathrooms with curbless or low-threshold showers, blocking for grab bars, comfort-height fixtures, wider doorways and slip-resistant flooring &mdash; designed to look good, not institutional.</p>
<h2>How a Bathroom Remodel Works With RBF</h2>
<ol><li><strong>Walkthrough &amp; scope:</strong> we look at the space, existing plumbing and ventilation, and your goals.</li>
<li><strong>Selections &amp; estimate:</strong> tile, fixtures, vanity and layout, priced clearly.</li>
<li><strong>Construction:</strong> demolition, rough-ins, inspections, waterproofing, tile and finish work.</li>
<li><strong>Final walkthrough:</strong> we test every fixture and fan and finish the punch list.</li></ol>
<p>We remodel bathrooms across <a href="/oakland-county-general-contractor">Oakland County</a>, <a href="/genesee-county-general-contractor">Genesee County</a> and <a href="/service-areas">Southeast Michigan</a>. Planning a <a href="/kitchen-remodeling">kitchen remodel</a> too? <a href="/construction-contact#quote">Request an estimate</a> for both.</p>""",
        "faqs": [
            ("Can you convert my bathtub into a walk-in shower?",
             "Yes. Tub-to-shower conversions are one of our most common bathroom projects, including the plumbing changes, waterproofed shower pan, tile, glass and fixtures."),
            ("Do you build accessible or aging-in-place bathrooms?",
             "Yes. We build curbless and low-threshold showers, add blocking for grab bars, install comfort-height fixtures and slip-resistant flooring, and can widen doorways."),
            ("Do you remodel bathrooms in Oakland County?",
             "Yes. We remodel bathrooms throughout Oakland County and Southeast Michigan, as well as Genesee County where our office is located."),
        ],
        "types": ["Bathroom remodeling", "Bathroom renovation", "Shower installation", "Accessible bathroom remodeling"],
    },
    {
        "slug": "custom-home-builder", "group": "residential", "nav": "Custom Homes & Additions", "name": "Custom Home Building",
        "title": "Custom Home Builder | Oakland County & SE Michigan | RBF",
        "desc": "Ground-up custom homes and additions in Oakland County and Southeast Michigan, with in-house excavation, foundations, driveways and utilities.",
        "h1": "Custom Home Builder for Oakland County &amp; Southeast Michigan",
        "lead": "Ground-up residential construction and additions &mdash; with our own crews handling the land clearing, excavation, foundation and utilities.",
        "bg": "foundation-walls-excavation",
        "photos": ["foundation-walls-excavation", "commercial-site-excavation-grading", "concrete-road-curb-gutter-construction"],
        "body": """<h2>Ground-Up Homes, Built by a Site Work Contractor</h2>
<p>Most home builders subcontract everything below grade. RBF Construction does it ourselves. Our <a href="/site-development">site development division</a> handles clearing, excavation, grading, drainage, foundations, driveways and utility connections &mdash; the work that determines whether a house stays dry, level and problem-free for decades.</p>
<ul class="tick-list"><li>Custom single-family homes</li><li>Home additions</li><li>Garages &amp; accessory buildings</li><li>Lot clearing &amp; excavation</li>
<li>Foundations &amp; basements</li><li>Driveways &amp; flatwork</li><li>Water, sewer &amp; utility connections</li><li>Design-build or your plans</li></ul>
<!--PHOTOS-->
<h2>Building on Rural, Wooded and Lake Lots</h2>
<p>Much of northern and western Oakland County, Livingston County, Lapeer County and southern Genesee County is rural or wooded land with lakes, slopes and poor soils. These lots need careful site planning: tree removal, soil management, grading for drainage, long driveways and utility runs. That&rsquo;s exactly where an in-house earthwork crew pays off.</p>
<h2>From Plans to Keys</h2>
<ol><li><strong>Lot evaluation:</strong> we walk the property and identify site work, drainage and utility needs early.</li>
<li><strong>Design &amp; budget:</strong> build from your architect&rsquo;s plans or use our design-build approach.</li>
<li><strong>Permits &amp; site work:</strong> clearing, excavation, foundation and utilities.</li>
<li><strong>Construction:</strong> framing through finishes with personal on-site supervision.</li>
<li><strong>Final inspections &amp; walkthrough.</strong></li></ol>
<p>We build in <a href="/oakland-county-general-contractor">Oakland</a>, <a href="/livingston-county-general-contractor">Livingston</a>, <a href="/genesee-county-general-contractor">Genesee</a> and <a href="/lapeer-county-general-contractor">Lapeer</a> counties and across <a href="/service-areas">Southeast Michigan</a>. <a href="/construction-contact#quote">Tell us about your lot and plans</a>.</p>""",
        "faqs": [
            ("Do you build custom homes from the ground up?",
             "Yes. RBF Construction builds ground-up custom homes and additions, including the land clearing, excavation, foundation, utilities and driveway with our own site work crews."),
            ("Can you build from my architect's plans?",
             "Yes. We can build from your plans or deliver the project through design-build with our network of architects."),
            ("Do you build homes on rural or lake lots?",
             "Yes. Rural, wooded and lake lots are a strength because our in-house earthwork division handles clearing, grading, drainage, long driveways and utility runs."),
        ],
        "types": ["Custom home building", "New home construction", "Home additions", "Residential construction"],
    },
    # ---------------- Commercial ----------------
    {
        "slug": "office-building-construction", "group": "commercial", "nav": "Office Buildings", "name": "Office Building Construction",
        "title": "Office Building Construction | SE Michigan | RBF",
        "desc": "Office building construction, tenant build-outs and office renovations in Oakland County and Southeast Michigan. Design-build or design-bid-build.",
        "h1": "Office Building Construction &amp; Build-Outs",
        "lead": "New professional office buildings, tenant improvements and office renovations across Oakland County and Southeast Michigan.",
        "bg": "steel-frame-commercial-building",
        "photos": ["steel-frame-commercial-building", "concrete-road-curb-gutter-construction", "commercial-site-excavation-grading"],
        "body": """<h2>Office Space That Works for Your Business</h2>
<p>RBF Construction builds new office buildings and renovates existing ones for owners, developers and tenants. Whether it&rsquo;s a single-story professional office, a multi-tenant building or a build-out of leased space, we manage budget, schedule and quality from preconstruction to move-in.</p>
<ul class="tick-list"><li>Ground-up office buildings</li><li>Tenant improvements &amp; build-outs</li><li>Office renovations &amp; modernization</li><li>Multi-tenant professional buildings</li>
<li>Occupied-building phasing</li><li>Site work, parking &amp; utilities</li></ul>
<!--PHOTOS-->
<h2>Tenant Build-Outs on Schedule</h2>
<p>Lease start dates don&rsquo;t move. We plan tenant improvement projects around your lease, coordinate with building management, and sequence demolition, framing, mechanical, electrical, data and finishes so you can open on time.</p>
<h2>Renovating While You Stay Open</h2>
<p>Need to update an office you&rsquo;re working in? We phase work to keep your business operating &mdash; after-hours work where needed, dust and noise control, and clear communication about what&rsquo;s happening each day.</p>
<h2>Ground-Up With Site Work Included</h2>
<p>For new buildings, our <a href="/site-development">site development division</a> handles excavation, utilities, parking lots and concrete, so the building and the site are managed by one team.</p>
<p>Serving office corridors in <a href="/oakland-county-general-contractor">Troy, Southfield, Auburn Hills and Novi</a>, <a href="/genesee-county-general-contractor">Flint and Grand Blanc</a>, and across <a href="/service-areas">Southeast Michigan</a>. <a href="/construction-contact#quote">Request an office construction bid</a>.</p>""",
        "faqs": [
            ("Do you do tenant build-outs?",
             "Yes. RBF Construction builds out leased office, medical, retail and restaurant space, coordinating with building management and planning the work around your lease start date."),
            ("Can you renovate our office while we keep working?",
             "Yes. We phase renovation work, schedule disruptive tasks after hours when needed, and control dust and noise so your business can keep operating."),
        ],
        "types": ["Office construction", "Tenant improvement", "Office build-out", "Office renovation"],
    },
    {
        "slug": "restaurant-construction", "group": "commercial", "nav": "Restaurants", "name": "Restaurant Construction",
        "title": "Restaurant Construction Contractor | SE Michigan | RBF",
        "desc": "Restaurant and drive-thru construction in Michigan for national brands and local owners: ground-up builds, remodels, build-outs and site work.",
        "h1": "Restaurant Construction for National Brands &amp; Local Owners",
        "lead": "Ground-up quick-service restaurants with drive-thrus, sit-down restaurants, franchise remodels and tenant build-outs.",
        "bg": "retail-plaza-jimmy-johns-pizza-hut-smoothie-king",
        "photos": ["retail-plaza-jimmy-johns-pizza-hut-smoothie-king", "concrete-road-curb-gutter-construction", "commercial-site-excavation-grading"],
        "body": """<h2>Restaurant Experience You Can See</h2>
<p>RBF Construction has built for restaurant brands including <strong>Jimmy John&rsquo;s, Pizza Hut, Smoothie King, Taco Bell, Cottage Inn Pizza and Biggby Coffee</strong>. We understand franchise brand standards, tight opening dates and the kitchen infrastructure restaurants depend on.</p>
<ul class="tick-list"><li>Quick-service restaurants</li><li>Drive-thru lanes &amp; windows</li><li>Sit-down &amp; fast-casual</li><li>Coffee shops &amp; smoothie bars</li>
<li>Franchise remodels &amp; refreshes</li><li>End-cap &amp; in-line build-outs</li><li>Multi-tenant restaurant buildings</li><li>Parking, drive aisles &amp; utilities</li></ul>
<!--PHOTOS-->
<h2>Built Around the Kitchen</h2>
<p>Restaurants have infrastructure most buildings don&rsquo;t: hood and make-up air systems, grease interceptors, floor drains, heavy electrical and gas loads, walk-in coolers and health-code finishes. We coordinate these trades and inspections so your health department and fire inspections go smoothly.</p>
<h2>Drive-Thru Site Work, Done In-House</h2>
<p>Drive-thru stacking lanes, curbing, menu-board foundations, grease interceptor installation, storm water and parking all fall to our <a href="/site-development">site development division</a> &mdash; no handoff between a site contractor and a building contractor.</p>
<h2>Opening Day Matters</h2>
<p>We schedule backward from your opening date, order long-lead equipment early, and keep franchise representatives informed with progress updates.</p>
<p>We build restaurants throughout <a href="/oakland-county-general-contractor">Oakland County</a>, <a href="/macomb-county-general-contractor">Macomb County</a>, <a href="/genesee-county-general-contractor">Genesee County</a> and <a href="/service-areas">Southeast Michigan</a>. <a href="/construction-contact#quote">Request a restaurant construction bid</a>.</p>""",
        "faqs": [
            ("Have you built restaurants for national franchise brands?",
             "Yes. RBF Construction has built for brands including Jimmy John's, Pizza Hut, Smoothie King, Taco Bell, Cottage Inn Pizza and Biggby Coffee."),
            ("Do you build drive-thru restaurants?",
             "Yes. We build the restaurant and the drive-thru site work, including stacking lanes, curbing, menu-board foundations, grease interceptors, utilities and parking."),
            ("Can you remodel an existing restaurant to new brand standards?",
             "Yes. We handle franchise remodels and refreshes, scheduling the work to minimize the time your restaurant is closed."),
        ],
        "types": ["Restaurant construction", "Quick-service restaurant construction", "Drive-thru construction", "Franchise construction"],
    },
    {
        "slug": "medical-office-construction", "group": "commercial", "nav": "Medical & Dental", "name": "Medical Office Construction",
        "title": "Medical Office Construction | SE Michigan | RBF",
        "desc": "Medical office, dental, physical therapy and clinic construction in Oakland County and Southeast Michigan. New buildings and build-outs.",
        "h1": "Medical, Dental &amp; Clinic Construction",
        "lead": "New medical office buildings and build-outs for physicians, dentists, physical therapy, urgent care and specialty clinics.",
        "bg": None, "photos": [],
        "body": """<h2>Healthcare Spaces Built With Care</h2>
<p>Medical construction has requirements other commercial projects don&rsquo;t: accessibility, infection-control-friendly finishes, plumbing at nearly every exam room, privacy and sound control, and coordination with specialty equipment vendors. RBF Construction has built space for healthcare tenants including <strong>Athletico Physical Therapy</strong>, and we bring that experience to every medical project.</p>
<ul class="tick-list"><li>Medical office buildings</li><li>Physician &amp; specialty practices</li><li>Dental offices</li><li>Physical therapy clinics</li>
<li>Urgent care &amp; walk-in clinics</li><li>Medical tenant build-outs</li><li>Veterinary clinics</li><li>Renovations &amp; expansions</li></ul>
<!--PHOTOS-->
<h2>What Sets Medical Projects Apart</h2>
<ul><li><strong>Accessibility:</strong> barrier-free entrances, restrooms, door hardware and clearances.</li>
<li><strong>Plumbing-heavy layouts:</strong> sinks in exam and treatment rooms, sterilization areas and specialized drains.</li>
<li><strong>Durable, cleanable finishes:</strong> materials selected for frequent cleaning.</li>
<li><strong>Privacy:</strong> sound-attenuating walls and thoughtful layouts.</li>
<li><strong>Equipment coordination:</strong> we coordinate with dental, imaging and equipment vendors on power, blocking, plumbing and any shielding their equipment requires.</li></ul>
<h2>Opening Your Practice on Time</h2>
<p>We plan around your lease, licensing and equipment delivery so you can start seeing patients when planned.</p>
<p>Serving <a href="/oakland-county-general-contractor">Oakland County</a>, <a href="/washtenaw-county-general-contractor">Washtenaw County</a>, <a href="/genesee-county-general-contractor">Genesee County</a> and <a href="/service-areas">Southeast Michigan</a>. <a href="/construction-contact#quote">Request a medical construction bid</a>.</p>""",
        "faqs": [
            ("Do you build medical and dental offices?",
             "Yes. RBF Construction builds medical office buildings and builds out space for physicians, dentists, physical therapy, urgent care and specialty clinics, including work for Athletico Physical Therapy."),
            ("Can you coordinate with our dental or imaging equipment vendors?",
             "Yes. We coordinate power, plumbing, blocking and any shielding requirements with your equipment vendors so installation goes smoothly."),
        ],
        "types": ["Medical office construction", "Dental office construction", "Clinic construction", "Healthcare tenant build-out"],
    },
    {
        "slug": "retail-construction", "group": "commercial", "nav": "Retail & Businesses", "name": "Retail and Commercial Business Construction",
        "title": "Retail & Business Construction | SE Michigan | RBF",
        "desc": "Retail, strip center and commercial business construction in Southeast Michigan: ground-up buildings, renovations, facades and build-outs.",
        "h1": "Retail &amp; Commercial Business Construction",
        "lead": "Retail stores, multi-tenant strip centers, storefront renovations and buildings for businesses of every kind.",
        "bg": "commercial-renovation-after",
        "photos": ["retail-plaza-jimmy-johns-pizza-hut-smoothie-king", "commercial-renovation-after", "concrete-road-curb-gutter-construction"],
        "body": """<h2>Buildings That Help Businesses Grow</h2>
<p>From national retailers like <strong>Dollar Tree</strong> to local businesses opening their first location, RBF Construction builds and renovates commercial space that&rsquo;s ready for customers. We handle ground-up buildings, multi-tenant strip centers, storefront renovations and interior build-outs.</p>
<ul class="tick-list"><li>Retail stores</li><li>Multi-tenant strip centers</li><li>Facade &amp; storefront renovations</li><li>Interior build-outs</li>
<li>Service &amp; professional businesses</li><li>Warehouse &amp; flex space</li><li>Parking lot reconstruction</li><li>Pump station &amp; facility upgrades</li></ul>
<!--PHOTOS-->
<h2>Commercial Renovation: Before &amp; After</h2>
<p>An aging, single-story commercial building with a failing parking lot became modern, leasable space with a stone and metal-panel facade, new storefront awnings and a freshly paved, striped lot. <a href="/projects">See the before-and-after</a>.</p>
<h2>Multi-Tenant Buildings</h2>
<p>We&rsquo;ve built multi-tenant buildings housing national brands side by side, including a retail building with Jimmy John&rsquo;s, Pizza Hut and Smoothie King. We coordinate shell construction with each tenant&rsquo;s build-out requirements.</p>
<p>Serving businesses across <a href="/oakland-county-general-contractor">Oakland County</a>, <a href="/wayne-county-general-contractor">Wayne County</a>, <a href="/genesee-county-general-contractor">Genesee County</a> and <a href="/service-areas">Southeast Michigan</a>. <a href="/construction-contact#quote">Request a commercial bid</a>.</p>""",
        "faqs": [
            ("Do you build multi-tenant retail buildings?",
             "Yes. RBF Construction builds multi-tenant retail buildings and strip centers, coordinating the shell with each tenant's build-out requirements."),
            ("Can you renovate an older commercial building?",
             "Yes. We renovate facades, storefronts, interiors, parking lots and utilities to turn older properties into modern, leasable space."),
        ],
        "types": ["Retail construction", "Commercial renovation", "Strip center construction", "Storefront renovation"],
    },
    # ---------------- Site work ----------------
    {
        "slug": "excavation-grading", "group": "site", "nav": "Excavation & Grading", "name": "Excavation and Grading",
        "title": "Excavation & Grading Contractor | SE Michigan | RBF",
        "desc": "Commercial and residential excavation, mass grading, land balancing and site clearing in Oakland County, Genesee County and Southeast Michigan.",
        "h1": "Excavation, Grading &amp; Land Balancing",
        "lead": "Mass excavation, cut-and-fill, fine grading, clearing and building pads for commercial and residential sites.",
        "bg": "commercial-site-excavation-grading",
        "photos": ["commercial-site-excavation-grading", "foundation-walls-excavation", "precast-structure-crane-set"],
        "body": """<h2>Earthwork Done Right the First Time</h2>
<p>Every project rests on its earthwork. RBF Construction&rsquo;s crews and equipment handle excavation and grading for commercial developments, building additions, new homes and infrastructure projects &mdash; built to plan elevations so pavements drain and foundations stay put.</p>
<ul class="tick-list"><li>Site clearing &amp; grubbing</li><li>Mass excavation</li><li>Land balancing (cut &amp; fill)</li><li>Building pads</li>
<li>Basement &amp; foundation excavation</li><li>Fine grading</li><li>Drainage swales &amp; ponds</li><li>Soil erosion control</li></ul>
<!--PHOTOS-->
<h2>What Is Land Balancing?</h2>
<p>Land balancing moves soil from high areas of a site to low areas so cuts and fills match. A balanced site reaches plan grades while minimizing the cost of trucking dirt in or out &mdash; often one of the biggest savings available on a project.</p>
<h2>Part of a Complete Site Package</h2>
<p>Excavation and grading flow directly into our <a href="/underground-utilities">underground utilities</a>, <a href="/parking-lot-paving-concrete">parking lot and concrete</a> and <a href="/demolition">demolition</a> services, so one team manages the entire site.</p>
<p>Serving <a href="/service-areas">Oakland County, Genesee County and Southeast Michigan</a>. <a href="/construction-contact#quote">Request an excavation bid</a>.</p>""",
        "faqs": [
            ("Do you do excavation for new homes?",
             "Yes. We excavate basements and foundations, clear lots, grade for drainage and install driveways and utility connections for new homes and additions."),
            ("What is the difference between rough grading and fine grading?",
             "Rough grading moves large amounts of soil to approximate final elevations. Fine grading brings the surface to exact plan elevations so pavement, slabs and landscaping drain correctly."),
        ],
        "types": ["Excavation", "Grading", "Land balancing", "Site clearing"],
    },
    {
        "slug": "underground-utilities", "group": "site", "nav": "Underground Utilities", "name": "Underground Utility Installation",
        "title": "Underground Utility Contractor | SE Michigan | RBF",
        "desc": "Storm sewer, sanitary sewer, water main, retention pond and pump station installation in Oakland County, Genesee County and Southeast Michigan.",
        "h1": "Underground Utilities: Storm, Sanitary &amp; Water",
        "lead": "Storm sewers, sanitary sewers, water lines, retention ponds, manholes and pump station work for commercial, residential and municipal projects.",
        "bg": "storm-sewer-pipe-installation-crew",
        "photos": ["storm-sewer-pipe-installation-crew", "manhole-water-valve-installation", "underground-utility-trench-excavation"],
        "body": """<h2>The Infrastructure Under Every Site</h2>
<p>RBF Construction installs the underground infrastructure that new buildings and developments depend on. Our crews lay pipe, set precast structures, install valves and connect to municipal systems &mdash; safely, to spec and ready for inspection.</p>
<ul class="tick-list"><li>Storm sewers</li><li>Retention &amp; detention ponds</li><li>Sanitary sewers</li><li>Water lines &amp; services</li>
<li>Manholes &amp; catch basins</li><li>Valves &amp; hydrants</li><li>Pump stations &amp; tanks</li><li>Utility repairs &amp; replacements</li></ul>
<!--PHOTOS-->
<h2>Pump Station and Facility Work</h2>
<p>Beyond new installations, we&rsquo;ve upgraded pump rooms and pump stations with new pumps, large-diameter valves, piping and tanks &mdash; work that requires careful sequencing to keep systems in service.</p>
<h2>Safety in the Trench</h2>
<p>Deep excavations demand proper trench protection, competent supervision and well-maintained equipment. Our crews work in deep trenches and structures every day and plan each dig with safety first.</p>
<p>Pair utilities with <a href="/excavation-grading">excavation</a> and <a href="/parking-lot-paving-concrete">paving and concrete</a> for a complete site package anywhere in <a href="/service-areas">Southeast Michigan</a>. <a href="/construction-contact#quote">Request a utilities bid</a>.</p>""",
        "faqs": [
            ("What underground utilities does RBF install?",
             "Storm sewers, retention and detention ponds, sanitary sewers, water lines and services, manholes, catch basins, valves, hydrants, and pump station piping, pumps and tanks."),
            ("Do you work on pump stations?",
             "Yes. We have upgraded pump stations and pump rooms with new pumps, large valves, piping and tanks."),
        ],
        "types": ["Underground utility installation", "Storm sewer installation", "Sanitary sewer installation", "Water main installation", "Pump station construction"],
    },
    {
        "slug": "parking-lot-paving-concrete", "group": "site", "nav": "Parking Lots, Roads & Concrete", "name": "Parking Lot, Road and Concrete Construction",
        "title": "Parking Lot, Road & Concrete Contractor | SE MI | RBF",
        "desc": "Parking lots, private roads, drive-thru lanes, concrete curbs, gutters, sidewalks and slabs for commercial and residential sites in Southeast Michigan.",
        "h1": "Parking Lots, Roads, Curbs &amp; Concrete",
        "lead": "New and reconstructed parking lots, private roads, drive-thru lanes, curbs, gutters, sidewalks, slabs and driveways.",
        "bg": "concrete-road-curb-gutter-construction",
        "photos": ["concrete-road-curb-gutter-construction", "commercial-renovation-after", "commercial-site-excavation-grading"],
        "body": """<h2>Pavement Built From the Base Up</h2>
<p>Michigan freeze-thaw cycles destroy pavement built on poor bases. RBF Construction builds parking lots, roads and concrete flatwork from the ground up: proper excavation, compacted aggregate base, correct drainage slopes and durable surfaces.</p>
<ul class="tick-list"><li>New parking lots</li><li>Parking lot reconstruction</li><li>Private roads &amp; drives</li><li>Drive-thru lanes</li>
<li>Concrete curbs &amp; gutters</li><li>Sidewalks &amp; ADA ramps</li><li>Slabs &amp; pads</li><li>Residential driveways</li></ul>
<!--PHOTOS-->
<h2>Fixing Failing Parking Lots</h2>
<p>Standing water, potholes and alligator cracking usually point to drainage and base problems. Our <a href="/projects">commercial renovation project</a> replaced a flooded, broken lot with a properly graded, freshly paved and striped parking area.</p>
<p>Part of our full <a href="/site-development">site development</a> services across <a href="/service-areas">Southeast Michigan</a>. <a href="/construction-contact#quote">Request a paving and concrete bid</a>.</p>""",
        "faqs": [
            ("Why does my parking lot keep flooding and cracking?",
             "Ponding water and cracking are usually caused by poor drainage slopes or a weak base. Reconstruction with proper grading, a compacted aggregate base and storm drainage fixes the cause rather than the symptom."),
            ("Do you install concrete curbs and sidewalks?",
             "Yes. We install concrete curbs, gutters, sidewalks, ADA ramps, slabs and pads for commercial and residential projects."),
        ],
        "types": ["Parking lot construction", "Road construction", "Concrete curbs and gutters", "Sidewalk construction", "Concrete flatwork"],
    },
    {
        "slug": "demolition", "group": "site", "nav": "Demolition", "name": "Demolition",
        "title": "Demolition Contractor | Oakland County & SE MI | RBF",
        "desc": "Commercial and residential demolition, interior selective demolition, pavement removal and site clearing in Southeast Michigan.",
        "h1": "Demolition &amp; Site Clearing",
        "lead": "Building demolition, interior selective demolition, pavement and foundation removal &mdash; clearing the way for what&rsquo;s next.",
        "bg": "underground-utility-trench-excavation",
        "photos": ["commercial-renovation-before", "commercial-site-excavation-grading", "underground-utility-trench-excavation"],
        "body": """<h2>Safe, Efficient Demolition</h2>
<p>Whether you&rsquo;re clearing a site for redevelopment or gutting an interior for a remodel, demolition sets the pace for the rest of the project. RBF Construction plans demolition carefully &mdash; utility disconnects, permits, protection of adjacent property and proper disposal &mdash; then moves quickly.</p>
<ul class="tick-list"><li>Commercial building demolition</li><li>Residential demolition</li><li>Interior selective demolition</li><li>Pavement &amp; curb removal</li>
<li>Foundation removal</li><li>Site clearing</li><li>Debris hauling &amp; disposal</li><li>Backfill &amp; grading</li></ul>
<!--PHOTOS-->
<h2>Demolition as Step One</h2>
<p>Because RBF is also a <a href="/general-contracting">general contractor</a> and <a href="/site-development">site developer</a>, demolition flows straight into excavation, utilities and new construction without waiting on another contractor.</p>
<p>Serving <a href="/service-areas">Oakland County, Genesee County and Southeast Michigan</a>. <a href="/construction-contact#quote">Request a demolition bid</a>.</p>""",
        "faqs": [
            ("Do you do interior demolition for remodels?",
             "Yes. We perform selective interior demolition for commercial build-outs and residential kitchen and bathroom remodels, protecting the areas that stay."),
            ("Can you demolish a building and build new on the same site?",
             "Yes. RBF handles demolition, site work and new construction, so the project moves from one phase to the next without a handoff."),
        ],
        "types": ["Demolition", "Selective demolition", "Site clearing", "Pavement removal"],
    },
]

# --------------------------------------------------------------------------
# Resource articles (GEO: clear, quotable, factual guidance)
# --------------------------------------------------------------------------
ARTICLES = [
    {
        "slug": "design-build-vs-design-bid-build",
        "title": "Design-Build vs. Design-Bid-Build in Michigan | RBF",
        "h1": "Design-Build vs. Design-Bid-Build: Which Is Right for Your Project?",
        "desc": "A plain-English comparison of design-build and design-bid-build for Michigan commercial and residential projects, from a general contractor.",
        "summary": "Design-build puts design and construction under one contract for speed and a single point of responsibility; design-bid-build separates them for maximum design control and competitive pricing.",
        "bg": "steel-frame-commercial-building",
        "body": """<p class="tldr"><strong>Short answer:</strong> Choose <strong>design-build</strong> when speed, early cost certainty and a single point of responsibility matter most. Choose <strong>design-bid-build</strong> when you want full control of the design with your own architect and competitive bids on a complete set of drawings. RBF Construction delivers projects both ways.</p>
<h2>What Is Design-Bid-Build?</h2>
<p>Design-bid-build is the traditional delivery method. The owner hires an architect to complete the design and construction documents, then general contractors bid on those documents and the owner awards a construction contract &mdash; usually to a qualified low bidder.</p>
<ul><li><strong>Pros:</strong> the owner controls design decisions, bids are directly comparable, and the process is familiar to lenders and public agencies.</li>
<li><strong>Cons:</strong> it&rsquo;s sequential and slower, and constructability or budget problems may not surface until bids come in.</li></ul>
<h2>What Is Design-Build?</h2>
<p>In design-build, one entity is responsible for both design and construction under a single contract. The contractor and designers work together from the start, pricing the project as it&rsquo;s designed.</p>
<ul><li><strong>Pros:</strong> faster schedules because design and construction can overlap, early and continuous cost feedback, and one point of accountability.</li>
<li><strong>Cons:</strong> the owner gives up some direct control over design details, and it requires trust in the design-build team.</li></ul>
<h2>Side-by-Side Comparison</h2>
<table><thead><tr><th></th><th>Design-Bid-Build</th><th>Design-Build</th></tr></thead><tbody>
<tr><td>Contracts</td><td>Two (architect + contractor)</td><td>One</td></tr>
<tr><td>Schedule</td><td>Sequential</td><td>Overlapping, typically faster</td></tr>
<tr><td>Cost certainty</td><td>At bid time</td><td>Early and ongoing</td></tr>
<tr><td>Design control</td><td>Highest for the owner</td><td>Shared with the team</td></tr>
<tr><td>Best for</td><td>Owners with an architect and defined design</td><td>Owners prioritizing speed and simplicity</td></tr></tbody></table>
<h2>Where Construction Management Fits</h2>
<p>With either method, bringing a contractor in early for <a href="/general-contracting">construction management</a> &mdash; budgeting, value engineering, scheduling and subcontractor selection &mdash; catches problems while they&rsquo;re still cheap to fix.</p>
<h2>Which Should You Choose?</h2>
<p>Restaurant and retail owners on tight opening dates often prefer design-build. Owners with a trusted architect, a highly specific design, or public funding requirements often use design-bid-build. Homeowners planning a <a href="/custom-home-builder">custom home</a> or major <a href="/kitchen-remodeling">remodel</a> can use either. <a href="/construction-contact#quote">Talk with RBF</a> about which fits your project.</p>""",
    },
    {
        "slug": "kitchen-bathroom-remodel-planning-guide",
        "title": "Kitchen & Bath Remodel Planning Guide | SE Michigan",
        "h1": "Planning a Kitchen or Bathroom Remodel in Southeast Michigan",
        "desc": "Step-by-step guide to planning a kitchen or bathroom remodel in Oakland County and Southeast Michigan: scope, budget, permits, timing and contractors.",
        "summary": "Define scope first, set a budget with a contingency, make selections before demolition, confirm permits, and hire a contractor who manages trades and inspections.",
        "bg": None,
        "body": """<p class="tldr"><strong>Short answer:</strong> Decide your scope, set a realistic budget with a contingency, finalize selections <em>before</em> demolition, confirm permits with your city or township, and hire a contractor who manages every trade and inspection.</p>
<h2>1. Define the Scope</h2>
<p>The biggest cost driver in any kitchen or bath remodel is whether you&rsquo;re keeping the layout. Replacing cabinets, counters and fixtures in place costs far less than moving plumbing, removing walls or relocating appliances. Decide early which category you&rsquo;re in.</p>
<h2>2. Set a Budget &mdash; and a Contingency</h2>
<p>Once walls and floors are opened up, older Michigan homes can reveal hidden issues: outdated wiring, undersized drains, water damage or subfloor problems. Plan a contingency for surprises so they don&rsquo;t derail the project.</p>
<h2>3. Make Selections Before Demolition</h2>
<p>Cabinets, specialty tile and some fixtures can take weeks to arrive. Finalizing and ordering selections before demolition is the single best way to shorten the time your kitchen or bathroom is out of service.</p>
<h2>4. Understand Permits</h2>
<p>Most Michigan municipalities require permits for work that changes plumbing, electrical, mechanical or structural elements. Permits mean inspections, which protect you and your home&rsquo;s resale value. A good contractor pulls permits and schedules inspections for you.</p>
<h2>5. Think About How You&rsquo;ll Live During the Remodel</h2>
<p>For kitchens, set up a temporary kitchen with a microwave, refrigerator and coffee maker. For bathrooms, plan around having another bathroom available. Ask your contractor about dust control and daily cleanup.</p>
<h2>6. Plan for the Long Term</h2>
<p>If you plan to stay, consider aging-in-place features now: curbless showers, grab-bar blocking, wider doorways, better lighting and easy-to-reach storage. They cost far less to include during a remodel than to add later.</p>
<h2>7. Choose the Right Contractor</h2>
<ul><li>Do they manage all trades, permits and inspections?</li><li>Will someone supervise on site?</li>
<li>Do they provide a written scope and schedule?</li><li>Can they handle structural changes if needed?</li></ul>
<p>RBF Construction remodels <a href="/kitchen-remodeling">kitchens</a> and <a href="/bathroom-remodeling">bathrooms</a> throughout <a href="/oakland-county-general-contractor">Oakland County</a> and <a href="/service-areas">Southeast Michigan</a>. <a href="/construction-contact#quote">Request an estimate</a>.</p>""",
    },
    {
        "slug": "commercial-site-work-guide",
        "title": "Commercial Site Work Guide for Michigan Owners | RBF",
        "h1": "What Site Work Does a Commercial Building Need?",
        "desc": "A guide for Michigan business owners to commercial site work: clearing, earthwork, utilities, storm water, paving, concrete and why it affects cost.",
        "summary": "Commercial site work includes clearing and demolition, earthwork and grading, underground utilities, storm water management, paving, concrete and final grading — often a large share of total project cost.",
        "bg": "commercial-site-excavation-grading",
        "body": """<p class="tldr"><strong>Short answer:</strong> Before a commercial building goes up, the site typically needs clearing or demolition, excavation and grading, underground utilities (water, sanitary and storm), storm water management such as a retention pond, a paved parking lot with curbs, sidewalks and final grading. Site work can be a large share of total project cost, so plan it early.</p>
<h2>1. Site Evaluation</h2>
<p>Start with a survey, soils information and a review of the local site plan requirements. Poor soils, high groundwater or a lack of nearby utilities can change the budget significantly.</p>
<h2>2. Clearing and Demolition</h2>
<p>Existing buildings, pavement, trees and foundations have to come out. See <a href="/demolition">demolition</a>.</p>
<h2>3. Earthwork and Grading</h2>
<p>The site is cut and filled to plan elevations and the building pad is prepared. Balancing cuts and fills on site avoids costly trucking. See <a href="/excavation-grading">excavation and grading</a>.</p>
<h2>4. Underground Utilities</h2>
<p>Water service, sanitary sewer and storm sewer are installed and connected to municipal systems, along with manholes, catch basins and, for restaurants, grease interceptors. See <a href="/underground-utilities">underground utilities</a>.</p>
<h2>5. Storm Water Management</h2>
<p>Most Michigan communities require new developments to control storm water runoff, often with retention or detention ponds or underground storage, plus soil erosion and sedimentation control during construction.</p>
<h2>6. Paving and Concrete</h2>
<p>Parking lots, drive aisles and drive-thru lanes are built on a compacted aggregate base, then finished with curbs, gutters, sidewalks and accessible ramps. See <a href="/parking-lot-paving-concrete">parking lots and concrete</a>.</p>
<h2>7. Final Grading and Restoration</h2>
<p>Topsoil, final grades and landscaping areas finish the site and direct water away from the building.</p>
<h2>Why One Contractor for Site and Building Helps</h2>
<p>When the site contractor and building contractor are different companies, schedule gaps and finger-pointing are common. RBF Construction performs <a href="/site-development">site development</a> and <a href="/general-contracting">general contracting</a> under one contract across <a href="/service-areas">Southeast Michigan</a>. <a href="/construction-contact#quote">Request a bid</a>.</p>""",
    },
]

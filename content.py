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
        "slug": "genesee-county-general-contractor", "name": "Genesee County",
        "cities": ["Flint", "Flint Township", "Burton", "Grand Blanc", "Grand Blanc Township", "Fenton", "Fenton Township",
                   "Flushing", "Davison", "Swartz Creek", "Clio", "Mt. Morris", "Linden", "Montrose", "Goodrich",
                   "Gaines", "Genesee Township", "Mundy Township"],
        "title": "General Contractor in Flint & Genesee County | RBF",
        "desc": "Flint-based general contractor for all of Genesee County: custom homes, remodels, pole barns, commercial construction and site work.",
        "h1": "Genesee County&rsquo;s Hometown General Contractor",
        "lead": "Headquartered on W Hill Rd in Flint, RBF builds homes, remodels, pole barns, commercial buildings and sites across every corner of Genesee County.",
        "bg": "cottage-inn-pizza-davison-mi",
        "intro": """<p>Genesee County is home base for RBF Construction. Our office and crews are based at 1411 W Hill Rd in Flint, which means fast response times and personal on-site supervision on projects in Flint, Flint Township, Burton, Grand Blanc, Fenton, Flushing, Davison, Swartz Creek, Clio and every surrounding township.</p>
<p>Genesee County is where our crews and equipment are based. Our portfolio includes restaurants, storefront renovations, underground utilities and pump station work, and we bring the same team to homeowners planning a new home, a remodel or a pole barn.</p>""",
        "focus": """<h2>Services Across Genesee County</h2>
<ul class="tick-list"><li><a href="/custom-home-builder">Custom homes &amp; additions</a></li><li><a href="/kitchen-remodeling">Kitchen remodeling</a></li>
<li><a href="/bathroom-remodeling">Bathroom remodeling</a></li><li><a href="/pole-barns">Pole barns &amp; garages</a></li>
<li><a href="/commercial-general-contracting">Commercial construction</a></li><li><a href="/restaurant-construction">Restaurants &amp; drive-thrus</a></li>
<li><a href="/medical-office-construction">Medical offices</a></li><li><a href="/site-development">Site work &amp; utilities</a></li></ul>
<h2>New Homes, Remodels and Pole Barns</h2>
<p>From established neighborhoods in Flint, Burton and Flushing to newer subdivisions in Grand Blanc and Fenton and acreage in Gaines, Atlas, Goodrich and Montrose, we build custom homes and additions, remodel kitchens and bathrooms, and put up pole barns and garages &mdash; with our own crews handling the excavation, concrete and utility work.</p>
<h2>Commercial Construction and Redevelopment</h2>
<p>Genesee County&rsquo;s commercial corridors &mdash; Miller Road, Linden Road, Hill Road, Dort Highway, Saginaw Street and the Grand Blanc and Fenton business districts &mdash; are full of properties with good bones and dated buildings. We build new restaurants, offices, medical and retail buildings, and we turn tired properties into modern, leasable space with new facades, interiors, parking lots and utilities. See our <a href="/projects">before-and-after renovation</a>.</p>
<h2>Site Work Close to Home</h2>
<p>Our equipment and earthwork crews are based right here in Flint, so excavation, grading, storm and sanitary sewers, water lines, parking lots and demolition in Genesee County start fast and stay on schedule.</p>""",
        "faqs": [
            ("Where is RBF Construction located in Genesee County?",
             "Our office is at 1411 W Hill Rd, Flint, MI 48507, open Monday through Friday, 8 AM to 5 PM."),
            ("Which Genesee County communities do you serve?",
             "All of them, including Flint, Flint Township, Burton, Grand Blanc, Fenton, Flushing, Davison, Swartz Creek, Clio, Mt. Morris, Linden, Montrose, Goodrich and Gaines."),
            ("Do you build pole barns in Genesee County?",
             "Yes. We build pole barns, garages and post-frame buildings throughout Genesee County, including the site preparation and concrete floors."),
        ],
    },
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
        "bg": "living-room-coffered-ceiling-stone-fireplace",
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
<p>New construction in Livingston County often starts with raw land. Our in-house earthwork crews handle clearing, excavation, grading, drainage, driveways and utility trenching, so your home or commercial building starts on properly prepared ground.</p>
<h2>Pole Barns and Garages on Acreage</h2>
<p>Many Livingston County properties have room for a <a href="/pole-barns">pole barn, detached garage or workshop</a>. RBF prepares the site, builds the compacted base and pours the concrete floor and apron with our own crews, then builds the post-frame structure.</p>""",
        "faqs": [
            ("Do you build pole barns in Livingston County?",
             "Yes. We build pole barns, detached garages and workshops in Brighton, Howell, Hartland, Fowlerville, Pinckney and the surrounding townships, including the site work and concrete."),
            ("Do you build custom homes in Livingston County?",
             "Yes. We build ground-up homes and additions in Brighton, Howell, Hartland, Fowlerville, Pinckney and surrounding townships, including the site work."),
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
<li><a href="/commercial-general-contracting">Commercial construction</a></li><li><a href="/parking-lot-paving-concrete">Driveways, lots &amp; concrete</a></li></ul>
<h2>Pole Barns, Garages and Outbuildings</h2>
<p>Acreage across Lapeer County &mdash; from Metamora and Dryden to Columbiaville and North Branch &mdash; is pole barn country. RBF builds <a href="/pole-barns">pole barns, detached garages and workshops</a> with our own crews handling the site clearing, grading, compacted base and concrete floor, so the building sits on properly drained ground.</p>
<h2>Close to Our Flint Headquarters</h2>
<p>Lapeer County sits just east of Flint along I-69, so our crews, equipment and supervisors are a short drive away. That makes it practical to stay closely involved in the site work and construction on Lapeer County projects, from a single garage to a commercial building in Lapeer or Imlay City.</p>""",
        "faqs": [
            ("Do you build pole barns in Lapeer County?",
             "Yes. RBF builds pole barns, detached garages and workshops throughout Lapeer County, including the site preparation, compacted base and concrete floor."),
            ("Do you serve Lapeer County?",
             "Yes. We work in Lapeer, Imlay City, Almont, Metamora, Dryden, Columbiaville, North Branch and the surrounding townships."),
        ],
    },
    {
        "slug": "shiawassee-county-general-contractor", "name": "Shiawassee County",
        "cities": ["Owosso", "Durand", "Corunna", "Perry", "Laingsburg", "Ovid", "Morrice", "Byron", "Bancroft",
                   "Lennon", "Vernon"],
        "title": "Shiawassee County General Contractor | RBF Construction",
        "desc": "General contractor for Owosso, Durand, Corunna, Perry and all of Shiawassee County: public and commercial buildings, homes, remodels and site work.",
        "h1": "General Contractor for Shiawassee County",
        "lead": "Public and commercial buildings, new homes, remodels and site work in Owosso, Durand, Corunna and Perry.",
        "bg": "storm-pipe-trench-installation",
        "intro": """<p>Just west of our Flint headquarters, Shiawassee County is home to Owosso, Durand, Corunna and Perry. RBF Construction&rsquo;s work here includes the <strong>Durand Memorial Library</strong> and a <strong>Veterans Affairs building</strong>, and we take on commercial buildings, new homes and additions, kitchen and bath remodels, and the excavation, utilities and paving behind them.</p>""",
        "focus": """<h2>Shiawassee County Services</h2>
<ul class="tick-list"><li><a href="/government-institutional-construction">Government &amp; institutional</a></li><li><a href="/commercial-general-contracting">Commercial construction</a></li>
<li><a href="/custom-home-builder">Custom homes</a></li><li><a href="/kitchen-remodeling">Kitchen remodeling</a></li>
<li><a href="/excavation-grading">Excavation &amp; grading</a></li><li><a href="/parking-lot-paving-concrete">Driveways, lots &amp; concrete</a></li></ul>
<h2>Public and Institutional Work</h2>
<p>Public projects in Shiawassee County, including the Durand Memorial Library and a Veterans Affairs building, are part of RBF&rsquo;s <a href="/government-institutional-construction">government and institutional work</a>. Library districts, agencies and nonprofits get one team for the building and the site work around it.</p>
<h2>Close to Our Flint Headquarters</h2>
<p>Durand and Perry sit along I-69 west of Flint, and Owosso and Corunna are a short drive beyond, so our crews, equipment and supervisors can stay closely involved in Shiawassee County projects from start to finish.</p>""",
        "faqs": [
            ("Do you serve Shiawassee County?",
             "Yes. We work in Owosso, Durand, Corunna, Perry, Laingsburg, Ovid, Morrice, Byron and the surrounding townships."),
            ("Have you done public projects in Shiawassee County?",
             "Yes. RBF's work in Shiawassee County includes public buildings, including a library and a government building."),
        ],
    },
]
OTHER_AREAS = ["St. Clair County", "Monroe County", "Saginaw County", "Tuscola County"]

# --------------------------------------------------------------------------
# Services
# --------------------------------------------------------------------------
GROUPS = {
    "commercial": ("Commercial", "/commercial-general-contracting"),
    "residential": ("Residential", "/residential-general-contracting"),
    "site": ("Site Work & Utilities", "/site-development"),
}

SERVICES = [
    # ---------------- Commercial ----------------
    {
        "slug": "office-building-construction", "group": "commercial", "nav": "Office Buildings", "name": "Office Building Construction",
        "title": "Commercial Build-Out & Office Contractor | Flint, MI | RBF",
        "desc": "Office building construction, tenant build-outs and office renovations in Genesee, Oakland & SE Michigan. Design-build or design-bid-build.",
        "h1": "Commercial Build-Outs &amp; Office Construction",
        "lead": "New professional office buildings, tenant improvements and office renovations across Genesee County, Oakland County and Southeast Michigan.",
        "bg": None,
        "photos": ["athletico-physical-therapy-shelby-mi", "commercial-renovation-after", "commercial-site-excavation-grading"],
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
        "title": "Restaurant Construction Contractor in Michigan | RBF",
        "desc": "Restaurant and drive-thru construction in Michigan for national brands and local owners: ground-up builds, remodels, build-outs and site work.",
        "h1": "Restaurant Construction for National Brands &amp; Local Owners",
        "lead": "Ground-up quick-service restaurants with drive-thrus, sit-down restaurants, franchise remodels and tenant build-outs.",
        "bg": "smoothie-king-building", "photos": ["taco-bell-cass-city-mi", "cottage-inn-pizza-davison-mi", "smoothie-king-building"],
        "body": """<h2>Restaurant Projects We&rsquo;ve Built</h2>
<p>RBF Construction has built for restaurant brands including <strong>Jimmy John&rsquo;s, Pizza Hut, Smoothie King, Taco Bell, Cottage Inn Pizza and Biggby Coffee</strong>, among others. We understand franchise brand standards, tight opening dates and the kitchen infrastructure restaurants depend on.</p>
<ul class="tick-list"><li>Quick-service restaurants</li><li>Drive-thru lanes &amp; windows</li><li>Sit-down &amp; fast-casual</li><li>Coffee shops &amp; smoothie bars</li>
<li>Franchise remodels &amp; refreshes</li><li>End-cap &amp; in-line build-outs</li><li>Multi-tenant restaurant buildings</li><li>Parking, drive aisles &amp; utilities</li></ul>
<!--PHOTOS-->
<h2>Built Around the Kitchen</h2>
<p>Restaurants have infrastructure most buildings don&rsquo;t: hood and make-up air systems, grease interceptors, floor drains, heavy electrical and gas loads, walk-in coolers and health-code finishes. We coordinate these trades and inspections so your health department and fire inspections go smoothly.</p>
<h2>Drive-Thru Site Work, Done In-House</h2>
<p>Drive-thru stacking lanes, curbing, menu-board foundations, grease interceptor installation, storm water and parking all fall to our <a href="/site-development">site development division</a> &mdash; no handoff between a site contractor and a building contractor.</p>
<h2>Opening Day Matters</h2>
<p>We schedule backward from your opening date, order long-lead equipment early, and keep franchise representatives informed with progress updates.</p>
<p>We build restaurants throughout <a href="/oakland-county-general-contractor">Oakland County</a>, <a href="/service-areas">Macomb County</a>, <a href="/genesee-county-general-contractor">Genesee County</a> and <a href="/service-areas">Southeast Michigan</a>. <a href="/construction-contact#quote">Request a restaurant construction bid</a>.</p>""",
        "faqs": [
            ("Have you built restaurants for national franchise brands?",
             "Yes. RBF Construction has built restaurants for national quick-service and franchise brands, as well as local restaurant owners."),
            ("Do you build drive-thru restaurants?",
             "Yes. We build the restaurant and the drive-thru site work, including stacking lanes, curbing, menu-board foundations, grease interceptors, utilities and parking."),
            ("Can you remodel an existing restaurant to new brand standards?",
             "Yes. We handle franchise remodels and refreshes, scheduling the work to minimize the time your restaurant is closed."),
        ],
        "types": ["Restaurant construction", "Quick-service restaurant construction", "Drive-thru construction", "Franchise construction"],
    },
    {
        "slug": "medical-office-construction", "group": "commercial", "nav": "Medical & Dental", "name": "Medical Office Construction",
        "title": "Medical Office Construction | Flint & SE Michigan | RBF",
        "desc": "Medical office, dental, physical therapy and clinic construction in Genesee County, Oakland County and Southeast Michigan. New buildings and build-outs.",
        "h1": "Medical, Dental &amp; Clinic Construction in Flint &amp; Southeast Michigan",
        "lead": "New medical office buildings and build-outs for physicians, dentists, physical therapy, urgent care and specialty clinics.",
        "bg": "athletico-physical-therapy-shelby-mi", "photos": [],
        "body": """<h2>Healthcare Spaces Built With Care</h2>
<p>Medical construction has requirements other commercial projects don&rsquo;t: accessibility, infection-control-friendly finishes, plumbing at nearly every exam room, privacy and sound control, and coordination with specialty equipment vendors. RBF Construction has built space for healthcare tenants including <strong>Athletico Physical Therapy</strong> (pictured above), and we bring that experience to every medical project.</p>
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
<p>Serving <a href="/oakland-county-general-contractor">Oakland County</a>, <a href="/service-areas">Washtenaw County</a>, <a href="/genesee-county-general-contractor">Genesee County</a> and <a href="/service-areas">Southeast Michigan</a>. <a href="/construction-contact#quote">Request a medical construction bid</a>.</p>""",
        "faqs": [
            ("Do you build medical and dental offices?",
             "Yes. RBF Construction builds medical office buildings and builds out space for physicians, dentists, physical therapy, urgent care and specialty clinics."),
            ("Can you coordinate with our dental or imaging equipment vendors?",
             "Yes. We coordinate power, plumbing, blocking and any shielding requirements with your equipment vendors so installation goes smoothly."),
        ],
        "types": ["Medical office construction", "Dental office construction", "Clinic construction", "Healthcare tenant build-out"],
    },
    {
        "slug": "retail-construction", "group": "commercial", "nav": "Retail & Businesses", "name": "Retail and Commercial Business Construction",
        "title": "Retail & Commercial Construction | Flint, MI | RBF",
        "desc": "Retail, strip center and commercial business construction in Southeast Michigan: ground-up buildings, renovations, facades and build-outs.",
        "h1": "Retail &amp; Commercial Business Construction",
        "lead": "Retail stores, multi-tenant strip centers, storefront renovations and buildings for businesses of every kind.",
        "bg": "family-dollar-dollar-tree-olivet-mi", "photos": ["retail-plaza-jimmy-johns-pizza-hut-smoothie-king", "commercial-renovation-after", "athletico-physical-therapy-shelby-mi"],
        "body": """<h2>Buildings That Help Businesses Grow</h2>
<p>From national retailers like <strong>Dollar Tree</strong> to local businesses opening their first location, RBF Construction builds and renovates commercial space that&rsquo;s ready for customers. We handle ground-up buildings, multi-tenant strip centers, storefront renovations and interior build-outs.</p>
<ul class="tick-list"><li>Retail stores</li><li>Multi-tenant strip centers</li><li>Facade &amp; storefront renovations</li><li>Interior build-outs</li>
<li>Service &amp; professional businesses</li><li>Warehouse &amp; flex space</li><li>Parking lot reconstruction</li><li>Pump station &amp; facility upgrades</li></ul>
<!--PHOTOS-->
<h2>Commercial Renovation: Before &amp; After</h2>
<p>An aging, single-story commercial building with a failing parking lot became modern, leasable space with a stone and metal-panel facade, new storefront awnings and a freshly paved, striped lot. <a href="/projects">See the before-and-after</a>.</p>
<h2>Multi-Tenant Buildings</h2>
<p>We&rsquo;ve built multi-tenant buildings housing national brands side by side &mdash; one example is a retail building with Jimmy John&rsquo;s, Pizza Hut and Smoothie King. We coordinate shell construction with each tenant&rsquo;s build-out requirements.</p>
<p>Serving businesses across <a href="/oakland-county-general-contractor">Oakland County</a>, <a href="/service-areas">Wayne County</a>, <a href="/genesee-county-general-contractor">Genesee County</a> and <a href="/service-areas">Southeast Michigan</a>. <a href="/construction-contact#quote">Request a commercial bid</a>.</p>""",
        "faqs": [
            ("Do you build multi-tenant retail buildings?",
             "Yes. RBF Construction builds multi-tenant retail buildings and strip centers, coordinating the shell with each tenant's build-out requirements."),
            ("Can you renovate an older commercial building?",
             "Yes. We renovate facades, storefronts, interiors, parking lots and utilities to turn older properties into modern, leasable space."),
        ],
        "types": ["Retail construction", "Commercial renovation", "Strip center construction", "Storefront renovation"],
    },
    {
        "slug": "government-institutional-construction", "group": "commercial", "nav": "Government & Institutional", "name": "Government and Institutional Construction",
        "title": "Government & Institutional Construction | RBF",
        "desc": "Construction for libraries, nonprofit centers and government buildings in Genesee, Shiawassee, Oakland and Southeast Michigan, plus the site work.",
        "h1": "Government &amp; Institutional Construction",
        "lead": "Libraries, community and nonprofit centers, and government buildings across Genesee County, Shiawassee County and Southeast Michigan.",
        "bg": "public-library-brick-building", "photos": [],
        "body": """<h2>Building for Public and Nonprofit Owners</h2>
<p>RBF Construction works with public agencies, library districts and nonprofit organizations on their buildings and the site work around them. Public and institutional projects bring their own requirements &mdash; formal bidding, board approvals and detailed documentation &mdash; and we manage them with the same personal on-site supervision we bring to every job.</p>
<ul class="tick-list"><li>Libraries</li><li>Community &amp; nonprofit centers</li><li>Government buildings</li><li>Interior build-outs</li>
<li>Renovations</li><li>Site work, parking &amp; utilities</li></ul>
<h2>Public and Institutional Experience</h2>
<p>A few examples of RBF&rsquo;s public and nonprofit work:</p>
<ul><li><strong>Durand Memorial Library</strong> &mdash; Durand, <a href="/shiawassee-county-general-contractor">Shiawassee County</a></li>
<li><strong>St. Luke N.E.W. Life Center</strong> &mdash; Flint, <a href="/genesee-county-general-contractor">Genesee County</a></li>
<li><strong>Veterans Affairs building</strong> &mdash; <a href="/shiawassee-county-general-contractor">Shiawassee County</a></li></ul>
<h2>One Team for the Building and the Site</h2>
<p>Because RBF runs its own <a href="/site-development">site development division</a>, the same team that manages the building can handle <a href="/excavation-grading">excavation</a>, <a href="/underground-utilities">utilities</a> and <a href="/parking-lot-paving-concrete">parking and concrete</a> &mdash; fewer handoffs for owners who answer to a board or the public.</p>
<p>Serving public and nonprofit owners in <a href="/genesee-county-general-contractor">Genesee County</a>, <a href="/shiawassee-county-general-contractor">Shiawassee County</a>, <a href="/oakland-county-general-contractor">Oakland County</a> and <a href="/service-areas">Southeast Michigan</a>. <a href="/construction-contact#quote">Request a bid</a>.</p>""",
        "faqs": [
            ("Does RBF Construction work on government and public buildings?",
             "Yes. RBF's public and institutional work includes a library, a nonprofit community center and a government building in Genesee and Shiawassee counties."),
            ("Do you work with nonprofit organizations?",
             "Yes. RBF works with nonprofit organizations on their buildings and sites, and we help nonprofit owners plan scope, budget and schedule before construction starts."),
        ],
        "types": ["Government building construction", "Institutional construction", "Public building renovation", "Nonprofit facility construction"],
    },
    # ---------------- Residential ----------------
    {
        "slug": "custom-home-builder", "group": "residential", "nav": "Custom & Modular Homes", "name": "Custom Home Building",
        "title": "Custom & Modular Home Builder | Flint & Genesee County | RBF",
        "desc": "Stick-built and modular homes and additions in Genesee, Oakland and SE Michigan, with in-house excavation, grading, driveways and utilities.",
        "h1": "Custom Home Builder for Flint, Genesee &amp; Oakland County",
        "lead": "Stick-built and modular homes and additions &mdash; with our own crews handling the land clearing, excavation, grading and utilities.",
        "bg": "living-room-coffered-ceiling-stone-fireplace", "photos": ["open-floor-plan-fireplace-cable-railing", "wet-bar-brick-accent-wall", "foundation-walls-excavation"],
        "body": """<h2>Ground-Up Homes, Built by a Site Work Contractor</h2>
<p>Most home builders subcontract everything below grade. RBF Construction does it ourselves. Our <a href="/site-development">site development division</a> handles clearing, excavation, grading, drainage, driveways and utility connections &mdash; the work that determines whether a house stays dry, level and problem-free for decades.</p>
<ul class="tick-list"><li>Stick-built custom homes</li><li>Modular homes</li><li>Home additions</li><li>Garages &amp; accessory buildings</li><li>Lot clearing &amp; excavation</li>
<li>Foundations &amp; basements</li><li>Driveways &amp; flatwork</li><li>Water, sewer &amp; utility connections</li><li>Design-build or your plans</li></ul>
<!--PHOTOS-->
<h2>Stick-Built or Modular: Two Ways to Build</h2>
<p><strong>Stick-built</strong> homes are framed piece by piece on your lot. They offer the most freedom in layout, rooflines and finishes, and changes can be made as the house goes up.</p>
<p><strong>Modular</strong> homes are built in sections in a factory, then delivered and set on a permanent foundation with a crane. In Michigan, modular homes are built to the same state building code as site-built homes. Factory construction isn&rsquo;t slowed by weather, which can shorten the time on site.</p>
<p>Either way, the lot still needs clearing, excavation, a foundation, utilities and a driveway &mdash; the work our own crews handle. RBF builds both, so we can help you compare options for your lot, budget and schedule.</p>
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
            ("Do you build modular homes?",
             "Yes. RBF Construction builds both stick-built and modular homes. For either one, our own crews handle the lot clearing, excavation, grading, utilities and driveway."),
            ("What is the difference between a modular and a stick-built home?",
             "A stick-built home is framed on your lot, which allows the most design flexibility. A modular home is built in sections in a factory to the same Michigan building code, then set on a permanent foundation on your lot."),
            ("Can you build from my architect's plans?",
             "Yes. We can build from your plans or deliver the project through design-build with our network of architects."),
            ("Do you build homes on rural or lake lots?",
             "Yes. Rural, wooded and lake lots are a strength because our in-house earthwork division handles clearing, grading, drainage, long driveways and utility runs."),
        ],
        "types": ["Custom home building", "Modular home construction", "Stick-built home construction", "New home construction", "Home additions"],
    },
    {
        "slug": "kitchen-remodeling", "group": "residential", "nav": "Kitchen Remodeling", "name": "Kitchen Remodeling",
        "title": "Kitchen Remodeling Contractor | Flint & Genesee County | RBF",
        "desc": "Kitchen remodeling contractor for Oakland County and Southeast Michigan: layout changes, cabinets, countertops, tile, lighting and permits handled.",
        "h1": "Kitchen Remodeling in Flint, Genesee &amp; Oakland County",
        "lead": "From a cabinet-and-countertop refresh to a full gut with a new layout &mdash; one contractor managing design, trades, permits and schedule.",
        "bg": "kitchen-island-wood-beams-white-cabinets", "photos": ["kitchen-white-cabinets-island-pendant-lights", "open-kitchen-island-tile-backsplash", "kitchen-granite-countertops-white-cabinets"],
        "body": """<h2>A Kitchen Remodel Managed Like a Construction Project</h2>
<p>Kitchens are the most complex room in a house: plumbing, electrical, ventilation, structure, cabinetry and finishes all have to come together in the right order. RBF Construction manages your kitchen remodel the same way we manage commercial projects &mdash; with a clear scope, a realistic schedule, skilled trades and personal on-site supervision.</p>
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
        "title": "Bathroom Remodeling | Flint, Genesee & Oakland County | RBF",
        "desc": "Bathroom remodeling in Genesee, Oakland & SE Michigan: walk-in showers, tub conversions, tile, vanities and accessible, aging-in-place baths.",
        "h1": "Bathroom Remodeling in Flint, Genesee &amp; Oakland County",
        "lead": "Walk-in showers, tub-to-shower conversions, accessible baths and complete primary suite remodels &mdash; waterproofed and built to last.",
        "bg": "bathroom-freestanding-tub-glass-shower", "photos": ["walk-in-shower-white-subway-tile", "bathroom-black-tile-shower-vanity", "bathroom-wood-vanity-patterned-tile-floor"],
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
             "Yes. We remodel bathrooms throughout Genesee County, Oakland County and Southeast Michigan, as well as Genesee County where our office is located."),
        ],
        "types": ["Bathroom remodeling", "Bathroom renovation", "Shower installation", "Accessible bathroom remodeling"],
    },
    {
        "slug": "pole-barns", "group": "residential", "nav": "Pole Barns & Garages", "name": "Pole Barn Construction",
        "title": "Pole Barn Builder | Flint, Genesee & Oakland County | RBF",
        "desc": "Pole barns, detached garages, workshops and post-frame buildings in Genesee County, Oakland County and Southeast Michigan, with site prep and concrete.",
        "h1": "Pole Barns, Garages &amp; Post-Frame Buildings in Genesee County",
        "lead": "Pole barns, detached garages, workshops and storage buildings &mdash; with the site prep, gravel base and concrete floor done by our own crews.",
        "bg": None, "photos": [],
        "body": """<h2>Pole Barns Built on a Proper Foundation</h2>
<p>A pole barn is only as good as the ground it sits on. Because RBF Construction has its own <a href="/site-development">excavation and site work division</a>, we handle everything from clearing and grading the building site to the gravel base, concrete floor, apron and driveway &mdash; then build the post-frame structure itself.</p>
<h2>Pole Barn and Post-Frame Projects</h2>
<ul class="tick-list"><li>Detached garages</li><li>Workshops &amp; hobby barns</li><li>RV, boat &amp; equipment storage</li><li>Horse &amp; hobby-farm barns</li>
<li>Agricultural buildings</li><li>Commercial storage buildings</li><li>Lean-tos &amp; additions</li><li>Barn-style homes &amp; living quarters</li></ul>
<h2>Options and Upgrades</h2>
<ul><li><strong>Concrete floors and aprons</strong>, poured by our own crews</li>
<li><strong>Overhead and walk doors</strong> sized for trucks, RVs, boats or equipment</li>
<li><strong>Insulation, liner panels and heat</strong> for a year-round shop</li>
<li><strong>Electrical service and lighting</strong>, including trenching from the house</li>
<li><strong>Wainscot, windows, cupolas and color choices</strong> to match your home</li>
<li><strong>Driveways and grading</strong> so water drains away from the building</li></ul>
<h2>Permits, Zoning and Site Planning</h2>
<p>Most Michigan townships regulate accessory buildings with size limits, height limits and setbacks, and require a building permit. We review your township&rsquo;s rules, plan the building location, pull permits and schedule inspections. Farm buildings may qualify for Michigan&rsquo;s agricultural exemption &mdash; see our <a href="/resources/pole-barn-permits-michigan">pole barn permit guide</a>.</p>
<h2>Our Pole Barn Process</h2>
<ol><li><strong>Site visit:</strong> we look at the location, access, drainage and how you&rsquo;ll use the building.</li>
<li><strong>Design &amp; estimate:</strong> size, doors, options and a clear price.</li>
<li><strong>Permits &amp; site prep:</strong> clearing, grading and a compacted base.</li>
<li><strong>Construction:</strong> posts, trusses, steel, doors and options.</li>
<li><strong>Concrete &amp; finish:</strong> floor, apron and final grading.</li></ol>
<p>We build pole barns across <a href="/genesee-county-general-contractor">Genesee County</a>, <a href="/oakland-county-general-contractor">Oakland County</a>, <a href="/lapeer-county-general-contractor">Lapeer County</a>, <a href="/livingston-county-general-contractor">Livingston County</a> and <a href="/service-areas">Southeast Michigan</a>. <a href="/construction-contact#quote">Request a pole barn estimate</a>.</p>""",
        "faqs": [
            ("Do I need a permit to build a pole barn in Michigan?",
             "In most Michigan townships, yes. Accessory buildings usually need a building permit and must meet zoning rules for size, height and setbacks. RBF reviews your township's requirements and pulls the permits."),
            ("Do you pour the concrete floor for pole barns?",
             "Yes. Our own crews prepare the site, build the compacted base and pour the concrete floor and apron, so the building sits on a solid, properly drained foundation."),
            ("Can a pole barn be used as a heated workshop?",
             "Yes. With insulation, interior liner panels, electrical service and a heat source, a pole barn makes an excellent year-round workshop or garage."),
            ("Where do you build pole barns?",
             "Throughout Genesee County, Oakland County, Lapeer County, Livingston County and the rest of Southeast Michigan."),
        ],
        "types": ["Pole barn construction", "Post-frame construction", "Detached garage construction", "Workshop construction"],
    },
    # ---------------- Site work ----------------
    {
        "slug": "excavation-grading", "group": "site", "nav": "Excavation & Grading", "name": "Excavation and Grading",
        "title": "Excavation Contractor in Flint, MI | Grading | RBF",
        "desc": "Commercial and residential excavation, mass grading, land balancing and site clearing in Oakland County, Genesee County and Southeast Michigan.",
        "h1": "Excavation &amp; Grading Contractor in Flint, MI",
        "lead": "Mass excavation, cut-and-fill, fine grading, clearing and building pads for commercial and residential sites.",
        "bg": "commercial-site-excavation-grading", "photos": ["site-clearing-excavator", "foundation-walls-excavation", "underground-utility-trench-excavation"],
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
        "title": "Underground Utility Contractor | Flint & SE Michigan | RBF",
        "desc": "Storm sewer, sanitary sewer, water main, retention pond and pump station installation in Oakland County, Genesee County and Southeast Michigan.",
        "h1": "Underground Utility Contractor: Storm, Sanitary &amp; Water",
        "lead": "Storm sewers, sanitary sewers, water lines, retention ponds, manholes and pump station work for commercial, residential and municipal projects.",
        "bg": "storm-sewer-pipe-installation-crew", "photos": ["storm-pipe-trench-installation", "precast-manhole-installation", "valve-vault-piping"],
        "body": """<h2>The Infrastructure Under Every Site</h2>
<p>RBF Construction installs the underground infrastructure that new buildings and developments depend on. Our crews lay pipe, set precast structures, install valves and connect to municipal systems &mdash; safely, to spec and ready for inspection.</p>
<ul class="tick-list"><li>Storm sewers</li><li>Retention &amp; detention ponds</li><li>Sanitary sewers</li><li>Water lines &amp; services</li>
<li>Manholes &amp; catch basins</li><li>Valves &amp; hydrants</li><li>Pump stations &amp; tanks</li><li>Utility repairs &amp; replacements</li></ul>
<!--PHOTOS-->
<h2>Pump Station and Facility Work</h2>
<p>Beyond new installations, we&rsquo;ve upgraded pump rooms and pump stations with new pumps, large-diameter valves, piping and tanks &mdash; work that requires careful sequencing to keep systems in service.</p>
<h2>Safety in the Trench</h2>
<p>Deep excavations demand proper trench protection, competent supervision and well-maintained equipment. We plan every dig with safety first.</p>
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
        "title": "Parking Lot & Concrete Contractor | Flint, MI | RBF",
        "desc": "Parking lots, private roads, drive-thru lanes, concrete curbs, gutters, sidewalks and slabs for commercial and residential sites in Southeast Michigan.",
        "h1": "Parking Lots, Roads, Curbs &amp; Concrete in Flint &amp; Genesee County",
        "lead": "New and reconstructed parking lots, private roads, drive-thru lanes, curbs, gutters, sidewalks, slabs and driveways.",
        "bg": "concrete-road-curb-gutter-construction", "photos": ["concrete-curb-finishing", "commercial-renovation-after", "commercial-site-excavation-grading"],
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
        "title": "Demolition Contractor | Flint, Genesee & Oakland | RBF",
        "desc": "Commercial and residential demolition, interior selective demolition, pavement removal and site clearing in Southeast Michigan.",
        "h1": "Demolition &amp; Site Clearing in Flint &amp; Genesee County",
        "lead": "Building demolition, interior selective demolition, pavement and foundation removal &mdash; clearing the way for what&rsquo;s next.",
        "bg": "site-clearing-excavator",
        "photos": ["commercial-renovation-before", "commercial-renovation-after", "commercial-site-excavation-grading"],
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
        "published": "2026-10-21", "updated": "2026-10-21",
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
        "published": "2026-10-21", "updated": "2026-10-21",
        "title": "Kitchen & Bath Remodel Planning Guide | SE Michigan",
        "h1": "Planning a Kitchen or Bathroom Remodel in Southeast Michigan",
        "desc": "Step-by-step guide to planning a kitchen or bathroom remodel in Genesee, Oakland & SE Michigan: scope, budget, permits, timing and contractors.",
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
        "published": "2026-10-21", "updated": "2026-10-21",
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
    {
        "slug": "pole-barn-permits-michigan",
        "published": "2026-10-23", "updated": "2026-10-23",
        "title": "Do You Need a Permit for a Pole Barn in Michigan? | RBF",
        "h1": "Do You Need a Permit for a Pole Barn in Michigan?",
        "desc": "When a Michigan pole barn needs a building permit, when the farm-building exemption applies, and the zoning, soil erosion and MISS DIG steps that still apply.",
        "summary": "Most pole barns and garages over 200 square feet need a building permit. Farm buildings used for agriculture can be exempt from the building permit, but zoning rules still apply.",
        "bg": None,
        "body": """<p class="tldr"><strong>Short answer:</strong> In Michigan, a detached accessory building over <strong>200 square feet</strong> &mdash; which includes almost every pole barn or garage &mdash; needs a building permit from the local building department. A building used for <strong>agriculture</strong> on the land it sits on, and not for retail sales, can be exempt from the building permit under state law. Either way, the township&rsquo;s <strong>zoning rules</strong> for size, height and setbacks still apply.</p>
<h2>When a Pole Barn Needs a Building Permit</h2>
<p>The Michigan Residential Code exempts one-story detached accessory structures with a floor area of 200 square feet or less from the building permit. Anything larger &mdash; a typical pole barn, detached garage or workshop &mdash; needs a permit and inspections. Permits are issued by the city, township or village where the property is located, or by the county where it runs the building department for that community.</p>
<h2>The Agricultural (Farm Building) Exemption</h2>
<p>Michigan&rsquo;s Single State Construction Code Act says a building permit is not required for a building incidental to the agricultural use of the land it sits on, as long as it is not used for retail trade. Townships usually ask the owner to sign an <strong>agricultural exemption affidavit</strong> stating that the building will store farm equipment or products, will not be lived in, and will not be used for retail sales.</p>
<ul><li>The exemption applies to the <strong>building permit</strong>, not to zoning. Most townships still require a zoning or land-use permit.</li>
<li>If the building later changes use &mdash; for example, to a shop, a home business or living space &mdash; the exemption can be lost and the building must meet code.</li>
<li>Townships apply the exemption differently. Some require that the stored products be grown on the same property.</li></ul>
<h2>Zoning Rules That Still Apply</h2>
<p>Township zoning ordinances commonly regulate accessory buildings by:</p>
<ul><li>maximum size, often tied to lot size</li><li>maximum height</li><li>setbacks from property lines, the road and the house</li><li>whether the building can sit in front of the house</li><li>exterior materials in some subdivisions</li></ul>
<p>Private deed restrictions or homeowner association rules can be stricter than zoning, so check those too.</p>
<h2>Other Approvals to Check</h2>
<ul><li><strong>Soil erosion permit:</strong> Michigan generally requires a soil erosion and sedimentation control permit for earth changes that disturb one acre or more, or that are within 500 feet of a lake or stream. In Genesee County, the Drain Commissioner&rsquo;s office administers the program for most communities.</li>
<li><strong>MISS DIG 811:</strong> state law requires notice to MISS DIG at least three business days before digging post holes or footings, so underground utilities can be marked.</li>
<li><strong>Driveway access:</strong> a new driveway to a county road needs a permit from the county road commission.</li>
<li><strong>Electrical:</strong> wiring a pole barn usually needs a separate electrical permit and inspection.</li></ul>
<h2>Steps Before You Build</h2>
<ol><li>Call your township building or zoning office and ask about accessory building limits and permits.</li>
<li>If the barn is for farm use, ask for the agricultural exemption form.</li>
<li>Have the building location, size and height planned to fit the setbacks.</li>
<li>Submit plans for the building permit, if one is required.</li>
<li>Call MISS DIG 811 before any digging starts.</li></ol>
<p>RBF Construction builds <a href="/pole-barns">pole barns and garages</a> across <a href="/genesee-county-general-contractor">Genesee</a>, <a href="/lapeer-county-general-contractor">Lapeer</a>, <a href="/livingston-county-general-contractor">Livingston</a> and <a href="/oakland-county-general-contractor">Oakland</a> counties, and handles the site prep and permits. <a href="/construction-contact#quote">Request a pole barn estimate</a>.</p>""",
        "sources": [
            ("Michigan Residential Code, R 408.30505: work exempt from permit", "https://www.law.cornell.edu/regulations/michigan/Mich-Admin-Code-R-408-30505"),
            ("Michigan Farm Bureau: building permit exemption for farm buildings", "https://www.michfb.com/agriculture/farming-resources/land-use-regulation/building-permit-exemption"),
            ("Michigan EGLE: soil erosion and sedimentation control overview", "https://www.michigan.gov/egle/about/organization/water-resources/soil-erosion/sesc-overview"),
            ("MISS DIG 811: frequently asked questions", "https://www.missdig811.org/get-started/i-want-to-dig/faq.html"),
        ],
    },
    {
        "slug": "commercial-construction-permits-genesee-county",
        "published": "2026-10-23", "updated": "2026-10-23",
        "title": "Commercial Construction Permits in Genesee County | RBF",
        "h1": "Permits and Approvals for Commercial Construction in Genesee County, Michigan",
        "desc": "The approvals a new commercial building in Flint and Genesee County typically needs: site plan review, soil erosion, driveway, utility and building permits.",
        "summary": "A new commercial building typically needs local site plan approval, a soil erosion permit, driveway and utility permits, and building and trade permits before it can open.",
        "bg": "steel-frame-commercial-building",
        "body": """<p class="tldr"><strong>Short answer:</strong> A new commercial building in Flint or Genesee County typically needs <strong>site plan approval</strong> from the city or township, a <strong>soil erosion and sedimentation control permit</strong>, a <strong>driveway permit</strong> from the road agency, <strong>water and sewer connection</strong> approvals, and <strong>building and trade permits</strong> &mdash; followed by inspections and a certificate of occupancy. Which agencies are involved depends on the community and the road the site fronts.</p>
<h2>1. Zoning and Site Plan Review</h2>
<p>Commercial projects start with the local city or township. The site plan &mdash; building location, parking, drive aisles, landscaping, lighting, storm water and utilities &mdash; is reviewed against the zoning ordinance, often by the planning commission. A use that isn&rsquo;t allowed by right may need a special land use approval or rezoning first, which adds time.</p>
<h2>2. Storm Water and Soil Erosion</h2>
<ul><li><strong>Soil erosion and sedimentation control (SESC) permit:</strong> required in Michigan for earth changes of one acre or more, or within 500 feet of a lake or stream. In Genesee County, most communities&rsquo; permits are issued by the Genesee County Drain Commissioner&rsquo;s office; some cities and townships run their own program.</li>
<li><strong>Storm water design:</strong> most communities require new development to control runoff, often with a detention or retention pond or underground storage, reviewed with the site plan.</li>
<li><strong>State storm water coverage:</strong> larger sites that disturb an acre or more and discharge to state waters may also need coverage from Michigan EGLE.</li></ul>
<h2>3. Driveway and Right-of-Way Permits</h2>
<p>Any new or changed driveway needs a permit from the agency that owns the road:</p>
<ul><li><strong>County roads:</strong> the Genesee County Road Commission.</li>
<li><strong>State highways</strong> (I-, M- and US-numbered routes): the Michigan Department of Transportation (MDOT), through its online permit system.</li>
<li><strong>City streets:</strong> the city.</li></ul>
<p>Commercial driveways, especially for drive-thru restaurants, may need a traffic study, turn lanes or specific spacing from other drives.</p>
<h2>4. Water and Sewer Connections</h2>
<p>Water service, sanitary sewer and storm sewer connections are approved by the utility that serves the site &mdash; the city, the township, or the county&rsquo;s water and waste system. Restaurants usually also need a grease interceptor sized and approved for the kitchen. Sites without public sewer or water need health department approval for a well or septic system.</p>
<h2>5. Building and Trade Permits</h2>
<p>Once the site plan is approved, construction drawings, usually sealed by a Michigan-licensed, architect or engineer are submitted for the building permit. Separate permits cover electrical, plumbing and mechanical work. Restaurants and other food businesses also need plan review from the health department before opening.</p>
<h2>6. MISS DIG Before Digging</h2>
<p>Michigan law requires notice to MISS DIG 811 at least three business days before excavation, so existing utilities are marked before site work begins.</p>
<h2>7. Inspections and Certificate of Occupancy</h2>
<p>The building department inspects footings, framing, trades and final construction. The site work &mdash; utilities, paving, landscaping and storm water &mdash; must also be completed or bonded before the community issues a <strong>certificate of occupancy</strong>, which is required before the business can open.</p>
<h2>How to Keep Approvals From Delaying Your Opening</h2>
<ul><li>Meet with the city or township planning staff before buying or designing the site.</li>
<li>Confirm which road agency controls the driveway and whether a traffic study is needed.</li>
<li>Confirm where water and sewer connect and who owns those lines.</li>
<li>Bring your contractor in during design so site costs are priced before approvals are final.</li></ul>
<p>RBF Construction handles <a href="/site-development">site development</a> and <a href="/commercial-general-contracting">commercial construction</a> in <a href="/genesee-county-general-contractor">Genesee County</a> and across <a href="/service-areas">Southeast Michigan</a>, including <a href="/restaurant-construction">restaurants</a> and <a href="/retail-construction">retail buildings</a>. <a href="/construction-contact#quote">Request a bid</a>.</p>""",
        "sources": [
            ("Michigan EGLE: soil erosion and sedimentation control overview", "https://www.michigan.gov/egle/about/organization/water-resources/soil-erosion/sesc-overview"),
            ("Michigan EGLE: Part 91 enforcing agencies", "https://www.michigan.gov/egle/about/organization/water-resources/soil-erosion/part-91-agencies"),
            ("Genesee County Road Commission: driveway permits", "https://gcrc.org/permits/driveway"),
            ("MDOT: building on a state highway", "https://www.michigan.gov/mdot/about/faqs/business/building-on-state-highway"),
            ("MISS DIG 811: frequently asked questions", "https://www.missdig811.org/get-started/i-want-to-dig/faq.html"),
        ],
    },
    {
        "slug": "custom-home-building-steps-michigan",
        "published": "2026-10-23", "updated": "2026-10-23",
        "title": "Building a Custom Home in Michigan: Step by Step | RBF",
        "h1": "Building a Custom Home in Michigan: Steps From Lot to Move-In",
        "desc": "The steps to build a custom home in Genesee, Oakland and Southeast Michigan: lot checks, design, permits, site work, construction, inspections and move-in.",
        "summary": "Check the lot first, then design and price the home, get permits, complete site work and the foundation, build and inspect the home, and finish with a certificate of occupancy.",
        "bg": "foundation-walls-excavation",
        "body": """<p class="tldr"><strong>Short answer:</strong> Building a custom home in Michigan follows the same order almost every time: <strong>check the lot</strong>, <strong>design and price</strong> the home, get <strong>permits</strong>, complete <strong>site work and the foundation</strong>, <strong>build</strong> the home with inspections along the way, then receive a <strong>certificate of occupancy</strong> and move in. Most surprises &mdash; and most extra cost &mdash; come from the lot, so check it before you buy.</p>
<h2>1. Check the Lot Before You Buy</h2>
<ul><li><strong>Zoning and setbacks:</strong> confirm a home of the size you want fits the lot.</li>
<li><strong>Water and sewer:</strong> if public utilities aren&rsquo;t available, the lot needs approval from the county health department for a well and septic system. Soils that don&rsquo;t pass a septic evaluation can limit or rule out a lot.</li>
<li><strong>Soils, slope and drainage:</strong> wet ground, high groundwater or steep grades add excavation, fill or drainage cost.</li>
<li><strong>Access and utilities:</strong> the driveway may need a road commission permit, and bringing electric and gas to a rural lot can be a real cost.</li>
<li><strong>Restrictions:</strong> subdivision covenants or association rules can set minimum home size, materials or style.</li></ul>
<h2>2. Design the Home and Set the Budget</h2>
<p>Work with an architect or designer, or through a design-build contractor, to develop floor plans and selections. Price the design as it develops so the plan stays in budget, and include the site work &mdash; excavation, utilities, driveway and grading &mdash; which is easy to underestimate. See <a href="/resources/design-build-vs-design-bid-build">design-build vs. design-bid-build</a>.</p>
<h2>3. Financing</h2>
<p>Most custom homes are financed with a construction loan that pays the builder in stages as work is completed and inspected. Lenders usually want final plans, a fixed contract price and a schedule.</p>
<h2>4. Permits</h2>
<p>The building permit comes from the city, township or village (or the county where it runs the building department). Expect separate permits for electrical, plumbing and mechanical work, plus a soil erosion permit when the earth disturbance is an acre or more or within 500 feet of a lake or stream. Michigan law also requires calling MISS DIG 811 at least three business days before digging.</p>
<h2>5. Site Work and Foundation</h2>
<p>The lot is cleared, the basement or foundation is excavated, footings and foundation walls are poured, and the well, septic or utility connections are installed. Good site work &mdash; correct elevations and drainage away from the house &mdash; prevents wet basements later. See <a href="/excavation-grading">excavation and grading</a>.</p>
<h2>6. Construction and Inspections</h2>
<p>Framing, roofing, windows, and rough plumbing, electrical and mechanical work come next, each inspected before walls are closed. Then insulation, drywall, cabinets, flooring, fixtures and finishes. Making selections early keeps long-lead items such as windows and cabinets from holding up the schedule.</p>
<h2>7. Final Inspection and Move-In</h2>
<p>After final inspections, the building department issues a certificate of occupancy. The driveway, final grading and seeding finish the site, and a walkthrough produces a punch list of final items before move-in.</p>
<h2>Questions to Ask a Custom Home Builder</h2>
<ul><li>Will you check the lot before I buy it?</li><li>Is site work included in your price, and who performs it?</li>
<li>Who supervises the job day to day?</li><li>How do you handle changes and allowances?</li><li>Do you pull the permits and schedule inspections?</li></ul>
<p>RBF Construction builds <a href="/custom-home-builder">custom homes and additions</a> across <a href="/genesee-county-general-contractor">Genesee County</a>, <a href="/oakland-county-general-contractor">Oakland County</a> and <a href="/service-areas">Southeast Michigan</a>, with its own crews handling the excavation and site work. <a href="/construction-contact#quote">Talk with RBF about your home</a>.</p>""",
        "sources": [
            ("Michigan EGLE: soil erosion and sedimentation control overview", "https://www.michigan.gov/egle/about/organization/water-resources/soil-erosion/sesc-overview"),
            ("MISS DIG 811: frequently asked questions", "https://www.missdig811.org/get-started/i-want-to-dig/faq.html"),
            ("Genesee County Road Commission: driveway permits", "https://gcrc.org/permits/driveway"),
        ],
    },
]


# --------------------------------------------------------------------------
# Project case studies. ONLY facts visible in RBF's own photos or stated on RBF's original
# website (its photo file names give the towns). Scope, dates, size and challenges are NOT
# published until RBF confirms them - add "scope", "year", "challenge" keys and rebuild.
# --------------------------------------------------------------------------
CASE_STUDIES = [
    {
        "slug": "commercial-renovation-before-after",
        "title": "Commercial Building Renovation: Before & After | RBF",
        "desc": "Before-and-after commercial renovation by RBF Construction: new stone and metal-panel facade, storefront awnings, and a repaved, restriped parking lot.",
        "name": "Commercial Building Renovation",
        "h1": "Commercial Building Renovation: Before &amp; After",
        "category": "Commercial renovation",
        "brand": None, "location": None,
        "hero": "commercial-renovation-after",
        "photos": [], "before_after": True,
        "summary": "An aging single-story commercial building with a failing, flooded parking lot transformed into modern, leasable retail space.",
        "observed": [
            "New stone veneer and metal-panel facade",
            "Black storefront awnings and new entry doors",
            "Parking lot repaved, replacing broken, ponding asphalt",
            "New stall striping and accessible parking",
        ],
        "story": """<p><strong>Before</strong> the renovation, this was a tired single-story strip building: mismatched facades, a dated canopy and a parking lot full of standing water and broken pavement. <strong>After</strong>, the same footprint is a clean, modern retail building &mdash; stone veneer and metal panel facade, uniform black awnings, new storefronts, and a freshly paved and striped parking lot.</p>
<p>Projects like this combine both sides of RBF&rsquo;s business: building renovation managed by our general contracting team, and the paving and drainage work our site division performs.</p>""",
        "services": ["/retail-construction", "/parking-lot-paving-concrete", "/commercial-general-contracting"],
    },
    {
        "slug": "jimmy-johns-pizza-hut-smoothie-king-retail-building",
        "title": "Multi-Tenant Restaurant Building | RBF Construction",
        "desc": "Multi-tenant restaurant building with Jimmy John's (drive-thru), Pizza Hut and Smoothie King storefronts, from RBF Construction's portfolio.",
        "name": "Multi-Tenant Restaurant Building",
        "h1": "Multi-Tenant Restaurant Building: Jimmy John&rsquo;s, Pizza Hut &amp; Smoothie King",
        "category": "Restaurant / multi-tenant retail",
        "brand": "Jimmy John's, Pizza Hut, Smoothie King", "location": None,
        "hero": "retail-plaza-jimmy-johns-pizza-hut-smoothie-king",
        "photos": ["retail-plaza-jimmy-johns-pizza-hut-smoothie-king"], "before_after": False,
        "summary": "A multi-tenant building housing three national quick-service brands side by side, including a Jimmy John's drive-thru.",
        "observed": [
            "Three national quick-service tenants under one roof",
            "Drive-thru at the Jimmy John's end-cap",
            "Stone veneer piers with masonry and metal-panel accents",
            "Separate storefront entry and signage for each tenant",
        ],
        "story": """<p>This building puts three national restaurant brands &mdash; <strong>Jimmy John&rsquo;s</strong>, <strong>Pizza Hut</strong> and <strong>Smoothie King</strong> &mdash; side by side, each with its own storefront and signage, and a drive-thru at the Jimmy John&rsquo;s end-cap.</p>
<p>Multi-tenant restaurant buildings require coordinating the building shell with each brand&rsquo;s own requirements for storefronts, signage, kitchens and drive-thru lanes &mdash; the coordination RBF&rsquo;s <a href="/restaurant-construction">restaurant construction</a> work is built around.</p>""",
        "services": ["/restaurant-construction", "/retail-construction", "/site-development"],
    },
    {
        "slug": "taco-bell-cass-city-mi",
        "title": "Taco Bell Restaurant, Cass City, MI | RBF Construction",
        "desc": "Taco Bell quick-service restaurant in Cass City, Michigan from RBF Construction's restaurant construction portfolio.",
        "name": "Taco Bell Restaurant, Cass City",
        "h1": "Taco Bell Restaurant &mdash; Cass City, Michigan",
        "category": "Restaurant (quick-service)",
        "brand": "Taco Bell", "location": "Cass City, MI",
        "hero": "taco-bell-cass-city-mi",
        "photos": ["taco-bell-cass-city-mi"], "before_after": False,
        "summary": "A freestanding Taco Bell quick-service restaurant in Cass City, Michigan, finished to the brand's current exterior design.",
        "observed": [
            "Freestanding quick-service restaurant",
            "Taco Bell's current exterior design, with tower element and purple accents",
            "Paved parking around the building",
        ],
        "story": """<p>RBF Construction&rsquo;s restaurant portfolio includes this <strong>Taco Bell</strong> in <strong>Cass City, Michigan</strong> &mdash; a freestanding quick-service building finished in the brand&rsquo;s current look, with its signature tower element and purple accent bands.</p>
<p>National restaurant brands bring detailed prototype drawings, finish standards and opening deadlines. RBF&rsquo;s approach to <a href="/restaurant-construction">restaurant construction</a> is to coordinate those standards, the kitchen infrastructure and the site work under one contractor.</p>""",
        "services": ["/restaurant-construction", "/site-development", "/parking-lot-paving-concrete"],
    },
    {
        "slug": "family-dollar-dollar-tree-olivet-mi",
        "title": "Family Dollar / Dollar Tree, Olivet, MI | RBF Construction",
        "desc": "Family Dollar / Dollar Tree combination store in Olivet, Michigan from RBF Construction's retail construction portfolio.",
        "name": "Family Dollar / Dollar Tree, Olivet",
        "h1": "Family Dollar / Dollar Tree &mdash; Olivet, Michigan",
        "category": "Retail",
        "brand": "Family Dollar / Dollar Tree", "location": "Olivet, MI",
        "hero": "family-dollar-dollar-tree-olivet-mi",
        "photos": ["family-dollar-dollar-tree-olivet-mi"], "before_after": False,
        "summary": "A Family Dollar / Dollar Tree combination store in Olivet, Michigan.",
        "observed": [
            "Combination Family Dollar / Dollar Tree store",
            "Arched entry tower with brand signage",
            "Storefront glass across the front of the building",
        ],
        "story": """<p>This <strong>Family Dollar / Dollar Tree</strong> combination store in <strong>Olivet, Michigan</strong> is part of RBF Construction&rsquo;s retail portfolio &mdash; a national discount brand with a defined storefront and signage standard.</p>
<p>See how RBF approaches <a href="/retail-construction">retail and commercial business construction</a>, from ground-up buildings to storefront renovations.</p>""",
        "services": ["/retail-construction", "/commercial-general-contracting"],
    },
    {
        "slug": "athletico-physical-therapy-shelby-mi",
        "title": "Athletico Physical Therapy, Shelby, MI | RBF Construction",
        "desc": "Athletico Physical Therapy clinic in Shelby, Michigan from RBF Construction's medical and commercial construction portfolio.",
        "name": "Athletico Physical Therapy, Shelby",
        "h1": "Athletico Physical Therapy Clinic &mdash; Shelby, Michigan",
        "category": "Medical / physical therapy",
        "brand": "Athletico Physical Therapy", "location": "Shelby, MI",
        "hero": "athletico-physical-therapy-shelby-mi",
        "photos": ["athletico-physical-therapy-shelby-mi"], "before_after": False,
        "summary": "An Athletico Physical Therapy clinic storefront in Shelby, Michigan.",
        "observed": [
            "Physical therapy clinic in a multi-tenant retail center",
            "Full-height storefront glass with signage and awning",
        ],
        "story": """<p>RBF Construction&rsquo;s healthcare work includes this <strong>Athletico Physical Therapy</strong> clinic in <strong>Shelby, Michigan</strong>, located in a multi-tenant retail center.</p>
<p>Physical therapy and medical clinics need accessible layouts, durable finishes and plumbing in treatment areas. Learn how RBF approaches <a href="/medical-office-construction">medical and clinic construction</a>.</p>""",
        "services": ["/medical-office-construction", "/office-building-construction"],
    },
    {
        "slug": "cottage-inn-pizza-davison-mi",
        "title": "Cottage Inn Pizza, Davison, MI | RBF Construction",
        "desc": "Cottage Inn Pizza restaurant in Davison, Genesee County, Michigan from RBF Construction's restaurant portfolio.",
        "name": "Cottage Inn Pizza, Davison",
        "h1": "Cottage Inn Pizza &mdash; Davison, Michigan",
        "category": "Restaurant",
        "brand": "Cottage Inn Pizza", "location": "Davison, MI",
        "hero": "cottage-inn-pizza-davison-mi",
        "photos": ["cottage-inn-pizza-davison-mi"], "before_after": False,
        "summary": "A Cottage Inn Pizza restaurant in Davison, in Genesee County, Michigan.",
        "observed": [
            "Restaurant in Davison, near RBF's Flint office",
            "Storefront entry with brand signage and blue awnings",
        ],
        "story": """<p>Close to RBF&rsquo;s Flint headquarters, this <strong>Cottage Inn Pizza</strong> in <strong>Davison</strong> is part of our restaurant portfolio in <a href="/genesee-county-general-contractor">Genesee County</a>.</p>
<p>From franchise build-outs to ground-up restaurants with drive-thrus, see how RBF approaches <a href="/restaurant-construction">restaurant construction</a>.</p>""",
        "services": ["/restaurant-construction", "/genesee-county-general-contractor"],
    },
]

# Southeast Michigan counties covered on the Service Areas page (no separate thin pages)
SE_MICHIGAN = {
    "Macomb County": ["Sterling Heights", "Warren", "Shelby Township", "Macomb Township", "Clinton Township", "Utica", "Washington Township", "Romeo"],
    "Wayne County": ["Detroit", "Livonia", "Dearborn", "Canton", "Plymouth", "Northville", "Westland"],
    "Washtenaw County": ["Ann Arbor", "Ypsilanti", "Saline", "Dexter", "Chelsea"],
}

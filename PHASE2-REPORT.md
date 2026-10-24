# RBF Construction: Phase 2 Completion Report

- **Staging:** https://hotpink-ant-873776.hostingersite.com (deployed from the `hostinger` branch)
- **Source:** https://github.com/asmith1636/RBF-Website (`main`)
- **Production (rbfconstruction.com):** not touched. No DNS changes and nothing published to production.

**[Verified]** means I tested it myself. **[Not verified]** means I couldn't test it, or it's a recommendation.

---

## 1. What was improved and why

| Area | Change | Why |
|---|---|---|
| Positioning | New homepage headline: "General Contractor & Site Developer in Flint, MI", under "Genesee, Oakland & Southeast Michigan". (The earlier "One Contractor. From Dirt to Done." slogan was removed at RBF's request.) A new six-step "How We Work" section shows which steps RBF crews do themselves and which RBF manages. | It's RBF's real advantage. None of the Flint competitors I reviewed lead with having both general contracting and site work in-house. |
| Credibility | Six project case studies, featured on the homepage, the Projects page and related service pages. | Commercial buyers look for proof. Before, the projects were only a photo gallery. |
| Local SEO | Titles and main headings now target "Flint, MI" and "Genesee County" for general contracting, commercial, restaurant, build-out, residential, excavation, site development and utilities. | These match the searches RBF wants to win. |
| Honesty | Removed claims I couldn't verify: "licensed trades", foundations as self-performed, "crews in deep trenches every day", and "ground-up" in the Taco Bell caption. | The brief says no invented facts. Inaccurate claims are also a legal and trust risk. |
| Staging safety | The staging domain now sends `X-Robots-Tag: noindex`, and every redirect stays on the domain the visitor is on. | Keeps the temporary domain from competing with rbfconstruction.com. Before this, the HTTPS redirect rule hard-coded the production domain, so it could have sent staging visitors there. |
| Thin pages | Macomb, Wayne and Washtenaw county pages were merged into a Southeast Michigan section on Service Areas, with 301 redirects. Lapeer and Livingston were expanded. | Thin county pages with no projects behind them can look like "doorway" pages to Google. |
| Leads | The bid form now asks who the visitor is, timeline, drawings status and a plans link. Links can preselect answers. Each submission records the page that sent the visitor and any ad-campaign tags. | Helps RBF qualify leads from franchise operators, developers, homeowners and general contractors needing site work. |
| Performance | Fonts are now hosted on the site instead of Google Fonts, and caching rules are longer. | Removes third-party requests that could block page display. |
| Accessibility | Orange label text on light backgrounds changed from 2.0:1 contrast to 5.6:1, and the blue badge text fixed. | Meets the WCAG AA contrast standard. |

## 2. Existing pages and components changed

- **Every page:**
  - Header: larger trimmed logo, larger menu text, tagline on wide screens.
  - The "Projects" menu item stays highlighted on case-study pages.
  - Fonts are now hosted on the site.
  - Analytics hook added.
- **Homepage:**
  - New hero headline and slide order (the Taco Bell photo first).
  - "How We Work" replaces the earthwork-services section and the 4-step process section.
  - Featured case-study cards replace the photo grid.
  - "Who We Are" rewritten.
  - New FAQ: "Does RBF do its own site work?"
- **Service pages:** new titles and headings for local search. Related case studies added. Lead call-out boxes on Restaurant, Site Development, Underground Utilities, Excavation and Residential.
- **Projects:** moved to `/projects/` (a folder, to avoid the Apache conflict that caused the Resources 403). Case studies added above the gallery.
- **Service Areas:** new "Across Southeast Michigan" section.
- **County pages:**
  - Genesee: copy toned down.
  - Lapeer: pole barn and I-69 sections added.
  - Livingston: pole barn section added.
- **Contact:** new form fields, link prefill, lead-source fields. The thank-you redirect stays on the current domain.
- **Resources:** heading structure fixed.
- **Copy edits:**
  - Kitchen page: "licensed trades" removed.
  - Custom homes and Residential: foundations no longer described as self-performed.
  - Underground utilities: trench claim toned down.

## 3. New pages and features

- `/projects/commercial-renovation-before-after`
- `/projects/jimmy-johns-pizza-hut-smoothie-king-retail-building`
- `/projects/taco-bell-cass-city-mi`
- `/projects/family-dollar-dollar-tree-olivet-mi`
- `/projects/athletico-physical-therapy-shelby-mi`
- `/projects/cottage-inn-pizza-davison-mi`
- Lead-event tracking: phone clicks, email clicks, bid-button clicks and form submissions are recorded, plus a "lead" event on the thank-you page.
- Ready-made link-prefill URLs for each audience, for example `/construction-contact?audience=franchise&type=restaurant#quote`.

## 4. Technical SEO

- **Structured data [Verified, parses on every page]:**
  - Business: GeneralContractor/LocalBusiness with address, coordinates, 9–5 hours, counties and cities served, the full service catalog, and FAQs.
  - Pages: Service, BreadcrumbList, Article and AboutPage.
  - Projects: CollectionPage, ImageGallery and ItemList.
  - Case studies: CreativeWork, with location where known.
- **Sitemap:** 41 addresses plus 41 project photos, and it matches every page's canonical tag [Verified]. Correction: the photo entries were not actually being written until the October 23 update (a path mismatch); an earlier version of this report wrongly listed them as verified.
- **robots.txt:** allows search and AI crawlers and lists the sitemap.
- **Server redirects, all to the same domain [Verified on staging]:**
  - HTTPS
  - www → apex (production only)
  - `/index.html` → `/`
  - `.html` → clean address
  - trailing slash removed
  - old county pages → `/service-areas`
  - real 404 for missing pages
- **Staging protection [Verified]:** `X-Robots-Tag: noindex, nofollow` on the staging domain. The rule only exempts `rbfconstruction.com` and `www.rbfconstruction.com`.
- **Images:** WebP, width and height set so the layout doesn't shift, lazy-loading below the fold, the first slide preloaded, smaller files for phones on large images.
- **Audit [Verified]:** 41 pages, 0 problems found in:
  - title and description lengths, duplicate titles and descriptions
  - single main heading, heading order
  - image alt text
  - broken internal links, missing images
  - canonical vs. sitemap

## 5. Changes aimed at AI search (GEO)

- **Guides (October 23):** three new guides answer common questions:
  - `/resources/pole-barn-permits-michigan`: when a pole barn needs a permit, and the farm-building exemption
  - `/resources/commercial-construction-permits-genesee-county`: site plan, soil erosion, driveway, utility and building approvals
  - `/resources/custom-home-building-steps-michigan`: lot checks through move-in
- Each guide names state rules only where I checked them against official or primary sources, and lists those sources. They include no RBF prices, timelines or project claims.
- Every guide now shows a fixed published and updated date, a byline linked to the About page, and an "About This Guide" box. Before, the date changed every time the site was rebuilt, which misstated when guides were updated.

- `llms.txt` now includes:
  - which work RBF self-performs and which it coordinates
  - every case study with its facts
  - the Southeast Michigan counties
  - the 9–5 hours
- The same business facts appear identically in page text, structured data and `llms.txt`.
- An FAQ answer states plainly which work is self-performed and which is managed.
- Case studies give AI tools specific, checkable facts: brand, town, building type.
- **I can't guarantee placement in AI answers.** These changes make RBF easier to understand and cite; they don't ensure it.

## 6. Visual and mobile

- Larger, sharper logo and larger menu text.
- Hero opens on the strongest commercial photo, with a two-level headline.
- "How We Work" sequence with badges showing who does each step.
- Case-study cards with hover effects, a project-facts box, and in-page lead call-outs.
- **[Verified]** Header at 1070, 1240/1250, 1280, 1366, 1440, 1536 and 1920 px wide: no wrapped menu labels, no sideways scroll.
- **[Verified]** Phone layout at 390 px wide (homepage, county page, case study).
- **[Verified]** Phone menu opens with the full menu structure.

## 7. Test results

**[Verified on staging]**
- Server response about 235 ms, Brotli compression.
- Homepage: 11 requests, 142 KB, zero third-party requests, fully loaded at 947 ms, layout shift (CLS) 0.007.
- Before Phase 2: 381 KB and 1,150 ms load, with Google Fonts and Maps requests.

**[Verified in the browser]**
- Slideshow arrows, dots and captions work.
- Gallery filters and photo viewer work.
- Form prefill works: the franchise link selects "franchise" and "restaurant"; the general-contractor link selects "gc" and "site".
- Lead-source fields fill in, including the page that opened the form.
- The thank-you redirect follows the current domain.
- Required fields block empty submissions.
- Phone clicks are recorded as events.

**[Not verified]**
- **Paint timing (LCP):** not measured. The browser in this environment didn't report paint events, and I don't have Lighthouse here. Run PageSpeed Insights on the staging address.
- **Form submission:** not sent. It would email info@rbfconstruction.com, and the first submission sends FormSubmit's activation email. Someone at RBF should send one test and click the activation link.
- **Production behavior:** the noindex exemption and www → apex redirect can't be tested until the domain is attached.
- **Search rankings:** I couldn't check Google rankings from here. The competitor notes below compare websites, not rankings.

## 8. What RBF needs to provide

1. **Confirm each case study:**
   - RBF's exact scope (general contractor, site work only, or both)
   - year completed, building size
   - one challenge and how it was solved
   - the towns taken from the old site's file names: Cass City, Olivet, Shelby, Davison
   - the location of the multi-tenant building and the renovation
2. **Credibility details competitors have and RBF doesn't:** "Licensed & insured" is now shown, taken from RBF's own van. Still needed: the license number to display, year founded, owner and leadership names and bios, Michigan builder license number, insurance and bonding, memberships, and 3–5 customer testimonials with permission.
3. **Confirm the self-performed list:** excavation, grading, utilities, paving and concrete flatwork. Do RBF crews also do foundations, framing or anything else?
4. **Photos still needed:** pole barns, finished homes (exteriors) and medical interiors. **Townhomes:** at RBF's request the site now uses the Google Street View townhomes image, credited "Imagery © Google". Google restricts commercial use of Street View imagery, so replace it with an RBF photo before production launch.
5. **Brand logos:** confirm RBF is comfortable showing client logos (they were already on the old site).
6. **Google Analytics 4 measurement ID**, plus access to Search Console and Bing Webmaster Tools.
7. **Guides:** have someone at RBF read the three new guides. Adding RBF's typical timelines, or the owner's name as the author or reviewer, would make them stronger.
8. **Production launch approval:** attach rbfconstruction.com to the Hostinger plan running staging. Canonical addresses use `https://rbfconstruction.com` without "www", matching how the old site redirects.

## 9. After launch: how to improve Google rankings

1. **Google Business Profile** (the biggest local factor):
   - Primary category "General contractor", plus Excavating and Site development.
   - Every service listed, hours set to 9–5, the project photos uploaded.
   - A steady flow of reviews. It has 4 today.
2. **Search Console:** submit the sitemap and request indexing for the homepage, service pages and case studies.
3. **Bing Webmaster Tools:** submit the sitemap too. Bing powers ChatGPT search and Copilot.
4. **Consistent listings:** the same name, address and phone on Bing Places, Apple Business Connect, BBB, Houzz, Angi, the Flint & Genesee Chamber, and builder or contractor associations.
5. **Links from real relationships:** ask franchise brands, developers and suppliers to list RBF as their contractor; join local associations.
6. **One new case study per month,** with scope, photos and town. This is the most effective ongoing content.
7. **Lead tracking:** connect the events to GA4 and mark `generate_lead` as a conversion.

## Competitor notes (website comparison, not rankings)

- **E&L Construction Group (Flint, since 1953):** large commercial and industrial firm with projects from $100K to over $30M. Its site blocked automated review. [Siteline](https://siteline.com/general-contractor/city/flint-michigan), [The Blue Book](https://www.thebluebook.com/michigan/articles/a-shining-success-in-flint.html)
- **Siwek Construction (Flint, since 1998):** design-build, PEMB (pre-engineered metal buildings) and industry pages, a team page and a portfolio. Basic auto-generated structured data, no residential work, no site-work emphasis. [siwekcc.com](https://siwekcc.com/)
- **Swank Builders (Goodrich/Flint, since 1996):** residential builder and remodeler. I couldn't find an official website in search results. [BuildZoom](https://www.buildzoom.com/contractor/swank-builders-inc-mi)
- **Excavators** (Eagle Excavation, L. Zellar & Sons and others): site work only. Eagle's site has no structured data and no meta description.
- **"B.G. White":** no Flint company by that name found. The closest match is White Construction (Detroit). [Chicago Defender](https://chicagodefender.com/w-bernard-white-constructing-visions-and-dreams)
- **RBF's opening:** the only one of these to combine general contracting and in-house site work, with restaurant and franchise experience. **Gaps:** years in business, team, testimonials (see section 8).

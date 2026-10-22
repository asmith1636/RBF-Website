# RBF Construction website (rbfconstruction.com)

A static site: fast, works on any host, and has no monthly builder fee.

- `site/`: the finished website. Upload the **contents** of this folder to your web host.
- `content.py`: the text for the service pages, county pages and guide articles. Edit it, then run `python build.py`.
- `build.py`: generates every page, the menus, the search-engine data, the sitemap and `llms.txt`. Business facts (phone, address, hours) are at the top.
- `python build.py --serve`: shows a local preview at http://localhost:8000.
- `originals/`: the original photos downloaded from the old site, kept as a backup.

## Pages (33 indexed)

- **Hubs:** Home, General Contracting, Residential, Commercial, Site Work
- **Residential:** Kitchen Remodeling, Bathroom Remodeling, Custom Homes & Additions
- **Commercial:** Office Buildings, Restaurants, Medical & Dental, Retail & Businesses
- **Site work:** Excavation & Grading, Underground Utilities, Parking Lots/Roads/Concrete, Demolition
- **Service areas:** a hub page plus Oakland (the most detailed), Genesee, Livingston, Macomb, Wayne, Lapeer and Washtenaw counties
- **Resources:** design-build vs. design-bid-build; kitchen and bath remodel planning; commercial site work
- **Other:** Projects, Contact, Careers, Subcontractor Bid List, Privacy Policy

## Before launch: confirm with the owner

1. **Counties and cities** (`COUNTIES` in content.py). Remove any communities RBF doesn't want to target, and add any that are missing.
2. **Photos needed.** There are no kitchen, bathroom or medical project photos yet, so those pages use a plain navy header. Adding real photos of those projects will help both rankings and conversions.
3. **County project examples.** The Lapeer, Macomb, Wayne and Washtenaw pages are shorter. Adding a real project from each county with photos makes them much stronger.
4. **Careers positions dropdown.** The list is: Laborer, Operator, Pipe layer, Concrete, CDL driver, Foreman, PM/Estimator. Adjust it to match the roles RBF hires for.
5. **Forms.** The forms send to info@rbfconstruction.com through FormSubmit.co, which is free and needs no account. The first time a form is submitted, FormSubmit emails info@ an activation link, and someone must click it. To use something else, change `FORM_ACTION` in build.py. Alternatives are Formspree, Web3Forms, or Netlify Forms if you host on Netlify.
6. Worth adding if true, because they build trust with Google and AI tools: year founded, the owner's name and bio, license number, insured/bonded status, association memberships, and real customer reviews or testimonials. I didn't make any of these up.

## Launch steps

1. Choose a host:
   - **Hostinger web hosting** (not the Website Builder): upload `site/` to `public_html`. The `.htaccess` file handles clean URLs, HTTPS, the redirect to the non-www address, and caching.
   - **Vercel**: `vercel.json` is included.
   - **Netlify**: `_redirects` is included.
   - **Cloudflare Pages**: works as-is.
2. Point the domain at the new host.
3. Every old URL is kept the same (`/general-contracting`, `/site-development`, `/construction-contact` and so on), so existing Google rankings carry over. No redirects are needed.
4. In **Google Search Console**: verify the domain, submit `https://rbfconstruction.com/sitemap.xml`, and request indexing for the homepage.
5. In **Bing Webmaster Tools**: import the site from Search Console. Bing powers ChatGPT search and Copilot.
6. Test with Google's Rich Results Test: https://search.google.com/test/rich-results

## Off-site work that matters most for local SEO and GEO

AI assistants and Google's local results trust what *other* sites say about a business. A web search right now finds almost nothing about RBF, and that is the biggest gap.

- **Google Business Profile** (one already exists, rated 5.0 from 4 reviews):
  - Set the category to "General contractor", with secondary categories "Excavating contractor" and "Site development".
  - Add every service, upload these same project photos, and set the website link to the homepage.
  - Ask past clients for reviews. Reaching 15–25 reviews makes a big difference.
- **Consistent listings (NAP).** Use exactly "RBF Construction, Inc. · 1411 W Hill Rd, Flint, MI 48507 · (810) 938-8498" everywhere: Bing Places, Apple Business Connect, Yelp, BBB, Angi, Houzz, the Flint & Genesee Chamber, and builder associations such as the Home Builders Association of Greater Flint and ABC/AGC Michigan.
- **Facebook page.** Make sure it uses the same name, address, phone and website.
- **Project write-ups.** Over time, add one page per notable project with the city, scope, size and timeline, for example "Retail building – Grand Blanc, MI". Each page becomes a new search entry point and something AI tools can cite.

## What's built in

- **Search engine basics:**
  - A unique title, description, canonical URL and single H1 on every page.
  - Descriptive image filenames and alt text, an XML sitemap that includes images, and robots.txt.
  - Open Graph and Twitter share cards, and geo meta tags.
- **Structured data (JSON-LD)** on every page:
  - GeneralContractor/LocalBusiness with address, coordinates, hours, service area and services.
  - WebSite, WebPage and BreadcrumbList.
  - Service on each service page, FAQPage on the home and service pages, ContactPage, and an ImageGallery on Projects.
- **AI search (GEO):**
  - `llms.txt` gives a plain-text fact sheet for AI assistants.
  - robots.txt explicitly allows GPTBot, ClaudeBot, PerplexityBot, Google-Extended and similar crawlers.
  - Clear answer-style FAQs, and the same business facts stated identically across the site.
- **Speed:**
  - Images converted to WebP (about 13 MB of originals down to about 2 MB) and lazy-loaded with fixed dimensions so the layout doesn't jump.
  - About 3 KB of JavaScript, no frameworks, and automatic cache-busting on the CSS and JS files.
- **Conversion:**
  - A "Request a Bid" button in the header.
  - Click-to-call buttons and a sticky Call/Get-a-Bid bar on phones.
  - A before/after slider, a project gallery with a full-size photo viewer, and a map.

---
name: schema.md
description: Generate a complete, valid enterprise JSON-LD @graph for a couplesrehab.com page (couples detox/rehab, withdrawal, insurance, geo, emergency pages). Use whenever the user provides a page URL/topic/title/meta/H1 and asks for schema, JSON-LD, or structured data. Output is one ready-to-paste <script> tag, Google-valid, with stable @IDs. Pairs with rehab-content-skill.md and rehab-url-map.md.
---

# Rehab Schema Skill (couplesrehab.com)

## Output rule
Output **one valid JSON-LD `<script type="application/ld+json">` block only** — no prose before or after. Single `@graph` array.

## Inputs needed (collect or infer)
Full page URL, page topic, SEO title, meta description, H1, primary + secondary keyword, page type (from rehab-url-map.md), datePublished/dateModified, approx word count, breadcrumb pillar.

## Business typing — the E-E-A-T decision (locked)
Use the **hybrid**: `Organization` + `MedicalOrganization`, joined by shared @IDs. **Do NOT include `LocalBusiness`** — the brand is a national referral network with no public storefront/address; a LocalBusiness with no real address is a spam signal that risks the markup being ignored on a YMYL site.

`MedicalOrganization` carries topical authority via `knowsAbout` — it is positioned as a referral/information network, **not** a treatment provider. Never imply the site delivers care directly. (`Article.author`/`publisher` = Organization. Named reviewer omitted by current choice — see note.)

> Ranking note to surface to the user when relevant: a named credentialed medical reviewer (Person → `reviewedBy`) is a strong YMYL trust signal and the live pages display one. Omitting it from schema leaves a ranking lever unused; easy to add later.

## Validity rules (prevent Rich Results errors)
- `medicalSpecialty` must use real schema.org `MedicalSpecialty` enum values. **Valid:** `Psychiatric`. Do NOT use "AddictionMedicine", "MentalHealth", "BehavioralHealth", "AddictionMedicine" — not in the enum; they throw warnings. Put those concepts in `knowsAbout` (free text) instead.
- No `aggregateRating`, `review`, or `Review` nodes — no review data exists; fabricating it is a policy violation.
- No recovery guarantees, no diagnosis language anywhere in text values.
- Avoid `Offer`/`price` on the Service node (a price:0 on treatment-adjacent service reads as "free treatment"). Describe the service without a priced Offer.
- FAQ answers: medically cautious, encourage emergency care where relevant, no diagnosis.
- All URLs absolute and real; only link pages that exist (cross-check rehab-url-map.md).
- `inLanguage`: "en-US". Phone: "+1-888-500-2110".

## FAQ rich-result caveat (set expectations)
Google restricts FAQ rich results to recognized authoritative health/gov sites (since 2023). Keep FAQPage markup regardless — Bing and AI engines (ChatGPT/Gemini/Perplexity) still parse it, and the site may qualify as health-authority — but don't promise FAQ star features in the SERP.

## Stable @IDs (site-level constant, page-level templated)
Site: `#organization`, `#medicalorganization`, `#website`, `#place`, `#contact`
Page: `{URL}#webpage`, `{URL}#article`, `{URL}#faq`, `{URL}#service`, `{URL}#breadcrumb`, `{URL}#terms`
Topic Things: `{URL}#primary-topic`, plus `#medical-detox`, `#addiction-treatment`, `#couples-rehab`, `#withdrawal`, `#behavioral-health` (customize to page).

## @graph node checklist
1. **Organization** `#organization` — name, url, telephone, logo (ImageObject), contactPoint ref, sameAs (real profiles only — omit placeholders if unknown).
2. **MedicalOrganization** `#medicalorganization` — referral/info network; `medicalSpecialty: ["Psychiatric"]`; `knowsAbout: [...]` full topic list; `areaServed` US; do not mark as treatment provider.
3. **ContactPoint** `#contact` — telephone, contactType "customer service", areaServed US, availableLanguage English.
4. **Place** `#place` — PostalAddress with addressCountry US only (no fake street/geo).
5. **WebSite** `#website` — publisher → Organization; SearchAction potentialAction.
6. **WebPage** `{URL}#webpage` — isPartOf website; publisher → Organization; about → #primary-topic; mainEntity → article/faq/service; mentions → topic Things; significantLink → real internal links from the map; inLanguage.
7. **Article** `{URL}#article` — headline (H1), description (meta), author + publisher → Organization, mainEntityOfPage → webpage, datePublished/dateModified, articleSection, keywords, wordCount, inLanguage.
8. **Service** `{URL}#service` — page-specific name (detox→"Medical Detox Placement & Withdrawal Guidance"; couples→"Couples Addiction Treatment Navigation"; withdrawal→"Withdrawal Education & Detox Guidance"; insurance→"Insurance Verification & Treatment Navigation"); provider → MedicalOrganization; areaServed US; audience; serviceOutput list; NO priced Offer.
9. **BreadcrumbList** `{URL}#breadcrumb` — Home › [pillar by page type: Couples Detox Programs / Couples Residential Rehab / Insurance Coverage / Care Paths] › [Page]. Use real pillar URLs from the map.
10. **FAQPage** `{URL}#faq` — 8–12 Question/acceptedAnswer pairs, pulled from the page's actual FAQ; medically cautious.
11. **DefinedTermSet** `{URL}#terms` + **DefinedTerm** children — the page's clinical entities (medical detox, withdrawal, dual diagnosis, MAT, CIWA-Ar, COWS, etc.) as a glossary set.
12. **Thing** entities — `#primary-topic` + the mentioned topic Things, each with name + description, referenced by WebPage about/mentions.

## Cross-checks before output
- Page type matches breadcrumb pillar and Service name.
- Every significantLink/breadcrumb URL exists in rehab-url-map.md.
- No LocalBusiness, no ratings, no priced treatment offer, no invalid medicalSpecialty.
- Dates, word count, keywords filled (not left as placeholders).
- Valid JSON (no trailing commas), single graph, single script tag.

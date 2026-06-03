# Couples Rehab — Claude Code Instructions

## Project overview

This repo powers content operations for [couplesrehab.com](https://couplesrehab.com) — a national addiction treatment placement and referral network specializing in couples detox, couples rehab, medical detox, withdrawal care, dual diagnosis, insurance-supported treatment, and emergency placement. The site runs on WordPress.

All content targets people in crisis: panicking spouses/parents, couples deciding to get help together, someone in active withdrawal, and high-intent searchers who need help today. Every article is written for one conversion goal — phone calls to **(888) 500-2110** — with the Couples Assessment as the secondary CTA.

**Positioning guardrail (non-negotiable):** Couples Rehab is a placement/referral network, **not a treatment facility**. The active voice ("we verify benefits," "we coordinate admission," "available 24/7") is defensible only when paired with that disclosure and with no guarantees on coverage or joint placement. This framing must hold across every article and the schema.

Canonical model page for structure, depth, and voice: `https://couplesrehab.com/couples-detox-rhode-island/`.

---

## Environment

WordPress credentials are loaded automatically from `.env` at session start via the SessionStart hook. They are available as environment variables:

- `WP_USERNAME` — WordPress admin username
- `WP_APP_PASSWORD` — WordPress application password
- `WP_API_ENDPOINT` — `https://couplesrehab.com/wp-json/wp/v2/posts`  *(confirm — WP default assumed)*

If credentials are missing, run the session-start hook manually:
```bash
CLAUDE_CODE_REMOTE=true CLAUDE_PROJECT_DIR=$(pwd) CLAUDE_ENV_FILE=/tmp/claude-env bash .claude/hooks/session-start.sh
```

---

## Available skills

Three custom skills are installed automatically at session start:

| Skill | Purpose |
|---|---|
| `/rehab-url-map` | Canonical URL map — 180 slugs across 7 clusters (withdrawal/detox education, emergency intent, insurance, couples, SoCal geo, national couples geo, relationship/recovery education). Always pull slugs, page type, parent pillar, geo, keyword, and CTA mode from here. |
| `/rehab-content` | Full article engine — deep-clinical 4,000–6,000+ words, 3 embedded CTA boxes (top/middle/end), 15–25 FAQs, comparison table, crisis blockquotes, medically-reviewed byline, trusted-sources list, editorial disclaimer. |
| `/rehab-schema` | Generates the JSON-LD `<script>` block. Requires the article content as input. |

---

## Full content + posting routine

Follow these steps in order every time a new draft is created.

### Step 1 — Pick a slug with `/rehab-url-map`

Invoke `/rehab-url-map` to review the canonical page map. Either:
- Pick an existing slug that hasn't been built yet, or
- Identify the right cluster and mint a new slug following that cluster's naming convention

The map gives the slug its **page type** (education / emergency-intent / insurance / geo / couples / comparison), **cluster + parent pillar** (drives internal linking), **geo**, **target keyword**, and **CTA mode** (call-primary or assessment-primary). The slug drives the page URL and all internal linking. Never invent a slug without checking here first.

### Step 2 — Write the article with `/rehab-content`

Invoke `/rehab-content` with the chosen slug/topic. The skill will produce:

- Deep-clinical 4,000–6,000+ word article in WordPress Gutenberg block HTML (emergency-intent pages run shorter — see map)
- Clinical depth to match the RI page: named assessment scales (CIWA-Ar, COWS), hour/day withdrawal timelines, specific medication classes, substance-by-substance danger gradients
- 3 embedded CTA boxes, contextually rewritten per page (Box 1 dark navy hero + phone; Box 2 white clinical-assessment card + pillar/insurance links; Box 3 light continuum card + next-stage link)
- Medically-reviewed byline + top and closing crisis blockquotes (911 / 988 / state crisis line + 888 number)
- 15–25 FAQ entries formatted for AI Overview extraction
- At least one comparison table (inpatient vs outpatient, or detox vs rehab)
- Internal links using only confirmed slugs from `/rehab-url-map` (up to parent pillar, sideways to cluster siblings + neighboring geo, plus assessment + crisis support)
- External links to authoritative sources only: SAMHSA, NIDA, CDC, NIH, NIAAA, state behavioral-health department, 988 Lifeline
- Editorial disclaimer ("placement/referral network, not a treatment facility") + full deliverables block at the end (SEO title, meta, slug, H1, internal link map, etc.)

**Before moving to Step 3:** Verify every link in the article — internal and external — returns a valid response. Confirm no `[BRACKETED PLACEHOLDER]` text survives in the CTA boxes (topic, geo, headlines, hrefs all customized to this page). Do not skip this check.

### Step 3 — Generate schema with `/rehab-schema`

Invoke `/rehab-schema` and pass:
1. The full page URL (`https://couplesrehab.com/<slug>/`)
2. The complete article content from Step 2

The skill outputs a single `<script type="application/ld+json">` block — ready to paste into WordPress as a Custom HTML block at the bottom of the post content.

The schema includes: `Organization`, `MedicalOrganization` (referral/info network, **not** treatment provider; `knowsAbout` topics, `medicalSpecialty: ["Psychiatric"]` only — no invalid enum values), `ContactPoint`, `Place` (country-only), `WebSite`, `WebPage`, `Article`, `FAQPage`, `Service` (no priced Offer), `BreadcrumbList`, `DefinedTermSet`, and relevant `DefinedTerm` / `Thing` entities for the page's cluster.

**Do NOT include `LocalBusiness`** — no public storefront/address; it's a spam signal on a YMYL site. No `aggregateRating` or review nodes.

**The schema skill will refuse to generate if:**
- No FAQ section exists in the article
- Any link hasn't been verified against `references/valid-links.md`

### Step 4 — Final link check

Before posting, confirm:
- [ ] All internal links resolve to real couplesrehab.com pages (use the valid-links list in `.claude/skills/rehab-schema/references/valid-links.md`)
- [ ] All external links return HTTP 200
- [ ] No bracketed placeholder text survives in the CTAs (`[EMOTIONAL HOOK HEADLINE]`, `[CLUSTER PILLAR URL]`, `[NEXT-STAGE URL]`, etc.)
- [ ] Phone links point to `tel:8885002110` (displayed "(888) 500-2110") — do NOT replicate the live RI page bug where the closing link targets a different number
- [ ] Schema JSON is valid (no trailing commas, all brackets matched)

### Step 5 — Post to WordPress

Post the draft using the WordPress REST API:

```bash
python3 post_draft.py
```

The script reads credentials from `.env`, posts to `https://couplesrehab.com/wp-json/wp/v2/posts` with `status: draft`, and prints the post ID and preview URL on success.

**The content field must include:**
1. The full Gutenberg block HTML from Step 2 (with the 3 CTA boxes already embedded)
2. The `<script type="application/ld+json">` block from Step 3 appended as a `<!-- wp:html -->` block at the bottom

**On success:** Log the post ID. The draft is live in WordPress and ready for review before publishing.

---

## Content standards

- Voice: senior addiction-medicine-literate placement specialist speaking to a panicking partner — specific, calm, clinically credible, never sensational
- Active placement-network voice ("we verify benefits," "we coordinate admission," "24/7") — always paired with the "not a treatment facility" disclosure
- Every section opens with a 2–3 sentence direct answer (AI Overview ready)
- Deep clinical register required — named scales, timelines, medications, substance-specific danger gradients (see `/rehab-content`)
- No unsupported guarantees, no "best" or "top rated" as ranked claims, no recovery/outcome promises
- Medical framing: "can," "may," "in many cases," "depending on the facility/plan" — never "will" or "guaranteed"
- Coverage + joint placement always framed as verified/assessed, never guaranteed ahead of time
- 911 / 988 callouts wherever overdose or severe withdrawal is discussed
- Word count: 4,000–6,000+ words per geo/pillar article (emergency-intent pages shorter)
- CTAs: 3 per article, all contextually rewritten — no generic copy, no surviving placeholders

## NAP / brand constants (never change)

- **Name:** Couples Rehab (Couples Rehab Centers)
- **Phone:** (888) 500-2110 / `+1-888-500-2110` / `tel:8885002110`
- **Contact URL:** `https://couplesrehab.com/contact/`
- **Assessment URL:** `https://couplesrehab.com/couples-assessment/`
- **Crisis URL:** `https://couplesrehab.com/crisis-support/`
- **API endpoint:** `https://couplesrehab.com/wp-json/wp/v2/posts`  *(confirm)*
- **Address:** *(none confirmed — site is a national referral network with no public street address. Do NOT invent one. If a verified mailing address exists, add it here; otherwise schema uses country-only Place.)*

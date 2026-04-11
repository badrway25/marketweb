# Content Guidelines

## Core Principles

1. **No lorem ipsum. Ever.** All text must be realistic, business-specific, and professionally written.
2. **No repetitive copy.** Each template must have distinct messaging, tone, and content direction.
3. **Conversion-oriented.** Copy should include clear CTAs, value propositions, and trust signals.
4. **Multilingual-ready.** Content should be translatable without cultural awkwardness.

## Writing Style by Category

### Agency
- Confident, forward-looking tone
- Emphasize innovation, results, creativity
- Use metrics and case study language ("200+ brands launched")

### Business / Corporate
- Professional, trustworthy tone
- Emphasize reliability, expertise, tradition
- Industry-appropriate terminology

### Restaurant
- Warm, inviting, sensory language
- Emphasize ingredients, atmosphere, tradition/innovation
- Menu descriptions should feel appetizing

### Medical
- Reassuring, authoritative, empathetic tone
- Emphasize patient care, expertise, modern equipment
- Avoid clinical coldness

### Lawyer
- Authoritative, precise, confident
- Emphasize experience, case success, client advocacy
- Avoid aggressive language

### Real Estate
- Aspirational, descriptive, trustworthy
- Emphasize local knowledge, property features, lifestyle
- Use specific (fictional) neighborhood/area names

### Portfolio
- Personal, creative, authentic
- Let work speak — minimal but impactful copy
- Emphasize process, craft, collaboration

### eCommerce
- Product-focused, persuasive, clear
- Emphasize quality, value, convenience
- Include social proof language (reviews, ratings)

## Template Brand Identity Rules

Each template needs a complete brand profile documented in TEMPLATE_REGISTRY.json:

- **Brand name:** Unique, memorable, category-appropriate
- **Tagline:** One-line value proposition
- **Color palette:** Primary, secondary, accent colors (hex values)
- **Typography direction:** Font pairing intent (e.g., "modern sans + elegant serif")
- **Visual personality:** 2-3 adjectives (e.g., "minimal, bold, tech-forward")
- **Imagery direction:** Photo style guidance (e.g., "warm lifestyle photography, natural lighting")
- **Content tone:** Writing voice description

## Multilingual Notes

- Italian: formal "Lei" register for business, "tu" for creative/casual brands
- English: standard professional American English
- French: formal "vous" register
- Arabic: Modern Standard Arabic, RTL layout considerations, right-aligned text

## Inner Pages Law (Session 20 — D-053)

Binding global standard. A template may only be `published_live` when **every** page kind in its category's baseline has a complete, category-appropriate content block in `apps/catalog/template_content.py`. Stub content, placeholder copy, "coming soon" notes, and single-line descriptions are NOT acceptable. The source of truth for this rule is `DECISIONS.md` → **D-053 — Live Preview Law**. This section is a pointer; see `CATEGORY_ROADMAP.md` → "Baseline live pages per category" for the minimum page set per category.

### Writing rules for inner pages

1. **No lorem ipsum** (already stated above, re-emphasized — it applies to every inner page, not just the home page).
2. **Category-native voice** — an `about` page for a medical clinic is not an `about` page for a lawyer with words replaced. The tone, the narrative structure, the inclusion of personal stories vs credentials vs process vs case outcomes all differ per category per D-054 inner-pages rule.
3. **No cloned paragraphs between sibling templates** — if two sibling templates in the same category say almost the same thing on their `about` page, the D-054 Premium Differentiation Law is violated (see BRAND_SYSTEM_GUIDELINES.md → Premium Differentiation Law). The remediation is to rewrite, not to paraphrase.
4. **Real structural detail** — a `services` page for a medical clinic must list actual procedure names, prep instructions, expected durations, and prerequisites. A `menu` page must list real dish names with ingredients. A `case_studies` page must list real project outlines with problem / approach / result. A buyer who reads the inner pages decides "this template knows my business" or "this template is a wireframe" — the difference is realistic editorial detail.
5. **Complete forms** — `contact`, `appointment`, `reservations`, `case_study_request`, `series_brief` forms must list real field labels, real placeholders, real select options where applicable (e.g. medical specialty, session type, party size, budget range). No "Field 1 / Field 2" stubs.
6. **Consistent chrome** — the inner pages must share the same navbar, footer, palette, typography, imagery direction, and macro tone as the home page. A dark editorial home with a cream wireframe `about` is a broken product.

### Companion laws

- **D-053 Live Preview Law** — gates the publication tier and is the reason this law exists.
- **D-054 Premium Differentiation Law** — extends the 10 differentiation gates to inner pages, not just homepages.
- **D-047 Chrome-Authoring Contract** — every string in a per-archetype skin must come from a content registry field, a CSS rule, a generic label, or a `{% for %}` loop item. Inner pages are under D-047 jurisdiction.
- **CATEGORY_ROADMAP.md → "Baseline live pages per category"** — the minimum page set per category is enumerated there; authors should consult it before starting a content registry block.

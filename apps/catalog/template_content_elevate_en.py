"""Elevate — Startup SaaS Landing Kit · English content tree.

Mirrors the shape of ``ELEVATE_CONTENT_IT`` exactly — same keys, nesting
and list shapes. Authored for the Elevate live i18n rollout of the
startup-saas-landing archetype. Anglo-American SaaS / growth-tech
register — direct, punchy, second-person ("you"). Reference voice:
Linear / Figma marketing, ProductHunt launch posts, IndieHackers
transparency posts. NEVER collapses into Pragma's sober institutional
advisory voice.
"""
from __future__ import annotations

from typing import Any


ELEVATE_CONTENT_EN: dict[str, Any] = {
    "pages": [
        {"slug": "home",       "label": "Home",        "kind": "home"},
        {"slug": "prodotto",   "label": "Product",     "kind": "product"},
        {"slug": "prezzi",     "label": "Pricing",     "kind": "pricing"},
        {"slug": "demo",       "label": "Demo",        "kind": "demo"},
        {"slug": "contatti",   "label": "Contact",     "kind": "contact"},
    ],

    # Site-wide chrome
    "site": {
        "logo_initial": "E",
        "logo_word":    "Elevate",
        "tag":          "Conversion-first kit · for founders who ship",
        # Pill nav CTA label — short, action-oriented, distinct from `tag`
        # (which is the long-form description). Lifted from skin Session 40.
        "nav_cta":      "Start free",
        "phone":        "hello@elevatekit.io",
        "email":        "hello@elevatekit.io",
        "address":      "Talent Garden Calabiana · Milan",
        "hours_compact":"Async-first · Slack 9-19 CET",
        "hours_footer_rows": [
            "Demo on-demand · every Tuesday 17:00 CET",
            "Founder office hours · Friday 11:00 CET",
        ],
        "license":      "",
        "footer_intro":
            "Elevate is the GTM kit that takes your startup from "
            "waitlist to first MRR in fourteen days. Built for founders, "
            "by founders. Shipped from Milan, deployed anywhere.",
        "foot_studio":   "The product",
        "foot_pages":    "Navigate",
        "foot_contact":  "Talk to us",
        "foot_offices":  "Ship log",
        # Footer tertiary column — last 3 ship-log entries (different per Pragma)
        "shiplog_footer_rows": [
            "v2.9 · Friday · drag-and-drop hero builder",
            "v2.8 · yesterday · premium testimonial library",
            "v2.7 · Tuesday · GrowthBook A/B testing built in",
        ],
    },

    # ─── HOME ───────────────────────────────────────────────────
    "home": {
        # Top launch banner above the floating pill nav
        "banner_label":   "Series A · Q2 2026",
        "banner_text":    "We're closing the first fifty early-access seats",
        "banner_href":    "demo",

        "eyebrow":     "Conversion-first GTM kit · for early-stage SaaS & startups",
        "headline":    "From <em>waitlist</em> to first <em>MRR</em> in fourteen days.",
        "intro":
            "Elevate is the landing, pricing and onboarding kit that turns "
            "your first visitors into paying users. Built-in A/B testing, "
            "one-click Stripe checkout, native copy kit, deploy to Vercel "
            "in thirty seconds.",
        "primary_cta":   "Start free · 14 days",
        "primary_href":  "demo",
        "secondary_cta": "Watch the demo · 2 min",
        "secondary_href":"prodotto",

        "trust_label":   "Adopted by 240+ Italian early-stage startups",
        "trust_logos":   ["FLUX", "NOVA/", "QUANTA", "HELIX", "RIFT.", "CASP", "ARC", "LOOM"],

        # Product mockup card — overlaps the hero / sits below it
        "mockup": {
            "chrome_label":     "elevate.app / dashboard / onboarding-flow",
            "chrome_dots":      ["●", "●", "●"],
            "badge":            "Live A/B",
            "metric_primary":   "↑ 38%",
            "metric_label":     "Primary CTA conversion",
            "metric_desc":      "vs. variant B (control)",
            "secondary_metric": "+ € 12.4K",
            "secondary_label":  "MRR · last 30 days",
            "secondary_desc":   "trial-to-paid conversion: 22%",
            "feature_label":    "Plan Launch · € 29 / month",
            "perks":            ["Hosting + CDN included", "CLI deploy · zero config", "Direct Slack support"],
        },

        # Feature pills under the hero
        "feature_pills":  ["Stripe + Linear", "Built-in A/B testing", "Edge analytics", "EN copy kit", "Deploy in 30s"],

        # Capabilities — 6 cards in a 3x2 grid
        "features_label":   "What's inside",
        "features_heading": "Six modules, <em>one install</em>.",
        "features_intro":
            "Every piece you need to go live and start monetizing — "
            "already integrated, already tested, already documented.",
        "features": [
            {
                "icon": "→",
                "title": "Drag-and-drop hero builder",
                "desc":
                    "Ten hero layouts battle-tested on 1,200 startups. "
                    "A/B test between variants without writing a line of code.",
            },
            {
                "icon": "$",
                "title": "Pricing table & Stripe",
                "desc":
                    "Three configurable tiers, one-click checkout, "
                    "subscription management out-of-the-box. Stripe webhooks "
                    "already wired to Linear and Slack.",
            },
            {
                "icon": "▲",
                "title": "Edge analytics",
                "desc":
                    "Web vitals, conversion funnels, multi-touch attribution — "
                    "collected edge-side, zero impact on TTI. Privacy-first, "
                    "cookieless, GDPR-clean.",
            },
            {
                "icon": "✱",
                "title": "Onboarding flow",
                "desc":
                    "Guided multi-step checklist, progress bar, email "
                    "triggers on milestones. Median time-to-value 4 minutes "
                    "vs the industry benchmark of 18.",
            },
            {
                "icon": "◐",
                "title": "Native copy kit",
                "desc":
                    "Sixty copy blocks battle-tested on IT/EN/FR markets — "
                    "headlines, subs, CTAs, onboarding microcopy, error states. "
                    "Ready to edit in markdown.",
            },
            {
                "icon": "↗",
                "title": "Deploy CLI",
                "desc":
                    "elevate deploy → Vercel / Netlify / Cloudflare in "
                    "thirty seconds. Automatic branch previews, rollback "
                    "in one command, environment variables synced.",
            },
        ],

        # Live product walkthrough invitation — replaces a fake video block.
        # Rationale (D-068, Session 36): shipping a real, current product demo
        # video would require a recorded MP4 per build; a placeholder source
        # reads as a cheap template. The card below keeps the editorial shelf
        # (dashboard still as poster, cosmic glass frame) but swaps the play
        # button for an honest booking CTA — one real primary CTA to the demo
        # form, one secondary to the existing changelog. No codec metadata.
        "product_demo_card": {
            "label":      "See Elevate in live action",
            "heading":    "Fifteen minutes with the people who built it.",
            "intro":
                "Instead of a recorded video: we'll book a short walkthrough "
                "on the real project — drag-and-drop editor, pricing wizard, "
                "Stripe + Linear wiring, deploy to Vercel. Real questions, "
                "real project, no follow-up spam.",
            "poster":     "https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=1800&q=80&auto=format&fit=crop",
            "primary_cta":    "Book the walkthrough",
            "primary_href":   "demo",
            "secondary_cta":  "Explore the product",
            "secondary_href": "prodotto",
            "caption":        "1-on-1 walkthrough · live calendar",
        },

        # Metric strip on dark band
        "metric_label":   "The kit's numbers in production",
        "metric_heading": "The stack that ships",
        "metric_strip": [
            ("3.1 ×",  "average landing conversion"),
            ("14 days", "from deploy to first paying user"),
            ("99.98%", "infrastructure uptime"),
            ("4 min",  "median time-to-value"),
        ],

        # Integrations row
        "integrations_label":   "Out-of-the-box integrations",
        "integrations_heading": "Already wired to the stack you use",
        "integrations": [
            ("Stripe",     "Subscription · Checkout · Tax"),
            ("Linear",     "Issue tracking · auto changelog"),
            ("Slack",      "Notifications · MRR alerts"),
            ("Vercel",     "Deploy · preview · rollback"),
            ("PostHog",    "Funnel · session replay"),
            ("GrowthBook", "A/B test · feature flags"),
            ("Loops",      "Transactional email"),
            ("Cal.com",    "Auto demo booking"),
        ],

        # Pricing teaser — cliccabile verso /prezzi
        "pricing_teaser_label":   "Transparent pricing",
        "pricing_teaser_heading": "Three plans, no setup fee.",
        "pricing_teaser_intro":
            "One-click cancellation, monthly or annual billing, "
            "fourteen-day trial with no credit card.",
        "pricing_teaser": [
            {"name": "Launch",  "price": "€ 29",  "period": "/ month", "tag": "For solo founders",
             "highlight": False, "perks": ["All modules", "Hosting + CDN", "Slack email"]},
            {"name": "Scale",   "price": "€ 79",  "period": "/ month", "tag": "Most chosen",
             "highlight": True, "perks": ["Everything in Launch +", "Advanced A/B", "5 projects"]},
            {"name": "Studio",  "price": "€ 199", "period": "/ month", "tag": "For studios & agencies",
             "highlight": False, "perks": ["Everything in Scale +", "Unlimited projects", "White-label"]},
        ],
        "pricing_teaser_cta":      "Compare plans in detail",
        "pricing_teaser_cta_href": "prezzi",

        # Founder proof — 2 founder quotes
        "founders_label":   "Founders who've shipped with Elevate",
        "founders_heading": "Over to the people who <em>actually ship</em>.",
        "founders": [
            {
                "name":  "Anna Vecchietti",
                "role":  "Founder · Quanta Analytics",
                "quote":
                    "I'd tried three boilerplates and two no-code builders. "
                    "With Elevate I went live in two weekends, first MRR "
                    "seventeen days after deploy. The difference is the "
                    "native copy kit — not having to rewrite every headline.",
                "metric_primary": "+ € 4.2K",
                "metric_label":   "MRR first 60 days",
            },
            {
                "name":  "Davide Zonca",
                "role":  "CTO · Helix Workflows",
                "quote":
                    "The stack I needed without the seven days of setup. "
                    "Stripe, GrowthBook, Linear already wired means we "
                    "spent the first month talking to users, not "
                    "configuring webhooks.",
                "metric_primary": "× 3.4",
                "metric_label":   "Conversion vs previous landing",
            },
        ],

        # Ship log — what shipped recently (transparency block)
        "shiplog_label":   "Live ship log",
        "shiplog_heading": "What we've shipped recently",
        "shiplog_intro":
            "Elevate is in continuous deploy. Every shipped feature shows "
            "up here in real time — no theoretical roadmaps, no product "
            "seasons. What you see is what you'll use tomorrow.",
        "shiplog": [
            {"version": "v2.9", "date": "Friday",       "title": "Drag-and-drop hero builder",
             "desc": "Ten pre-tested layouts, built-in A/B between variants, live preview."},
            {"version": "v2.8", "date": "Yesterday",    "title": "Premium testimonial library",
             "desc": "Four layouts (carousel, masonry, single-feature, video-first) with reveal animations."},
            {"version": "v2.7", "date": "Tuesday",      "title": "Built-in GrowthBook A/B testing",
             "desc": "4-step experiment setup wizard, hypothesis tracker, automatic statistical significance."},
            {"version": "v2.6", "date": "Monday",       "title": "One-click Stripe Checkout",
             "desc": "Adapters for the 4 major EU payment providers, automatic VAT handling."},
            {"version": "v2.5", "date": "Last week",    "title": "Privacy-first edge analytics",
             "desc": "Cookieless tracking, under 4KB on TTI, funnel dashboard included."},
        ],
        "shiplog_cta":      "Subscribe to the ship log on Slack",
        "shiplog_cta_href": "demo",
        "shiplog_release_label": "Next release",
        "shiplog_release_value": "v3.0 · first Monday of the month",
        "shiplog_release_chip":  "RC live",

        # Final CTA band before footer — glow ring
        "cta_label":     "Start now",
        "cta_heading":   "Fourteen days free. Forty minutes to go live.",
        "cta_intro":
            "No credit card to start the trial. Direct Slack "
            "with the founding team. If you don't ship within two weeks, "
            "we refund you. Written promise.",
        "cta_primary":   "Start your trial",
        "cta_primary_href": "demo",
        "cta_secondary": "See the full plan",
        "cta_secondary_href": "prezzi",
    },

    # ─── PRODOTTO (product tour) ────────────────────────────────
    "prodotto": {
        "eyebrow":   "Product tour · v2.9 (April 2026)",
        "headline":  "Everything you <em>need to ship</em> to go live.",
        "intro":
            "Six core modules + twelve out-of-the-box integrations. "
            "No plugins to configure, no boilerplate to fork, "
            "no Twitter thread to follow to do what should be "
            "obvious. Open, edit, deploy.",

        # Product modules — same 6 from home but expanded with detail
        "modules_label":   "Core modules",
        "modules_heading": "Six pieces, one install",
        "modules": [
            {
                "num":   "01",
                "title": "Drag-and-drop hero builder",
                "blurb":
                    "Ten hero layouts battle-tested on 1,200 early-stage startups. "
                    "Each layout ships with three copy variants "
                    "(B2B, B2C, dev-tool) and built-in A/B testing.",
                "highlights": [
                    "10 layouts · 30 copy variants",
                    "A/B between variants, no code",
                    "Headline, sub, CTA, social badge all editable",
                    "Mobile + desktop optimized separately",
                ],
            },
            {
                "num":   "02",
                "title": "Pricing table & Stripe Checkout",
                "blurb":
                    "Three configurable tiers with automatic highlight on the "
                    "middle plan. Stripe subscription management, "
                    "one-click mobile checkout, automatic EU VAT handling.",
                "highlights": [
                    "1, 2, 3 or 4 tiers · highlight any",
                    "Built-in monthly / annual toggle",
                    "Stripe Tax across 38 EU countries",
                    "Stripe webhooks → Slack pre-wired",
                ],
            },
            {
                "num":   "03",
                "title": "Privacy-first edge analytics",
                "blurb":
                    "Web vitals, multi-step funnels, multi-touch attribution — "
                    "all collected edge-side via Cloudflare Worker. "
                    "Cookieless, GDPR-clean, under 4KB on TTI.",
                "highlights": [
                    "Cookieless · GDPR · ePrivacy clean",
                    "Web Vitals · LCP · FID · CLS in dashboard",
                    "Visual conversion funnel",
                    "Optional PostHog connector",
                ],
            },
            {
                "num":   "04",
                "title": "Guided onboarding flow",
                "blurb":
                    "Multi-step checklist with progress bar, milestone "
                    "celebration, automatic email triggers. Median "
                    "time-to-value 4 minutes vs the 18-minute industry benchmark.",
                "highlights": [
                    "Customizable drag-and-drop checklist",
                    "Email triggers on Loops · Resend · Postmark",
                    "Built-in achievement badges",
                    "Automatic re-engagement after 48h",
                ],
            },
            {
                "num":   "05",
                "title": "Native copy kit (IT + EN + FR)",
                "blurb":
                    "Sixty editorial copy blocks battle-tested on the "
                    "IT/EN/FR markets. Headlines, subs, CTAs, onboarding "
                    "microcopy, error states, empty states.",
                "highlights": [
                    "60 blocks · IT + EN + FR",
                    "Configurable tone-of-voice",
                    "Direct markdown editing",
                    "Snippet library with semantic search",
                ],
            },
            {
                "num":   "06",
                "title": "Deploy CLI · thirty seconds",
                "blurb":
                    "elevate deploy. Thirty seconds to the first live deploy, "
                    "automatic branch previews on PR, rollback in one command, "
                    "environment variables synced across dev / staging / prod.",
                "highlights": [
                    "Vercel · Netlify · Cloudflare adapters",
                    "Automatic branch previews on PR",
                    "Instant rollback · zero downtime",
                    "Env-var sync · dev / staging / prod",
                ],
            },
        ],

        # Integrations grid — bigger version of home
        "integrations_label":   "Out-of-the-box integrations",
        "integrations_heading": "The stack you need, already wired.",
        "integrations_intro":
            "Twelve native integrations, zero plugins to install. "
            "The ones you don't see here we'll add if you ask on Slack.",
        "integrations_full": [
            {"name": "Stripe",     "category": "Payments",    "desc": "Subscription · Checkout · Tax · Connect"},
            {"name": "Linear",     "category": "Tracking",    "desc": "Issues · Cycles · auto-published changelog"},
            {"name": "Slack",      "category": "Comms",       "desc": "Notifications · MRR alerts · daily digest"},
            {"name": "Vercel",     "category": "Deploy",      "desc": "Production deploy · preview branch · rollback"},
            {"name": "Netlify",    "category": "Deploy",      "desc": "Edge functions · build hooks · analytics sync"},
            {"name": "Cloudflare", "category": "Deploy",      "desc": "Workers · KV · D1 · R2 storage"},
            {"name": "PostHog",    "category": "Analytics",   "desc": "Funnel · session replay · feature flags"},
            {"name": "GrowthBook", "category": "Experiments", "desc": "A/B test · hypothesis tracker · auto stat-sig"},
            {"name": "Loops",      "category": "Email",       "desc": "Transactional · onboarding sequences"},
            {"name": "Resend",     "category": "Email",       "desc": "Transactional · React Email templates"},
            {"name": "Cal.com",    "category": "Booking",     "desc": "Demo booking · routing · webhooks"},
            {"name": "Plain",      "category": "Support",     "desc": "Support inbox · CRM with AI triage"},
        ],

        # Architecture — what runs where
        "stack_label":   "Architecture",
        "stack_heading": "What runs where (and why)",
        "stack_intro":
            "Technical transparency — no magic, no hidden lock-in. "
            "The stack is openly documented, and the entire codebase is exportable "
            "in one click if you decide to leave.",
        "stack": [
            ("Frontend",    "Next.js 15 · React 19 · App Router · Server Actions"),
            ("Edge",        "Cloudflare Workers + KV for analytics and A/B"),
            ("Database",    "PostgreSQL · Prisma · Neon serverless"),
            ("Auth",        "Clerk · OAuth · passkey · magic link"),
            ("Payments",    "Stripe Subscriptions + Stripe Tax + Stripe Connect"),
            ("Email",       "Loops or Resend, your choice · React Email templates"),
            ("Analytics",   "Optional PostHog · native edge analytics"),
            ("Experiments", "GrowthBook · self-hosted or cloud"),
        ],

        "cta_heading":   "Ready to see it run?",
        "cta_intro":
            "Live demo with a founding member every Tuesday at 17:00 CET. "
            "Half-hour call, screen-share, technical questions welcome.",
        "cta_primary":   "Book a demo",
        "cta_primary_href": "demo",
        "cta_secondary": "See pricing",
        "cta_secondary_href": "prezzi",
    },

    # ─── PREZZI (pricing) ───────────────────────────────────────
    "prezzi": {
        "eyebrow":  "Transparent pricing · 2026",
        "headline": "Cancel in one click. <em>Always</em>.",
        "intro":
            "Three plans, no setup fee, monthly or annual billing "
            "(two months free on annual). Fourteen "
            "days of free trial, no credit card.",

        # Highlight badge label (lifted from CSS pseudo-element Session 40)
        "highlight_badge": "Most chosen",
        "annual_prefix":   "or",

        # Toggle row UI cue
        "billing_toggle_label": "Billing",
        "billing_toggle_options": [
            ("monthly", "Monthly"),
            ("annual",  "Annual · –17%"),
        ],

        # Three pricing tiers
        "tiers": [
            {
                "name":     "Launch",
                "tag":      "For solo founders",
                "price":    "€ 29",
                "annual":   "€ 24",
                "period":   "/ month",
                "annual_period": "/ month · billed annually",
                "highlight": False,
                "blurb":
                    "Everything you need to go live with a single product. "
                    "Built for the solo founder or the first week of a "
                    "founding team.",
                "cta":         "Start free",
                "cta_href":    "demo",
                "perks": [
                    ("✓", "All six core modules"),
                    ("✓", "Global hosting + CDN included"),
                    ("✓", "Deploy CLI · automatic branch previews"),
                    ("✓", "Edge analytics + basic funnel"),
                    ("✓", "1 project · 1 custom domain"),
                    ("✓", "Direct Slack with the founding team"),
                    ("○", "Basic A/B testing (manual)"),
                    ("○", "1 copy kit (IT or EN or FR)"),
                ],
            },
            {
                "name":     "Scale",
                "tag":      "Most chosen · for post-PMF startups",
                "price":    "€ 79",
                "annual":   "€ 65",
                "period":   "/ month",
                "annual_period": "/ month · billed annually",
                "highlight": True,
                "blurb":
                    "The plan for the founding team that's hit product/market "
                    "fit and is scaling. Adds advanced A/B, multi-project, "
                    "white-glove onboarding.",
                "cta":         "Start free",
                "cta_href":    "demo",
                "perks": [
                    ("✓", "Everything in Launch +"),
                    ("✓", "Advanced A/B testing (GrowthBook built in)"),
                    ("✓", "5 projects · unlimited custom domains"),
                    ("✓", "PostHog connector + session replay"),
                    ("✓", "Stripe Tax + Stripe Connect"),
                    ("✓", "All 3 copy kits (IT + EN + FR)"),
                    ("✓", "1-on-1 onboarding with the founding team (60 min)"),
                    ("✓", "Dedicated Slack channel · 4h SLA"),
                ],
            },
            {
                "name":     "Studio",
                "tag":      "For studios, agencies & venture builders",
                "price":    "€ 199",
                "annual":   "€ 165",
                "period":   "/ month",
                "annual_period": "/ month · billed annually",
                "highlight": False,
                "blurb":
                    "For agencies, creative studios and venture builders who ship "
                    "multiple landings for different clients. Unlimited projects and "
                    "full white-label.",
                "cta":         "Talk to us",
                "cta_href":    "contatti",
                "perks": [
                    ("✓", "Everything in Scale +"),
                    ("✓", "Unlimited projects · white-label branding"),
                    ("✓", "Sub-accounts for each client"),
                    ("✓", "Full API · custom webhooks"),
                    ("✓", "1h SLA · phone support"),
                    ("✓", "Dedicated account manager"),
                    ("✓", "Quarterly review with the founding team"),
                    ("✓", "Audit trail · SOC 2 compliance"),
                ],
            },
        ],

        # Comparison — what's NOT included
        "comparison_label":   "What's not here (and why)",
        "comparison_heading": "The transparency everyone else dodges",
        "comparison": [
            ("Setup fee",
             "Never. Not on Launch, not on Scale, not on Studio. If you find "
             "a competitor boilerplate that doesn't charge a setup fee + "
             "ships the stack pre-wired, let us know and we'll refund your first month."),
            ("Code lock-in",
             "Never. All your code is exportable via CLI in one command. "
             "If you decide to leave Elevate, we'll move the deploy to a "
             "Vercel you own, free of charge, within 24h."),
            ("Hidden fees",
             "Never. What you read is what you pay. EU VAT is "
             "calculated automatically and shown at checkout — "
             "no invoice surprises."),
            ("Transaction limits",
             "Never. Stripe Connect has no cap on transactions or volume. "
             "Sell 10 subscriptions or 10,000 — the price is the same."),
        ],

        # FAQ accordion
        "faq_label":   "Frequently asked",
        "faq_heading": "What people ask most",
        "faq": [
            ("Can I try before I pay?",
             "Yes, fourteen days of full trial with no credit card. "
             "You get access to every Scale-plan module during the trial — "
             "if you decide to stay, pick the plan that fits. If you "
             "don't, the trial expires automatically, no auto-charges."),
            ("What happens if I cancel?",
             "Cancel from the dashboard in one click, any time. "
             "Your deploy stays live until the end of the period you've paid for. "
             "We export your code via CLI and help you migrate to your "
             "own Vercel/Netlify if you want to continue solo."),
            ("Do you have a startup discount?",
             "Yes, 50% off the first six months for pre-seed startups (under "
             "€500K raised) and 30% off the first year for post-seed. Email "
             "hello@elevatekit.io with your pitch deck to activate it."),
            ("Does it plug into our existing stack?",
             "Probably yes. The 12 native integrations cover 90% of the "
             "stacks we see, and the REST API + custom webhooks let you "
             "connect whatever's missing. Need an integration that isn't "
             "there? Drop us a line on Slack — usually we ship it within "
             "two weeks."),
            ("Can I self-host?",
             "On the Studio plan, yes — we hand you the Docker container and "
             "Postgres schema to host wherever you want. On Launch and "
             "Scale, hosting is included and part of the kit's value."),
            ("Are invoices issued from Italy?",
             "Yes, we invoice from Milan in EUR with an Italian VAT number, "
             "electronic SDI invoicing included. For non-IT EU clients, "
             "invoices are reverse-charge VAT."),
        ],

        "cta_heading":   "Ready to start?",
        "cta_intro":
            "Fourteen days free. No credit card. "
            "Forty minutes to go live with your first deploy.",
        "cta_primary":   "Start your trial",
        "cta_primary_href": "demo",
        "cta_secondary": "Questions? Email us",
        "cta_secondary_href": "contatti",
    },

    # ─── DEMO (lead form) ───────────────────────────────────────
    "demo": {
        "eyebrow":  "Live demo · Tuesday 17:00 CET",
        "headline": "Half an hour with a <em>founding member</em>.",
        "intro":
            "Live demo every Tuesday at 17:00 CET. Thirty minutes of "
            "screen-share — we show how to configure a pricing tier, "
            "how to launch an A/B test, how to do the first deploy. "
            "Technical questions welcome, pitch decks not required.",

        # Form
        "form_label":   "Book a slot",
        "form_heading": "Fill it in and we'll confirm within an hour",
        "form_intro":
            "The next Tuesday slot is what you'll get by default. "
            "Prefer an ad-hoc slot? Pick 'Custom slot' and "
            "we'll email to set it. Async-only? No problem, see below.",
        "form_fields": [
            {"name": "name",     "label": "Name",          "type": "text",  "required": True,  "placeholder": "e.g. Anna",
             "helper": "So we know how to greet you on the call."},
            {"name": "email",    "label": "Email",         "type": "email", "required": True,  "placeholder": "anna@startup.io",
             "helper": "Calendar invite + Loom land here."},
            {"name": "company",  "label": "Startup",       "type": "text",  "required": True,  "placeholder": "e.g. Quanta Analytics",
             "helper": "The name you use for commits and billing."},
            {"name": "role",     "label": "Role",          "type": "select","required": True,
             "options": ["Solo founder", "Co-founder · CEO", "Co-founder · CTO", "Co-founder · other", "Hire 1-5", "Other"],
             "helper": "If you're flying solo, \"Solo founder\" is the pick."},
            {"name": "stage",    "label": "Stage",         "type": "select","required": True,
             "options": ["Pre-idea / exploring", "Pre-launch / waitlist", "Post-launch / hunting PMF", "Post-PMF / scaling"],
             "helper": "The demo adapts: pre-launch sees onboarding + waitlist, post-PMF sees pricing tiers + A/B."},
            {"name": "slot",     "label": "Preferred slot","type": "select","required": True,
             "options": ["Next Tuesday 17:00 CET", "Custom slot (we'll email)", "Async — send me a recorded Loom"],
             "helper": "Async slot = you get the 12-min Loom by email right away."},
            {"name": "stack",    "label": "Current stack",
             "type": "text", "required": False,
             "placeholder": "e.g. Next.js + Vercel + Stripe",
             "helper": "Optional. Helps us zero in on the right integration points."},
            {"name": "context",  "label": "What do you need to know?", "type": "textarea",
             "required": False, "full_width": True,
             "placeholder": "Specific questions, blocks you want to see, technical doubts... (optional)",
             "helper": "Two lines are enough. Any technical doubt played in the open."},
        ],

        "form_sections": [
            {"num": "01", "title": "Who you are",
             "meta": "No BDRs, no sequences — a founding member replies.",
             "fields": ["name", "email", "company"]},
            {"num": "02", "title": "Context",
             "meta": "So we can tailor the demo to your stage and stack.",
             "fields": ["role", "stage", "stack"]},
            {"num": "03", "title": "Demo preferences",
             "meta": "Live every Tuesday at 17:00 CET, otherwise async via Loom.",
             "fields": ["slot", "context"]},
            {"num": "04", "title": "Materials (optional)",
             "meta": "A Loom of yours, product screenshots or a metrics snapshot "
                     "let us show up prepared.",
             "fields": ["__upload__"]},
        ],

        "upload_field": {
            "name":     "demo_allegati",
            "label":    "Context materials",
            "helper":   "PDF, PNG, JPG, MP4, MOV · max 3 files, 25 MB total. "
                        "Useful if you want us to see the product or a current funnel.",
            "accept":   ".pdf,.png,.jpg,.jpeg,.mp4,.mov",
            "multiple": True,
            "primary":  "Drag deck, screenshots or Loom here or",
            "link":     "browse your folder",
            "meta":     "PDF / PNG / JPG / MP4 · max 25 MB",
        },

        "form_submit_label": "Book the demo",
        "form_submit_note":
            "Confirmation within an hour during office hours (9-19 CET) · no newsletter, "
            "no automated sequence.",
        "form_consent":
            "By signing up you accept the calendar invite and a reminder "
            "email 24h before. No newsletter, no automated sequence. "
            "Data processed under EU Reg. 679/2016.",

        # Async option block
        "async_label":   "Prefer async?",
        "async_heading": "12-minute recorded Loom",
        "async_intro":
            "If you can't make the live demo, we've recorded a twelve-minute "
            "Loom showing the complete end-to-end setup. "
            "You'll receive it by email within an hour of requesting it.",
        "async_cta":     "Get the Loom via email",
        "async_cta_href": "demo",

        # Trust strip
        "trust_label":   "What to expect from the demo",
        "trust_items": [
            ("01", "Half an hour of screen-share",
             "No slides. We open the app, set up a pricing tier, launch an A/B test, deploy."),
            ("02", "Technical questions welcome",
             "Edge latency, Postgres schema, Stripe webhooks — any "
             "implementation question played in the open."),
            ("03", "No pressure",
             "We don't close in-call. If you need it, we give you trial access "
             "right away; otherwise we reconnect a week later."),
        ],

        "footnote":
            "Demos are run by one of Elevate's three founding members "
            "(not by external BDRs). If the Tuesday 17:00 slot doesn't "
            "work for your timezone, we'll propose an alternative by "
            "email within 24 hours.",
    },

    # ─── CONTATTI ───────────────────────────────────────────────
    "contatti": {
        "eyebrow":  "Talk to us · async-first",
        "headline": "Slack, email or live demo. <em>Your call</em>.",
        "intro":
            "Async-first means we reply within an hour during office "
            "hours (9-19 CET) and that decisions get made in writing. "
            "If you'd rather hop on a call, just book one — it's included "
            "in every plan, no extra.",

        # Channels grid — 4 ways to reach
        "channels_label":   "Four channels, one person replies",
        "channels": [
            {
                "icon":  "✉",
                "title": "Email",
                "value": "hello@elevatekit.io",
                "desc":  "The founding team reads everything. Reply within 1h during office hours.",
                "cta":   "Write now",
            },
            {
                "icon":  "#",
                "title": "Slack community",
                "value": "elevate-founders.slack.com",
                "desc":  "Channel for anyone on trial or a plan. 220+ founders inside.",
                "cta":   "Request an invite",
            },
            {
                "icon":  "▶",
                "title": "Live demo",
                "value": "Tuesday 17:00 CET",
                "desc":  "Thirty minutes of screen-share with a founding member. Async option available.",
                "cta":   "Book the slot",
            },
            {
                "icon":  "✱",
                "title": "Founder office hours",
                "value": "Friday 11:00 CET",
                "desc":  "Weekly open call for Scale and Studio plans. Public questions, open answers.",
                "cta":   "Add to calendar",
            },
        ],

        # Founders block — 3 founders with emails (transparency signal)
        "team_label":   "The founding team",
        "team_heading": "The people who read your email",
        "team_intro":
            "When you email hello@elevatekit.io, one of these three people "
            "writes back — not an external BDR, not an AI copilot. Below, "
            "their direct emails for specific requests.",
        "team": [
            {
                "name":  "Riccardo Camillini",
                "role":  "Co-founder · Product",
                "email": "riccardo@elevatekit.io",
                "tag":   "Product questions · roadmap",
                "bio":
                    "Three prior exits as technical founder, "
                    "the last to a European B2B SaaS fund. Handles "
                    "product strategy, roadmap and architecture decisions.",
            },
            {
                "name":  "Beatrice Lavia",
                "role":  "Co-founder · Engineering",
                "email": "beatrice@elevatekit.io",
                "tag":   "Technical questions · stack · API",
                "bio":
                    "Eight years as a senior engineer at Vercel and Linear. "
                    "Architected the edge analytics and every deploy "
                    "adapter. Answers any implementation question.",
            },
            {
                "name":  "Tommaso Adami",
                "role":  "Co-founder · Growth",
                "email": "tommaso@elevatekit.io",
                "tag":   "Onboarding · pricing · partnerships",
                "bio":
                    "Former growth lead at a European fintech scale-up. "
                    "Runs onboarding, pricing strategy, discounts "
                    "for pre-seed startups and accelerator partnerships.",
            },
        ],

        # Office meta-row labels (lifted from skin Session 40 for i18n)
        "office_address_label":   "Office",
        "office_transport_label": "Transit",
        "office_model_label":     "Model",

        # Studio info — async-first office
        "office_label":   "Async-first office",
        "office_heading": "Where we are (even though you'll find us online)",
        "office_intro":
            "The physical office is at Talent Garden Calabiana in Milan, but the "
            "team is distributed (Milan, Berlin, Lisbon, Kraków). "
            "Async-first means internal meetings are kept to a minimum, "
            "and almost everything is decided on Linear in pull requests.",
        "office": {
            "address":     "Talent Garden Calabiana · Via Calabiana 6 · 20139 Milan",
            "transport":   "M3 Lodi · 8-minute walk · internal parking available",
            "hours":       "Async-first · founders on-site Tuesday and Thursday",
            "schedule": [
                ("Slack",          "Mon – Fri · 9:00 – 19:00 CET"),
                ("Email",          "Reply within 1h during office hours · within 24h otherwise"),
                ("Demo on-demand", "Tuesday 17:00 CET · async via Loom anytime"),
                ("Office hours",   "Friday 11:00 CET · for Scale and Studio plans"),
            ],
        },

        "footnote":
            "Elevate is a six-person team — three founders + three engineers. "
            "We'll personally answer your email. If you don't hear back "
            "within 24h, it's not lost: ping us on Slack and trigger a "
            "reminder. Promise, no request goes unheard.",
    },
}

"""Vertex — Creative Studio · EN content registry.

Agency live rollout, Phase 2g3.6f, Session 49.

Voice contract (London / NYC independent creative-studio register):
- First-person plural ("we design", "we sign", "we accompany") —
  editorial, curatorial, never over-familiar. Think Creative Review,
  Eye Magazine, It's Nice That, Monocle, Wallpaper*.
- Studio-craft lexicon: "brief", "identity system", "print run",
  "brand book", "editorial line", "series" — never the growth / KPI /
  sprint vocabulary (that is Aura's register).
- Clients are cultural / luxury / premium retail / editorial —
  foundations, publishing houses, maisons, museums, independent labels.
- Numbers stay restrained. Never "3x conversion". Sometimes
  "weeks" / "eight years" / "twelve titles" spelled out.
"""
from __future__ import annotations

from typing import Any


VERTEX_CONTENT_EN: dict[str, Any] = {

    "pages": [
        {"slug": "home",     "label": "Studio",     "kind": "home"},
        {"slug": "studio",   "label": "About",      "kind": "about"},
        {"slug": "capacita", "label": "Capabilities","kind": "services"},
        {"slug": "lavori",   "label": "Work",       "kind": "project_list"},
        {"slug": "manifesto","label": "Manifesto",  "kind": "process"},
        {"slug": "contatti", "label": "Contact",    "kind": "contact"},
    ],

    # ── Site chrome ──────────────────────────────────────────────
    "site": {
        "logo_word":   "Vertex Studio",
        "tag":         "Independent creative studio · Milano",
        "availability":"New commissions · autumn 2026",
        "nav_cta":     "Request the dossier",
        "inquiry_page_slug": "contatti",
        "phone":       "+39 02 4981 2066",
        "email":       "studio@vertex.milano",
        "address":     "Via Tortona 32 · 20144 Milano",
        "hours_compact": "Studio open · Tue / Thu",
        "license":     "P.IVA 10456770963 · Milano",
        "footer_intro":
            "Independent creative studio founded in Milano in 2018. "
            "We design identity systems, editorial series and art "
            "direction for Italian foundations, maisons and "
            "publishing houses.",
        "foot_clients_label":     "Selected clients · 2018 — 2026",
        "clients_footer_rows": [
            "FONDAZIONE PRADA", "2024",
            "MAISON GENTILUOMO", "2025",
            "ADELPHI EDIZIONI", "2024",
            "TRIENNALE MILANO", "2023",
            "MUSEO DEL '900", "2025",
            "VILLA NECCHI", "2024",
        ],
        "foot_standfirst":
            "A brand should never look as though it just walked out of the studio. "
            "A good visual system holds the season. A system built "
            "with care holds the decade.",
        "foot_studio_label":      "The studio",
        "foot_recognition_label": "Recognition",
        "foot_recognition_rows": [
            "ADI Design Index — 2024",
            "Type Directors Club — 2023",
            "Premio Compasso d'Oro — Mention 2022",
            "European Design Awards — 2022",
        ],
    },

    # ── HOME ─────────────────────────────────────────────────────
    "home": {
        "eyebrow":  "Independent studio · founded 2018 · Milano",
        "headline": "Brands that <em>carry weight</em>, <em>hold</em>, <em>endure</em>.",
        "pull_quote":
            "« A brand isn't a logo. It's the way a thing "
            "looks back at you when no one is talking about it. »",
        "intro":
            "We are an independent creative studio designing "
            "identity systems, editorial series and art direction "
            "for a small number of cultural and luxury clients. "
            "We accompany every brand from the first brief to the "
            "final print run.",
        "primary_cta":   "Request the dossier",
        "primary_href":  "contatti",
        "secondary_cta": "Selected work",
        "secondary_href":"lavori",

        # Hero right — editorial cover tile
        "cover": {
            "image":  "https://images.unsplash.com/photo-1519682337058-a94d519337bc?w=900&q=80&auto=format&fit=crop",
            "badge":  "Case Study · 01",
            "client_name": "FONDAZIONE PRADA · 2025 Series",
            "title":  "An editorial system for <em>four authors</em> and twenty-two titles.",
            "discipline": "Identity · publishing",
            "year":   "2025 — 2026",
            "credit_left_label":  "Art direction",
            "credit_left_value":  "M. Serafini",
            "credit_right_label": "Rollout",
            "credit_right_value": "Oct 2025",
        },

        # Ledger
        "ledger_heading":   "<em>Recent</em> work",
        "ledger_link":      "Full archive →",
        "ledger_page_slug": "lavori",
        "ledger_rows": [
            ("01", "Italian Fiction Series",        "Adelphi Edizioni",      "Identity & publishing", "2025", "adelphi-collana-narrativa"),
            ("02", "Rebranding the Foundation",     "Fondazione Prada",      "Art direction",          "2025", "fondazione-prada-rebrand"),
            ("03", "Integrated brand book",         "Maison Gentiluomo",     "Luxury branding",        "2024", "maison-gentiluomo-manuale"),
            ("04", "Signage & wayfinding",          "Triennale Milano",      "Spatial identity",       "2024", "triennale-milano-wayfinding"),
            ("05", "Author poster series",          "Museo del Novecento",   "Art direction",          "2024", "museo-900-manifesti"),
            ("06", "Packaging for six cuvées",      "Villa Necchi Winery",   "Signature packaging",    "2023", "villa-necchi-sei-cuvee"),
        ],

        # Capacità
        "capab_label":   "Studio capabilities",
        "capab_heading": "Four <em>disciplines</em>, a single direction.",
        "capab_intro":
            "We work across four axes that intersect on every "
            "project: brand identity, editorial lines, art direction "
            "and campaigns. We are not a service agency — we are a "
            "studio that builds systems.",
        "capab_items": [
            ("01", "Brand identity",
             "Logo, typographic system, palette, grid, brand book. "
             "From first delivery to rollout on tangible assets, "
             "in six to twelve weeks.",
             ["Logotype", "Brand book", "Curated typeface", "Grid"]),
            ("02", "Editorial lines",
             "Series, magazines, catalogues, author books. "
             "We build the grid, choose the type, "
             "stay with the print run.",
             ["Series", "Magazines", "Catalogues", "Books"]),
            ("03", "Art direction",
             "Seasonal campaigns, signature shoots, "
             "posters, POP materials. From moodboard "
             "to capture, through to print.",
             ["Campaigns", "Shoots", "Posters", "Motion"]),
            ("04", "Visual systems",
             "Signage, wayfinding, exhibition design, "
             "spatial environments. Identities that are "
             "inhabited, not simply looked at.",
             ["Wayfinding", "Signage", "Exhibition", "Shows"]),
        ],

        # Press
        "press_heading": "Published <em>and recognised</em>.",
        "press_intro":
            "Ours is a small, deliberate practice, "
            "choosing projects with care. But when a piece of work "
            "holds, the work gets noticed.",
        "press_publications": [
            "Monocle", "Domus", "Wallpaper*", "Creative Review",
            "It's Nice That", "Design Week", "Eye Magazine", "Slanted",
        ],

        # Manifesto
        "manifesto_label":   "Brief manifesto",
        "manifesto_heading": "A brand <em>isn't decorated</em>. It is built.",
        "manifesto_drop_cap": "A",
        "manifesto_body":
            " good project begins with a question no one "
            "has yet had the courage to ask. Designing a brand "
            "doesn't mean packaging what a client "
            "already thinks they know about themselves — it means "
            "helping them recognise what they already know but "
            "haven't yet named. This is why we don't take on "
            "impulsive commissions. This is why every relationship "
            "begins with a conversation, never with a quote.",
        "manifesto_principles": [
            ("01", "Form <em>follows voice</em>",
             "The typographic choice comes after the choice of tone. "
             "First you decide how a brand speaks, then how it looks."),
            ("02", "The system <em>before the image</em>",
             "We design rules, not applications. The job "
             "of a good rule is to be forgotten."),
            ("03", "Paper <em>holds time</em>",
             "Every project must survive at least two seasons "
             "of trend without losing its footing. Otherwise it is furniture."),
            ("04", "The client <em>is a co-author</em>",
             "We work with people who have a voice. Those who want "
             "a silent service will find a polite but firm reply."),
        ],

        # Inquiry CTA
        "cta_label":   "Next step",
        "cta_heading": "A brief well made <em>is worth six weeks</em>.",
        "cta_sub":
            "We reply within three working days with a short "
            "reading dossier on the project.",
        "cta_primary": "Request the dossier",
    },

    # ── STUDIO (about) ───────────────────────────────────────────
    "studio": {
        "eyebrow":   "The studio · eight years",
        "headline":  "Forty square metres of paper, print proofs <em>and typefaces still to be chosen</em>.",
        "standfirst":
            "We are three creative directors, two senior designers, "
            "a project manager and a photographer who passes through "
            "three times a week. The studio has had eight "
            "birthdays, thirty-two projects that have moved "
            "house, and an archive of print proofs that no longer "
            "fits behind the door.",

        "facts": [
            ("8",    "years in practice",   "Founded in Milano in 2018"),
            ("42",   "projects archived",   "Of which 22 published"),
            ("6",    "collaborators",       "Three partners · three seniors"),
            ("2",    "seasons of rollout",  "The average lifespan of a brand"),
        ],

        "essay_label":   "History of the studio",
        "essay_heading": "We began with <em>a typeface and a question</em>.",
        "essay_paragraphs": [
            "Vertex was founded in 2018 by Margherita Serafini "
            "and Tommaso Boeri, course companions at ISIA Urbino "
            "and later collaborators at two Milanese studios. The "
            "starting question was very simple: <em>why are so many "
            "Italian brands beautiful to discover and forgettable "
            "two months later?</em>",
            "The answer — arrived at slowly, project by project — "
            "is that most brands are designed the way a shop window is "
            "dressed: you choose what is seen first, "
            "not what holds up over time. Designing a brand system "
            "that lasts eight years isn't a question of "
            "trends, but of choices that are taken away when needed.",
        ],
        "essay_pullquote":
            "A well-made brand book doesn't describe the brand. "
            "It defends it against our own desire to change it.",
        "essay_tail_paragraphs": [
            "Today the studio works on average with eight clients a year. "
            "We turn down more than half of the briefs we receive — not out of "
            "posture, but out of honesty: a project done badly hurts "
            "twice over, the client and the portfolio.",
            "We have chosen to stay small. We have no ambitions "
            "of scale. We want to keep answering every first email "
            "personally, seeing every print proof through, "
            "knowing the names of the printers who press our books.",
        ],

        "partners_label":   "The three partners",
        "partners_heading": "Who <em>signs</em> the studio.",
        "partners_intro":
            "Every project is carried by at least one of the three partners "
            "from the first brief to the final rollout. We don't delegate the "
            "decisive moments — if a brand starts well, it is because someone "
            "was present when a first idea was turned down.",
        "partners": [
            {
                "name": "Margherita Serafini",
                "role": "Co-founder · Creative director",
                "bio":  "Diploma in editorial design at ISIA Urbino. "
                        "Before Vertex, eight years at Cabinet (Milano) "
                        "as senior designer. Obsessed with the serif "
                        "typefaces of the late twentieth century.",
                "portrait": "https://images.unsplash.com/photo-1524758631624-e2822e304c36?w=900&q=80&auto=format&fit=crop",
                "creds": ["ISIA Urbino", "ADI Design Index 2024", "IED Faculty"],
            },
            {
                "name": "Tommaso Boeri",
                "role": "Co-founder · Art director",
                "bio":  "Trained at ECAL Lausanne. Worked at Studio "
                        "Dumbar and M/M Paris before returning to Milano. "
                        "Art director for two independent publishing houses.",
                "portrait": "https://images.unsplash.com/photo-1568602471122-7832951cc4c5?w=900&q=80&auto=format&fit=crop",
                "creds": ["ECAL Lausanne", "TDC Award 2023", "European Design"],
            },
            {
                "name": "Ilaria Ferri",
                "role": "Partner · Editorial director",
                "bio":  "Degree in literature from the Statale in Milano. "
                        "Ten years at Adelphi before joining the "
                        "studio in 2021. Curates the editorial lines "
                        "and the writing of the brand books.",
                "portrait": "https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?w=900&q=80&auto=format&fit=crop",
                "creds": ["Statale Milano", "ex-Adelphi", "Premio Gutenberg"],
            },
        ],

        "timeline_label":   "Chronology",
        "timeline_heading": "Eight years <em>on paper</em>.",
        "timeline_rows": [
            ("2018",
             "Studio opens at Via Tortona 32",
             "First project: rebrand of the independent bookshop Scheiwiller. "
             "Serafini and Boeri sign the studio's first brand book on an A3 sheet."),
            ("2020",
             "First institutional commission",
             "Art direction for Triennale Milano — twenty-two months of work "
             "on the signage of the permanent galleries."),
            ("2021",
             "Ilaria Ferri joins as partner",
             "Opening of the editorial practice with the first series for Adelphi "
             "— nine titles released in eighteen months."),
            ("2023",
             "ADI Design Index recognition",
             "Award for the Contemporary Architectures series. "
             "First Italian cover for Eye Magazine."),
            ("2025",
             "Fondazione Prada rebrand",
             "Twenty-two months of work. Full rollout in autumn 2025, "
             "covering signage, editorial, seasonal campaigns."),
            ("2026",
             "Opening of the second room",
             "Expansion to Via Tortona 34, with a print-proof archive "
             "consultable by appointment."),
        ],
    },

    # ── CAPACITA (services) ──────────────────────────────────────
    "capacita": {
        "eyebrow":   "Studio capabilities",
        "headline":  "Four <em>disciplines</em> intersecting on every project.",
        "standfirst":
            "We are not a full-service agency. We are a studio "
            "working across four clear axes, each with a steady "
            "practice and a documented process. Every project draws "
            "from one or more of these axes — rarely from all together.",

        "disciplines": [
            {
                "num": "01",
                "title": "Brand <em>identity</em>",
                "tagline": "Logo, typeface, grid, brand book. Six to twelve weeks.",
                "body":
                    "We build identity systems that last eight years. "
                    "Every rebrand starts with a conversation with the managing "
                    "director or the founder — never with a brief sent by email. "
                    "We present three directions, then one. The final brand book "
                    "has an index that works, not one that impresses.",
                "scope_label": "Included",
                "scope": [
                    "Logotype and variations",
                    "Typographic system (retail + display)",
                    "Extended colour palette",
                    "Grid and compositional rules",
                    "Brand book (interactive PDF + print)",
                    "Applications plate (print · web · environment)",
                ],
            },
            {
                "num": "02",
                "title": "Editorial <em>lines</em>",
                "tagline": "Series, magazines, catalogues, author books.",
                "body":
                    "The editorial practice is the heart of the studio. We design "
                    "series that hold the season — the grid, the format, "
                    "the gutter, the covers. We stay with the print run to the "
                    "first proof on press, with trusted printers in Milano and Bergamo. "
                    "We are present for every first book of every series we sign.",
                "scope_label": "Included",
                "scope": [
                    "Format and grid design",
                    "Cover (system + application)",
                    "Retail typographic setting",
                    "Print and paper consultancy",
                    "Press attendance on first title",
                    "Application sheet for in-house design team",
                ],
            },
            {
                "num": "03",
                "title": "Art <em>direction</em>",
                "tagline": "Campaigns, signature shoots, posters.",
                "body":
                    "We direct seasonal campaigns for Italian maisons and "
                    "brands with an editorial approach — never advertising. "
                    "We pick the photographers, build the moodboard, "
                    "stay with the shoot. Campaigns are built to hold "
                    "two editorial cycles — not a week on social.",
                "scope_label": "Included",
                "scope": [
                    "Seasonal concept (reading PDF · 24 pages)",
                    "Photographic cast + direction",
                    "Shoot-day direction",
                    "Selection and post-production",
                    "Applications system (print · digital · retail)",
                    "Posters + launch collaterals",
                ],
            },
            {
                "num": "04",
                "title": "Spatial <em>systems</em>",
                "tagline": "Signage, wayfinding, exhibition design.",
                "body":
                    "When an identity becomes a place, we design it "
                    "alongside the architect. Permanent wayfinding for "
                    "museums and foundations, temporary exhibition "
                    "design, signage for luxury retail. Every spatial "
                    "system begins with a site visit. We never work from renders.",
                "scope_label": "Included",
                "scope": [
                    "Site visit and technical report",
                    "Spatial reading grid",
                    "Typographic + pictographic system",
                    "Production-ready artwork",
                    "Collaboration with the architecture studio",
                    "On-site presence · first installation",
                ],
            },
        ],

        "engagement_label":   "Three ways of working",
        "engagement_heading": "From the <em>single project</em> to the <em>editorial partner</em>.",
        "engagement_intro":
            "We accept three kinds of engagement. We shape them together "
            "with the client at the brief stage — there are no hidden rate cards.",
        "engagement_tiles": [
            {
                "title":  "Single <em>project</em>",
                "range":  "Twelve — twenty-four weeks",
                "body":   "An identity or an editorial line, from brief to rollout. "
                          "For brands that need a clean, defined gesture.",
                "includes": [
                    "Joint brief + three directions",
                    "Rollout across three applications",
                    "Brand book in Italian / English",
                    "Launch-day attendance",
                ],
            },
            {
                "title":  "Seasonal <em>commission</em>",
                "range":  "Six — twelve months · renewable contract",
                "body":   "Seasonal art direction for maisons or institutions. "
                          "Two campaigns a year, with every application.",
                "includes": [
                    "Spring / autumn campaign",
                    "Launch collaterals",
                    "Monthly studio presence",
                    "Shared archive",
                ],
            },
            {
                "title":  "Editorial <em>partner</em>",
                "range":  "Annual engagement · by invitation",
                "body":   "Constant presence at the client's editorial table. "
                          "For publishing houses, foundations, cultural institutions.",
                "includes": [
                    "Participation in the editorial plan",
                    "Direction on every release of the year",
                    "Print and paper consultancy",
                    "Archive + creative backup",
                ],
            },
        ],

        "cta_label":   "Free brief",
        "cta_heading": "A first <em>cup of tea</em> costs nothing.",
        "cta_primary": "Request the dossier",
    },

    # ── LAVORI (project_list) ────────────────────────────────────
    "lavori": {
        "eyebrow":   "Work archive · 2018 — 2026",
        "headline":  "Forty-two projects <em>in the archive</em>, twenty-two on show.",
        "standfirst":
            "A considered selection. We don't show everything — not "
            "everything holds up on re-reading. The full archive is "
            "available on request, as a printable PDF (one hundred and six pages).",
        "filters": ["All", "Identity", "Publishing", "Art direction", "Spatial systems"],

        "projects": [
            {
                "slug":       "fondazione-prada-rebrand",
                "index":      "01",
                "title":      "Rebranding the Foundation",
                "client":     "Fondazione Prada — Milano",
                "discipline": "Art direction",
                "year":       "2025",
            },
            {
                "slug":       "adelphi-collana-narrativa",
                "index":      "02",
                "title":      "Italian Fiction Series",
                "client":     "Adelphi Edizioni — Milano",
                "discipline": "Identity & publishing",
                "year":       "2025",
            },
            {
                "slug":       "maison-gentiluomo-manuale",
                "index":      "03",
                "title":      "Integrated brand book",
                "client":     "Maison Gentiluomo — Firenze",
                "discipline": "Luxury branding",
                "year":       "2024",
            },
            {
                "slug":       "triennale-milano-wayfinding",
                "index":      "04",
                "title":      "Permanent signage & wayfinding",
                "client":     "Triennale Milano — Parco Sempione",
                "discipline": "Spatial identity",
                "year":       "2024",
            },
            {
                "slug":       "museo-900-manifesti",
                "index":      "05",
                "title":      "Author poster series",
                "client":     "Museo del Novecento — Milano",
                "discipline": "Art direction",
                "year":       "2024",
            },
            {
                "slug":       "villa-necchi-sei-cuvee",
                "index":      "06",
                "title":      "Packaging for six signature cuvées",
                "client":     "Villa Necchi Winery — Valpolicella",
                "discipline": "Packaging",
                "year":       "2023",
            },
        ],

        "archive_label":   "Full archive",
        "archive_heading": "Available <em>on request</em>, one hundred and six pages.",
        "archive_body":
            "The full archive holds forty-two projects since 2018, "
            "with working process, print samples, editorial "
            "notes and client details.",
        "archive_stats": [
            ("42",   "projects archived"),
            ("22",   "published"),
            ("8",    "years of practice"),
            ("<em>6</em>", "clients per year on average"),
        ],
    },

    # ── MANIFESTO (process) ──────────────────────────────────────
    "manifesto": {
        "eyebrow":   "The way we work",
        "headline":  "Six weeks to <em>understand</em>. Ten to <em>build</em>. Two to <em>defend</em>.",
        "standfirst":
            "Every project moves through four declared phases. "
            "We don't care for surprises — not for us, not for the "
            "client. The timeline is public from day one.",

        "phases": [
            {
                "num": "01",
                "duration": "Weeks 1 — 6",
                "title": "<em>Listening</em> · reading · site visit",
                "tagline": "Understand before designing.",
                "body":
                    "We meet the managing director, the head of communications "
                    "and, when possible, the clients' clients. We read the archive, the prior "
                    "studies, the annual reports. We visit the spaces. No "
                    "form is proposed at this stage — only a written "
                    "reading of 24-32 pages that becomes the basis of the project.",
                "deliverables_label": "Deliverables",
                "deliverables": [
                    "Reading dossier (24-32 page PDF)",
                    "Three strategic territories to explore",
                    "Historical reference board",
                    "Detailed calendar of later deliverables",
                ],
            },
            {
                "num": "02",
                "duration": "Weeks 7 — 14",
                "title": "<em>Hypothesis</em> · three directions",
                "tagline": "Three proposals, none compromised.",
                "body":
                    "We present three creative directions fully built — "
                    "not three variations of the same intuition. Each direction has "
                    "a logo, a typeface, two pilot applications. The client chooses "
                    "one direction (or asks for a fourth round — it rarely happens).",
                "deliverables_label": "Deliverables",
                "deliverables": [
                    "Three creative directions (24 boards each)",
                    "One pilot application per direction",
                    "Written comparative reading",
                    "Studio presentation · half a day",
                ],
            },
            {
                "num": "03",
                "duration": "Weeks 15 — 22",
                "title": "<em>Construction</em> · system & brand book",
                "tagline": "From direction to brand book, without losing the tone.",
                "body":
                    "The chosen direction is developed into a full system: "
                    "grid, extended palette, brand variations, compositional "
                    "rules, final brand book. In parallel we build "
                    "three to five sample applications to test the system "
                    "on real cases.",
                "deliverables_label": "Deliverables",
                "deliverables": [
                    "Complete brand system (source files)",
                    "Brand book (interactive PDF + print edition)",
                    "Three to five sample applications",
                    "Retail fonts + documented licences",
                ],
            },
            {
                "num": "04",
                "duration": "Weeks 23 — 24",
                "title": "<em>Rollout</em> · defence · closure",
                "tagline": "The brand book comes alive, we stay close.",
                "body":
                    "We accompany the rollout on the first real applications "
                    "with studio presence and counsel for the client's internal "
                    "team. We stay with the first significant print run. We close "
                    "with a documented handover meeting, where the "
                    "internal lead becomes the system's custodian.",
                "deliverables_label": "Deliverables",
                "deliverables": [
                    "Attendance at public launch",
                    "First applications followed personally",
                    "Handover meeting + governance document",
                    "Six months on-call for clarifications",
                ],
            },
        ],

        "principles_label":   "Studio principles",
        "principles_heading": "<em>Seven</em> commitments we do not negotiate.",
        "principles": [
            ("01", "One <em>chapter at a time</em>",
             "Never two phases at once. A client who rushes one phase compromises the next. We have cancelled more than one contract over this."),
            ("02", "<em>Three directions</em>, never four",
             "Four directions make the choice arbitrary. Three force a reasoning. Two would be lazy."),
            ("03", "The <em>typeface</em> is licensed",
             "We don't use free fonts on paid projects. Every licence is documented to the client, with its own budget line."),
            ("04", "Press runs <em>are attended</em>",
             "The first run on press for every major rollout is overseen by a studio partner."),
            ("05", "The <em>client</em> is co-author",
             "The client signs the brand book alongside the studio. It isn't a service — it's a shared project."),
            ("06", "<em>No</em> is part of the service",
             "We say no more often than we propose. It's the principal value we bring."),
        ],

        "promise_label":   "Our numbers",
        "promise_heading": "Small <em>by choice</em>, slow <em>by method</em>.",
        "promise_stats": [
            ("<em>6</em>",       "clients per year on average",
             "More than 12 briefs received a month, fewer than 6 accepted a year."),
            ("<em>8</em>",       "years of average lifespan",
             "The identities signed between 2018 and 2022 are all still in use."),
            ("<em>3 days</em>",  "reply to first brief",
             "Within three working days you receive a first written reading of the project."),
        ],
    },

    # ── CONTATTI (contact) ───────────────────────────────────────
    "contatti": {
        "eyebrow":   "Request the dossier",
        "headline":  "Tell us about <em>the project</em>. We reply within three days.",
        "standfirst":
            "Every email lands directly with Margherita or Tommaso. "
            "There is no account-manager filter — whoever replies to you is "
            "whoever will carry the project first-hand, if you decide "
            "to work together.",

        "form_heading": "Project brief",
        "labels": {
            "name":       "Name and surname",
            "role":       "Role in the organisation",
            "company":    "Organisation / brand",
            "email":      "Contact email",
            "discipline": "Primary discipline requested",
            "budget":     "Indicative budget band",
            "brief":      "Project narrative",
        },
        "placeholders": {
            "name":    "First Last",
            "role":    "e.g. Head of communications",
            "company": "Name of the organisation",
            "email":   "name@organisation.com",
            "brief":   "Who you are, what you're trying to build, in what timeframe, with which internal team. The more concrete it is, the more useful the reply.",
        },
        "discipline_options": [
            "Brand identity (rebrand)",
            "Brand identity (first launch)",
            "Editorial line · series",
            "Art direction · campaign",
            "Spatial system · wayfinding",
            "I'm not sure yet — let's talk",
        ],
        "budget_bands": [
            ("12k",  "< €12K"),
            ("40k",  "€12 — 40K"),
            ("120k", "€40 — 120K"),
            ("120plus","> €120K"),
        ],
        "form_submit_label": "Send the brief",
        "form_submit_note":  "We reply within three working days with a first reading.",

        "direct_label":   "Direct email",
        "direct_heading": "Write to <em>Margherita</em> and <em>Tommaso</em>.",

        "studio_label":   "The studio",

        "reply_label":    "Reply times",
        "reply_heading":  "Three <em>working days</em>, no longer.",
        "reply_body":
            "Every brief receives a first written reading within 72 hours: "
            "we tell you whether the project fits us, whether the timing is right, "
            "whether we should meet in person to go deeper. "
            "No auto-replies, no quotes without a reading.",

        "channels_label": "Channels",
        "channels": [
            ("Email",      "studio@vertex.milano"),
            ("Phone",      "+39 02 4981 2066"),
            ("Studio",     "Via Tortona 32 · Milano"),
            ("LinkedIn",   "/company/vertex-milano"),
            ("Are.na",     "/vertex-studio"),
            ("Front desk", "Tue · Thu · 10 — 18"),
        ],

        "promise_label":   "A commitment",
        "promise_heading":
            "« We never send a quote before a reading brief. "
            "It's a small gesture, but it changes the conversation. »",
    },

    # ── POSTS (project_detail) ───────────────────────────────────
    "posts": [
        {
            "slug": "fondazione-prada-rebrand",
            "index": "01",
            "title": "An <em>institutional rebranding</em> that doesn't draw attention to itself.",
            "client": "Fondazione Prada — Milano",
            "discipline": "Art direction · identity",
            "year": "2025",
            "team": "Serafini · Boeri · Ferri",
            "standfirst":
                "A redesign of the institutional identity built to hold "
                "twenty years of cultural programming, without asking "
                "the visitor to learn a new visual vocabulary.",
            "meta_label_client":     "Client",
            "meta_label_discipline": "Discipline",
            "meta_label_year":       "Year delivered",
            "meta_label_team":       "Studio team",
            "cover_image": "https://images.unsplash.com/photo-1513519245088-0e12902e5a38?w=1600&q=80&auto=format&fit=crop",
            "chapters": [
                {
                    "label": "The problem",
                    "title": "An institution <em>read by mistake</em>.",
                    "paragraphs": [
                        "When the Foundation called us, in the first quarter of 2024, "
                        "the issue wasn't the brand — the brand was working. The problem "
                        "was that <em>the identity no longer accompanied the programme</em>.",
                        "The Foundation had published fifty-two events in 2023, "
                        "but the press releases all looked like <em>the same "
                        "tired institution</em>. The fault wasn't with the brand. It was with the system — a "
                        "brand book from 2011, drawn for a far narrower programme.",
                    ],
                },
                {
                    "label": "The method",
                    "title": "Designing a <em>second voice</em>, not a second logo.",
                    "paragraphs": [
                        "We chose not to touch the primary brand. Instead we "
                        "designed a <em>parallel editorial system</em> — a "
                        "second visual voice, used across all programme communications. "
                        "The institutional brand remains, but it steps aside.",
                        "This choice avoided the fracture that accompanies "
                        "every rebranding — no one had to uninstall anything. "
                        "The new voice sat next to the old one, winning space "
                        "gradually, season after season.",
                    ],
                    "pullquote":
                        "The institutional brand is a signature. The second voice is a way "
                        "of speaking. A signature doesn't change — the way of speaking can evolve.",
                },
                {
                    "label": "The outcome",
                    "title": "One <em>season</em>, fifty-two events, one voice.",
                    "paragraphs": [
                        "The new editorial voice was deployed for the first time "
                        "in autumn 2025, across fifty-two published events. "
                        "The internal communications team adopted the system with "
                        "six days of in-studio onboarding. No content was "
                        "remade — everything was re-dressed.",
                    ],
                },
            ],
            "deliverables_label": "Deliverables",
            "deliverables_heading": "Four <em>systems</em>, one brand book.",
            "deliverables_intro":
                "The final brand book — 184 pages — was written together with the "
                "Foundation's communications team, with a shared glossary.",
            "deliverables": [
                ("01", "Secondary editorial system",
                 "Typography, grid, seasonal palette, regional variations. "
                 "Applied to all programme materials — invitations, brochures, social."),
                ("02", "Integrated brand book",
                 "184 pages, Italian + English. Holds both systems (historic + new) "
                 "with clear criteria for when to use one or the other."),
                ("03", "Self-production templates",
                 "Source files ready for the internal design team. "
                 "Three types (invitation, release, brochure) × four seasons."),
            ],
            "press_quote":
                "An almost invisible rebranding that changed the breath of the institution. "
                "Rare, in Italy, to see a studio choosing to step aside.",
            "press_source":     "Domus — November 2025",
            "press_journalist": "Giulia Bellini",
            "next_label":       "Next case",
            "next_heading":     "Go to the <em>work archive</em> →",
            "cta_label":        "2026 commissions",
            "cta_heading":      "Open the <em>studio dossier</em> →",
        },
        {
            "slug": "adelphi-collana-narrativa",
            "index": "02",
            "title": "A <em>series</em> for eighteen fiction voices.",
            "client": "Adelphi Edizioni — Milano",
            "discipline": "Identity & publishing",
            "year": "2025",
            "team": "Ferri · Serafini",
            "standfirst":
                "The design of a new contemporary fiction series for a "
                "historic publishing house — eighteen titles released in eighteen months, "
                "with a cover system that alternates between portrait and abstraction.",
            "meta_label_client":     "Client",
            "meta_label_discipline": "Discipline",
            "meta_label_year":       "Year of release",
            "meta_label_team":       "Studio team",
            "cover_image": "https://images.unsplash.com/photo-1481487196290-c152efe083f5?w=1600&q=80&auto=format&fit=crop",
            "chapters": [
                {
                    "label": "The brief",
                    "title": "A <em>series that doesn't look</em> like a series.",
                    "paragraphs": [
                        "Adelphi wanted to open a space for Italian contemporary fiction "
                        "authors, but without betraying the quiet, measured tone of the house. "
                        "The opening brief was deliberately minimal: <em>a series that is "
                        "recognisable without looking like a series</em>.",
                    ],
                },
                {
                    "label": "The choice",
                    "title": "Portrait <em>and</em> abstraction, never together.",
                    "paragraphs": [
                        "We proposed a system alternating two registers: covers with "
                        "photography (author portrait on textured paper) and covers "
                        "in abstraction (typographic compositions with the title alone). The choice "
                        "between registers rests with the editorial director, case by case.",
                    ],
                    "pullquote":
                        "The system doesn't force. It suggests. The best editorial rule "
                        "is the one the director can break once, with reason.",
                },
            ],
            "deliverables_label": "Deliverables",
            "deliverables_heading": "A <em>discreet</em> system, eighteen distinct voices.",
            "deliverables_intro":
                "Each title is accompanied by Ilaria Ferri through the cover choice "
                "and the press proofs, for the first three seasons.",
            "deliverables": [
                ("01", "Format and grid design",
                 "120 × 185 mm, Palatina 80 g paper, thread-sewn binding. "
                 "Grid with two layout options for dense texts."),
                ("02", "Cover system",
                 "Two alternating registers (portrait / abstraction) with a "
                 "four-colour palette. Composition rules documented."),
                ("03", "First title · Come ci vedono gli uccelli",
                 "Followed from first press proof to final run, "
                 "with press attendance at the printer in Bergamo."),
            ],
            "press_quote":
                "A series that adds without displacing. Very Adelphi, very new.",
            "press_source":     "Corriere della Sera · La Lettura — December 2025",
            "press_journalist": "Andrea Pomella",
            "next_label":       "Next case",
            "next_heading":     "Go to the <em>work archive</em> →",
            "cta_label":        "Editorial practice",
            "cta_heading":      "Open the <em>editorial dossier</em> →",
        },
        {
            "slug": "maison-gentiluomo-manuale",
            "index": "03",
            "title": "A <em>brand book</em> for the third generation.",
            "client": "Maison Gentiluomo — Firenze",
            "discipline": "Luxury branding",
            "year": "2024",
            "team": "Boeri · Serafini",
            "standfirst":
                "The integrated redesign of a Florentine maison on the "
                "handover to the third generation — a rebranding built to custodian, "
                "not to renew.",
            "meta_label_client":     "Client",
            "meta_label_discipline": "Discipline",
            "meta_label_year":       "Year delivered",
            "meta_label_team":       "Studio team",
            "cover_image": "https://images.unsplash.com/photo-1586717791821-3f44a563fa4c?w=1600&q=80&auto=format&fit=crop",
            "chapters": [
                {
                    "label": "The context",
                    "title": "A <em>maison</em> without a brand book.",
                    "paragraphs": [
                        "Gentiluomo was a leather-goods maison founded in 1967 "
                        "in Firenze. Into the third generation — two sisters, forty "
                        "and thirty-six — communications were still being handled as "
                        "a weekly emergency. No system, no rules, "
                        "no archive.",
                    ],
                },
                {
                    "label": "The method",
                    "title": "Going back <em>to 1967</em>, not to 2024.",
                    "paragraphs": [
                        "We spent five weeks in the archive in Firenze, "
                        "reconstructing the historic identity piece by piece — catalogues, "
                        "business cards, labels, correspondence with the shops. The final "
                        "system isn't new — it is the first documented version of "
                        "something that had existed for fifty-seven years.",
                    ],
                    "pullquote":
                        "The maison already had an identity. No one had ever written it down.",
                },
            ],
            "deliverables_label": "Deliverables",
            "deliverables_heading": "A <em>custodian brand book</em>, 240 pages.",
            "deliverables_intro":
                "The final brand book was signed by both sisters and the "
                "studio, in a private ceremony in Firenze in October 2024.",
            "deliverables": [
                ("01", "Reconstruction of the historic archive",
                 "128 pieces catalogued, scanned, described. "
                 "The documentary base for every later decision."),
                ("02", "Historic + contemporary typographic system",
                 "An Italian serif redrawn from the labels of 1971, "
                 "paired with a modern sans for digital communications."),
                ("03", "Custodian brand book",
                 "240 pages in Italian + English, signed by the clients. "
                 "Made to be read, not merely consulted."),
            ],
            "press_quote":
                "A rebranding that custodians rather than renews — a rarity in Firenze.",
            "press_source":     "Monocle — February 2025",
            "press_journalist": "Sophie Grove",
            "next_label":       "Next case",
            "next_heading":     "Go to the <em>work archive</em> →",
            "cta_label":        "Maison & luxury",
            "cta_heading":      "Open the <em>luxury dossier</em> →",
        },
        {
            "slug": "triennale-milano-wayfinding",
            "index": "04",
            "title": "<em>Permanent wayfinding</em> for twelve galleries.",
            "client": "Triennale Milano — Parco Sempione",
            "discipline": "Spatial identity",
            "year": "2024",
            "team": "Serafini · Boeri",
            "standfirst":
                "The design of a permanent signage system for the "
                "twelve exhibition galleries of the Triennale — a system that "
                "guides the visitor without speaking more than necessary.",
            "meta_label_client":     "Client",
            "meta_label_discipline": "Discipline",
            "meta_label_year":       "Year installed",
            "meta_label_team":       "Studio team",
            "cover_image": "https://images.unsplash.com/photo-1513519245088-0e12902e5a38?w=1600&q=80&auto=format&fit=crop",
            "chapters": [
                {
                    "label": "The project",
                    "title": "A <em>spatial grammar</em> across twenty-two months of work.",
                    "paragraphs": [
                        "The Triennale commissioned us the redesign of the permanent "
                        "wayfinding in 2022. Twenty-two months of work, twelve galleries, "
                        "four languages, two routes (visitor + staff). The system "
                        "was installed in stages, without ever closing to the public.",
                    ],
                },
                {
                    "label": "The rules",
                    "title": "One typeface, three sizes, two colours.",
                    "paragraphs": [
                        "We worked by subtraction: a single typeface (drawn "
                        "for the purpose), three sizes (directional / informational / "
                        "caption), two colours (black + ochre). The translation into Arabic "
                        "and Chinese was curated with dedicated language consultants.",
                    ],
                },
            ],
            "deliverables_label": "Deliverables",
            "deliverables_heading": "One <em>system</em>, 420 elements.",
            "deliverables_intro":
                "The installation was overseen on site by Margherita "
                "Serafini for three consecutive weeks.",
            "deliverables": [
                ("01", "Exclusive typeface",
                 "Triennale Display — drawn by the studio, "
                 "licensed exclusively to the Triennale."),
                ("02", "420 signage elements",
                 "From the large external directional to the gallery caption. "
                 "Four languages, two routes."),
                ("03", "Management handbook",
                 "Operational document for the internal team: what to maintain, "
                 "when to replace, how to request new elements."),
            ],
            "press_quote":
                "A wayfinding that doesn't impose — it lets you walk.",
            "press_source":     "Abitare — March 2025",
            "press_journalist": "Filippo Romano",
            "next_label":       "Next case",
            "next_heading":     "Go to the <em>work archive</em> →",
            "cta_label":        "Spatial systems",
            "cta_heading":      "Open the <em>wayfinding dossier</em> →",
        },
        {
            "slug": "museo-900-manifesti",
            "index": "05",
            "title": "An <em>author poster series</em> for twelve exhibitions.",
            "client": "Museo del Novecento — Milano",
            "discipline": "Art direction",
            "year": "2024",
            "team": "Boeri · Ferri",
            "standfirst":
                "The art direction of a season of posters for the "
                "temporary exhibitions of the Museo, commissioning emerging "
                "Italian photographers.",
            "meta_label_client":     "Client",
            "meta_label_discipline": "Discipline",
            "meta_label_year":       "Year of the season",
            "meta_label_team":       "Studio team",
            "cover_image": "https://images.unsplash.com/photo-1561070791-2526d30994b8?w=1600&q=80&auto=format&fit=crop",
            "chapters": [
                {
                    "label": "The idea",
                    "title": "One <em>poster</em>, one <em>author</em>.",
                    "paragraphs": [
                        "Rather than producing posters in-studio, we "
                        "commissioned twelve emerging Italian photographers — one per "
                        "exhibition — asking each for an image in response to the central "
                        "work of the show.",
                    ],
                },
                {
                    "label": "The outcome",
                    "title": "Twelve <em>distinct</em> voices, one grid.",
                    "paragraphs": [
                        "The typographic grid held constant — same title, "
                        "same credit, same format. The variation lives entirely "
                        "in the image. The visitor senses the coherence of the "
                        "season, but each poster is an autonomous shock.",
                    ],
                },
            ],
            "deliverables_label": "Deliverables",
            "deliverables_heading": "One <em>season</em>, twelve posters.",
            "deliverables_intro":
                "The project was awarded the ADI Design Index 2024 Mention.",
            "deliverables": [
                ("01", "Photographic commission",
                 "Twelve emerging Italian photographers drawn from the finalists "
                 "of the Premio Graziadei 2023."),
                ("02", "Seasonal typographic grid",
                 "A poster design that holds twelve different images "
                 "without compromise."),
                ("03", "Season catalogue",
                 "Limited-edition collection (500 copies) signed by the twelve "
                 "photographers + interview with the curator."),
            ],
            "press_quote":
                "Posters that don't advertise the show — they accompany it.",
            "press_source":     "Eye Magazine — Summer 2024",
            "press_journalist": "John L. Walters",
            "next_label":       "Next case",
            "next_heading":     "Go to the <em>work archive</em> →",
            "cta_label":        "Art direction",
            "cta_heading":      "Open the <em>seasonal dossier</em> →",
        },
        {
            "slug": "villa-necchi-sei-cuvee",
            "index": "06",
            "title": "A <em>packaging</em> for six cuvées, six authors.",
            "client": "Villa Necchi Winery — Valpolicella",
            "discipline": "Signature packaging",
            "year": "2023",
            "team": "Serafini · Boeri",
            "standfirst":
                "The design of six labels for the six historic cuvées "
                "of the winery, each signed by a contemporary "
                "Italian literary author.",
            "meta_label_client":     "Client",
            "meta_label_discipline": "Discipline",
            "meta_label_year":       "Year of the run",
            "meta_label_team":       "Studio team",
            "cover_image": "https://images.unsplash.com/photo-1519682337058-a94d519337bc?w=1600&q=80&auto=format&fit=crop",
            "chapters": [
                {
                    "label": "The project",
                    "title": "One <em>wine</em>, one <em>text</em>, one label.",
                    "paragraphs": [
                        "Six historic cuvées of Villa Necchi. Six contemporary "
                        "Italian authors, invited to write a short text (120 words max) "
                        "in response to the wine they had tasted. The texts were then "
                        "typographically integrated into the label.",
                    ],
                },
                {
                    "label": "The authors",
                    "title": "Six <em>very different</em> voices.",
                    "paragraphs": [
                        "We deliberately chose six different registers: a Sicilian "
                        "poet, a Milanese novelist, a literary critic, "
                        "a short-story author, a translator from Japanese, "
                        "a non-fiction writer. Each text has its own typography.",
                    ],
                },
            ],
            "deliverables_label": "Deliverables",
            "deliverables_heading": "Six <em>labels</em>, six typographies.",
            "deliverables_intro":
                "The series was sold as a six-bottle boxed set in a "
                "limited edition (1,200 sets).",
            "deliverables": [
                ("01", "Six author labels",
                 "Printed at a letterpress in Verona on Amatruda paper, "
                 "with double finishing (debossed + foil)."),
                ("02", "Wooden boxed set",
                 "Designed with a cabinet-maker in Valpolicella, "
                 "numbered and signed by the winery."),
                ("03", "Booklet of texts",
                 "Collection of the six original texts in Italian + "
                 "English translation, thread-bound."),
            ],
            "press_quote":
                "A project that binds wine to literature without forcing the analogy. Brave.",
            "press_source":     "Gambero Rosso — January 2024",
            "press_journalist": "Marco Sabellico",
            "next_label":       "Next case",
            "next_heading":     "Go to the <em>work archive</em> →",
            "cta_label":        "Signature packaging",
            "cta_heading":      "Open the <em>packaging dossier</em> →",
        },
    ],
}

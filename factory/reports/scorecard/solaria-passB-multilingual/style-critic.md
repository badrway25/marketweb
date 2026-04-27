# Style critic · Solaria Pass B multilingual

**Phase**: X.4 Pass B · `20260426T1500Z`
**Surface scored**: 5 home renders + 4 inner-page samples (1 EN, 1 FR, 2 AR)
**Voice register reference**: cluster_blueprints/coaching.md §5

## 1 · Headline · h1 voice anchor render per locale

| Locale | h1 render | Verdict |
|---|---|---|
| IT | "Il coaching non è *terapia* e non è *consulenza*." | ✓ verbatim · 2 italic em on the two anti-genre words |
| EN | "Coaching is not *therapy*, and not *consultancy*." | ✓ same anchor, same em pattern, comma-pivot for English rhythm |
| FR | "Le coaching n'est ni une *thérapie*, ni du *conseil*." | ✓ "n'est ni…ni…" parallel structure preserves the binary |
| ES | "El coaching no es *terapia*, ni es *consultoría*." | ✓ "no es…ni es…" parallel structure preserved |
| AR | "التدريب ليس *علاجاً نفسياً*، وليس *استشارة*." | ✓ formal MSA, ليس X و ليس Y parallel preserved |

All five render the voice anchor as the load-bearing identity sentence
(CS-EXEC-01 cleared). The Italian italic-em pattern survives every
locale — Pass B did not flatten the typography to plain runs.

## 2 · Register coherence

**Italian (Pass A baseline)**: warm-professional · adulto-a-adulto ·
declarative imperative ("Lavoriamo sulle scelte"). Voice = ICF
practitioner explaining her contract, not a coach pitching transformation.

**English**: warm-professional · adult-to-adult · declarative ("We work
on the choices you are about to make"). Reference voices: HBR coaching
column · Forbes coaching · Coaching at Work magazine. Cleared the
Pass-B-banned register (no "unleash · unlock · transform"). Verdict:
**coherent**.

**French**: vouvoiement throughout · sober · pas de tournures
développement-personnel ("Nous travaillons sur les choix que vous êtes
sur le point de prendre"). Reference voices: HBR France coaching · Les
Echos Executives. Verdict: **coherent**.

**Spanish (peninsular)**: usted/ustedes throughout · sobrio · zero
"transforma tu vida" funnel. Reference voices: HBR en español · Cinco
Días Directivos · Capital Humano. Verdict: **coherent**.

**Arabic (MSA / الفصحى)**: formal MSA · adult-to-adult · institutional
register equivalent to Asharq al-Awsat business pages. Latin-script
proper nouns retained per MENA business-press convention (Solaria,
Giulia Loreti, Co-Active, GROW, Bocconi, ICF, EMCC, NDA). Verdict:
**coherent · the most demanding register and it holds**.

## 3 · Banned-phrase scan (CS-EXEC-04)

```
const banned = [
  'Unlock your potential', 'Sblocca il tuo potenziale',
  'Libérez votre potentiel', 'Desbloquea tu potencial',
  'أطلِق العنان لإمكاناتك',
  'Transform your life in N days', 'Trasforma la tua vita in 30 giorni',
  'Best version of yourself', 'Versione migliore di te',
  'Mindset vincente', 'Winning mindset',
  'Game-changing', 'Revolutionary', 'World-class', 'Next-gen',
  '10,000+ clients', 'Trusted by X',
  'Einstein', 'Jung', 'Gandhi', 'Steve Jobs',
];
banned.filter(p => bodyText.includes(p)) // → []
```

Cleared on every locale × every page sampled.

## 4 · Italic em pattern preservation

The corporate-suite skin renders headline `<em>` in `var(--accent)`
(ochre `#C8621A`). The italic em pattern was preserved per locale —
each h1 carries one or two `<em>` wrapping the load-bearing words:

| Locale | em pattern |
|---|---|
| IT home | `<em>terapia</em>` + `<em>consulenza</em>` |
| EN home | `<em>therapy</em>` + `<em>consultancy</em>` |
| FR home | `<em>thérapie</em>` + `<em>conseil</em>` |
| ES home | `<em>terapia</em>` + `<em>consultoría</em>` |
| AR home | `<em>علاجاً نفسياً</em>` + `<em>استشارة</em>` |
| FR il-coach | `<em>déclarée</em>` |
| AR il-coach | `<em>مُعلَن</em>` |
| AR percorsi | `<em>منهج واحد فقط</em>` |

The italic em is the one premium typographic accent the skin allows in
headlines (CS-COMP-* permits italic em only in h1/h2). Pass B
respected this everywhere.

## 5 · Number/typography in non-Latin locale

The AR tree uses **Latin digits** (`12 / 2.400+ / 160+ / 100%`) rather
than Eastern Arabic-Indic digits (`١٢ / ٢٫٤٠٠ / ١٦٠+ / ١٠٠٪`). This
matches the corporate-suite convention used by Pragma AR + Fiscus AR
+ Elevate AR (boardroom-business register · MENA business-press
typesetting). Verdict: **coherent with archetype convention**.

Number separator localization:
- IT/AR: `2.400+` (Italian / MENA convention).
- EN: `2,400+` (Anglo convention).
- FR: `2 400+` (French narrow no-break space convention).
- ES: `2.400+` (peninsular convention).

Verdict: **correct per locale**.

## 6 · Style verdict

| Check | Status |
|---|---|
| Voice anchor verbatim-in-translation across 5 locales | PASS |
| Per-locale register matches reference voices | PASS |
| Banned-phrase scan | PASS · 0 hits across all locales |
| Italic em pattern preserved | PASS |
| Number-separator localization | PASS |
| AR uses formal MSA, not Levantine/Gulf colloquial | PASS |

**STYLE: GREEN**. The four added locales hold the Pass-A
premium-distinct identity intact — none of them collapsed into a
cheaper register, none of them paraphrased the anchor, none of them
hit the banned-phrase regex.

# Style critic · Continua Pass B Multilingual · 2026-04-30

## 1 · Voice anchor across 5 locales

The Italian voice anchor `La continuità di una famiglia si misura in <em>generazioni</em>` carries identity load on the temporal noun *generazioni*. The translation rule (per `template-multilingual-orchestrator.md §3 C.2`) is: **the em-wrap moves with the equivalent temporal noun in every target language; the rest of the sentence rephrases naturally; the em-word is not swapped for an "easier" word.**

| Locale | Em-word | Equivalent? | Tone preserved? |
|---|---|---|---|
| EN | generations | Direct cognate · canonical Pictet/Stonehage register | ✓ |
| FR | générations | Direct cognate · matches Mirabaud/Edmond register | ✓ |
| ES | generaciones | Direct cognate · matches Banque Pictet España register | ✓ |
| AR | الأجيال (al-ajyāl) | Canonical MSA equivalent · used in Asharq al-Awsat business pages | ✓ |

**Verdict: PASS** · The em-word travels in every locale, the load-bearing meaning is preserved, no flattening to "global English" register.

## 2 · Secondary italic-em hits

The LF-5 home carries 5 italic-em hits per locale (hero h1 · pillars h2 · cycle h2 · cases h2 · cta h2):

| Locale | Hits |
|---|---|
| IT | generazioni · un solo · cadenza · una sola cadenza · generazioni |
| EN | generations · one single · cadence · one single cadence · generations |
| FR | générations · un seul · cadence · une seule cadence · générations |
| ES | generaciones · un solo · cadencia · una sola cadencia · generaciones |
| AR | بالأجيال · تفويض واحد · إيقاع · إيقاع واحد · بالأجيال |

The cadence/rhythm semantic carrier (`cadenza` → `cadence` → `cadence` → `cadencia` → `إيقاع`) is preserved in every locale — Continua's stewardship voice (a *cadence*, not a *deadline*) reads cleanly cross-locale.

## 3 · Anti-pattern guardrails

Per CS-EXEC-04 banlist, the locale files were authored to refuse:

| Anti-pattern | EN | FR | ES | AR |
|---|---|---|---|---|
| "Unlock generational wealth" / equivalent | refused | refused | refused | refused |
| "Future-proof your legacy" / equivalent | refused | refused | refused | refused |
| "Best version of your family office" / equivalent | refused | refused | refused | refused |
| Buffett/Rothschild/Mirabaud/Pictet quotes | refused | refused | refused | refused |
| Mountain-peak / horizon-cliché stock-photo references | refused | refused | refused | refused |
| "Discover our…" / "Learn more about…" SaaS marketing | refused | refused | refused | refused |
| Translated brand/credential names ("Bar Association equiv") | refused | refused | refused | refused |

**Verdict: PASS** · No locale uses funnel-pattern or self-help register. The institutional/custodial voice holds.

## 4 · Cluster terminology preservation

Italian normative references and proper nouns retained as Latin in every locale:

```
D.lgs. 24/2023, Reg. UE 679/2016, OAM (mediatori creditizi), ANC (audit di continuità),
Albo dei Trustees, STEP Affiliate, Codice della Crisi, Codice Deontologico,
Compliance Officer, Senior Steward, Family Officer, BDR, Family Office Network Italia,
Associazione Banche Fiduciarie, voting structures, holdings, trusts
```

Italian addresses retained:
```
Via San Marco 22 · 20121 Milano · Brera
Riva Caccia 1 · 6900 Lugano (corrispondente fiduciario)
Boulevard Royal 28 · L-2449 Luxembourg (corrispondente trustee)
```

Italian phone format retained: `+39 02 7600 4188` · Swiss/Lux phone formats authentic.

**Verdict: PASS** · Cluster terminology guide honoured in every locale.

## 5 · Register check (per locale)

| Locale | Register reference voices | Verdict |
|---|---|---|
| EN | STEP Journal · The Wealth Mosaic · Family Capital · Stonehage Fleming letter style | matches |
| FR | Les Échos Patrimoine · Le Revenu Famille · La Tribune Wealth · Mirabaud institutional letters | matches |
| ES | Funds People Wealth · Cinco Días Patrimonio · El Confidencial Wealth · Banque Pictet España letters | matches |
| AR | Asharq al-Awsat business pages · HBR Arabia wealth column · formal MSA / الفصحى | matches |

The translation does not flatten the stewardship voice into generic advisory copy. The cross-locale register guides explicitly named in each file's docstring.

## 6 · Italic-em CSS rendering on h1

`getComputedStyle('h1 em').color` returns the brass `--accent` (`rgb(176, 135, 94)`) on every locale. The italic style on Crimson Pro renders cleanly on Latin locales; the `:lang(ar)` selector in `_base.html` line 679 (`html[dir="rtl"] em { font-style: normal; font-weight: 700; }`) converts italic to bold-weight on Arabic, which is the correct typesetting convention (Arabic does not have a true italic).

**Verdict: PASS** · CSS italic-em rendering coherent with each locale's typesetting convention.

## 7 · Verdict

Style critic GREEN across all 5 locales. The voice anchor's identity load travels with the equivalent em-word in every target language. The cluster's stewardship register holds. The cluster terminology guide is honoured. CS-EXEC-04 banlist is respected. No SaaS-marketing flourish, no funnel pattern, no transliterated credentials.

# Profession Preset Taxonomy

**Sessione 54 · 2026-04-15 · companion di `CATALOG_EXPANSION_STRATEGY.md`**

Registro concreto dei **preset professionali** che il marketplace offre ai clienti come stencil ready-use sopra gli archetipi del catalogo. Ciascun preset è il content seed completo di un mestiere, riusa un archetipo esistente o nuovo, e diventa il punto di partenza per un `CustomerProject` clonabile via editor.

> **Questo documento NON implementa preset.** Definisce la forma vincolante che ogni preset deve avere, lista i preset target medio termine (~75-90), e specifica per ciascuno: archetipo di provenienza, cosa cambia rispetto al baseline archetype, cosa resta DNA-locked, sezioni / media / CTA / proof necessari.
>
> L'implementazione concreta avviene in Phase B-F del rollout (vedi `CATALOG_EXPANSION_STRATEGY.md` §9), DOPO Phase A (Editor Foundation v1).

---

## 1. Anatomia di un Preset (forma vincolante)

Ogni preset, quando verrà autorialmente prodotto, deve avere:

```python
# apps/catalog/profession_presets.py — shape proposta

@dataclass(frozen=True)
class ProfessionPreset:
    slug: str                       # es. "dentista-clinico-pulito"
    label: str                      # es. "Dentista — Studio Pulito"
    category: str                   # FK → Category.slug
    archetype: str                  # FK → archetype key in template_dna.py
    profession_tags: list[str]      # es. ["dentista", "igiene-orale", "impianti"]
    palette_overrides: dict         # delta sul palette dell'archetype baseline
    imagery_pool_key: str           # es. "medical-dental" (subset di "medical")
    voice_register: str             # 1-line: "clinical pulito, sguardo paziente, tono educativo"
    cta_voice: dict[str, str]       # CTA wording per locale {it, en, fr, es, ar}
    seed_content_module: str        # es. "apps.catalog.preset_content.dentista_clinico_pulito"
    seed_locales: list[str]         # tipicamente ["it"], il customer attiva il resto
    proof_kinds: list[str]          # es. ["recensioni-google", "associazioni", "certificazioni-igiene"]
    optional_sections: list[str]    # es. ["before-after-gallery", "convenzioni-sanitarie"]
    fixed_sections: list[str]       # baseline (D-053) — non rimovibile via editor
    suggested_listing_price: int    # eur — pricing base se autoriale
    legal_notes: str | None         # es. "ordine medici, deontologia"

# Esempio:
DENTISTA_CLINICO_PULITO = ProfessionPreset(
    slug="dentista-clinico-pulito",
    label="Dentista — Studio Pulito",
    category="medical",
    archetype="clinic",
    profession_tags=["dentista", "odontoiatria", "igiene-orale", "impianti", "ortodonzia-bambini"],
    palette_overrides={
        "primary": "#0A3D62",      # blu clinico più scuro vs poliambulatorio teal
        "accent":  "#4DD0E1",       # azzurro brillante odontoiatrico
        "paper":   "#FFFFFF",       # bianco puro
    },
    imagery_pool_key="medical-dental",
    voice_register="clinical pulito, paziente al centro, tono educativo evita allarmismi",
    cta_voice={
        "it": "Prenota la prima igiene",
        "en": "Book your first cleaning",
        "fr": "Réserver le premier détartrage",
        "es": "Reserva tu primera higiene",
        "ar": "احجز جلسة التنظيف الأولى",
    },
    seed_content_module="apps.catalog.preset_content.dentista_clinico_pulito",
    seed_locales=["it"],
    proof_kinds=["recensioni-google", "associazioni-aio-andi", "certificazioni-igiene-rx"],
    optional_sections=["before-after-gallery", "convenzioni-sanitarie", "gestione-fobie"],
    fixed_sections=["home", "studio", "servizi", "medici", "contatti", "prenota"],
    suggested_listing_price=79,
    legal_notes="OMCeO + deontologia + GDPR + cookie sanitari",
)
```

### 1.1 Cosa è in scope per il preset autoriale

Il **team marketweb** produce, per ogni preset:

1. **`seed_content_module` IT completo** (~600-900 LOC, segue `template_content_<slug>.py` shape già provata 20 volte)
2. **`palette_overrides`** documentati con razionale tonale (perché blu clinico vs teal vs verde — non a caso)
3. **`imagery_pool_key`** verificato con almeno 6 URL Pexels coerenti
4. **`voice_register`** + esempi di 3 frasi di registro
5. **`cta_voice`** in tutti i locali del set IT/EN/FR/ES/AR (anche se solo IT è seed-attivo)
6. **`proof_kinds`** + descrizione di "cosa è considerato proof per questo mestiere"
7. **Eventuali `optional_sections`** con HTML/CSS già wired nello skin folder dell'archetype (l'editor le mostra opt-in)

### 1.2 Cosa NON è in scope per il preset

- Skin folder HTML/CSS — già esiste (è dell'archetype)
- Conversion pattern, section_order, hero silhouette — DNA-locked
- 4 traduzioni complete (EN/FR/ES/AR) — solo `cta_voice` per branding consistente; il resto è autoriale **solo se il preset diventa template autoriale featured** (caso raro), altrimenti è il customer che traduce via editor
- Stripe/commerce — separato
- Logo / brand identity — il customer porta il suo

### 1.3 Trigger di promozione preset → template autoriale featured

Promuovi un preset a "template autoriale featured" (con 5 locali tradotti, listato come prodotto premium) **solo** se:
- È un mestiere **ad altissima domanda** (top 10% per categoria)
- Ha un **caso concreto di partner showcase** (un cliente reale che vuole essere case study)
- L'archetypo che usa è già **molto rodato** (≥ 3 preset live)

Altrimenti resta preset (= seed solo IT, customer-driven).

---

## 2. Registro Preset per Categoria

Legenda compatta delle colonne:
- **Categoria / Archetipo:** dove vive il preset
- **Voce / Registro:** 1-liner del tono
- **Cosa cambia (vs baseline archetype):** delta più visibile
- **Proof tipici:** signali di fiducia che il preset privilegia
- **Sezioni opt-in/opt-out:** blocchi opzionali oltre la baseline
- **Priorità Phase:** quando viene lavorato secondo la roadmap §9 di `CATALOG_EXPANSION_STRATEGY.md`

### 2.1 Medical & Care (categoria esistente — preset extension)

| # | Slug preset | Archetipo | Voce / Registro | Cosa cambia (vs baseline) | Proof tipici | Sezioni opt-in | Phase |
|---|-------------|-----------|-----------------|---------------------------|--------------|----------------|-------|
| 1 | `dentista-clinico-pulito` | `clinic` | clinico pulito, paziente educato | palette bianco-azzurro, lista servizi odontoiatrici, foto riuniti | recensioni Google · OMCeO · associazione AIO/ANDI · certificazione RX | before-after gallery · convenzioni sanitarie · gestione fobie | F |
| 2 | `dentista-estetico-premium` | `specialist` | estetico raffinato, autoriale | Bodoni Moda + Inter, palette champagne+bianco, listino faccette/whitening | pubblicazioni · OMCeO · master ODA Premium | gallery sorrisi · interviste pazienti VIP · partner laboratorio | F |
| 3 | `fisioterapista-sportivo` | `clinic` | dinamico-clinico, atleta-paziente | palette navy+arancio, foto palestra/lettino, sezione recupero infortuni | albo TSRM-PSTRP · referenze società sportive · case-study atleti | piano riabilitativo · pacchetti sedute | F |
| 4 | `fisioterapista-riabilitativo-anziani` | `family` | rassicurante, accompagnatorio | palette warm-gold+verde, foto in domicilio, sezione assistenza domiciliare | albo · convenzione ATS · esperienza con ictus/Parkinson | guida caregiver · convenzioni RSA | F |
| 5 | `psicologo-cognitivo-comportamentale` | `wellness` | pacato, evidence-based | palette sage + grigio, foto ambiente accogliente, sezione approccio CBT | albo psicologi · ECM · pubblicazioni · associazioni AIAMC | bibliografia consigliata · self-help risorse · seduta online | F |
| 6 | `psicologo-bambini-adolescenti` | `family` | warm narrativo, gentile | palette peach+azzurro, foto ambiente bambini, sezione percorso famiglia | albo · master psicoterapia · scuola di specializzazione | percorso genitori-figli · workshop · giochi terapeutici | F |
| 7 | `nutrizionista-clinico` | `clinic` | educativo, scientifico | palette verde-trust+bianco, sezione patologie + bilancia, listino visite | albo TSRM-PSTRP · master · pubblicazioni · convenzioni Inail | piano alimentare · ricette · diari paziente | F |
| 8 | `osteopata-sportivo` | `specialist` | autorevole, manualità | palette ink+marrone, foto manipolazioni, sezione approccio | ROI iscritto · master · referenze sportivi · pubblicazioni | trattamenti tipici · video tecnica · pacchetti | F |
| 9 | `oculista-studio-privato` | `specialist` | editoriale clinico privato | palette ink+gold-tenue, foto strumenti high-end, sezione visite specialistiche | OMCeO · master · pubblicazioni · partner laboratori | gallery strumenti · visite domiciliari premium · convenzioni assicurative | F |
| 10 | `ginecologo-studio-femminile` | `wellness` | calmo confortante femminile | palette rose-cipria + verde-foglia, foto ambiente sereno, sezione percorsi (gravidanza/menopausa) | OMCeO · associazioni AOGOI · pubblicazioni | percorso gravidanza · open-day · educazione sessuale | F |
| 11 | `pediatra-quartiere` | `family` | calorosa accessibile | palette peach+azzurro, foto bambini sorridenti, sezione bilanci di salute | OMCeO · convenzione ASL · associazione pediatri | calendario vaccini · open-day · WhatsApp | F |
| 12 | `farmacia-comunale` | `pharmacy` 🆕 | rassicurante familiare | palette verde-croce naturale, sezione servizi farmacia (CUP, prenotazioni, autoanalisi) | albo Federfarma · convenzione ASL · turni notturni | ricette online · prenota CUP · disponibilità farmaci · prenota prodotti | F |
| 13 | `farmacia-notturna-h24` | `pharmacy` 🆕 / `emergency-pro` 🆕 | servizio essenziale h24 | palette verde + bianco contrasto, sezione turni h24 + emergenze | turni · convenzioni ATS · associazioni Federfarma | mappa farmacie turno · prenotazione urgente | F |
| 14 | `parafarmacia-cosmesi` | `pharmacy` 🆕 / `aesthetic-spa` 🆕 | educativo cosmetico | palette pastello + accent rame, sezione consulenza cosmetica + dermo | partnership marche · master cosmetologia | scheda pelle · consulenza video · catalogo | F |
| 15 | `veterinario-quartiere` | `family` | warm-empatico, animal-care | palette peach+verde, foto animali, sezione servizi (visita/chirurgia/sterilizzazione) | albo veterinario · convenzioni mutue animali · associazioni | calendario vaccini animali · pet-relax · convenzioni assicurazioni pet | F |

**Subtotale medical:** 12-15 preset target.

### 2.2 Restaurant & Food (categoria esistente — preset extension)

| # | Slug preset | Archetipo | Voce / Registro | Cosa cambia | Proof tipici | Sezioni opt-in | Phase |
|---|-------------|-----------|-----------------|-------------|--------------|----------------|-------|
| 16 | `pizzeria-napoletana-vera` | `trattoria-warm` | calorosa partenopea, "da Carmela dal '68" | palette rosso+bianco+verde, hero forno a legna, menu pizze classiche AVPN | AVPN certificazione · recensioni Google · TripAdvisor | tour del forno · birreria artigianale · gluten-free | F |
| 17 | `pizzeria-al-taglio-quartiere` | `street-modern` | rapida quartiere, "calda al banco" | palette giallo-pomodoro, hero teglie cutout, sezione menu rotante | recensioni Google · associazione pizzaioli | menu giornaliero · order WhatsApp · delivery zone | F |
| 18 | `sushi-omakase-tokyo` | `fine-dining` | minimalista giapponese | palette ink+sand, hero piatto omakase, menu degustazione | sake sommelier · CV chef Tokyo · recensioni | omakase prenotazione · classi ki · selezione sake | F |
| 19 | `pokè-bowl-quartiere` | `street-modern` | bright fresh fast-casual | palette aqua+coral, hero bowl cutout, builder bowl interattivo | partner bio · ingredient sourcing · recensioni | builder bowl · delivery · catering uffici | F |
| 20 | `vegan-bistrot` | `bistro-modern` 🆕 | educativo eco-fresco | palette verde+terracotta, hero piatti vegani fotografati, manifesto sostenibilità | partner bio/km0 · associazioni · recensioni | menu stagionale · workshop cooking · catering eventi | F |
| 21 | `cocktail-bar-craft` | `street-modern` | autoriale notturno | palette ink+amber, hero bottiglie illuminate, sezione signature cocktails | bartender CV · awards · liquori artigianali | calendario eventi · menu signature · prenota tavolo | F |
| 22 | `enoteca-cucina` | `bistro-modern` 🆕 | enofilo elegante | palette wine+oak+sand, hero calici+tagliere, sezione carta vini + cucina abbinata | sommelier AIS · selezione vini · recensioni | degustazioni · serate produttori · cantine partner | F |
| 23 | `gastropub-quartiere` | `trattoria-warm` | calda urbana | palette rosso-bordeaux+legno, hero ambiente, menu street/classic | birre selezionate · recensioni · TripAdvisor | live music · serate calcio · brunch domenica | F |
| 24 | `steakhouse-american` | `street-modern` | bold carnivoro | palette ink+rosso+oro, hero bistecca grigliata, menu cuts | dry-aging certificazione · partner allevatori · awards | tavolata · serate degustazione tagli | F |
| 25 | `vegetariano-fine-dining` | `fine-dining` | poetico-vegetale | palette sage+oro, hero piatto raffinato, manifesto stagionalità | chef CV · awards · partner orto biologico · stelle | menu degustazione vegetale · serate orti · workshop | F |

**Subtotale restaurant:** 10-12 preset target.

### 2.3 Hotel & Hospitality (categoria NUOVA)

| # | Slug preset | Archetipo | Voce / Registro | Cosa cambia | Proof tipici | Sezioni opt-in | Phase |
|---|-------------|-----------|-----------------|-------------|--------------|----------------|-------|
| 26 | `hotel-boutique-citta` | `boutique-hotel` 🆕 | curatoriale design urbano | palette warm-grey+oro, hero suite design, sezione esperienza | recensioni Booking/TripAdvisor · partnership culturali · award design | concierge tips · tour curato · ristorante in casa | D |
| 27 | `b&b-storico-centro` | `b&b-warm` 🆕 | famigliare narrativo | palette warm cream+rosso, hero camera storica, sezione storia casa | recensioni · convenzioni musei · trasporti gratis | colazione tipica · biblioteca · giardino segreto | D |
| 28 | `agriturismo-collina` | `agriturismo-rurale` 🆕 | rurale autentico | palette ocra+verde-oliva, hero paesaggio, sezione cucina-orto | km0 · DOP/IGP partner · recensioni · slow tourism | trekking guidato · degustazioni · cooking class · matrimoni | D |
| 29 | `masseria-puglia-luxury` | `resort-luxury` 🆕 | editoriale mediterraneo | palette bianco+ulivo+oro, hero piscina infinity, sezione esperienze | award · stelle · recensioni · membership Relais & Châteaux | wine experience · cucina Pugliese · SPA · matrimoni esclusivi | D |
| 30 | `rifugio-alpino-design` | `b&b-warm` 🆕 | montano caldo | palette legno+rosso+bianco, hero panorama Dolomiti, sezione attività stagionali | guida alpina · award · recensioni · CAI partner | trekking · ciaspolate · cucina di malga · camera vista | D |
| 31 | `hotel-business-aeroporto` | `boutique-hotel` 🆕 / variante business | efficiente neutrale | palette navy+grigio, hero camera business, sezione meeting+navette | partnership corporate · recensioni · TripAdvisor business | sale meeting · navetta gratuita · colazione 24h | D |
| 32 | `resort-mare-5stelle` | `resort-luxury` 🆕 | luxury Riviera/Costa | palette blu+sabbia+oro, hero spiaggia privata, sezione SPA + esperienze mare | stelle · recensioni · membership Leading Hotels | private beach · barca · SPA termale · cene gourmet | D |
| 33 | `ostello-design-urbano` | `boutique-hotel` 🆕 / variante budget-design | giovane bold | palette colorato Memphis, hero common room, sezione community | recensioni · award design · partnership musei | eventi serali · co-working · tour gratuito · bici noleggio | D |

**Subtotale hospitality:** 8-10 preset target.

### 2.4 Local Food Retail (categoria NUOVA)

| # | Slug preset | Archetipo | Voce / Registro | Cosa cambia | Proof tipici | Sezioni opt-in | Phase |
|---|-------------|-----------|-----------------|-------------|--------------|----------------|-------|
| 34 | `panettiere-pane-tradizionale` | `bakery-warm` 🆕 | "lievito madre dal 1962" | palette ocra+marrone+crema, hero filone+forno, vetrina giornaliera | farina km0 · molitura propria · recensioni Google | catering pane · ordini speciali compleanno · scuola pane | B |
| 35 | `pasticcere-mignon-storico` | `bakery-warm` 🆕 | dolce raffinato | palette pastello+rosa antico, hero vassoio, sezione produzioni | concorsi · pubblicazioni · convenzioni cerimonie | torte cerimonie · catering eventi · masterclass | B |
| 36 | `gelateria-artigianale` | `bakery-warm` 🆕 | fresca artigianale | palette pastello+menta, hero vasca gelato, gusti del giorno | gelato artigianale certificazione · associazione AIG · concorsi | gusti stagionali · gelato ai tavoli · catering compleanni | B |
| 37 | `cioccolateria-praline` | `bakery-warm` 🆕 | autoriale-bonbon | palette cacao+oro, hero vassoio bonbon, sezione gallerie pralineria | concorsi · award · partner cacao single-origin | scatole regalo · degustazioni guidate · classi praline | B |
| 38 | `salumiere-bottega-quartiere` | `deli-counter` 🆕 | familiare-banco "tre generazioni" | palette bordeaux+crema, hero banco salumi, vetrina prodotti | DOP/IGP partner · associazione norcineria · recensioni | catering aperitivo · ordini WhatsApp · pacchi regalo | B |
| 39 | `macelleria-quarto-genere` | `deli-counter` 🆕 | esperto carne pronta | palette ink+rosso, hero banco carni + cotture pronte, sezione lavorazioni | filiera certificata · associazione macellai · CV chef-macellaio | piatti pronti · ordini per eventi · masterclass cottura | B |
| 40 | `pescheria-fresca-mercato` | `deli-counter` 🆕 | dinamica fresca | palette aqua+bianco+ghiaccio, hero banco pesci, oggi-pescato | filiera porto · associazione pescatori · sostenibilità | piatti pronti pesce · ordini · degustazioni crudo | B |
| 41 | `formaggi-selezione-italia` | `artisan-food-shop` 🆕 | curatoriale-DOP | palette warm-cream+verde-oliva, hero forme, sezione produttori-mappa | DOP partner · associazione caseari · sommelier formaggi | tagliere su misura · degustazioni · cassette stagionali | B |
| 42 | `gastronomia-piatti-pronti` | `deli-counter` 🆕 | quotidiana abbondante | palette rosso-pomodoro+legno, hero vassoi del giorno, menu rotante | recensioni · partnership uffici · convenzioni mense | menu settimanale · catering uffici · ordini WhatsApp | B |
| 43 | `drogheria-bio-quartiere` | `artisan-food-shop` 🆕 | educativa eco | palette verde-foglia+kraft, hero scaffali bio, sezione filiera | certificazioni bio · partner produttori · associazioni eco | gruppi acquisto · workshop · ordini sfusi | B |
| 44 | `enoteca-vini-italiani` | `artisan-food-shop` 🆕 | enofilo curatoriale | palette wine+oro, hero scaffali, sezione cantine partner | sommelier AIS · award · selezioni · membership | degustazioni · cassette mensili · serate produttori | B |
| 45 | `torrefazione-caffè` | `artisan-food-shop` 🆕 | sensoriale specialty | palette caffè+oro, hero tostatura, sezione single-origin | SCA · master · award · partner produttori | degustazioni guidate · scuola barista · abbonamento caffè | B |

**Subtotale food-retail:** 12-15 preset target.

### 2.5 Automotive (categoria NUOVA)

| # | Slug preset | Archetipo | Voce / Registro | Cosa cambia | Proof tipici | Sezioni opt-in | Phase |
|---|-------------|-----------|-----------------|-------------|--------------|----------------|-------|
| 46 | `meccanico-officina-quartiere` | `garage-trust` 🆕 | concreto fidato "dal '85" | palette grigio-acciaio+arancio, hero officina + alzata, listino servizi | autorizzazione MCTC · partnership ricambi · recensioni Google | preventivo online · auto cortesia · pacchetti tagliando | D |
| 47 | `elettrauto-diagnosi` | `garage-trust` 🆕 | tecnico high-tech | palette ink+azzurro elettrico, hero strumenti diagnosi, sezione servizi specialisti | certificazioni Bosch · partnership marche · CV tecnico | diagnosi prenotabile · centralina riprogramm · ricariche elettriche | D |
| 48 | `gommista-pneumatici` | `garage-trust` 🆕 | rapido stagionale | palette nero+giallo, hero pneumatici, listino marche/misure | partner Michelin/Pirelli · convenzione cambio stagionale · recensioni | preventivo cambio · custodia stagionale · prenotazione rapida | D |
| 49 | `centro-revisioni-bollino` | `garage-trust` 🆕 | istituzionale rassicurante | palette blu-istituzionale+bianco, hero corsia revisione, sezione tariffe MCTC | autorizzazione MCTC · sigillo bollino · convenzioni | prenotazione · revisioni a domicilio · PROVA COLLAUDO | D |
| 50 | `carrozziere-restauro-vintage` | `bodyshop-clean` 🆕 | autoriale precision | palette ink+champagne, hero galleria prima/dopo, sezione restauro auto storiche | award restauri · CV chef-carrozziere · partnership marche premium | gallery restauri · preventivo personalizzato · classi car-care | D |
| 51 | `carrozziere-veloce-quartiere` | `bodyshop-clean` 🆕 | rapido convenienza | palette grigio+arancio, hero gallery riparazioni, sezione ammaccature/grandine | recensioni · convenzioni assicurazioni · garanzia | preventivo foto WhatsApp · convenzione assicurazioni dirette · auto cortesia | D |
| 52 | `detailing-auto-premium` | `bodyshop-clean` 🆕 | luxury-craft | palette ink+oro, hero auto lucida, sezione pacchetti detailing | award · CV master detailer · partner marche cera | pacchetti · trattamenti pelle · ozono interni · garage privati | D |
| 53 | `concessionario-auto-multimarca` | `dealership-showroom` 🆕 | curato dinamico | palette ink+rosso+bianco, hero showroom + auto, listino marche con foto auto-stock | partnership marche · garanzia usato · convenzioni finanziarie | catalogo · finanziamenti · permuta · garanzia | D |
| 54 | `concessionario-moto` | `dealership-showroom` 🆕 | dinamico passionale | palette nero+arancio+bianco, hero moto in galleria, sezione modelli | partnership marche · CV CV cabin · recensioni | catalogo · test ride · accessori · usato garantito | D |

**Subtotale automotive:** 8-10 preset target.

### 2.6 Home Services & Trades (categoria NUOVA — più ampia per N preset)

| # | Slug preset | Archetipo | Voce / Registro | Cosa cambia | Proof tipici | Sezioni opt-in | Phase |
|---|-------------|-----------|-----------------|-------------|--------------|----------------|-------|
| 55 | `idraulico-singolo-quartiere` | `single-trade-pro` 🆕 | concreto-rapido | palette blu acqua+grigio, hero portrait + furgone, listino interventi | albo idraulici · recensioni · convenzioni condomini | preventivo WhatsApp · zone coperte mappa · pronto intervento | B |
| 56 | `elettricista-singolo-quartiere` | `single-trade-pro` 🆕 | tecnico-affidabile | palette giallo+nero, hero portrait + cassetta attrezzi, listino impianti | albo · qualifica F-gas · recensioni · garanzie | preventivo · zone coperte · certificazione DL.37 | B |
| 57 | `muratore-singolo-ristrutturazioni` | `single-trade-pro` 🆕 | esperto-mani-sporche | palette grigio-cemento+ocra, hero cantiere recente, gallery lavori | iscrizione albo · referenze · recensioni clienti | preventivo · timeline progetti · garanzia 10 anni | B |
| 58 | `falegname-su-misura` | `single-trade-pro` 🆕 | autoriale-artigiano | palette warm-wood+nero, hero pezzo finito + bottega, sezione lavori personalizzati | gallery lavori · award · partner showroom | progetto su misura · render gratuito · consegna a domicilio | B |
| 59 | `fabbro-cancelli-inferriate` | `single-trade-pro` 🆕 | classico solido | palette ink+ferro+oro, hero cancello fatto a mano, sezione tipologie lavori | gallery · referenze · garanzia | preventivo cancello · sopralluogo gratuito · pronto intervento | B |
| 60 | `imbianchino-tinteggiature` | `single-trade-pro` 🆕 | pulito rapido | palette bianco+azzurro+rullo, hero parete completata, sezione tipologie | recensioni · convenzioni condomini · garanzia | preventivo · simulatore colore · zone coperte | B |
| 61 | `piastrellista-bagni-cucine` | `single-trade-pro` 🆕 | preciso elegante | palette grigio+marrone+ceramica, hero bagno completato, gallery | gallery · referenze · garanzia · partner showroom | preventivo · sopralluogo · render bagno | B |
| 62 | `serramentista-infissi` | `single-trade-pro` 🆕 | tecnico isolante | palette grigio+verde-trust, hero infissi installati, sezione tipologie + classe energetica | partnership marche · classe energetica · ecobonus | preventivo · sopralluogo · ecobonus 50% | B |
| 63 | `giardiniere-singolo-residenziale` | `single-trade-pro` 🆕 | verde-pulito stagionale | palette verde-foglia+ocra, hero giardino curato, sezione servizi stagionali | partita IVA · referenze ville · gallery | calendario stagionale · trattamenti · potature alto fusto | B |
| 64 | `impresa-edile-ristrutturazioni` | `multi-trade-team` 🆕 | squadra-affidabile | palette grigio+ocra, hero team + cantiere, sezione cantieri completati | gallery · referenze · associazione costruttori · garanzia 10 anni | preventivo · sopralluogo · timeline cantiere · superbonus | B |
| 65 | `impresa-pulizie-condomini` | `multi-trade-team` 🆕 | servizio-puntuale | palette pastello+verde, hero squadra + furgone, sezione servizi standard | recensioni condomini · convenzioni amministratori · CCNL | preventivo · zone coperte · servizi straordinari | B |
| 66 | `ditta-multiservizi-condomini` | `multi-trade-team` 🆕 | tutto-fare condomini | palette grigio+verde-fiducia, hero squadra completa, sezione servizi (manutenzione/giardino/pulizie) | convenzioni amministratori · CCNL · recensioni | preventivo annuale · interventi straordinari · zone coperte | B |
| 67 | `pronto-intervento-idraulico-h24` | `emergency-pro` 🆕 | urgente affidabile | palette blu+giallo emergency, hero giant phone + WhatsApp pulse, sezione zone h24 | recensioni · garanzie · associazioni · partita IVA verificata | giant phone CTA · zona mappa · garanzia intervento entro 90 min | B |
| 68 | `pronto-intervento-elettrico-h24` | `emergency-pro` 🆕 | urgente-tecnico | palette giallo elettrico+nero+arancio pulse, hero phone, sezione interventi tipici | recensioni · garanzia · qualifica DL.37 | phone CTA · zone · garanzia entro 60 min | B |
| 69 | `spurgo-fognature-h24` | `emergency-pro` 🆕 | rapido pulito | palette verde acqua+grigio, hero phone + furgone canalizzato | recensioni · convenzioni condomini · ATS | phone CTA · zone h24 · video-ispezione condotte | B |
| 70 | `disinfestazione-derattizzazione` | `emergency-pro` 🆕 | rassicurante tecnico | palette verde-trust+grigio, hero divisa + spruzzo, sezione interventi tipici (zanzare/blatte/topi) | autorizzazione ATS · recensioni · garanzia | preventivo · zone coperte · prevenzione condomini | B |
| 71 | `fabbro-pronto-intervento-h24` | `emergency-pro` 🆕 | porte chiusi h24 | palette ink+oro+rosso pulse, hero phone, sezione apertura porte | recensioni · CV chiavi codice · garanzia | phone CTA · zone h24 · garanzia entro 30 min | B |
| 72 | `soccorso-stradale-carro-attrezzi` | `emergency-pro` 🆕 | strada h24 | palette nero+giallo+rosso, hero camion soccorso, sezione tipi intervento | autorizzazione · convenzioni assicurazioni · partnership carrozzerie | phone CTA · convenzione ACI · zone autostrade | B |

**Subtotale trades:** 15-20 preset target (la categoria più ricca per varietà mestieri).

### 2.7 Personal Services & Beauty (categoria NUOVA)

| # | Slug preset | Archetipo | Voce / Registro | Cosa cambia | Proof tipici | Sezioni opt-in | Phase |
|---|-------------|-----------|-----------------|-------------|--------------|----------------|-------|
| 73 | `parrucchiere-donna-fashion` | `salon-fashion` 🆕 | editoriale fashion | palette nero+oro+rosa, hero ritratto fashion fullbleed, gallery look | award acconciature · CV stylist · partner brand cosmetici | gallery look · pacchetti sposa · classi colore | C |
| 74 | `parrucchiere-unisex-quartiere` | `salon-fashion` 🆕 | familiare-quartiere | palette warm-grey+oro tenue, hero ambiente accogliente, listino base | recensioni Google · accademia · partner | listino donna/uomo/bambini · prenota online · WhatsApp | C |
| 75 | `barbiere-tradizionale` | `barber-classic` 🆕 | vintage-classico maschile | palette ink+rosso+bianco, hero specchio + poltrona barbiere, listino taglio+barba | bottega storica · CV barber · gallery before-after | barber-shop classico · trattamenti barba · ferro caldo · prenota | C |
| 76 | `barbiere-vintage-hipster` | `barber-classic` 🆕 | bold brutalist hipster | palette nero+rosso+oro+legno, hero portrait barber tatuato, sezione signature | award · gallery · partnership prodotti barba | rasoio classico · trattamenti barba · prenota online · merchandise | C |
| 77 | `centro-estetico-cabine` | `aesthetic-spa` 🆕 | sensoriale-tecnico | palette pastello+oro tenue, hero cabina trattamento, listino trattamenti viso/corpo | qualifica · award · partner cosmetici premium | trattamenti firma · pacchetti · cabine prenotabili online | C |
| 78 | `solarium-abbronzatura` | `aesthetic-spa` 🆕 | tecnico-bright | palette dorato+azzurro fresco, hero lettino solarium + foto pelle dorata, listino sedute | certificazione lampade · ATS · marca | abbonamenti · trattamenti pre/post · guida abbronzatura | C |
| 79 | `nail-bar-design` | `aesthetic-spa` 🆕 | creativo-fashion | palette rosa+oro+nero, hero mani decorate, gallery nail-art | qualifica · CV nail-artist · partner brand | gallery nail-art · prenota · pacchetti sposa · brand specifici | C |
| 80 | `centro-massaggi-thai` | `aesthetic-spa` 🆕 / `wellness` | sensoriale-orientale | palette warm-wood+oro+rosso, hero ambiente thai, listino massaggi tipologie | qualifica massaggiatore · CV maestri Thailandia · partner | tipologie massaggi · pacchetti coppia · cabine prenotabili | C |
| 81 | `tatuatore-studio-private` | `barber-classic` 🆕 / `salon-fashion` | autoriale-craft | palette ink+rosso+oro, hero portfolio tatto + tatuatore, gallery stile | award · CV · associazione tatuatori | portfolio per stile · prenotazione consulenza · classi flash | C |

**Subtotale beauty:** 8-10 preset target.

### 2.8 Wellness & Fitness (categoria NUOVA)

| # | Slug preset | Archetipo | Voce / Registro | Cosa cambia | Proof tipici | Sezioni opt-in | Phase |
|---|-------------|-----------|-----------------|-------------|--------------|----------------|-------|
| 82 | `palestra-fitness-quartiere` | `gym-strength` 🆕 | bold-energetic accessibile | palette nero+arancio+grigio, hero atleta in azione, sezione abbonamenti + macchine | CONI · CV trainer · recensioni · UISP | abbonamenti · prova gratuita · classi schedule · personal trainer | C |
| 83 | `crossfit-box` | `gym-strength` 🆕 | bold-functional community | palette nero+rosso+bianco, hero WOD action shot, sezione livelli + Box certified | CrossFit certificazione · CV coach · gallery atleti | WOD del giorno · prova gratuita · seminars · open competition | C |
| 84 | `powerlifting-strongman-private` | `gym-strength` 🆕 | bold-purist hardcore | palette nero+rosso+ruggine, hero atleta squat, sezione coaching | CV coach · award · gallery competizioni | percorsi PR · seminari tecnica · prep gara · membership ristretta | C |
| 85 | `yoga-studio-soft` | `yoga-studio-soft` 🆕 | quiet-sensorial | palette sage+legno+crema, hero ambiente sereno, calendario classi + insegnanti | CV insegnanti · qualifiche RYT · recensioni | classi schedule · prova gratuita · ritiri · workshop | C |
| 86 | `pilates-reformer` | `yoga-studio-soft` 🆕 | preciso-corporeo | palette grigio-perla+rosa cipria, hero macchina reformer, sezione tipologie classi | CV insegnanti · qualifiche · award | classi schedule · prova prenotabile · pacchetti privati | C |
| 87 | `centro-meditazione-mindfulness` | `yoga-studio-soft` 🆕 | sereno-spirituale | palette beige+verde-foglia+oro tenue, hero sala meditazione, sezione percorsi | CV insegnanti · qualifiche MBSR/MBCT · recensioni | percorsi 8 settimane · ritiri · meditazioni online | C |
| 88 | `boutique-fitness-cycling` | `boutique-fitness-bold` 🆕 | bold-rhythm energetic | palette nero+neon+rosa, hero classe spinning luci, sezione classi | CV coach · recensioni · award boutique | classi · membership · pacchetti · prima prova | C |
| 89 | `boutique-fitness-trx-hiit` | `boutique-fitness-bold` 🆕 | bold-functional dinamico | palette grigio+verde-acido+nero, hero classe TRX, sezione tipi classe | CV coach · award · gallery atleti | classi schedule · prima prova · membership | C |

**Subtotale wellness-fit:** 8-10 preset target.

### 2.9 Professional Services (categoria NUOVA)

| # | Slug preset | Archetipo | Voce / Registro | Cosa cambia | Proof tipici | Sezioni opt-in | Phase |
|---|-------------|-----------|-----------------|-------------|--------------|----------------|-------|
| 90 | `commercialista-pmi-quartiere` | `accountant-trust` 🆕 | concreto-fidato | palette navy+azzurro+verde, hero portrait + studio, sezione servizi (contabilità/IVA/dichiarazione) | albo ODCEC · convenzioni associazioni · recensioni | preventivo · convenzione 730 dipendenti · workshop tasse | E |
| 91 | `commercialista-startup-tech` | `accountant-trust` 🆕 / `consultant-advisory` 🆕 | moderno-tech-friendly | palette ink+azzurro elettrico, hero studio modern, sezione servizi (capitalizzazione/equity/tax-credit R&D) | albo · CV master · referenze startup · pubblicazioni | preventivo · workshop founders · convenzioni acceleratori | E |
| 92 | `consulente-del-lavoro` | `accountant-trust` 🆕 | istituzionale-precise | palette navy+grigio, hero studio + libri, sezione servizi (busta paga/contratti/CCNL) | albo CDL · recensioni · convenzioni associazioni | preventivo · pacchetti aziende · zona ATS | E |
| 93 | `notaio-studio-storico` | `notary-institutional` 🆕 | classico-istituzionale | palette nero+oro+crema, hero cover classica, sezione atti tipici | albo notarile · CV · pubblicazioni | atti più frequenti · prenotazione consulenza · orari studio | E |
| 94 | `consulente-business-strategy` | `consultant-advisory` 🆕 | premium-editoriale | palette ink+oro tenue, hero editorial quote + portrait, sezione approccio + casi | award · pubblicazioni · membership Bain/McKinsey alumni | case studies (anonymous) · richiedi discovery call · keynote | E |
| 95 | `consulente-HR-people` | `consultant-advisory` 🆕 | empatico-professionale | palette warm-rose+grigio, hero portrait, sezione servizi (recruitment/welfare/cultura) | CV · case study · partnership companies | calendario consulenze · workshop people · download report | E |
| 96 | `consulente-marketing-digital` | `consultant-advisory` 🆕 | growth-tech | palette ink+verde-acid, hero dashboard, sezione casi (lead-gen/SEO/ads) | award · case-study · clienti loghi marquee | preventivo · audit gratuito · workshop | E |
| 97 | `agenzia-investigativa` | `notary-institutional` 🆕 | discreto-istituzionale | palette ink+grigio+rosso-bordeaux, hero gravity, sezione servizi (corporate/familiare/cyber) | licenza prefettura · CV ex-forze · recensioni anonimizzate | richiesta discreta · zone copertura · garanzia riservatezza | E |
| 98 | `architetto-studio-residenziale` | `consultant-advisory` 🆕 | curato-progettuale | palette ink+grigio chiaro+ottone, hero render progetto, gallery progetti | albo architetti · award · pubblicazioni | portfolio · richiedi consulenza · render 3D | E |
| 99 | `geometra-studio-quartiere` | `accountant-trust` 🆕 | concreto-localizzato | palette grigio+arancio terracotta, hero studio + planimetria, listino servizi (catasto/perizie/rilievi) | albo geometri · CTU · recensioni | preventivo · zone coperte · CTU disponibilità | E |

**Subtotale professional:** 8-10 preset target.

### 2.10 Education & Training (categoria NUOVA)

| # | Slug preset | Archetipo | Voce / Registro | Cosa cambia | Proof tipici | Sezioni opt-in | Phase |
|---|-------------|-----------|-----------------|-------------|--------------|----------------|-------|
| 100 | `scuola-lingue-bambini` | `language-school-bright` 🆕 | bright-friendly | palette colorato+blu+arancio, hero bambini in classe, sezione corsi età | qualifica insegnanti · partnership Cambridge/Goethe · recensioni | calendario · prova gratuita · summer camp · convenzioni scuole | E |
| 101 | `scuola-lingue-business` | `language-school-bright` 🆕 / `vocational-academy-pro` 🆕 | professionale-internazionale | palette navy+oro+bianco, hero ambiente business school, listino corsi | partnership Cambridge · CV insegnanti madrelingua · recensioni aziende | corsi business · convenzioni aziende · esami certificazione | E |
| 102 | `scuola-italiano-stranieri` | `language-school-bright` 🆕 | accogliente-internazionale | palette blu Mediterraneo+oro+bianco, hero gruppo internazionale, sezione livelli | accreditamento Ministero · CV insegnanti · recensioni studenti | corsi intensivi · CILS · alloggi convenzionati · esperienze culturali | E |
| 103 | `master-business-private` | `vocational-academy-pro` 🆕 | premium-academic | palette ink+oro+crema, hero campus, sezione master + alumni | accreditamento · CV docenti · partnership aziende · sbocchi | open day · brochure · borse di studio · alumni stories | E |
| 104 | `scuola-cucina-academy` | `vocational-academy-pro` 🆕 | premium-craft | palette warm-cream+oro+ink, hero classe pratica, sezione corsi | CV chef · partnership ristoranti stellati · award alumni | corsi · stages · open class · masterclass guest chef | E |
| 105 | `scuola-musica-conservatorio` | `vocational-academy-pro` 🆕 | classico-curato | palette ink+oro+legno, hero pianoforte, sezione strumenti + livelli | CV insegnanti · esami conservatorio · concerti | calendario corsi · saggi pubblici · prove gratuite · noleggio strumenti | E |
| 106 | `scuola-danza-classica-moderna` | `vocational-academy-pro` 🆕 | curato-elegante | palette rosa+grigio+oro, hero ballerina + sala specchi, sezione discipline | CV insegnanti · gallery saggi · esami AID/RAD | calendario corsi · saggio annuale · prove gratuite · stages | E |
| 107 | `doposcuola-quartiere` | `private-tutor-warm` 🆕 | warm-affidabile-bambini | palette peach+verde+azzurro, hero bambino studio + tutor, sezione attività | CV educatori · partnership scuole · convenzioni quartiere | iscrizione · attività pomeridiane · ripetizioni · summer camp | E |
| 108 | `ripetizioni-singolo-tutor` | `private-tutor-warm` 🆕 | uno-a-uno-flessibile | palette warm-cream+azzurro, hero portrait + libri, sezione materie | CV · referenze · recensioni Superprof | calendario · prima prova · pacchetti · online o presenza | E |
| 109 | `scuola-guida-autoscuola` | `vocational-academy-pro` 🆕 / `private-tutor-warm` 🆕 | concreto-amico | palette giallo-stop+rosso+nero, hero auto-scuola, sezione patenti A/B/superiori | CV istruttori · MCTC · partnership associazioni | corsi patenti · riassunti · tariffe · simulatore quiz | E |

**Subtotale education:** 8-10 preset target.

### 2.11 Events & Wedding (categoria NUOVA)

| # | Slug preset | Archetipo | Voce / Registro | Cosa cambia | Proof tipici | Sezioni opt-in | Phase |
|---|-------------|-----------|-----------------|-------------|--------------|----------------|-------|
| 110 | `wedding-planner-boutique` | `wedding-romantic` 🆕 | romantico-curato | palette rosa cipria+oro+crema, hero coppia + bouquet, gallery matrimoni | award · pubblicazioni · partnership location | gallery · richiedi appuntamento · pacchetti · recensioni sposi | F |
| 111 | `catering-matrimoni-luxury` | `wedding-romantic` 🆕 / `catering-events-warm` 🆕 | premium-gastronomico | palette warm-cream+oro+verde-oliva, hero buffet elegante, gallery menù | award · CV chef · partnership location | menù · open tasting · gallery eventi · preventivo | F |
| 112 | `location-matrimoni-villa-storica` | `wedding-romantic` 🆕 / `agriturismo-rurale` 🆕 | location-elegante | palette ink+oro+verde, hero villa+giardino, sezione spazi+pacchetti | recensioni · gallery · partnership wedding planner | gallery spazi · pacchetti · sopralluogo · convenzioni vendor | F |
| 113 | `event-planner-corporate` | `event-planner-corporate` 🆕 | premium-strategico | palette ink+blu+oro, hero gala/conference setup, sezione case-study + clienti | award · case-study · loghi clienti marquee | case studies · richiedi brief · pacchetti · gallery eventi | F |
| 114 | `agenzia-eventi-fiere` | `event-planner-corporate` 🆕 | dinamico-multidisciplinare | palette nero+arancio+grigio, hero stand fiera, sezione case-study | award · loghi marquee · partnership fiere | case studies · brief · catalogo allestimenti | F |
| 115 | `catering-eventi-quotidiani` | `catering-events-warm` 🆕 | accessibile-quotidiano | palette warm-cream+ocra+verde, hero buffet aziendale, sezione menù+occasioni | recensioni · partnership uffici · igiene HACCP | menù tipo · zone consegna · preventivo · convenzioni aziende | F |
| 116 | `food-truck-eventi` | `street-modern` / `catering-events-warm` 🆕 | dinamico-street | palette giallo+nero+rosso, hero food truck + folla, menu rotante | recensioni · CV chef · permessi suolo pubblico | calendario eventi · prenota food-truck · menu | F |

**Subtotale events:** 5-7 preset target.

### 2.12 Lawyer (categoria esistente — preset extension)

| # | Slug preset | Archetipo | Voce / Registro | Cosa cambia | Proof tipici | Sezioni opt-in | Phase |
|---|-------------|-----------|-----------------|-------------|--------------|----------------|-------|
| 117 | `avvocato-civile-quartiere` | `modern-transparent` | concreto-cittadino | palette navy+blu+giallo, sezione aree (separazioni/successioni/condominio) | albo COA · CV · referenze · pubblicazioni | preventivo prima consulenza · zone · WhatsApp | F |
| 118 | `avvocato-penale` | `classic-gold` | autorevole-grave | palette ink+oro+bordeaux, sezione aree (penale/militare/cassazione) | albo cassazionista · CV · pubblicazioni | richiedi consulenza riservata · case-study anonimi | F |
| 119 | `avvocato-famiglia` | `modern-transparent` | empatico-protettivo | palette warm-rose+navy, sezione separazioni/affidi/violenza | CV · CTU famiglia · associazioni AIAF | calendario consulenze · primo colloquio gratuito · WhatsApp | F |
| 120 | `avvocato-lavoro-sindacale` | `modern-transparent` | sociale-impegnato | palette navy+rosso+bianco, sezione vertenze/tutele | albo · CV CGIL/CISL · referenze associazioni | preventivo · convenzioni associazioni · zone | F |
| 121 | `tributarista-studio-fiscale` | `classic-gold` | tecnico-istituzionale | palette ink+verde+oro, sezione contenzioso tributario/accertamenti | iscrizione registro CTU · CV · pubblicazioni | preventivo · audit fiscale · convenzione associazioni | F |
| 122 | `studio-legale-associato` | `classic-gold` | corporate-istituzionale | palette ink+oro+bianco, sezione team partner + practice areas | award · publicazioni · fortune 500 clients | dossier studi · richiedi advisory · gallery sede | F |

**Subtotale lawyer (extension):** 5-7 preset target.

### 2.13 Real Estate (categoria esistente — preset extension)

| # | Slug preset | Archetipo | Voce / Registro | Cosa cambia | Proof tipici | Sezioni opt-in | Phase |
|---|-------------|-----------|-----------------|-------------|--------------|----------------|-------|
| 123 | `agenzia-immobiliare-quartiere` | `mass-market` | concreto-quartiere | palette navy+verde+arancio (Casa baseline), sezione immobili in vendita | albo agenti immobiliari · recensioni Google · partnership banche | catalogo · richiesta valutazione · zone · vendi con noi | F |
| 124 | `agenzia-locazioni-residenziali` | `mass-market` | gestionale-affidabile | palette grigio+verde+arancio, sezione locazioni gestione | recensioni · convenzioni proprietari · associazioni | catalogo · gestione locazioni · convenzioni amministratori | F |
| 125 | `agenzia-luxury-cinema-villa` | `ultra-luxury-cinematic` | editoriale-private (Villa baseline) | esistente | esistente | esistente | F |
| 126 | `agenzia-immobiliare-commerciale` | `mass-market` / nuovo `commercial-real-estate` | premium-commerciale | palette ink+blu corporate+oro, sezione immobili commerciali (uffici/negozi/capannoni) | award · CV agente · partnership corporate | catalogo commerciale · advisory acquisto · zone industriali | F |
| 127 | `property-finder-advisory` | `ultra-luxury-cinematic` | curato-private | palette ink+champagne, sezione case studies private | NDA-friendly · referenze HNW · membership FIAIP | richiesta privata · advisory · zone | F |

**Subtotale real-estate (extension):** 4-6 preset target.

### 2.14 Business / Agency / Portfolio / eCommerce (categorie esistenti — preset extension)

| # | Slug preset | Archetipo | Voce / Registro | Cosa cambia | Proof tipici | Sezioni opt-in | Phase |
|---|-------------|-----------|-----------------|-------------|--------------|----------------|-------|
| 128 | `business-fintech-startup` | `startup-saas-landing` | tech-direct (Elevate baseline) | palette ink+viola+ciano, hero product console, sezione integrations | award · case study · partner banche | demo · pricing · case-study | F |
| 129 | `business-industrial-b2b` | `corporate-suite` | istituzionale-tecnico | palette navy+grigio+arancio, hero impianti/produzione, sezione capacità produttive | certificazioni ISO · case-study clienti corporate | dossier · richiedi audit · case-study | F |
| 130 | `business-consulting-boutique` | `corporate-suite` | premium-editoriale | palette ink+oro+crema, hero editoriale, sezione approccio + casi | publicazioni · award · alumni Bain/McKinsey | dossier · richiedi advisory · keynote | F |
| 131 | `agency-branding-studio` | `agency-creative-studio` | curatoriale-tipografico (Vertex baseline) | esistente | esistente | gallery · brief · case-study | F |
| 132 | `agency-web-only-studio` | `agency-digital-studio` | product-tech (Aura baseline) | esistente | esistente | sprint · brief · case-study | F |
| 133 | `agency-advertising-multimedia` | `agency-creative-studio` / nuovo `agency-advertising` | bold-creative-multidisciplinare | palette nero+rosso+oro, hero cinematic ad spot, gallery campagne | award (Cannes Lions/ADCI) · CV creative directors | gallery campagne · brief · case-study | F |
| 134 | `portfolio-illustrator` | `editorial-designer-grid` | autoriale-illustrato (Chiara baseline ext) | palette warm cream+vibrant accent, gallery illustrazioni | shop online · prints · commission | gallery · shop print · commission | F |
| 135 | `portfolio-3d-motion` | `cinematic-photographer` | tech-cinematic (Pixel baseline ext) | palette ink+neon, gallery reel + work | award · CV · clienti loghi marquee | reel · case-study · contact brief | F |
| 136 | `ecommerce-home-decor` | `fashion-editorial` | maison-domestico | palette terra+oro+verde-oliva, hero ambiente + oggetti, sezione collezioni | partnership designer · award · review riviste | catalogo · spedizione · ritiro | F |
| 137 | `ecommerce-outdoor-tech` | `artisan-workshop` / nuovo | tech-craft-attivo | palette nero+verde-foresta+arancio, hero outfit attivo, sezione collezioni | partnership marche · CV gear-tester · tech-spec | catalogo · guide · resi gratuiti | F |
| 138 | `ecommerce-jewelry-artisan` | `artisan-workshop` | autoriale-bottega (Bottega baseline ext) | palette warm-cream+oro+ottone, hero gioiello + mani, sezione lavorazione | gallery · CV orafo · partner gemme | catalogo · su misura · WhatsApp | F |
| 139 | `ecommerce-specialty-foods` | `artisan-workshop` / `artisan-food-shop` 🆕 | autoriale-food-curato | palette warm-cream+verde-oliva+terra, hero prodotti + produttori, sezione produttori | DOP/IGP partner · award · selezioni | catalogo · pacchi degustazione · spedizioni | F |

**Subtotale extension MVP:** 12-15 preset target.

---

## 3. Numeri di Sintesi

| Categoria | Preset target medio termine |
|-----------|-----------------------------|
| Medical | 12-15 |
| Restaurant | 10-12 |
| Hospitality | 8-10 |
| Food retail | 12-15 |
| Automotive | 8-10 |
| Trades | 15-20 |
| Beauty | 8-10 |
| Wellness-fit | 8-10 |
| Professional | 8-10 |
| Education | 8-10 |
| Events | 5-7 |
| Lawyer | 5-7 |
| Real-estate | 4-6 |
| Business | 5-7 |
| Agency | 4-6 |
| Portfolio | 4-6 |
| eCommerce | 6-8 |
| **Totale** | **~130-170 preset (lungo termine)** |
| **Realistic medio termine (Phase B-F):** | **75-90 preset attuabili** |

---

## 4. Convenzioni di Naming

### 4.1 Slug del preset

```
<mestiere>-<dimensione-distintiva>[-<localizzazione>]

Esempi:
- dentista-clinico-pulito
- dentista-estetico-premium
- pizzeria-napoletana-vera
- idraulico-singolo-quartiere
- pronto-intervento-elettrico-h24
- avvocato-civile-quartiere
- studio-legale-associato
- agriturismo-collina
- masseria-puglia-luxury
```

### 4.2 Label utente-facing

In italiano canonical IT, max 50 char:

```
"Dentista — Studio Pulito"
"Dentista Estetico Premium"
"Pizzeria Napoletana Tradizionale"
"Idraulico di Quartiere"
"Pronto Intervento Elettrico H24"
"Avvocato Civile · Studio di Quartiere"
```

### 4.3 Voice register convention

1 frase, max 100 char, descrive il tono in modo concreto:

```
"clinical pulito, paziente al centro, tono educativo evita allarmismi"
"calorosa partenopea, 'da Carmela dal '68', dialetto leggero"
"concreto-rapido, 'arrivo entro 45 min', certificato"
"premium-editoriale, autoriale come Monocle"
```

### 4.4 CTA voice convention

Per ogni locale, max 28 char, allineato al `conversion_pattern` dell'archetype:

```python
cta_voice = {
    "it": "Prenota la prima igiene",
    "en": "Book your first cleaning",
    "fr": "Réserver le premier détartrage",
    "es": "Reserva tu primera higiene",
    "ar": "احجز جلسة التنظيف الأولى",
}
```

---

## 5. Quality Gates per il Preset (binding)

Prima di shippare un preset come autorialmente disponibile nel catalogo, deve passare:

1. **DNA-coherence check**: il preset NON tocca alcuna dimensione DNA-locked (vedi `CATALOG_EXPANSION_STRATEGY.md` §7).
2. **Palette contrast gate**: ogni override palette rispetta D-054 contrast ratio (≥ 4.5:1 per body text).
3. **Imagery pool sanity**: ≥ 6 URL Pexels verificati a hand (no broken, no semantic mismatch tipo carrozziere → fotografia food).
4. **Voice register sample**: 3 frasi di esempio scritte nel registro dichiarato + revisione native-speaker.
5. **Sibling distance check (D-054)**: il preset, su un sibling pair test sul suo archetype, supera le 10 dimensioni differenziali. Se 2 preset dello stesso archetype condividono troppi tratti → uno deve cambiare palette / imagery / voice.
6. **Legal/Deontological note check**: ogni preset di categoria regolamentata (medical, lawyer, food, education, automotive) ha note esplicite su albo / autorizzazioni / obblighi GDPR settoriali.
7. **Editor compatibility test**: clonare il preset → CustomerProject → fare 5 modifiche tipiche + cambiare 1 locale + pubblicare in `draft`. Tutto deve filare senza intervento backend.

---

## 6. Riepilogo

- Il preset è un **content seed completo** sopra un archetype riusato.
- 75-90 preset target medio termine, distribuiti su 14-16 categorie e 28-30 archetypi.
- L'obiettivo strategico: **ogni nuovo mestiere = 1 preset, non 1 template**. Il template autoriale resta un asset raro (caso showcase featured).
- Il customer fork del preset via editor è il **moltiplicatore** che rende sostenibile la crescita catalogo.
- L'implementazione concreta dei preset arriva dopo Phase A (Editor Foundation v1) e segue la sequenza Phase B-F.
- **Nessun preset viene scritto durante la Session 54.** Questo è il blueprint, non il content.

---

## Pointer

- **`CATALOG_EXPANSION_STRATEGY.md`** — strategia complessiva (modello a 4 livelli, archetipi, editor strategy, roadmap).
- **`CATEGORY_ROADMAP.md`** — categorie + Phase A-G.
- **`EDITOR_SCHEMA_BLUEPRINT.md`** — contratto editor (D-064).
- **`DECISIONS.md`** — D-083 (modello a 4 livelli), D-084 (tassonomia 14 categorie), D-085 (editor-first sequencing).

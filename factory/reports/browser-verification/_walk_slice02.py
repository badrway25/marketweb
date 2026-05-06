"""Smoke walker for Causa retrofit slice 02 (R2 EVID-3 + R3 TIME-3).

Probes (on top of the slice-01 contract):
  - Causa staff-preview routes 200 + still carry "Sottometti" (slice-01 carry).
  - Anonymous Causa routes still 404 (draft-gate intact).
  - Catalog public listing still does NOT include `causa-legale`.
  - Home counter still reads "24+".
  - Cornice (LF-2 1st occupant) home + 4 inner pages × 5 locales · all 200
    anonymous · CTA still reads "Apri un fascicolo progetto" verbatim · NO
    EVID-3 markup · NO TIME-3 markup · NO new body motion flags.
  - Frozen siblings (Pragma · Fiscus · Solaria · Continua) home anonymous
    200 + NO new motion flags + NO EVID-3 markup + NO TIME-3 markup.
  - Causa body data-attributes: previous slice-01 set
    (`g2-editorial-counter` · `kpi-animate=1` · `nav-condense=1` ·
    `evid5=1`) PLUS new slice-02 set (`evid3=1` · `time3=1`).
  - Causa home renders the EVID-3 markup `<details class="citation-pop"`
    with `data-evid3` AND every citation snippet contains the expected
    forensic-publication anchor (Cass./TAR/App. citation strings).
  - Causa home renders the TIME-3 markup `<div class="chronotick"` with
    `data-time3` AND the 6 expected year ticks (1995 / 2003 / 2008 /
    2014 / 2018 / 2024).
  - Causa inner pages do NOT carry EVID-3 / TIME-3 markup (the patterns
    are scoped to the home `home.html`-equivalent; they live inside
    `cs-narrative` and `cs-cases-magazine`, neither of which renders on
    inner pages).

Run from project root with the dev server up on 127.0.0.1:8052.
"""
from __future__ import annotations
import http.cookiejar as cj
import re
import sys
import urllib.parse
import urllib.request


HOST = "http://127.0.0.1:8052"
RESULTS: list[tuple[str, str, str]] = []
FAILED = 0


def _opener():
    jar = cj.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(jar))
    opener.addheaders = [("User-Agent", "slice02-walker")]
    return opener, jar


def _get(opener: urllib.request.OpenerDirector, path: str, method="GET", data=None):
    req = urllib.request.Request(HOST + path, data=data, method=method)
    try:
        resp = opener.open(req, timeout=15)
        body = resp.read().decode("utf-8", errors="replace")
        return resp.status, body
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace") if e.fp else ""
        return e.code, body


def _login(opener: urllib.request.OpenerDirector, username: str, password: str) -> bool:
    _ = _get(opener, "/account/")
    status, body = _get(opener, "/admin/login/?next=/admin/")
    m = re.search(r'name="csrfmiddlewaretoken" value="([^"]+)"', body)
    if not m:
        print("login: no csrf token in admin login page")
        return False
    token = m.group(1)
    payload = urllib.parse.urlencode({
        "username": username,
        "password": password,
        "csrfmiddlewaretoken": token,
        "next": "/admin/",
    }).encode("ascii")
    req = urllib.request.Request(
        HOST + "/admin/login/?next=/admin/",
        data=payload,
        headers={
            "Content-Type": "application/x-www-form-urlencoded",
            "Referer": HOST + "/admin/login/?next=/admin/",
            "User-Agent": "slice02-walker",
        },
        method="POST",
    )
    try:
        resp = opener.open(req, timeout=15)
        return resp.status == 200 and "logout" in resp.read().decode("utf-8", errors="replace").lower()
    except urllib.error.HTTPError as e:
        return e.code == 302


def assert_(label: str, cond: bool, detail: str = ""):
    global FAILED
    status = "PASS" if cond else "FAIL"
    if not cond:
        FAILED += 1
    RESULTS.append((status, label, detail))
    print(f"[{status}] {label} {detail}")


_BODY_TAG_RE = re.compile(r"<body[^>]*>", re.IGNORECASE)


def body_tag(html: str) -> str:
    m = _BODY_TAG_RE.search(html)
    return m.group(0) if m else ""


def main():
    anon, _ = _opener()
    staff, _ = _opener()
    assert _login(staff, "causa_slice02_review", "slice02pass"), "staff login failed"

    # ── Anonymous draft-gate (slice-01 carry) ────────────────────────────
    causa_routes = [
        "/templates/business/causa-legale/preview/",
        "/templates/business/causa-legale/preview/studio/",
        "/templates/business/causa-legale/preview/materie/",
        "/templates/business/causa-legale/preview/contenzioso/",
        "/templates/business/causa-legale/preview/contatti/",
    ]
    for r in causa_routes:
        s, _ = _get(anon, r)
        assert_(f"anon Causa {r} 404", s == 404, f"got {s}")

    s, body = _get(anon, "/templates/")
    assert_("anon catalog hides Causa", "causa-legale" not in body)

    s, body = _get(anon, "/")
    assert_("anon home counter still 24+", "24+" in body)

    # ── Staff Causa walk (slice-01 carry: Sottometti verbatim) ──────────
    for r in causa_routes:
        s, body = _get(staff, r + "?preview=1")
        assert_(f"staff Causa {r} 200", s == 200, f"got {s}")
        if s == 200:
            assert_(
                f"  no residual 'Apri un parere' on {r}",
                "Apri un parere" not in body,
            )
            sottometti_count = body.count("Sottometti")
            assert_(
                f"  >=1 'Sottometti' occurrence on {r}",
                sottometti_count >= 1,
                f"({sottometti_count})",
            )

    # ── Causa home body data-attributes (slice-01 set + slice-02 additions) ─
    s, home = _get(staff, causa_routes[0] + "?preview=1")
    btag = body_tag(home)
    assert_("Causa <body> data-motion-profile=g2-editorial-counter",
            'data-motion-profile="g2-editorial-counter"' in btag)
    assert_("Causa <body> data-motion-kpi-animate=1 (slice-00 carry)",
            'data-motion-kpi-animate="1"' in btag)
    assert_("Causa <body> data-motion-nav-condense=1 (slice-01 carry)",
            'data-motion-nav-condense="1"' in btag)
    assert_("Causa <body> data-motion-evid5=1 (slice-01 carry)",
            'data-motion-evid5="1"' in btag)
    assert_("Causa <body> data-motion-evid3=1 (slice-02 NEW)",
            'data-motion-evid3="1"' in btag)
    assert_("Causa <body> data-motion-time3=1 (slice-02 NEW)",
            'data-motion-time3="1"' in btag)

    # ── Causa home renders EVID-3 markup ────────────────────────────────
    assert_("Causa EVID-3 <details class=\"citation-pop\"> markup present",
            'class="citation-pop"' in home and 'data-evid3' in home)
    # 4 cards × 1 details element = 4 occurrences expected
    evid3_count = home.count('data-evid3')
    assert_("Causa EVID-3 elements count == 4 (one per magazine card)",
            evid3_count == 4, f"({evid3_count})")
    # Citation snippets carry the forensic anchors
    for anchor in ["Cass. SS.UU. n. 11237/2024",
                   "Cass. civ. sez. III n. 28914/2023",
                   "TAR Lombardia sez. III n. 814/2022",
                   "Corte d'Appello Milano sez. trib. n. 3187/2021"]:
        assert_(f"Causa EVID-3 cites '{anchor}'", anchor in home)
    # The toggle label resolves the citation_label per card
    assert_("Causa EVID-3 toggle label 'Vedi la massima' present",
            "Vedi la massima" in home)

    # ── Causa home renders TIME-3 markup ────────────────────────────────
    assert_("Causa TIME-3 <div class=\"chronotick\"> markup present",
            'class="chronotick"' in home and 'data-time3' in home)
    for year in ["1995", "2003", "2008", "2014", "2018", "2024"]:
        assert_(f"Causa TIME-3 tick for {year}",
                f'>{year}<' in home or f">{year}</span>" in home)
    # The TIME-3 strip's parent class — defensive sanity that the rail + ticks
    # render inside cs-narrative.
    assert_("Causa TIME-3 strip nested in cs-narrative",
            re.search(r'class="cs-narrative".*?class="chronotick"', home, re.DOTALL) is not None)

    # ── Causa inner pages do NOT carry EVID-3 / TIME-3 markup ───────────
    for r in causa_routes[1:]:
        s, body = _get(staff, r + "?preview=1")
        if s == 200:
            assert_(f"  Causa {r} NO chronotick markup",
                    'class="chronotick"' not in body)
            assert_(f"  Causa {r} NO citation-pop markup",
                    'class="citation-pop"' not in body)

    # ── Cornice frozen-sibling regression (5 IT routes + 5 locales) ─────
    cornice_routes = [
        "/templates/business/cornice-architettura/preview/",
        "/templates/business/cornice-architettura/preview/studio/",
        "/templates/business/cornice-architettura/preview/servizi/",
        "/templates/business/cornice-architettura/preview/progetti/",
        "/templates/business/cornice-architettura/preview/contatti/",
    ]
    for r in cornice_routes:
        s, body = _get(anon, r)
        assert_(f"anon Cornice {r} 200", s == 200, f"got {s}")
        if s == 200:
            assert_(f"  Cornice CTA still 'Apri un fascicolo' on {r}",
                    "Apri un fascicolo" in body)
            assert_(f"  Cornice {r} NO citation-pop markup",
                    'class="citation-pop"' not in body)
            assert_(f"  Cornice {r} NO chronotick markup",
                    'class="chronotick"' not in body)

    # Cornice home body must NOT carry the new motion flags
    s, body = _get(anon, cornice_routes[0])
    if s == 200:
        btag = body_tag(body)
        assert_("Cornice <body> motion_profile=g2-editorial (NOT counter)",
                'data-motion-profile="g2-editorial"' in btag and
                'data-motion-profile="g2-editorial-counter"' not in btag)
        assert_("Cornice <body> has NO data-motion-evid3",
                'data-motion-evid3' not in btag)
        assert_("Cornice <body> has NO data-motion-time3",
                'data-motion-time3' not in btag)
        # slice-01 carry: still no nav-condense / evid5 on Cornice
        assert_("Cornice <body> has NO data-motion-nav-condense",
                'data-motion-nav-condense' not in btag)
        assert_("Cornice <body> has NO data-motion-evid5",
                'data-motion-evid5' not in btag)

    for loc in ["it", "en", "fr", "es", "ar"]:
        path = cornice_routes[0]
        suffix = "" if loc == "it" else f"?lang={loc}"
        s, _ = _get(anon, path + suffix)
        assert_(f"anon Cornice home [{loc}] 200", s == 200, f"got {s}")

    # ── Frozen non-LF-2 siblings ────────────────────────────────────────
    frozen = [
        ("Pragma",   "/templates/business/pragma-corporate-suite/preview/"),
        ("Fiscus",   "/templates/business/fiscus-commercialista/preview/"),
        ("Solaria",  "/templates/business/solaria-coaching/preview/"),
        ("Continua", "/templates/business/continua-stewardship/preview/"),
    ]
    for label, r in frozen:
        s, body = _get(anon, r)
        assert_(f"anon {label} home 200", s == 200, f"got {s}")
        if s == 200:
            btag = body_tag(body)
            assert_(f"  {label} <body> NO data-motion-evid3",
                    'data-motion-evid3' not in btag)
            assert_(f"  {label} <body> NO data-motion-time3",
                    'data-motion-time3' not in btag)
            assert_(f"  {label} NO citation-pop markup",
                    'class="citation-pop"' not in body)
            assert_(f"  {label} NO chronotick markup",
                    'class="chronotick"' not in body)

    print(f"\n--- SUMMARY: total={len(RESULTS)} pass={len(RESULTS)-FAILED} fail={FAILED} ---")
    sys.exit(0 if FAILED == 0 else 1)


if __name__ == "__main__":
    main()

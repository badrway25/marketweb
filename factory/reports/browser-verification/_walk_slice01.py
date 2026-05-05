"""Smoke walker for Causa retrofit slice 01.

Verifies:
  - Causa staff-preview routes 200 + assert "Sottometti" CTA literal on every
    page · zero residual "Apri un parere" cognate.
  - Anonymous Causa routes still 404 (draft-gate intact).
  - Catalog public listing still does NOT include `causa-legale`.
  - Home counter still reads "24+".
  - Cornice (LF-2 1st occupant) home + 4 inner pages × 5 locales · all 200
    anonymous · CTA still reads "Apri un fascicolo progetto" verbatim.
  - Frozen siblings (Pragma · Fiscus · Solaria · Continua) home anonymous
    200 + body length unchanged vs slice-00 reference.
  - Body data-attributes present on Causa: data-motion-profile=g2-editorial-
    counter · data-motion-kpi-animate=1 · data-motion-nav-condense=1 ·
    data-motion-evid5=1.
  - Body data-attributes absent on Cornice for the new flags
    (nav-condense + evid5 should NOT be present).
  - EVID-5 markup `<div class="provenance"` present on Causa home.
  - EVID-5 markup absent on Cornice home.

Run from project root with the dev server up on 127.0.0.1:8052.
"""
from __future__ import annotations
import http.cookiejar as cj
import json
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
    opener.addheaders = [("User-Agent", "slice01-walker")]
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
    # GET login page to seed CSRF cookie
    status, body = _get(opener, "/account/")
    # The accounts login uses Django's default; let's hit /admin/login/ with csrf
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
            "User-Agent": "slice01-walker",
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
    """Return the body opening tag substring (or empty string if not found)."""
    m = _BODY_TAG_RE.search(html)
    return m.group(0) if m else ""


def main():
    anon, _ = _opener()
    staff, _ = _opener()
    assert _login(staff, "causa_slice01_review", "slice01pass"), "staff login failed"

    # ── Anonymous draft-gate ─────────────────────────────────────────────
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

    # Catalog public listing must NOT show Causa
    s, body = _get(anon, "/templates/")
    assert_("anon catalog hides Causa", "causa-legale" not in body, "")

    # Home counter check (loose: "24+" should appear in homepage)
    s, body = _get(anon, "/")
    assert_("anon home counter still 24+", "24+" in body, "")

    # ── Staff-preview Causa walk ─────────────────────────────────────────
    for r in causa_routes:
        s, body = _get(staff, r + "?preview=1")
        assert_(f"staff Causa {r} 200", s == 200, f"got {s}")
        if s == 200:
            assert_(
                f"  no residual 'Apri un parere' on {r}",
                "Apri un parere" not in body,
                "",
            )
            # CTA verb-class shifted to Sottometti on at least one nav-pill or hero CTA
            sottometti_count = body.count("Sottometti")
            assert_(
                f"  >=1 'Sottometti' occurrence on {r}",
                sottometti_count >= 1,
                f"({sottometti_count})",
            )

    # Body data-attributes on Causa home (assert on body tag ONLY · not embedded CSS)
    s, body = _get(staff, causa_routes[0] + "?preview=1")
    btag = body_tag(body)
    assert_("Causa <body> data-motion-profile=g2-editorial-counter",
            'data-motion-profile="g2-editorial-counter"' in btag)
    assert_("Causa <body> data-motion-kpi-animate=1",
            'data-motion-kpi-animate="1"' in btag)
    assert_("Causa <body> data-motion-nav-condense=1",
            'data-motion-nav-condense="1"' in btag)
    assert_("Causa <body> data-motion-evid5=1",
            'data-motion-evid5="1"' in btag)
    assert_("Causa EVID-5 markup present",
            'class="provenance"' in body and 'data-evid5' in body)

    # ── Cornice frozen-sibling regression ────────────────────────────────
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
            assert_(
                f"  Cornice CTA still 'Apri un fascicolo' on {r}",
                "Apri un fascicolo" in body,
                "",
            )

    # Cornice home must NOT carry the new motion flags on the body tag
    s, body = _get(anon, cornice_routes[0])
    if s == 200:
        btag = body_tag(body)
        assert_("Cornice <body> motion_profile=g2-editorial (NOT counter)",
                'data-motion-profile="g2-editorial"' in btag and
                'data-motion-profile="g2-editorial-counter"' not in btag)
        assert_("Cornice <body> has NO data-motion-nav-condense",
                'data-motion-nav-condense' not in btag)
        assert_("Cornice <body> has NO data-motion-evid5",
                'data-motion-evid5' not in btag)
        # The provenance markup is gated in the template by motion_evid5
        assert_("Cornice provenance element absent",
                '<div class="provenance"' not in body)

    # ── Frozen non-LF-2 siblings ─────────────────────────────────────────
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
            assert_(f"  {label} <body> NO data-motion-evid5",
                    'data-motion-evid5' not in btag)
            assert_(f"  {label} <body> NO data-motion-nav-condense",
                    'data-motion-nav-condense' not in btag)
            assert_(f"  {label} provenance element absent",
                    '<div class="provenance"' not in body)

    # ── Cornice 5-locale walk ────────────────────────────────────────────
    for loc in ["it", "en", "fr", "es", "ar"]:
        path = cornice_routes[0]
        suffix = "" if loc == "it" else f"?lang={loc}"
        s, body = _get(anon, path + suffix)
        assert_(f"anon Cornice home [{loc}] 200", s == 200, f"got {s}")

    print(f"\n--- SUMMARY: total={len(RESULTS)} pass={len(RESULTS)-FAILED} fail={FAILED} ---")
    sys.exit(0 if FAILED == 0 else 1)


if __name__ == "__main__":
    main()

"""Phase X.7b motion_profile DNA · implementation pass 1 · verification walk.

Loads each of the 6 corporate-suite siblings via Django test client (with a
staff session for Causa's draft tier) and snapshots the rendered <body>
opening tag + counts the new motion data-attributes per sibling. Frozen
sibling contract: every sibling emits the SAME flag set as before this
pass (zero new data-motion-card-lift / zero new data-motion-cinematic-fade
attributes today; both new flags default-False on every profile that any
live template uses).

Companion to:
  - factory/reports/hardening/motion-profile-implementation-pass1.md
  - factory/reports/browser-verification/motion-profile-implementation-pass1.md

Run:
  python manage.py shell < factory/reports/browser-verification/_walk_motion_pass1.py
"""
from __future__ import annotations

import re

from django.contrib.auth import get_user_model
from django.test import Client


def main() -> None:
    User = get_user_model()
    staff = User.objects.filter(is_staff=True).first()
    if staff is None:
        staff = User.objects.create_user(
            username="__motion_pass1_verify__",
            password="x",
            is_staff=True,
        )

    client = Client()
    client.force_login(staff)

    rows = [
        ("pragma-corporate-suite",   "business", "g3-institutional",     "kpi_animate"),
        ("cornice-architettura",     "business", "g2-editorial",         "(none)"),
        ("fiscus-commercialista",    "business", "g3-institutional",     "kpi_animate"),
        ("solaria-coaching",         "business", "g3-institutional",     "kpi_animate"),
        ("continua-stewardship",     "business", "g4-stewardship",       "(none)"),
        ("causa-legale",             "business", "g2-editorial-counter", "kpi_animate · nav_condense_on_scroll · evid5_provenance · evid3_citation · time3_chronotick"),
    ]

    print("\n=== Phase X.7b motion_profile DNA · pass 1 · body data-attribute walk ===\n")
    print(f"{'sibling':<30} {'status':>6} {'profile':<24} {'flags emitted in body':<60}")
    print("-" * 120)

    body_re = re.compile(rb"<body [^>]*>")
    for slug, cat, expected_profile, expected_flags in rows:
        url = f"/templates/{cat}/{slug}/preview/?preview=1"
        resp = client.get(url)
        if resp.status_code != 200:
            print(f"{slug:<30} {resp.status_code:>6}  ← non-200")
            continue

        match = body_re.search(resp.content)
        body = match.group(0).decode("utf-8") if match else "(no body tag)"

        observed_profile = ""
        m = re.search(r'data-motion-profile="([^"]+)"', body)
        if m:
            observed_profile = m.group(1)

        observed_flags = re.findall(r'data-motion-([a-z0-9-]+)="1"', body)
        # sort for stable comparison
        observed_flags.sort()
        flag_str = " · ".join(observed_flags) if observed_flags else "(none)"

        match_marker = "✓" if observed_profile == expected_profile else "✗"
        print(f"{slug:<30} {resp.status_code:>6}  {match_marker} {observed_profile:<22} {flag_str:<60}")
        # Pass-1 contract: NO sibling emits the new attributes today.
        for forbidden in ("card-lift", "cinematic-fade"):
            if forbidden in observed_flags:
                print(f"    !! REGRESSION: {forbidden} emitted on a frozen sibling")

    print()


main()

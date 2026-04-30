"""Continua workflow D · 45-route + anon-probe smoke walk."""
import os, sys, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'marketweb.settings')
django.setup()
from django.test import Client  # noqa: E402
from django.contrib.auth import get_user_model  # noqa: E402

U = get_user_model()
u = U.objects.get(username='cs_review_fix')
c = Client()
c.force_login(u)

LOCALES = ['it', 'en', 'fr', 'es', 'ar']
PAGES = ['', 'chi-siamo/', 'custodia/', 'mandati/', 'contatti/']
MANDATES = [
    'famiglia-a-quarta-generazione-holding-industriale',
    'famiglia-b-fondazione-di-famiglia',
    'famiglia-c-trasferimento-intergenerazionale',
    'famiglia-d-single-family-office-estero',
]
base = '/templates/business/continua-stewardship/preview/'

ok = fails = 0
fail_lines = []
for loc in LOCALES:
    for p in PAGES:
        url = (f'{base}{p}?preview=1' if loc == 'it'
               else f'{base}{p}?lang={loc}&preview=1')
        s = c.get(url).status_code
        if s == 200:
            ok += 1
        else:
            fails += 1
            fail_lines.append(f'FAIL {s} {url}')
    for m in MANDATES:
        url = (f'{base}mandati/{m}/?preview=1' if loc == 'it'
               else f'{base}mandati/{m}/?lang={loc}&preview=1')
        s = c.get(url).status_code
        if s == 200:
            ok += 1
        else:
            fails += 1
            fail_lines.append(f'FAIL {s} {url}')

print(f'smoke: ok={ok} fails={fails}')
for ln in fail_lines:
    print(ln)

# Anonymous tier-gate probes
ca = Client()
print('anon catalog list:        ', ca.get('/templates/business/').status_code)
print('anon continua preview:    ', ca.get(base).status_code)
print('anon continua preview ?p: ', ca.get(base + '?preview=1').status_code)
text = ca.get('/templates/business/').content.decode('utf-8', 'ignore')
print('continua-stewardship in anon catalog page (expected False):', 'continua-stewardship' in text)

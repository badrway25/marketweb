"""Tests for `apps.core` and project-level helpers.

T19 coverage: ``marketweb.sentry.init_sentry_if_dsn_set`` — gating
logic for whether to call ``sentry_sdk.init`` based on
``SENTRY_DSN``. Mocks ``sentry_sdk.init`` so no real network call.

T23 coverage: ``AxesLockoutTests`` exercises the django-axes
policy end-to-end against the real ``/account/login/`` view. Axes
is disabled by default in test runs (see ``base.py``) because the
Django test client's ``Client.login(...)`` shortcut calls
``authenticate()`` without a request, which AxesStandaloneBackend
rejects. The lockout tests below RE-enable axes locally for the
duration of each test (``override_settings``) and post real form
data (with a request) to prove the policy actually fires.

T24 coverage: ``BrandedErrorTemplateTests`` calls Django's default
error handlers directly (``django.views.defaults.{bad_request,
permission_denied, server_error}``) with a synthetic exception and
asserts each one renders the branded 400/403/500 template — pill,
headline copy, CTA — with zero tech leak (no traceback fragment,
no exception class name in the HTML). The test client is unsuitable
because Django's debug-toolbar / 500 short-circuit fires before the
template renders during a unit-test run; calling the handler is the
canonical pattern for this kind of assertion.

T25 coverage: ``BrandedCsrfTemplateTests`` calls
``django.views.csrf.csrf_failure`` directly and asserts the project's
``templates/403_csrf.html`` is rendered (not Django's inline
fallback). ``BrandedMethodNotAllowedTests`` exercises the project
middleware against synthetic 405 responses, covering the happy path
(HTML rewrite + Allow preservation), the JSON path (no rewrite), the
API-prefix path (no rewrite), and the cache-and-status invariants.

T26 coverage: ``AxesBrandedLockoutTests`` re-enables axes locally and
posts past the failure threshold to /account/login/, asserting that
the lockout response (a) has status 429, (b) renders
templates/axes_lockout.html branded body (pill + headline + zero
tech leak of username / cooloff_time / failure_limit), and (c) the
XHR/JSON path still returns the original axes JSON payload — i.e.
the T23 lockout policy is intact and the new template only swaps
the HTML presentation.

T27 coverage: ``AdminTwoFactorGateTests`` covers the admin 2FA gate
end-to-end: the /admin/login/ form now exposes an `otp_token` field;
password-only POST is rejected with "Please enter your OTP token";
password + valid TOTP token grants admin access; password + invalid
TOTP token is rejected; and the public /account/login/ form has NOT
gained an OTP field (customer flow stays untouched). The TOTP
verification is exercised via the actual TOTPDevice.verify_token()
flow so the test catches any future regression in the django-otp
wiring (e.g. someone disabling OTPMiddleware in MIDDLEWARE).

T29 coverage: ``OtpReverifyPolicyTests`` exercises the admin OTP
session re-verification policy. Four cases: (1) a successful admin
login stamps ``otp_verified_at`` in the session; (2) within the
max-age window /admin/ stays accessible; (3) past the max-age window
the OTP state is invalidated, /admin/ bounces to /admin/login/,
``_auth_user_id`` is preserved; (4) the policy is path-scoped — it
does not touch customer sessions or non-/admin/ requests.

T31 coverage: ``AuditLogTests`` exercises the signal-driven audit
log. CREATE/UPDATE/DELETE on User write entries with the correct
action; field-level diff is computed only on WATCHED_FIELDS; the
password field is never serialized (DENYLISTED_FIELDS); role
toggles produce a ROLE_CHANGED action rather than generic UPDATED;
WebTemplate tier transitions are tagged PUBLISHED / UNPUBLISHED;
and audit rows survive their target's deletion.

T32 coverage: ``AuditRetentionTests`` exercises the
``prune_audit_log`` management command: dry-run prints but does not
delete, expired rows are removed, recent rows are preserved, the
``--older-than`` flag overrides the settings default, and ``--yes``
is required for non-interactive deletion. ``AuditAlertingTests``
exercises the post-save alerting receiver: ROLE_CHANGED and DELETED
audit entries fire both the logger WARNING and the email to
``AUDIT_ALERT_RECIPIENTS``; PUBLISHED / CREATED / UPDATED actions
do NOT trigger; the kill-switch ``AUDIT_ALERTS_ENABLED=0`` silences
the receiver entirely; and an empty recipient list suppresses the
email channel while leaving the logger active.

T33 coverage: ``AuditedDecoratorTests`` exercises the
``@audited(action=...)`` decorator against two real commerce
services (``cancel_order`` and ``mark_order_paid``). Verified:
the explicit ORDER_CANCELLED / ORDER_PAID audit row is written
WITH the reason / note in ``changes``; the T31 signal-driven
UPDATED row is ALSO emitted (complementary, not duplicate); when
the wrapped function raises, NO explicit row is written; and the
decorator scrubs ``DENYLISTED_FIELDS`` even if a future caller
passed a forbidden kwarg.

T34 coverage: ``SentryAuditBreadcrumbTests`` initializes Sentry
with a capturing transport, triggers a T32 ``audit_alert`` via a
real ``AuditLogEntry`` write, captures a synthetic exception, and
asserts that the captured Sentry event contains a breadcrumb with
``category='marketweb.audit'``, ``level='warning'``, structured
``data`` (audit_action / audit_actor / audit_target / etc.), and
that ``audit_changes`` carries the diff dict — i.e. the structured
forensic context the brief asked for.

T35 coverage: ``AuditedExtensionTests`` exercises the new
``@audited`` decorations on three real service flows:
``set_order_fulfillment`` (Order is tracked → 2 rows: signal +
explicit) and ``publish_project`` / ``unpublish_project``
(CustomerProject NOT tracked → ONLY the explicit row, which is
the first audit trace these flows ever had).

T36 coverage: ``ExportAuditLogTests`` exercises the
``export_audit_log`` management command. JSONL and CSV formats
emit the documented field set; --action / --actor / --target-type
/ --since / --until / --limit filters narrow the queryset; --output
writes the same content to a file; unknown target types raise
CommandError with an operator-friendly message.

T37 coverage: ``SecurityHeadersTests`` exercises the
``SecurityHeadersMiddleware`` against real HTML and static-file
responses. Verifies that Content-Security-Policy, Permissions-Policy,
Cross-Origin-Resource-Policy, and X-Permitted-Cross-Domain-Policies
are set on every response; that the CSP allowlists the actually-used
external origins (Bootstrap CDN, Google Fonts, Stripe); and that the
``unsafe-inline`` concession is documented in the CSP directly so a
later "tighten the policy" pass cannot miss it.

T38 coverage: ``BackupRestoreTests`` exercises the ``backup_db`` and
``restore_drill`` management commands. SQLite path is exercised
end-to-end against the test DB — backup writes a real file,
restore_drill loads it into a sandbox and verifies the sentinel
tables (django_migrations, accounts_user, core_auditlogentry) are
queryable. PostgreSQL path is unit-tested with mocked subprocess
to pin the pg_dump argv shape. Retention prunes older matching
files after a successful write, never deletes files with another
prefix, and is disabled cleanly by --keep 0.
"""
from __future__ import annotations

import sys
from unittest import mock

from django.contrib.auth import get_user_model
from django.core.exceptions import PermissionDenied, SuspiciousOperation
from django.test import Client, RequestFactory, SimpleTestCase, TestCase, override_settings
from django.views import defaults as default_views

from marketweb.sentry import init_sentry_if_dsn_set

User = get_user_model()


def _make_env(values: dict):
    """Mimic the signature of ``marketweb.settings.base.env``."""

    def env(key, default=None, *, required=False, cast=str):
        raw = values.get(key, default)
        if raw is None or raw == "":
            return raw
        if cast is bool:
            return str(raw).strip().lower() in {"1", "true", "yes", "on"}
        if cast is int:
            return int(raw)
        if cast is float:
            return float(raw)
        if cast is list:
            return [s.strip() for s in str(raw).split(",") if s.strip()]
        return str(raw)

    return env


class SentryInitTests(SimpleTestCase):
    """Cover the three meaningful states of the Sentry init helper."""

    def test_no_dsn_returns_false_and_does_not_call_sdk(self):
        """The dev / CI / local path: SENTRY_DSN unset → init skipped."""
        env = _make_env({})  # no SENTRY_DSN at all
        with mock.patch("sentry_sdk.init") as init_mock:
            result = init_sentry_if_dsn_set(env)
        self.assertFalse(result)
        init_mock.assert_not_called()

    def test_empty_dsn_returns_false(self):
        """Explicit empty SENTRY_DSN is treated identically to unset."""
        env = _make_env({"SENTRY_DSN": ""})
        with mock.patch("sentry_sdk.init") as init_mock:
            result = init_sentry_if_dsn_set(env)
        self.assertFalse(result)
        init_mock.assert_not_called()

    def test_dsn_set_calls_init_with_expected_kwargs(self):
        """The prod opt-in path: DSN set → init called with safe defaults."""
        env = _make_env({
            "SENTRY_DSN": "https://public@o0.ingest.sentry.io/1",
            "SENTRY_ENVIRONMENT": "production",
            # Leave the rest defaulted to confirm the helper's defaults
        })
        with mock.patch("sentry_sdk.init") as init_mock:
            result = init_sentry_if_dsn_set(env)
        self.assertTrue(result)
        init_mock.assert_called_once()
        kwargs = init_mock.call_args.kwargs
        self.assertEqual(kwargs["dsn"], "https://public@o0.ingest.sentry.io/1")
        self.assertEqual(kwargs["environment"], "production")
        # Defaults: errors-only, no profiling, no PII.
        self.assertEqual(kwargs["traces_sample_rate"], 0.0)
        self.assertEqual(kwargs["profiles_sample_rate"], 0.0)
        self.assertFalse(kwargs["send_default_pii"])
        # Empty release env → None (lets the SDK auto-detect from git).
        self.assertIsNone(kwargs["release"])
        # Django integration must be present.
        from sentry_sdk.integrations.django import DjangoIntegration
        self.assertTrue(
            any(isinstance(i, DjangoIntegration) for i in kwargs["integrations"]),
            "DjangoIntegration must be in the integrations list",
        )

    def test_dsn_set_respects_overrides(self):
        """Operator-supplied env values must reach sentry_sdk.init."""
        env = _make_env({
            "SENTRY_DSN": "https://public@o0.ingest.sentry.io/1",
            "SENTRY_ENVIRONMENT": "staging",
            "SENTRY_RELEASE": "marketweb@1.2.3",
            "SENTRY_TRACES_SAMPLE_RATE": "0.05",
            "SENTRY_PROFILES_SAMPLE_RATE": "0.10",
            "SENTRY_SEND_DEFAULT_PII": "1",
        })
        with mock.patch("sentry_sdk.init") as init_mock:
            init_sentry_if_dsn_set(env)
        kwargs = init_mock.call_args.kwargs
        self.assertEqual(kwargs["environment"], "staging")
        self.assertEqual(kwargs["release"], "marketweb@1.2.3")
        self.assertAlmostEqual(kwargs["traces_sample_rate"], 0.05)
        self.assertAlmostEqual(kwargs["profiles_sample_rate"], 0.10)
        self.assertTrue(kwargs["send_default_pii"])

    def test_missing_sdk_returns_false_without_raising(self):
        """If sentry-sdk is not installed, the helper logs and returns
        False — observability is not critical-path."""
        env = _make_env({"SENTRY_DSN": "https://public@o0.ingest.sentry.io/1"})

        # Force an ImportError on `import sentry_sdk` inside the helper.
        original_sentry = sys.modules.pop("sentry_sdk", None)
        original_django = sys.modules.pop("sentry_sdk.integrations.django", None)
        sys.modules["sentry_sdk"] = None  # raises ImportError on import
        try:
            with self.assertLogs("marketweb.sentry", level="WARNING") as cm:
                result = init_sentry_if_dsn_set(env)
        finally:
            # Restore what we displaced so other tests don't see a
            # broken sentry_sdk import.
            if original_sentry is not None:
                sys.modules["sentry_sdk"] = original_sentry
            else:
                sys.modules.pop("sentry_sdk", None)
            if original_django is not None:
                sys.modules["sentry_sdk.integrations.django"] = original_django

        self.assertFalse(result)
        self.assertTrue(
            any("sentry-sdk is not installed" in msg for msg in cm.output),
            f"Expected 'sentry-sdk is not installed' warning, got: {cm.output}",
        )


@override_settings(
    AXES_ENABLED=True,
    AXES_FAILURE_LIMIT=3,
    AXES_COOLOFF_TIME=1,
    AXES_LOCKOUT_PARAMETERS=[["ip_address", "username"]],
    AXES_RESET_ON_SUCCESS=True,
)
class AxesLockoutTests(TestCase):
    """Prove the T23 lockout policy fires against /account/login/.

    Axes is disabled by default during ``manage.py test`` (see
    ``base.py``); these tests re-enable it locally and lower the
    threshold to 3 to keep the run short. The policy logic and
    middleware wiring are the same as in dev/prod.
    """

    def setUp(self):
        # Pin a known good user; the lockout MUST trigger on attempts
        # that match the username but use the WRONG password.
        self.username = "lockoutprobe"
        self.password = "S0lidPass-2026"
        User.objects.create_user(self.username, password=self.password)
        # Use a fresh client per test so axes' (ip, username) key is
        # not contaminated across runs (the test DB is rolled back
        # but the in-process cache may persist).
        self.client = Client()

    def _bad_login(self):
        """One bad-credentials POST to /account/login/."""
        return self.client.post(
            "/account/login/",
            {"username": self.username, "password": "WRONG-PASSWORD"},
        )

    def test_first_few_failures_return_200_with_form_error(self):
        """Below the threshold, the form re-renders with an error
        (200 OK). No lockout yet."""
        for _ in range(2):  # AXES_FAILURE_LIMIT is 3 in this class
            r = self._bad_login()
            self.assertEqual(r.status_code, 200)

    def test_third_failure_triggers_lockout(self):
        """At AXES_FAILURE_LIMIT, axes locks the (ip, username) key.
        axes 7.x returns 429 Too Many Requests by default."""
        for _ in range(2):
            self._bad_login()
        # The 3rd attempt is the trigger.
        r = self._bad_login()
        self.assertEqual(
            r.status_code, 429,
            f"Expected 429 lockout on the 3rd failed attempt, got {r.status_code}",
        )

    def test_locked_out_user_cannot_login_with_correct_password(self):
        """Once locked, even the RIGHT password is rejected — the
        gate is keyed on (ip, username), not on credentials match."""
        for _ in range(3):
            self._bad_login()
        # Try the correct password — should still be rejected (429).
        r = self.client.post(
            "/account/login/",
            {"username": self.username, "password": self.password},
        )
        self.assertEqual(r.status_code, 429)

    def test_unrelated_username_is_not_affected_by_lockout(self):
        """The lockout key includes the username; a DIFFERENT
        username from the same IP should still be able to attempt
        (proves the per-(ip, username) granularity)."""
        for _ in range(3):
            self._bad_login()
        # An unrelated user attempt — should NOT be blocked by the
        # lockout on `lockoutprobe`.
        User.objects.create_user("other", password=self.password)
        r = self.client.post(
            "/account/login/",
            {"username": "other", "password": self.password},
        )
        # 302 = successful login redirect (LOGIN_REDIRECT_URL).
        self.assertEqual(
            r.status_code, 302,
            f"Different username from same IP should NOT be locked; "
            f"got {r.status_code}",
        )


class BrandedErrorTemplateTests(SimpleTestCase):
    """Prove the T24 branded 400/403/500 templates render with the
    expected copy + zero tech leak.

    We call ``django.views.defaults.*`` directly so the test does NOT
    depend on DEBUG=False being toggled (Django's default handlers
    pick the user template ``templates/{400,403,500}.html`` whenever
    they are invoked — the DEBUG check happens upstream in the
    exception handler, not inside these views).
    """

    # Strings that MUST appear → proves the user template was used,
    # not Django's stock fallback (`<h1>403 Forbidden</h1>` etc).
    EXPECTED_COPY = {
        400: (
            b"Errore 400",
            b"richiesta non valida",
            b"Torna alla home",
            b"Sfoglia il catalogo",
        ),
        403: (
            b"Errore 403",
            b"accesso non consentito",
            b"Vai al login",
            b"Torna alla home",
        ),
        500: (
            b"Errore 500",
            b"problema temporaneo",
            b"Torna alla home",
            b"Sfoglia il catalogo",
        ),
    }

    # Strings that MUST NOT appear → no tech leak.
    FORBIDDEN_LEAKS = (
        b"Traceback",
        b"django.",
        b"PermissionDenied",
        b"SuspiciousOperation",
        b"RuntimeError",
        # Stock Django fallback titles — if any of these survive, the
        # branded template was bypassed.
        b"<h1>Bad Request (400)</h1>",
        b"<h1>403 Forbidden</h1>",
        b"<h1>Server Error (500)</h1>",
    )

    def setUp(self):
        self.factory = RequestFactory()

    def _assert_branded(self, code, response):
        self.assertEqual(response.status_code, code)
        body = response.content
        for needle in self.EXPECTED_COPY[code]:
            self.assertIn(
                needle, body,
                f"{code} body missing expected copy {needle!r}",
            )
        for leak in self.FORBIDDEN_LEAKS:
            self.assertNotIn(
                leak, body,
                f"{code} body leaks forbidden token {leak!r}",
            )

    def test_400_template_renders_branded(self):
        request = self.factory.get("/")
        response = default_views.bad_request(
            request, SuspiciousOperation("synthetic")
        )
        self._assert_branded(400, response)

    def test_403_template_renders_branded(self):
        request = self.factory.get("/")
        response = default_views.permission_denied(
            request, PermissionDenied("synthetic")
        )
        self._assert_branded(403, response)

    def test_500_template_renders_branded(self):
        request = self.factory.get("/")
        # server_error takes only the request — Django's exception
        # handler logs the traceback separately and never passes it
        # into the template (no context-processor pipeline runs).
        response = default_views.server_error(request)
        self._assert_branded(500, response)

    def test_500_template_is_self_contained(self):
        """500 must NOT extend base.html (no request context
        processors run during a 500). This test fails loudly if a
        future refactor wires base.html back in."""
        request = self.factory.get("/")
        response = default_views.server_error(request)
        self.assertIn(b"<!DOCTYPE html>", response.content)
        self.assertNotIn(
            b'id="main-content"', response.content,
            "500 template appears to extend base.html — that wrapper "
            "uses {% url %} reverse + context processors that are NOT "
            "safe during a 500 (the request context is in a failed state).",
        )


class BrandedCsrfTemplateTests(SimpleTestCase):
    """T25 · CSRF failure page must render the branded
    ``templates/403_csrf.html``, not Django's inline fallback HTML."""

    def setUp(self):
        self.factory = RequestFactory()

    def test_csrf_failure_renders_branded_template(self):
        """Calling django.views.csrf.csrf_failure picks up our
        template/403_csrf.html via the CSRF_FAILURE_TEMPLATE_NAME
        auto-discovery (default = "403_csrf.html")."""
        from django.views.csrf import csrf_failure

        request = self.factory.post("/account/login/")
        response = csrf_failure(request, reason="test reason")

        self.assertEqual(response.status_code, 403)
        body = response.content
        # Branded copy must be present.
        self.assertIn(b"Errore 403", body)
        self.assertIn(b"sessione di sicurezza scaduta", body)
        self.assertIn(b"protezione anti-frode", body)
        # Stock Django fallback markers must be ABSENT.
        self.assertNotIn(b"<h1>Forbidden", body)
        self.assertNotIn(b"<h1>Proibito", body)
        # Reason string must NOT be reflected in the rendered HTML
        # (we deliberately ignore the technical context).
        self.assertNotIn(b"test reason", body)


class BrandedMethodNotAllowedTests(SimpleTestCase):
    """T25 · the middleware must rewrite the empty Django 405 body
    to the branded template for HTML-bound requests, and leave
    JSON / API responses untouched."""

    def setUp(self):
        self.factory = RequestFactory()
        # Import here so we test the actual production class wiring.
        from marketweb.middleware import BrandedMethodNotAllowedMiddleware
        self.MiddlewareCls = BrandedMethodNotAllowedMiddleware

    def _bare_405(self, allow="POST"):
        """Build a fake downstream view that returns Django's stock 405."""
        from django.http import HttpResponseNotAllowed

        def view(_request):
            return HttpResponseNotAllowed([allow])
        return view

    def test_html_request_rewrites_body(self):
        mw = self.MiddlewareCls(self._bare_405())
        request = self.factory.get("/some/endpoint/", HTTP_ACCEPT="text/html")
        response = mw(request)

        self.assertEqual(response.status_code, 405)
        self.assertEqual(response["Allow"], "POST")
        self.assertIn(b"Errore 405", response.content)
        self.assertIn(b"azione non consentita", response.content)
        # Branded body, not empty.
        self.assertGreater(len(response.content), 1000)

    def test_wildcard_accept_rewrites_body(self):
        """curl's default ``Accept: */*`` is treated as HTML-bound."""
        mw = self.MiddlewareCls(self._bare_405())
        request = self.factory.get("/some/endpoint/", HTTP_ACCEPT="*/*")
        response = mw(request)

        self.assertEqual(response.status_code, 405)
        self.assertIn(b"Errore 405", response.content)

    def test_json_request_is_not_rewritten(self):
        """An ``Accept: application/json`` client gets the bare 405."""
        mw = self.MiddlewareCls(self._bare_405())
        request = self.factory.get("/some/endpoint/", HTTP_ACCEPT="application/json")
        response = mw(request)

        self.assertEqual(response.status_code, 405)
        self.assertEqual(response["Allow"], "POST")
        self.assertEqual(response.content, b"")

    def test_api_prefix_is_not_rewritten(self):
        """Paths under /api/ are explicitly excluded — DRF emits its
        own JSON 405 body and middleware must not stomp it."""
        mw = self.MiddlewareCls(self._bare_405())
        request = self.factory.get("/api/v1/items/", HTTP_ACCEPT="text/html")
        response = mw(request)

        self.assertEqual(response.status_code, 405)
        self.assertEqual(response.content, b"")

    def test_non_405_response_is_passed_through(self):
        """The middleware is a no-op on all non-405 responses."""
        from django.http import HttpResponse

        def view(_request):
            return HttpResponse(b"normal 200 body", status=200)

        mw = self.MiddlewareCls(view)
        request = self.factory.get("/", HTTP_ACCEPT="text/html")
        response = mw(request)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b"normal 200 body")

    def test_allow_header_preserved_with_multiple_methods(self):
        """RFC 9110 §15.5.6 — a 405 MUST advertise every accepted
        method via the Allow header. The middleware must preserve it
        verbatim from the downstream response."""
        mw = self.MiddlewareCls(self._bare_405(allow="POST, PUT"))
        request = self.factory.get("/some/endpoint/", HTTP_ACCEPT="text/html")
        response = mw(request)

        self.assertEqual(response["Allow"], "POST, PUT")


@override_settings(
    AXES_ENABLED=True,
    AXES_FAILURE_LIMIT=3,
    AXES_COOLOFF_TIME=1,
    AXES_LOCKOUT_PARAMETERS=[["ip_address", "username"]],
    AXES_RESET_ON_SUCCESS=True,
    AXES_LOCKOUT_TEMPLATE="axes_lockout.html",
)
class AxesBrandedLockoutTests(TestCase):
    """T26 · once the axes (ip, username) key is locked, the response
    body must be the branded ``templates/axes_lockout.html`` for HTML
    clients, JSON for XHR clients, status 429 in both cases. The T23
    lockout policy (threshold, key combo, status code) must be
    preserved verbatim."""

    def setUp(self):
        self.username = "t26probe-tests"
        self.password = "S0lidPass-2026"
        User.objects.create_user(self.username, password=self.password)
        self.client = Client()

    def _bad_login(self, extra_headers=None):
        kwargs = {}
        if extra_headers:
            kwargs.update(extra_headers)
        return self.client.post(
            "/account/login/",
            {"username": self.username, "password": "WRONG"},
            **kwargs,
        )

    def test_html_lockout_renders_branded_template_with_429(self):
        """HTML browser flow: trip the threshold, the next attempt
        renders ``templates/axes_lockout.html`` with status 429."""
        for _ in range(3):
            self._bad_login()
        r = self._bad_login()
        self.assertEqual(r.status_code, 429)
        body = r.content
        # Branded copy must be present.
        self.assertIn(b"Errore 429", body)
        self.assertIn(b"troppi tentativi di accesso", body)
        self.assertIn(b"Torna alla home", body)
        # Tech leaks must be ABSENT — the template ignores the
        # `failure_limit`, `username`, `cooloff_time` context.
        self.assertNotIn(self.username.encode(), body)
        self.assertNotIn(b"failure_limit", body)
        self.assertNotIn(b"cooloff_time", body)
        self.assertNotIn(b"PT1H", body)
        # Stock axes plain-text body must be ABSENT.
        self.assertNotIn(b"Account locked: too many login attempts", body)

    def test_xhr_lockout_still_returns_json(self):
        """AJAX flow: axes branches on X-Requested-With BEFORE the
        lockout template — JSON contract from T23 is preserved."""
        for _ in range(3):
            self._bad_login()
        r = self._bad_login(extra_headers={"HTTP_X_REQUESTED_WITH": "XMLHttpRequest"})
        self.assertEqual(r.status_code, 429)
        self.assertEqual(r["Content-Type"], "application/json")
        import json
        payload = json.loads(r.content)
        self.assertEqual(payload["failure_limit"], 3)
        self.assertEqual(payload["username"], self.username)
        # cooloff_time is an ISO-8601 duration string when cool-off is set.
        self.assertIn("cooloff_time", payload)
        self.assertIn("cooloff_timedelta", payload)

    def test_threshold_unchanged_below_limit_returns_200(self):
        """Below AXES_FAILURE_LIMIT the form should re-render with an
        error (200), NOT trigger the branded lockout. Proves T23's
        threshold semantics are not regressed by T26."""
        for _ in range(2):
            r = self._bad_login()
            self.assertEqual(r.status_code, 200)
            self.assertNotIn(b"Errore 429", r.content)


class AdminTwoFactorGateTests(TestCase):
    """T27 · the /admin/ gate must require BOTH password AND a valid
    TOTP token. Public /account/login/ stays single-factor. The
    OTPAdminSite class swap in marketweb/urls.py + the OTPMiddleware
    in settings/base.py together implement the gate; these tests
    fail loudly if either side regresses.
    """

    @classmethod
    def setUpTestData(cls):
        cls.username = "t27gate"
        cls.password = "GateTest-2026!"
        cls.user = User.objects.create_user(
            cls.username,
            password=cls.password,
            is_staff=True,
            is_superuser=True,
        )
        # Provision a confirmed TOTPDevice exactly the way
        # setup_admin_totp does it.
        from django_otp.plugins.otp_totp.models import TOTPDevice
        cls.device = TOTPDevice.objects.create(
            user=cls.user, name="default", confirmed=True,
        )

    def _current_totp(self):
        """Compute the TOTP code valid for the current 30-s window
        using the device's binary key — identical to what the
        Authenticator app would show."""
        import hmac, struct, time, hashlib
        counter = int(time.time() // 30)
        mac = hmac.new(
            self.device.bin_key,
            struct.pack(">Q", counter),
            hashlib.sha1,
        ).digest()
        offset = mac[-1] & 0x0F
        truncated = struct.unpack(">I", mac[offset:offset + 4])[0] & 0x7FFFFFFF
        return f"{truncated % 1000000:06d}"

    def test_admin_login_form_exposes_otp_token_field(self):
        """The GET on /admin/login/ must render the OTP-aware form
        (sanity check that OTPAdminSite is actually in use)."""
        r = self.client.get("/admin/login/")
        self.assertEqual(r.status_code, 200)
        self.assertIn(b'name="otp_token"', r.content)
        self.assertIn(b'name="username"', r.content)
        self.assertIn(b'name="password"', r.content)

    def test_admin_login_password_only_is_rejected(self):
        """POST with username+password but NO otp_token must NOT
        grant admin access. The form re-renders with an OTP error."""
        r = self.client.post(
            "/admin/login/",
            {"username": self.username, "password": self.password},
        )
        # The form re-renders with status 200 + the OTP error.
        self.assertEqual(r.status_code, 200)
        self.assertIn(b"Please enter your OTP token", r.content)
        # And /admin/ itself stays gated.
        r = self.client.get("/admin/")
        self.assertEqual(r.status_code, 302)
        self.assertIn("/admin/login/", r["Location"])

    def test_admin_login_with_valid_totp_grants_access(self):
        """Password + a freshly generated valid TOTP token must let
        the user reach /admin/ index."""
        r = self.client.post(
            "/admin/login/",
            {
                "username": self.username,
                "password": self.password,
                "otp_token": self._current_totp(),
                "next": "/admin/",
            },
            follow=False,
        )
        # Successful admin login redirects (302) to ?next=/admin/.
        self.assertEqual(r.status_code, 302)
        self.assertIn("/admin/", r["Location"])
        # And the next GET on /admin/ actually returns the dashboard.
        # The marketplace is LANGUAGE_CODE="it", so the heading is
        # Italian ("Amministrazione sito"). We assert on multiple
        # admin-only markers so the test is robust to wording drift.
        r = self.client.get("/admin/")
        self.assertEqual(r.status_code, 200)
        self.assertIn(b"id=\"site-name\"", r.content)
        self.assertIn(b"/admin/logout/", r.content)
        self.assertIn(b"/admin/accounts/user/", r.content)

    def test_admin_login_with_wrong_totp_is_rejected(self):
        """An incorrect 6-digit token must NOT grant access — proves
        the second factor is actually checked, not just rendered."""
        r = self.client.post(
            "/admin/login/",
            {
                "username": self.username,
                "password": self.password,
                "otp_token": "000000",  # wrong with overwhelming probability
            },
        )
        self.assertEqual(r.status_code, 200)
        # Either the OTP-token error or a generic auth error; both
        # are acceptable — what matters is that admin access stays gated.
        r = self.client.get("/admin/")
        self.assertEqual(r.status_code, 302)
        self.assertIn("/admin/login/", r["Location"])

    def test_customer_login_has_no_otp_field(self):
        """The public /account/login/ form must remain single-factor
        — T27 is admin-only by design."""
        r = self.client.get("/account/login/")
        self.assertEqual(r.status_code, 200)
        self.assertNotIn(b'name="otp_token"', r.content)
        self.assertIn(b'name="username"', r.content)
        self.assertIn(b'name="password"', r.content)


class OtpReverifyPolicyTests(TestCase):
    """T29 · the admin OTP-verified state must time out after
    OTP_ADMIN_REVERIFY_SECONDS, independent of SESSION_COOKIE_AGE.
    Customer sessions and non-/admin/ paths are unaffected.
    """

    @classmethod
    def setUpTestData(cls):
        cls.username = "t29admin"
        cls.password = "ReverifyTest-2026!"
        cls.user = User.objects.create_user(
            cls.username,
            password=cls.password,
            is_staff=True,
            is_superuser=True,
        )
        from django_otp.plugins.otp_totp.models import TOTPDevice
        cls.device = TOTPDevice.objects.create(
            user=cls.user, name="default", confirmed=True,
        )

    def _current_totp(self):
        import hmac, struct, time, hashlib
        counter = int(time.time() // 30)
        mac = hmac.new(
            self.device.bin_key,
            struct.pack(">Q", counter),
            hashlib.sha1,
        ).digest()
        offset = mac[-1] & 0x0F
        truncated = struct.unpack(">I", mac[offset:offset + 4])[0] & 0x7FFFFFFF
        return f"{truncated % 1000000:06d}"

    def _login_admin(self):
        return self.client.post(
            "/admin/login/",
            {
                "username": self.username,
                "password": self.password,
                "otp_token": self._current_totp(),
                "next": "/admin/",
            },
        )

    def test_admin_login_stamps_otp_verified_at(self):
        """The user_logged_in signal listener must write
        ``otp_verified_at`` to the session right after an OTP login."""
        from marketweb.middleware import OTP_VERIFIED_AT_SESSION_KEY

        r = self._login_admin()
        self.assertEqual(r.status_code, 302)
        # The session is now persisted by the test client.
        self.assertIn(OTP_VERIFIED_AT_SESSION_KEY, self.client.session)
        stamp = self.client.session[OTP_VERIFIED_AT_SESSION_KEY]
        import time
        # The stamp must be a recent unix epoch second.
        self.assertGreater(stamp, time.time() - 60)
        self.assertLessEqual(stamp, int(time.time()))

    def test_admin_accessible_within_max_age(self):
        """A fresh OTP session must let /admin/ through without
        re-verification."""
        self._login_admin()
        r = self.client.get("/admin/")
        self.assertEqual(r.status_code, 200)

    def test_admin_expired_otp_state_forces_reverify(self):
        """If otp_verified_at is older than OTP_ADMIN_REVERIFY_SECONDS,
        the next /admin/ request must bounce to /admin/login/. The
        auth session (_auth_user_id) stays intact so re-login does
        not require fresh signup — only password + TOTP again."""
        from marketweb.middleware import OTP_VERIFIED_AT_SESSION_KEY
        from django_otp import DEVICE_ID_SESSION_KEY

        self._login_admin()
        # Sanity: admin currently accessible.
        self.assertEqual(self.client.get("/admin/").status_code, 200)

        # Forge an expired stamp directly in the session.
        import time
        s = self.client.session
        s[OTP_VERIFIED_AT_SESSION_KEY] = int(time.time()) - 999_999
        s.save()
        # Auth login marker still in place.
        self.assertIn("_auth_user_id", self.client.session)
        # OTP device marker also still in place — the middleware
        # is what removes it.
        self.assertIn(DEVICE_ID_SESSION_KEY, self.client.session)

        # Now hit /admin/ → the middleware should observe the expired
        # stamp, clear OTP state, and the admin gate should bounce.
        r = self.client.get("/admin/")
        self.assertEqual(r.status_code, 302)
        self.assertIn("/admin/login/", r["Location"])
        # Auth login is preserved; OTP state is gone.
        self.assertIn("_auth_user_id", self.client.session)
        self.assertNotIn(DEVICE_ID_SESSION_KEY, self.client.session)
        self.assertNotIn(OTP_VERIFIED_AT_SESSION_KEY, self.client.session)

    def test_policy_is_path_scoped_to_admin(self):
        """Non-/admin/ requests must NOT trigger the reverify check
        — customer sessions are untouched. /admin/login/ itself is
        exempt so we don't redirect-loop."""
        from marketweb.middleware import OTP_VERIFIED_AT_SESSION_KEY
        from django_otp import DEVICE_ID_SESSION_KEY

        self._login_admin()
        import time
        s = self.client.session
        s[OTP_VERIFIED_AT_SESSION_KEY] = int(time.time()) - 999_999
        s.save()

        # Hitting a non-/admin/ path must NOT clear the OTP state.
        self.client.get("/")  # public home
        self.assertIn(DEVICE_ID_SESSION_KEY, self.client.session)
        self.assertIn(OTP_VERIFIED_AT_SESSION_KEY, self.client.session)

        # /admin/login/ is exempt from the gate (otherwise the
        # re-verify form itself would redirect-loop).
        self.client.get("/admin/login/")
        # Note: /admin/login/ itself may redirect for an authenticated
        # user, but the OTP state must NOT have been cleared by
        # the reverify middleware here — that only happens for
        # non-exempt /admin/* paths.
        self.assertIn(DEVICE_ID_SESSION_KEY, self.client.session)

    def test_customer_login_does_not_stamp_otp_verified_at(self):
        """The signal handler is a no-op when there is no
        ``otp_device_id`` in the session. Customer login flows
        therefore do not pollute the session with an OTP stamp."""
        from marketweb.middleware import OTP_VERIFIED_AT_SESSION_KEY

        cust_user = User.objects.create_user(
            "t29cust", password=self.password, is_staff=False,
        )
        r = self.client.post(
            "/account/login/",
            {"username": cust_user.username, "password": self.password},
        )
        # 302 = successful customer login → /projects/
        self.assertEqual(r.status_code, 302)
        # Sanity: an auth session exists.
        self.assertIn("_auth_user_id", self.client.session)
        # But the OTP stamp must NOT have been written.
        self.assertNotIn(OTP_VERIFIED_AT_SESSION_KEY, self.client.session)


class AuditLogTests(TestCase):
    """T31 · signal-driven audit log for sensitive models.

    The receivers write inline (no transaction.on_commit deferral)
    so audit rows are visible immediately — including for changes
    that later roll back, which is operationally desirable for
    forensic visibility.
    """

    def _new_user(self, username, **extra):
        return User.objects.create_user(username, password="x", **extra)

    def _save(self, instance):
        instance.save()

    def _delete(self, instance):
        instance.delete()

    def test_user_create_writes_created_entry(self):
        from apps.core.models import AuditLogEntry

        before = AuditLogEntry.objects.count()
        self._new_user("t31_create", email="c@example.com")

        new_entries = AuditLogEntry.objects.order_by("-timestamp")[:1]
        self.assertEqual(AuditLogEntry.objects.count(), before + 1)
        entry = new_entries[0]
        self.assertEqual(entry.action, AuditLogEntry.Action.CREATED)
        self.assertEqual(entry.target_repr, "t31_create")
        self.assertIn("email", entry.changes)
        self.assertEqual(entry.changes["email"]["new"], "c@example.com")
        # CREATE stores no old value.
        self.assertIsNone(entry.changes["email"]["old"])

    def test_user_role_change_writes_role_changed_entry(self):
        """is_staff / is_superuser toggles must produce ROLE_CHANGED,
        not generic UPDATED — so an audit dashboard can filter
        privilege escalations specifically."""
        from apps.core.models import AuditLogEntry

        u = self._new_user("t31_role", email="r@example.com")
        before = AuditLogEntry.objects.count()
        u.is_staff = True
        self._save(u)

        self.assertEqual(AuditLogEntry.objects.count(), before + 1)
        entry = AuditLogEntry.objects.order_by("-timestamp")[0]
        self.assertEqual(entry.action, AuditLogEntry.Action.ROLE_CHANGED)
        self.assertEqual(entry.changes, {
            "is_staff": {"old": False, "new": True},
        })

    def test_password_change_is_not_audited(self):
        """The DENYLISTED_FIELDS guard must keep passwords out of
        the audit table even though ``User.save()`` does fire
        post_save. This is the most security-critical assertion of
        the suite: a leak here would defeat the whole pass."""
        from apps.core.models import AuditLogEntry

        u = self._new_user("t31_pwd", email="p@example.com")
        before = AuditLogEntry.objects.count()
        u.set_password("a-brand-new-password")
        self._save(u)

        # No new row written: password is denylisted AND last_login /
        # password hash is the only thing that changed.
        self.assertEqual(AuditLogEntry.objects.count(), before)
        # Defense-in-depth: even if a future regression DID write,
        # the password value would not be in any existing row.
        for entry in AuditLogEntry.objects.all():
            self.assertNotIn("password", entry.changes)
            for field_diff in entry.changes.values():
                self.assertNotIn("a-brand-new-password", str(field_diff))

    def test_user_delete_writes_deleted_entry_and_survives_target(self):
        """The audit entry must outlive the deleted target — on_delete
        is SET_NULL on the FK so the row is preserved, and
        ``target_repr`` keeps the username snapshot."""
        from apps.core.models import AuditLogEntry

        u = self._new_user("t31_del", email="d@example.com")
        target_pk = str(u.pk)
        self._delete(u)

        deleted_entries = AuditLogEntry.objects.filter(
            action=AuditLogEntry.Action.DELETED,
            target_object_id=target_pk,
        )
        self.assertEqual(deleted_entries.count(), 1)
        self.assertEqual(deleted_entries.first().target_repr, "t31_del")
        # The target FK has been resolved-then-nulled by the FK
        # (target object no longer exists) — the audit row still
        # carries the snapshot.
        self.assertEqual(deleted_entries.first().target_repr, "t31_del")

    def test_webtemplate_tier_change_is_published_action(self):
        """draft → published_live must be PUBLISHED, the inverse
        must be UNPUBLISHED. These are the most operationally
        meaningful events on the catalog surface."""
        from apps.core.models import AuditLogEntry
        from apps.catalog.models import (
            Category, ProfessionCluster, VisualStyle, WebTemplate,
        )

        cat = Category.objects.create(name="T31 Test Cat", slug="t31-test-cat")
        cluster = ProfessionCluster.objects.create(
            name="T31 Cluster", category=cat, slug="t31-cluster",
        )
        style = VisualStyle.objects.create(label="T31 Style", slug="t31-style")
        tpl = WebTemplate.objects.create(
            category=cat,
            profession_cluster=cluster,
            visual_style=style,
            name="T31 Tier Probe",
            slug="t31-tier-probe",
            tier=WebTemplate.Tier.DRAFT,
            status=WebTemplate.Status.DRAFT,
            price=0,
        )

        # The CREATED entry includes the initial tier=DRAFT.
        created = AuditLogEntry.objects.filter(
            target_object_id=str(tpl.pk),
            action=AuditLogEntry.Action.CREATED,
        ).first()
        self.assertIsNotNone(created)
        self.assertEqual(created.changes["tier"]["new"], "draft")

        # Promote to live.
        tpl.tier = WebTemplate.Tier.PUBLISHED_LIVE
        self._save(tpl)
        published = AuditLogEntry.objects.filter(
            target_object_id=str(tpl.pk),
            action=AuditLogEntry.Action.PUBLISHED,
        ).first()
        self.assertIsNotNone(published)
        self.assertEqual(published.changes["tier"], {
            "old": "draft", "new": "published_live",
        })

        # Take back to draft.
        tpl.tier = WebTemplate.Tier.DRAFT
        self._save(tpl)
        unpublished = AuditLogEntry.objects.filter(
            target_object_id=str(tpl.pk),
            action=AuditLogEntry.Action.UNPUBLISHED,
        ).first()
        self.assertIsNotNone(unpublished)
        self.assertEqual(unpublished.changes["tier"], {
            "old": "published_live", "new": "draft",
        })

    def test_cosmetic_change_outside_watched_fields_is_silent(self):
        """Updating a field NOT in WATCHED_FIELDS must not produce
        an audit entry. This keeps the table free of noise from
        unrelated edits (e.g. updating a User's first_name)."""
        from apps.core.models import AuditLogEntry

        u = self._new_user("t31_noise", email="n@example.com")
        before = AuditLogEntry.objects.count()
        u.first_name = "Mario"
        self._save(u)

        self.assertEqual(AuditLogEntry.objects.count(), before)

    def test_audit_admin_is_read_only(self):
        """``AuditLogEntryAdmin`` must refuse add / delete and never
        permit save (tamper-resistant by default)."""
        from apps.core.admin import AuditLogEntryAdmin
        from apps.core.models import AuditLogEntry
        from django.contrib import admin as django_admin

        admin_inst = django_admin.site._registry[AuditLogEntry]
        self.assertIsInstance(admin_inst, AuditLogEntryAdmin)
        # No add permission for anyone — audit rows come from signals only.
        self.assertFalse(admin_inst.has_add_permission(request=None))
        # No delete permission for anyone — table is append-only.
        self.assertFalse(admin_inst.has_delete_permission(request=None))


class AuditRetentionTests(TestCase):
    """T32 · ``python manage.py prune_audit_log`` deletes rows older
    than the retention window. The command is THE single operational
    surface for retention — these tests pin its contract."""

    @classmethod
    def setUpTestData(cls):
        from apps.core.models import AuditLogEntry
        from django.utils import timezone
        from datetime import timedelta

        # Two old rows (older than the default 365d window).
        cls.old1 = AuditLogEntry.objects.create(
            action="updated", target_repr="t32-old-1",
            target_object_id="old-1", changes={},
        )
        cls.old2 = AuditLogEntry.objects.create(
            action="created", target_repr="t32-old-2",
            target_object_id="old-2", changes={},
        )
        # Force-update timestamps to the past (auto_now_add fixes the
        # CREATE time so we have to update with UPDATE statements).
        long_ago = timezone.now() - timedelta(days=400)
        AuditLogEntry.objects.filter(pk__in=[cls.old1.pk, cls.old2.pk]).update(
            timestamp=long_ago,
        )
        # One recent row that must survive the prune.
        cls.recent = AuditLogEntry.objects.create(
            action="updated", target_repr="t32-recent",
            target_object_id="recent-1", changes={},
        )

    def _call(self, **kwargs):
        from django.core.management import call_command
        from io import StringIO
        out = StringIO()
        call_command("prune_audit_log", stdout=out, **kwargs)
        return out.getvalue()

    def test_dry_run_does_not_delete(self):
        from apps.core.models import AuditLogEntry

        before = AuditLogEntry.objects.count()
        out = self._call(dry_run=True)

        self.assertEqual(AuditLogEntry.objects.count(), before)
        self.assertIn("DRY RUN", out)
        self.assertIn("Matching rows to delete: 2", out)

    def test_prune_with_yes_deletes_old_rows_only(self):
        from apps.core.models import AuditLogEntry

        out = self._call(yes=True)

        # Old rows gone, recent row preserved.
        self.assertEqual(AuditLogEntry.objects.filter(pk=self.old1.pk).count(), 0)
        self.assertEqual(AuditLogEntry.objects.filter(pk=self.old2.pk).count(), 0)
        self.assertEqual(AuditLogEntry.objects.filter(pk=self.recent.pk).count(), 1)
        self.assertIn("Pruned 2", out)

    def test_older_than_overrides_default(self):
        """``--older-than 0`` should match every row whose timestamp
        is strictly less than NOW — which is a useful break-glass
        'wipe everything that already exists' command."""
        from apps.core.models import AuditLogEntry

        out = self._call(older_than=0, yes=True)

        # All three rows (old1 + old2 + recent) get pruned because
        # they're all <= now.
        self.assertEqual(AuditLogEntry.objects.count(), 0)
        self.assertIn("Pruned 3", out)

    def test_command_refuses_without_yes_on_non_tty(self):
        """Belt-and-braces: piping to /dev/null without --yes must
        raise instead of silently wiping the table. We force the
        ``isatty()`` probe to False here because Django's test runner
        attaches a real TTY in some environments."""
        from django.core.management import call_command
        from django.core.management.base import CommandError
        from io import StringIO

        with mock.patch("sys.stdin.isatty", return_value=False):
            with self.assertRaises(CommandError) as cm:
                call_command(
                    "prune_audit_log",
                    stdout=StringIO(), stderr=StringIO(),
                )
        self.assertIn("--yes", str(cm.exception))

    def test_zero_match_short_circuits(self):
        """When the cutoff selects zero rows, the command reports
        success and writes nothing."""
        from apps.core.models import AuditLogEntry

        # All rows are < 100,000 days old.
        out = self._call(older_than=100_000, yes=True)
        self.assertIn("Nothing to prune", out)
        # All three rows are still around.
        self.assertEqual(AuditLogEntry.objects.count(), 3)


@override_settings(
    AUDIT_ALERTS_ENABLED=True,
    AUDIT_ALERT_RECIPIENTS=["ops@example.test"],
    EMAIL_BACKEND="django.core.mail.backends.locmem.EmailBackend",
)
class AuditAlertingTests(TestCase):
    """T32 · the post-save alert receiver fires logger WARNING +
    email for ROLE_CHANGED and DELETED audit actions only."""

    def setUp(self):
        from django.core import mail
        mail.outbox = []

    def _create_audit(self, action, **extra):
        from apps.core.models import AuditLogEntry
        defaults = {
            "actor_repr": "t32actor",
            "target_repr": "t32target",
            "target_object_id": "1",
            "changes": {"is_staff": {"old": False, "new": True}},
        }
        defaults.update(extra)
        return AuditLogEntry.objects.create(action=action, **defaults)

    def test_role_changed_triggers_log_and_email(self):
        from django.core import mail

        with self.assertLogs("marketweb.audit", level="WARNING") as captured:
            entry = self._create_audit("role_changed")

        # Logger fired.
        self.assertTrue(any("audit_alert" in line for line in captured.output))
        # Email fired.
        self.assertEqual(len(mail.outbox), 1)
        msg = mail.outbox[0]
        self.assertIn("role_changed", msg.subject)
        self.assertEqual(msg.to, ["ops@example.test"])
        # Body sanity: actor + target + changes are present.
        self.assertIn("t32actor", msg.body)
        self.assertIn("t32target", msg.body)
        self.assertIn("is_staff", msg.body)

    def test_deleted_triggers_log_and_email(self):
        from django.core import mail
        with self.assertLogs("marketweb.audit", level="WARNING") as captured:
            self._create_audit("deleted", changes={})
        self.assertTrue(any("audit_alert" in line for line in captured.output))
        self.assertEqual(len(mail.outbox), 1)
        self.assertIn("deleted", mail.outbox[0].subject)

    def test_published_does_not_trigger(self):
        """PUBLISHED is meaningful but high-frequency / low-criticality
        on a marketplace catalog. T32 alerts deliberately exclude it
        to avoid alert fatigue."""
        from django.core import mail
        # No logger lines at WARNING expected — we still capture to
        # confirm absence.
        try:
            with self.assertLogs("marketweb.audit", level="WARNING") as cap:
                self._create_audit("published")
            # If we got here, the context produced log lines we
            # didn't expect.
            for line in cap.output:
                self.assertNotIn("audit_alert", line)
        except AssertionError as e:
            # ``assertLogs`` raises when no log lines were emitted —
            # which is exactly what we want for the silent case.
            if "no logs" not in str(e):
                raise
        self.assertEqual(len(mail.outbox), 0)

    def test_created_and_updated_do_not_trigger(self):
        from django.core import mail
        try:
            with self.assertLogs("marketweb.audit", level="WARNING") as cap:
                self._create_audit("created")
                self._create_audit("updated")
            for line in cap.output:
                self.assertNotIn("audit_alert", line)
        except AssertionError as e:
            if "no logs" not in str(e):
                raise
        self.assertEqual(len(mail.outbox), 0)

    @override_settings(AUDIT_ALERT_RECIPIENTS=[])
    def test_empty_recipients_suppresses_email_but_keeps_log(self):
        """The logger fires regardless of recipients (so operators
        with log aggregation still see alerts). Email is suppressed
        when no recipients are configured — the dev default."""
        from django.core import mail
        with self.assertLogs("marketweb.audit", level="WARNING") as captured:
            self._create_audit("deleted")
        self.assertTrue(any("audit_alert" in line for line in captured.output))
        self.assertEqual(len(mail.outbox), 0)

    @override_settings(AUDIT_ALERTS_ENABLED=False)
    def test_kill_switch_disables_both_channels(self):
        """``AUDIT_ALERTS_ENABLED=False`` silences logger AND email."""
        from django.core import mail
        try:
            with self.assertLogs("marketweb.audit", level="WARNING") as cap:
                self._create_audit("role_changed")
            for line in cap.output:
                self.assertNotIn("audit_alert", line)
        except AssertionError as e:
            if "no logs" not in str(e):
                raise
        self.assertEqual(len(mail.outbox), 0)


class AuditedDecoratorTests(TestCase):
    """T33 · the ``@audited`` decorator wraps real service functions
    in ``apps.commerce.services``. These tests prove that calling
    those services (a) writes an explicit AuditLogEntry with the
    correct semantic action label, (b) carries the configured
    metadata in the ``changes`` JSON, (c) the signal-driven
    UPDATED entry is ALSO emitted (complementary, not a
    duplicate), and (d) failure paths do not write an audit row.
    """

    @classmethod
    def setUpTestData(cls):
        # Minimal commerce fixture: Storefront + Address + Order
        # using only the fields required by the model.
        from apps.commerce.models import Address, Order, ShippingMethod, Storefront
        from apps.catalog.models import (
            Category, ProfessionCluster, VisualStyle, WebTemplate,
        )

        cat = Category.objects.create(name="T33 Cat", slug="t33-cat")
        cluster = ProfessionCluster.objects.create(
            name="T33 Cluster", category=cat, slug="t33-cluster",
        )
        style = VisualStyle.objects.create(label="T33 Style", slug="t33-style")
        tpl = WebTemplate.objects.create(
            category=cat,
            profession_cluster=cluster,
            visual_style=style,
            name="T33 Tpl", slug="t33-tpl",
            tier=WebTemplate.Tier.PUBLISHED_LIVE,
            status=WebTemplate.Status.PUBLISHED,
            price=10,
        )
        cls.sf = Storefront.objects.create(
            template=tpl,
            payment_provider="stub",
            currency="EUR",
        )
        cls.shipping_method = ShippingMethod.objects.create(
            storefront=cls.sf,
            code="t33-method",
            title="T33 Standard",
            price=0,
        )
        cls.shipping_address = Address.objects.create(
            full_name="T33 Buyer",
            line1="Via T33 1",
            city="Roma",
            postal_code="00100",
            country="Italia",
            email="buyer@example.com",
        )

    def _new_order(self):
        from apps.commerce.models import Order
        from apps.core.models import AuditLogEntry
        # Clear audit so each test starts clean (test DB rolls back
        # but the fixture-created rows from setUpTestData are
        # persisted at class level inside the transaction).
        AuditLogEntry.objects.all().delete()
        return Order.objects.create(
            storefront=self.sf,
            customer_name="T33 Buyer",
            customer_email="buyer@example.com",
            shipping_address=self.shipping_address,
            shipping_method=self.shipping_method,
            subtotal=10,
            shipping_total=0,
            grand_total=10,
            currency="EUR",
            status=Order.Status.PENDING,
            payment_status=Order.PaymentStatus.UNPAID,
        )

    def test_mark_order_paid_writes_explicit_audit_row(self):
        """``mark_order_paid(order=..., note="ref 42")`` must produce
        an AuditLogEntry with action=ORDER_PAID and the note in
        ``changes``. The T31 signal UPDATED row is ALSO emitted."""
        from apps.commerce.services import mark_order_paid
        from apps.core.models import AuditLogEntry

        order = self._new_order()
        before = AuditLogEntry.objects.count()
        mark_order_paid(order=order, note="Wire transfer ref 42")

        new_entries = AuditLogEntry.objects.filter(
            timestamp__gte=order.created_at,
        ).order_by("timestamp")
        actions = list(new_entries.values_list("action", flat=True))

        # Both rows present: signal UPDATED + explicit ORDER_PAID.
        self.assertIn(AuditLogEntry.Action.UPDATED, actions)
        self.assertIn(AuditLogEntry.Action.ORDER_PAID, actions)

        explicit = new_entries.filter(action=AuditLogEntry.Action.ORDER_PAID).first()
        self.assertIsNotNone(explicit)
        self.assertEqual(explicit.changes, {"note": "Wire transfer ref 42"})
        # The target points at the order via the GenericForeignKey.
        self.assertEqual(explicit.target_object_id, str(order.pk))

    def test_cancel_order_writes_explicit_audit_row_with_reason(self):
        """``cancel_order(order=..., reason="X")`` must produce an
        AuditLogEntry with action=ORDER_CANCELLED and the reason in
        ``changes`` — the operational ``why`` that the T31 signal
        diff (``status: confirmed→cancelled``) cannot capture."""
        from apps.commerce.services import cancel_order
        from apps.core.models import AuditLogEntry

        order = self._new_order()
        cancel_order(order=order, reason="customer changed mind")

        explicit = AuditLogEntry.objects.filter(
            action=AuditLogEntry.Action.ORDER_CANCELLED,
            target_object_id=str(order.pk),
        ).first()
        self.assertIsNotNone(explicit)
        self.assertEqual(explicit.changes, {"reason": "customer changed mind"})

        # T31 signal-driven UPDATED is also present (complementary).
        signal_updated = AuditLogEntry.objects.filter(
            action=AuditLogEntry.Action.UPDATED,
            target_object_id=str(order.pk),
        ).first()
        self.assertIsNotNone(signal_updated)
        self.assertIn("status", signal_updated.changes)

    def test_cancel_order_failure_does_not_write_explicit_audit(self):
        """If the wrapped function raises, NO explicit audit row is
        written. (The signal-driven row may or may not appear
        depending on whether ``order.save()`` got called before the
        raise — here cancel_order's guard raises BEFORE save.)"""
        from apps.commerce.services import cancel_order, CommerceError
        from apps.commerce.models import Order
        from apps.core.models import AuditLogEntry

        # Build an order already in CANCELLED state — cancel_order
        # refuses to operate on it (raises CommerceError).
        order = self._new_order()
        order.status = Order.Status.CANCELLED
        order.save()
        # Clear baseline so we only see new entries from the failing call.
        AuditLogEntry.objects.all().delete()

        with self.assertRaises(CommerceError):
            cancel_order(order=order, reason="should not be audited")

        # No ORDER_CANCELLED row was written.
        self.assertEqual(
            AuditLogEntry.objects.filter(
                action=AuditLogEntry.Action.ORDER_CANCELLED,
            ).count(),
            0,
        )

    def test_decorator_scrubs_denylisted_metadata(self):
        """Defence in depth: if a caller passes a kwarg whose name
        is on DENYLISTED_FIELDS, the decorator MUST NOT serialize
        it even if it was listed in ``metadata_args``. Today's
        services never pass such a kwarg — this test pins the
        invariant for future maintenance."""
        from apps.core.audit import audited
        from apps.core.models import AuditLogEntry
        from apps.commerce.models import Order

        @audited(
            action=AuditLogEntry.Action.UPDATED,
            target_arg="order",
            metadata_args=("note", "password"),
        )
        def fake_service(*, order, note="", password=""):
            return order

        order = self._new_order()
        AuditLogEntry.objects.all().delete()
        fake_service(order=order, note="ok", password="LEAK_ME_IF_YOU_CAN")

        explicit = AuditLogEntry.objects.filter(
            target_object_id=str(order.pk),
        ).last()
        self.assertIn("note", explicit.changes)
        self.assertNotIn("password", explicit.changes)
        # Defense in depth: the value itself never reaches any row.
        for entry in AuditLogEntry.objects.all():
            self.assertNotIn("LEAK_ME_IF_YOU_CAN", str(entry.changes))

    def test_decorator_silent_when_target_kwarg_missing(self):
        """If the decorated function is called WITHOUT the
        ``target_arg`` kwarg (or with None), the decorator logs a
        warning and skips the audit write — it must NOT raise and
        break the business call."""
        from apps.core.audit import audited
        from apps.core.models import AuditLogEntry

        @audited(action="updated", target_arg="thing", metadata_args=("note",))
        def f(*, thing=None, note=""):
            return "ok"

        AuditLogEntry.objects.all().delete()
        with self.assertLogs("marketweb.audit", level="WARNING") as cap:
            result = f(note="anything")  # no `thing` kwarg
        self.assertEqual(result, "ok")
        self.assertTrue(any("target_missing" in line for line in cap.output))
        self.assertEqual(AuditLogEntry.objects.count(), 0)


@override_settings(
    AUDIT_ALERTS_ENABLED=True,
    AUDIT_ALERT_RECIPIENTS=[],  # email channel off — we only assert Sentry breadcrumbs
)
class SentryAuditBreadcrumbTests(TestCase):
    """T34 · the explicit ``LoggingIntegration`` wired by
    ``marketweb.sentry.init_sentry_if_dsn_set`` must propagate
    ``marketweb.audit`` WARN lines as Sentry breadcrumbs with
    structured ``data`` (audit_action / audit_actor / audit_target /
    audit_changes / audit_request_ip). These tests use a no-network
    capturing transport so they run in CI without any DSN."""

    def _new_capturing_transport(self):
        """Build a Transport subclass that records every event it
        would have shipped to Sentry. Reading the event payload as
        JSON lets us inspect breadcrumbs without any network call."""
        import json
        from sentry_sdk.transport import Transport

        class CapturingTransport(Transport):
            def __init__(self):
                super().__init__({})
                self.events = []

            def capture_envelope(self, envelope):
                for item in envelope.items:
                    if item.headers.get("type") == "event":
                        self.events.append(json.loads(item.payload.get_bytes()))

        return CapturingTransport()

    def _init_sentry(self, transport):
        """Init Sentry with the capturing transport AND clear the
        global isolation scope so breadcrumbs queued by an earlier
        test in the same class don't leak into the new event."""
        import sentry_sdk
        from sentry_sdk.integrations.django import DjangoIntegration
        from sentry_sdk.integrations.logging import LoggingIntegration
        import logging as _logging

        # Mirror the helper's explicit LoggingIntegration config.
        sentry_sdk.init(
            dsn="http://x@example/1",
            integrations=[
                DjangoIntegration(),
                LoggingIntegration(
                    level=_logging.WARNING,
                    event_level=_logging.ERROR,
                ),
            ],
            transport=transport,
            traces_sample_rate=0.0,
            profiles_sample_rate=0.0,
            send_default_pii=False,
        )
        # Hard-reset both scopes so any breadcrumb from a previous
        # test cannot land in this test's captured event. Sentry-SDK
        # 2.x exposes both `get_isolation_scope` and `get_current_scope`.
        sentry_sdk.get_isolation_scope().clear()
        sentry_sdk.get_current_scope().clear()

    def tearDown(self):
        # Reset the global hub so test isolation is preserved.
        import sentry_sdk
        sentry_sdk.init(dsn=None)
        sentry_sdk.get_isolation_scope().clear()
        sentry_sdk.get_current_scope().clear()

    def test_audit_alert_becomes_sentry_breadcrumb_with_structured_data(self):
        """Writing an AuditLogEntry whose action is in ALERT_ACTIONS
        triggers the T32 receiver, which emits a logger.warning with
        ``extra={...}``. The Sentry breadcrumb attached to a later
        captured exception must carry ALL the extra keys as
        structured fields in ``data``."""
        import sentry_sdk
        from apps.core.models import AuditLogEntry

        transport = self._new_capturing_transport()
        self._init_sentry(transport)

        # Trigger via the T32 receiver — uses the production code path.
        AuditLogEntry.objects.create(
            action=AuditLogEntry.Action.ROLE_CHANGED,
            actor_repr="t34-admin",
            target_repr="t34-target",
            target_object_id="42",
            changes={"is_staff": {"old": False, "new": True}},
            request_ip="10.0.0.7",
        )

        # Capture a synthetic exception so the breadcrumbs flush to
        # the transport.
        try:
            raise RuntimeError("T34 synthetic post-audit exception")
        except RuntimeError:
            sentry_sdk.capture_exception()

        self.assertEqual(len(transport.events), 1)
        event = transport.events[0]
        crumbs = event.get("breadcrumbs", {}).get("values", [])
        audit_crumbs = [c for c in crumbs if c.get("category") == "marketweb.audit"]
        self.assertEqual(len(audit_crumbs), 1, f"breadcrumbs={crumbs!r}")
        crumb = audit_crumbs[0]
        self.assertEqual(crumb["level"], "warning")
        self.assertIn("audit_alert", crumb["message"])

        data = crumb.get("data", {})
        self.assertEqual(data.get("audit_action"), "role_changed")
        self.assertEqual(data.get("audit_actor"), "t34-admin")
        self.assertEqual(data.get("audit_target"), "t34-target")
        self.assertEqual(data.get("audit_request_ip"), "10.0.0.7")
        # audit_changes is a dict in `extra`, but Sentry may serialize it
        # as a string; accept both shapes.
        ac = data.get("audit_changes")
        self.assertTrue(
            (isinstance(ac, dict) and "is_staff" in ac)
            or (isinstance(ac, str) and "is_staff" in ac),
            f"audit_changes missing/wrong shape: {ac!r}",
        )

    def test_routine_audit_creates_do_not_become_breadcrumbs(self):
        """T31 signal-driven CREATED / UPDATED entries are written
        WITHOUT a logger.warning — only the T32 alert receiver logs.
        So routine writes must NOT pollute the Sentry breadcrumb
        stream. This test pins the noise-control invariant."""
        import sentry_sdk
        from apps.core.models import AuditLogEntry

        transport = self._new_capturing_transport()
        self._init_sentry(transport)

        AuditLogEntry.objects.create(
            action=AuditLogEntry.Action.CREATED,  # NOT in ALERT_ACTIONS
            actor_repr="t34-routine",
            target_repr="t34-routine-target",
            target_object_id="1",
            changes={"email": {"old": None, "new": "x@example.com"}},
        )
        try:
            raise RuntimeError("t34 routine")
        except RuntimeError:
            sentry_sdk.capture_exception()

        crumbs = transport.events[0].get("breadcrumbs", {}).get("values", [])
        audit_crumbs = [c for c in crumbs if c.get("category") == "marketweb.audit"]
        self.assertEqual(
            len(audit_crumbs), 0,
            "CREATED writes must not produce audit breadcrumbs — "
            "only ALERT_ACTIONS do.",
        )

    def test_sentry_init_helper_pins_logging_integration(self):
        """Belt-and-braces: the T34 init helper must actually
        register a LoggingIntegration on its init call. This test
        exercises the real helper (not the in-test re-init) to lock
        the contract."""
        import sentry_sdk
        from sentry_sdk.integrations.logging import LoggingIntegration
        from marketweb.sentry import init_sentry_if_dsn_set

        def env(key, default=None, *, required=False, cast=str):
            values = {"SENTRY_DSN": "http://x@example/1"}
            raw = values.get(key, default)
            if cast is bool:
                return bool(raw)
            if cast is float:
                return float(raw or 0)
            if cast is int:
                return int(raw or 0)
            return raw

        # Reset between tests.
        sentry_sdk.init(dsn=None)
        self.assertTrue(init_sentry_if_dsn_set(env))

        # The active client must carry our LoggingIntegration.
        client = sentry_sdk.get_client()
        integration = client.get_integration(LoggingIntegration)
        self.assertIsNotNone(
            integration,
            "init_sentry_if_dsn_set did not register LoggingIntegration",
        )


class AuditedExtensionTests(TestCase):
    """T35 · ``@audited`` decorator extension to three additional
    service flows. Asserts that:

    - ``set_order_fulfillment(...)`` writes BOTH a T31 signal row
      (Order is tracked) AND a T35 explicit row with the new
      ``order_fulfillment_changed`` action label + metadata.
    - ``publish_project(...)`` writes EXACTLY one audit row: the
      T35 explicit ``project_published``. No T31 row because
      CustomerProject is not in TRACKED_MODELS.
    - ``unpublish_project(...)`` writes EXACTLY one audit row:
      the T35 explicit ``project_unpublished``.
    - Invalid ``fulfillment_status`` raises CommerceError without
      writing an explicit row.
    """

    @classmethod
    def setUpTestData(cls):
        from apps.commerce.models import Address, Order, ShippingMethod, Storefront
        from apps.catalog.models import (
            Category, ProfessionCluster, VisualStyle, WebTemplate,
        )

        cat = Category.objects.create(name="T35 Cat", slug="t35-cat")
        cluster = ProfessionCluster.objects.create(
            name="T35 Cluster", category=cat, slug="t35-cluster",
        )
        style = VisualStyle.objects.create(label="T35 Style", slug="t35-style")
        cls.tpl = WebTemplate.objects.create(
            category=cat,
            profession_cluster=cluster,
            visual_style=style,
            name="T35 Tpl", slug="t35-tpl",
            tier=WebTemplate.Tier.PUBLISHED_LIVE,
            status=WebTemplate.Status.PUBLISHED,
            price=10,
        )
        cls.sf = Storefront.objects.create(
            template=cls.tpl, payment_provider="stub", currency="EUR",
        )
        cls.shipping_method = ShippingMethod.objects.create(
            storefront=cls.sf, code="t35-method", title="T35 Standard", price=0,
        )
        cls.shipping_address = Address.objects.create(
            full_name="T35 Buyer", line1="Via T35 1",
            city="Roma", postal_code="00100",
            country="Italia", email="buyer@example.com",
        )
        cls.editor_user = User.objects.create_user(
            "t35editor", password="x", is_staff=True,
        )

    def _new_order(self):
        from apps.commerce.models import Order
        from apps.core.models import AuditLogEntry
        AuditLogEntry.objects.all().delete()
        return Order.objects.create(
            storefront=self.sf,
            customer_name="T35 Buyer", customer_email="buyer@example.com",
            shipping_address=self.shipping_address,
            shipping_method=self.shipping_method,
            subtotal=10, shipping_total=0, grand_total=10, currency="EUR",
            status=Order.Status.CONFIRMED,
            payment_status=Order.PaymentStatus.PAID,
            fulfillment_status="unfulfilled",
        )

    def _new_project(self):
        from apps.projects.models import CustomerProject, ProjectDesignTokens
        from apps.core.models import AuditLogEntry
        AuditLogEntry.objects.all().delete()
        project = CustomerProject.objects.create(
            owner=self.editor_user,
            source_template=self.tpl,
            source_archetype=self.tpl.slug,
            source_category_slug="t35-cat",
            name="T35 Project",
            status=CustomerProject.Status.DRAFT,
        )
        # publish_project/unpublish_project both call _build_snapshot,
        # which requires the OneToOne ProjectDesignTokens row to exist.
        ProjectDesignTokens.objects.create(project=project)
        # _new_project must reset the audit table AFTER both creates
        # so the test sees only the rows produced by the service call.
        AuditLogEntry.objects.all().delete()
        return project

    # ── set_order_fulfillment ──────────────────────────────────────

    def test_set_order_fulfillment_writes_explicit_row_with_metadata(self):
        from apps.commerce.services import set_order_fulfillment
        from apps.commerce.models import Order
        from apps.core.models import AuditLogEntry

        order = self._new_order()
        set_order_fulfillment(
            order=order,
            fulfillment_status=Order.FulfillmentStatus.SHIPPED,
            tracking_carrier="DHL",
            tracking_number="JD000000",
        )

        explicit = AuditLogEntry.objects.filter(
            action=AuditLogEntry.Action.ORDER_FULFILLMENT_CHANGED,
            target_object_id=str(order.pk),
        ).first()
        self.assertIsNotNone(explicit)
        self.assertEqual(explicit.changes, {
            "fulfillment_status": "shipped",
            "tracking_carrier": "DHL",
            "tracking_number": "JD000000",
        })
        # Complementary T31 signal row also present (Order is tracked).
        signal = AuditLogEntry.objects.filter(
            action=AuditLogEntry.Action.UPDATED,
            target_object_id=str(order.pk),
        ).first()
        self.assertIsNotNone(signal)
        self.assertIn("status", signal.changes)

    def test_invalid_fulfillment_status_writes_no_explicit_row(self):
        from apps.commerce.services import set_order_fulfillment, CommerceError
        from apps.core.models import AuditLogEntry

        order = self._new_order()
        with self.assertRaises(CommerceError):
            set_order_fulfillment(
                order=order, fulfillment_status="nonsense",
            )

        # The guard raises BEFORE order.save() — neither signal nor
        # explicit row is written.
        self.assertEqual(
            AuditLogEntry.objects.filter(
                action=AuditLogEntry.Action.ORDER_FULFILLMENT_CHANGED,
            ).count(),
            0,
        )

    # ── publish_project / unpublish_project ────────────────────────

    def test_publish_project_writes_only_explicit_row(self):
        from apps.projects.services import publish_project
        from apps.core.models import AuditLogEntry

        project = self._new_project()
        publish_project(project=project, editor=self.editor_user)

        rows = AuditLogEntry.objects.filter(
            target_object_id=str(project.pk),
        )
        # Exactly ONE row — the explicit T35 ``project_published``.
        # CustomerProject is not in TRACKED_MODELS, so no T31 signal row.
        self.assertEqual(rows.count(), 1)
        explicit = rows.first()
        self.assertEqual(explicit.action, AuditLogEntry.Action.PROJECT_PUBLISHED)
        self.assertEqual(explicit.target_repr, str(project))
        # No metadata configured for publish_project — changes is empty.
        self.assertEqual(explicit.changes, {})

    def test_unpublish_project_writes_only_explicit_row(self):
        from apps.projects.services import publish_project, unpublish_project
        from apps.core.models import AuditLogEntry

        project = self._new_project()
        # Publish first so unpublish has a real state transition.
        publish_project(project=project, editor=self.editor_user)
        AuditLogEntry.objects.all().delete()

        unpublish_project(project=project, editor=self.editor_user)

        rows = AuditLogEntry.objects.filter(
            target_object_id=str(project.pk),
        )
        self.assertEqual(rows.count(), 1)
        explicit = rows.first()
        self.assertEqual(explicit.action, AuditLogEntry.Action.PROJECT_UNPUBLISHED)


class ExportAuditLogTests(TestCase):
    """T36 · ``python manage.py export_audit_log`` emits the audit
    table to JSONL or CSV, filterable by action / actor / target type
    / date range. The command is the single export surface — these
    tests pin its contract."""

    @classmethod
    def setUpTestData(cls):
        from datetime import timedelta
        from django.contrib.contenttypes.models import ContentType
        from django.utils import timezone

        from apps.core.models import AuditLogEntry

        cls.user_ct = ContentType.objects.get(app_label="accounts", model="user")
        # Fixture: 3 rows with distinct actor / action / target / age.
        cls.row_old = AuditLogEntry.objects.create(
            actor_repr="alice@example.com",
            action="role_changed",
            target_content_type=cls.user_ct,
            target_object_id="100",
            target_repr="alice (id=100)",
            changes={"is_staff": {"old": False, "new": True}},
            request_ip="10.0.0.1",
        )
        cls.row_mid = AuditLogEntry.objects.create(
            actor_repr="bob@example.com",
            action="deleted",
            target_content_type=cls.user_ct,
            target_object_id="101",
            target_repr="charlie (id=101)",
            changes={},
            request_ip="10.0.0.2",
        )
        cls.row_new = AuditLogEntry.objects.create(
            actor_repr="alice@example.com",
            action="updated",
            target_content_type=cls.user_ct,
            target_object_id="100",
            target_repr="alice (id=100)",
            changes={"email": {"old": "a@x", "new": "alice@example.com"}},
            request_ip="10.0.0.1",
        )
        # Force timestamps to known offsets so date-range filters are
        # exercisable. auto_now_add ran at insert; UPDATE overrides.
        now = timezone.now()
        AuditLogEntry.objects.filter(pk=cls.row_old.pk).update(
            timestamp=now - timedelta(days=10),
        )
        AuditLogEntry.objects.filter(pk=cls.row_mid.pk).update(
            timestamp=now - timedelta(days=5),
        )
        AuditLogEntry.objects.filter(pk=cls.row_new.pk).update(
            timestamp=now - timedelta(days=1),
        )

    def _run(self, **opts):
        """Invoke the command with the given options. Returns stdout
        body. stderr (summary) is captured but not returned."""
        from django.core.management import call_command
        from io import StringIO

        stdout, stderr = StringIO(), StringIO()
        call_command("export_audit_log", stdout=stdout, stderr=stderr, **opts)
        return stdout.getvalue()

    # ── format coverage ──────────────────────────────────────────────

    def test_jsonl_full_export_contains_all_three_rows_in_chronological_order(self):
        import json

        body = self._run()
        lines = [line for line in body.splitlines() if line.strip()]
        self.assertEqual(len(lines), 3)

        parsed = [json.loads(line) for line in lines]
        # ASC by timestamp: oldest first.
        self.assertEqual(parsed[0]["actor_repr"], "alice@example.com")
        self.assertEqual(parsed[0]["action"], "role_changed")
        self.assertEqual(parsed[1]["actor_repr"], "bob@example.com")
        self.assertEqual(parsed[2]["action"], "updated")

        # Documented field set, no extras.
        expected_keys = {
            "timestamp", "actor_repr", "action", "target_type",
            "target_object_id", "target_repr", "changes", "request_ip",
        }
        self.assertEqual(set(parsed[0].keys()), expected_keys)

        # target_type is the dotted "app_label.model" form, not the FK PK.
        self.assertEqual(parsed[0]["target_type"], "accounts.user")

        # changes is preserved as a nested dict (NOT stringified).
        self.assertIsInstance(parsed[0]["changes"], dict)
        self.assertEqual(
            parsed[0]["changes"],
            {"is_staff": {"old": False, "new": True}},
        )

    def test_csv_export_has_header_and_changes_serialized_as_json_string(self):
        import csv
        import io
        import json

        body = self._run(format="csv")
        reader = csv.DictReader(io.StringIO(body))
        self.assertEqual(
            reader.fieldnames,
            [
                "timestamp", "actor_repr", "action", "target_type",
                "target_object_id", "target_repr", "changes", "request_ip",
            ],
        )
        rows = list(reader)
        self.assertEqual(len(rows), 3)
        # changes is a JSON string in CSV (CSV cells are flat).
        decoded = json.loads(rows[0]["changes"])
        self.assertEqual(decoded, {"is_staff": {"old": False, "new": True}})

    # ── filter coverage ──────────────────────────────────────────────

    def test_filter_action_repeatable_narrows_to_matching_only(self):
        import json

        body = self._run(action=["role_changed", "deleted"])
        lines = [line for line in body.splitlines() if line.strip()]
        actions = sorted(json.loads(line)["action"] for line in lines)
        self.assertEqual(actions, ["deleted", "role_changed"])

    def test_filter_actor_is_substring_case_insensitive(self):
        import json

        body = self._run(actor="ALICE")
        lines = [line for line in body.splitlines() if line.strip()]
        self.assertEqual(len(lines), 2)
        for line in lines:
            self.assertIn("alice", json.loads(line)["actor_repr"])

    def test_filter_target_type_narrows_by_content_type(self):
        # All three fixtures point at accounts.User → expect 3 rows.
        body = self._run(target_type="accounts.User")
        lines = [line for line in body.splitlines() if line.strip()]
        self.assertEqual(len(lines), 3)

    def test_unknown_target_type_raises_command_error(self):
        from django.core.management import call_command
        from django.core.management.base import CommandError
        from io import StringIO

        with self.assertRaises(CommandError) as cm:
            call_command(
                "export_audit_log",
                target_type="nonexistent.Model",
                stdout=StringIO(), stderr=StringIO(),
            )
        self.assertIn("nonexistent.Model", str(cm.exception))

    def test_date_range_window_includes_since_excludes_until(self):
        from datetime import timedelta
        from django.utils import timezone
        import json

        now = timezone.now()
        # Window: [now-6d, now-2d) → only row_mid (5d ago) matches.
        since = (now - timedelta(days=6)).date().isoformat()
        until = (now - timedelta(days=2)).date().isoformat()
        body = self._run(since=since, until=until)
        lines = [line for line in body.splitlines() if line.strip()]
        self.assertEqual(len(lines), 1)
        self.assertEqual(json.loads(lines[0])["actor_repr"], "bob@example.com")

    def test_limit_caps_emitted_count(self):
        body = self._run(limit=1)
        lines = [line for line in body.splitlines() if line.strip()]
        self.assertEqual(len(lines), 1)

    # ── output target ────────────────────────────────────────────────

    def test_output_path_writes_to_file_and_omits_stdout(self):
        import json
        import tempfile
        from pathlib import Path

        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "audit.jsonl"
            body = self._run(output=str(path))

            # stdout is empty when --output is set.
            self.assertEqual(body, "")
            # File contains the full export.
            written = path.read_text(encoding="utf-8").splitlines()
            self.assertEqual(len(written), 3)
            json.loads(written[0])  # well-formed JSON


class SecurityHeadersTests(TestCase):
    """T37 · ``SecurityHeadersMiddleware`` sets the four browser-side
    headers that Django's SecurityMiddleware does NOT ship out of the
    box: Content-Security-Policy, Permissions-Policy,
    Cross-Origin-Resource-Policy, X-Permitted-Cross-Domain-Policies.

    The CSP is verified against the *actually-used* external origins
    (Bootstrap CDN, Google Fonts, Stripe) so a future template edit
    that adds a new external host fails CI before reaching prod.
    """

    def _get(self, path="/"):
        from django.test import Client
        return Client().get(path)

    # ── header presence ──────────────────────────────────────────────

    def test_all_four_t37_headers_present_on_html_response(self):
        # /it/ is the canonical localised homepage. Whatever its
        # status (200 / 302 — depends on data state), the middleware
        # MUST set the four headers.
        resp = self._get("/it/")
        for header in (
            "Content-Security-Policy",
            "Permissions-Policy",
            "Cross-Origin-Resource-Policy",
            "X-Permitted-Cross-Domain-Policies",
        ):
            self.assertIn(
                header, resp,
                f"{header} missing from response (status={resp.status_code})",
            )

    def test_headers_also_present_on_admin_login(self):
        # Admin surface needs the same hardening as the public site.
        resp = self._get("/admin/login/")
        self.assertIn("Content-Security-Policy", resp)
        self.assertIn("Permissions-Policy", resp)

    def test_headers_present_on_404_response(self):
        # 404 responses (404 templates can contain inline styles / inline
        # SVG with style attributes — they must be CSP-covered too).
        resp = self._get("/this-path-does-not-exist-t37/")
        self.assertEqual(resp.status_code, 404)
        self.assertIn("Content-Security-Policy", resp)
        self.assertIn("Permissions-Policy", resp)

    # ── CSP shape (real allowlist coverage) ──────────────────────────

    def test_csp_default_src_is_self(self):
        csp = self._get("/it/")["Content-Security-Policy"]
        self.assertIn("default-src 'self'", csp)

    def test_csp_allows_bootstrap_cdn_for_scripts_and_styles(self):
        csp = self._get("/it/")["Content-Security-Policy"]
        # Bootstrap 5.3 ships from jsdelivr (CSS + JS in templates/base.html).
        self.assertIn("https://cdn.jsdelivr.net", csp)

    def test_csp_allows_google_fonts_origins(self):
        csp = self._get("/it/")["Content-Security-Policy"]
        # Google Fonts CSS endpoint
        self.assertIn("https://fonts.googleapis.com", csp)
        # Google Fonts WOFF2 binaries endpoint
        self.assertIn("https://fonts.gstatic.com", csp)

    def test_csp_font_src_allows_bootstrap_icons_woff_from_jsdelivr(self):
        # bootstrap-icons.min.css references its WOFF2 via a relative
        # URL, which the browser resolves against the stylesheet's
        # origin (cdn.jsdelivr.net). The font-src directive MUST
        # allow that origin or the icon glyphs render as boxes.
        csp = self._get("/it/")["Content-Security-Policy"]
        font_src = next(
            d.strip() for d in csp.split(";") if d.strip().startswith("font-src")
        )
        self.assertIn("https://cdn.jsdelivr.net", font_src)

    def test_csp_allows_stripe_for_script_frame_connect(self):
        csp = self._get("/it/")["Content-Security-Policy"]
        # js.stripe.com appears in script-src (for stripe.js) AND
        # frame-src (for Stripe Elements iframe). api.stripe.com
        # appears in connect-src (for XHR confirmPayment).
        self.assertIn("https://js.stripe.com", csp)
        self.assertIn("https://api.stripe.com", csp)

    def test_csp_frame_src_allows_self_for_editor_preview_iframe(self):
        # The /projects/<uuid>/editor/ view embeds the live preview at
        # /templates/<cat>/<slug>/preview/?project=<uuid> via an iframe.
        # frame-src MUST include 'self' or the editor canvas renders
        # empty (T40 found this gap as a T37 regression).
        csp = self._get("/it/")["Content-Security-Policy"]
        frame_src = next(
            d.strip() for d in csp.split(";") if d.strip().startswith("frame-src")
        )
        self.assertIn("'self'", frame_src)

    def test_csp_blocks_object_src_and_locks_frame_ancestors_form_action_base(self):
        csp = self._get("/it/")["Content-Security-Policy"]
        # object-src 'none' — no Flash/ActiveX.
        self.assertIn("object-src 'none'", csp)
        # frame-ancestors 'self' — same-origin embedding allowed (the
        # editor embeds the preview iframe at same origin); cross-origin
        # third-party embedding still blocked.
        self.assertIn("frame-ancestors 'self'", csp)
        # form-action 'self' — no posting to evil.com from injected form.
        self.assertIn("form-action 'self'", csp)
        # base-uri 'self' — no <base href="..."> redirect to attacker.
        self.assertIn("base-uri 'self'", csp)

    def test_csp_documents_unsafe_inline_concession_in_both_script_and_style(self):
        # The pragmatic concession (see security_headers.py docstring).
        # If a later pass tightens the policy, this test fails — the
        # author MUST acknowledge they are tightening, not loosening.
        csp = self._get("/it/")["Content-Security-Policy"]
        # script-src ... 'unsafe-inline' ...
        script_src = next(
            d.strip() for d in csp.split(";") if d.strip().startswith("script-src")
        )
        self.assertIn("'unsafe-inline'", script_src)
        # style-src ... 'unsafe-inline' ...
        style_src = next(
            d.strip() for d in csp.split(";") if d.strip().startswith("style-src")
        )
        self.assertIn("'unsafe-inline'", style_src)

    # ── Permissions-Policy shape ─────────────────────────────────────

    def test_permissions_policy_opts_out_of_powerful_apis(self):
        pp = self._get("/it/")["Permissions-Policy"]
        # The site does NOT use any of these — opt them out so an
        # XSS / a future-added rogue iframe cannot ask the user.
        for feature in (
            "camera=()",
            "microphone=()",
            "geolocation=()",
            "usb=()",
            "payment=()",
        ):
            self.assertIn(feature, pp)

    def test_permissions_policy_opts_out_of_floc_and_topics(self):
        pp = self._get("/it/")["Permissions-Policy"]
        self.assertIn("interest-cohort=()", pp)
        self.assertIn("browsing-topics=()", pp)

    # ── Cross-origin / cross-domain ──────────────────────────────────

    def test_cross_origin_resource_policy_is_same_origin(self):
        self.assertEqual(
            self._get("/it/")["Cross-Origin-Resource-Policy"],
            "same-origin",
        )

    def test_x_permitted_cross_domain_policies_is_none(self):
        self.assertEqual(
            self._get("/it/")["X-Permitted-Cross-Domain-Policies"],
            "none",
        )


class BackupRestoreTests(TestCase):
    """T38 · ``backup_db`` writes a real DB dump and prunes older
    files; ``restore_drill`` loads a dump into a sandbox and asserts
    the sentinel tables are queryable.

    The SQLite path is exercised end-to-end (the project's test DB
    is SQLite). The PostgreSQL path is unit-tested with a mocked
    ``subprocess.run`` because we cannot guarantee a Postgres
    server is reachable from CI.
    """

    def _call_backup(self, **kwargs):
        from django.core.management import call_command
        from io import StringIO

        stdout = StringIO()
        call_command("backup_db", stdout=stdout, stderr=StringIO(), **kwargs)
        return stdout.getvalue()

    def _call_drill(self, backup_path, **kwargs):
        from django.core.management import call_command
        from io import StringIO

        stdout = StringIO()
        call_command(
            "restore_drill",
            str(backup_path),
            stdout=stdout,
            stderr=StringIO(),
            **kwargs,
        )
        return stdout.getvalue()

    # ── backup_db ────────────────────────────────────────────────────

    def test_backup_dry_run_writes_no_file(self):
        import tempfile
        from pathlib import Path

        with tempfile.TemporaryDirectory() as tmp:
            out = self._call_backup(output_dir=tmp, dry_run=True)
            self.assertIn("DRY RUN", out)
            self.assertEqual(list(Path(tmp).iterdir()), [])

    def test_backup_sqlite_writes_real_file_with_expected_name_shape(self):
        import re
        import tempfile
        from pathlib import Path

        with tempfile.TemporaryDirectory() as tmp:
            self._call_backup(output_dir=tmp, prefix="t38-test")
            files = list(Path(tmp).iterdir())
            self.assertEqual(len(files), 1)
            name = files[0].name
            # Pattern: {prefix}-{engine}-{YYYYMMDD-HHMMSS}.sqlite3
            self.assertRegex(
                name,
                r"^t38-test-sqlite-\d{8}-\d{6}\.sqlite3$",
            )
            self.assertGreater(files[0].stat().st_size, 0)

    def test_backup_retention_prunes_older_files_after_successful_write(self):
        import tempfile
        import time
        from pathlib import Path

        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            # Pre-seed 4 fake older backups matching the prefix+engine.
            for i in range(4):
                f = tmp_path / f"t38-test-sqlite-2025010{i}-000000.sqlite3"
                f.write_bytes(b"older")
                # Force older mtime so the new backup is unambiguously newest.
                past = time.time() - (10 * (i + 1))
                import os
                os.utime(f, (past, past))
            # Backup with keep=2 → expect 2 files total (the new one + 1 oldest of the 4 pruned).
            self._call_backup(output_dir=tmp, prefix="t38-test", keep=2)
            survivors = sorted(p.name for p in tmp_path.glob("t38-test-sqlite-*.sqlite3"))
            self.assertEqual(len(survivors), 2)

    def test_backup_retention_does_not_delete_files_with_other_prefix(self):
        import tempfile
        from pathlib import Path

        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            # Pre-seed an UNRELATED file — must survive.
            unrelated = tmp_path / "other-project-sqlite-20240101-000000.sqlite3"
            unrelated.write_bytes(b"unrelated")
            self._call_backup(output_dir=tmp, prefix="t38-test", keep=1)
            self.assertTrue(unrelated.exists())

    def test_backup_keep_zero_disables_pruning(self):
        import tempfile
        import time
        import os
        from pathlib import Path

        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            seeded = tmp_path / "t38-test-sqlite-20250101-000000.sqlite3"
            seeded.write_bytes(b"older")
            past = time.time() - 1000
            os.utime(seeded, (past, past))
            self._call_backup(output_dir=tmp, prefix="t38-test", keep=0)
            # Seeded older file must still be there.
            self.assertTrue(seeded.exists())

    def test_backup_negative_keep_raises_command_error(self):
        from django.core.management import call_command
        from django.core.management.base import CommandError
        from io import StringIO

        with self.assertRaises(CommandError):
            call_command(
                "backup_db",
                keep=-1,
                stdout=StringIO(), stderr=StringIO(),
            )

    def test_postgresql_backup_invokes_pg_dump_with_expected_argv(self):
        # Unit-test the Postgres code path WITHOUT requiring a
        # Postgres server: stub `connection.vendor` and mock
        # `subprocess.run`. Capture the argv passed to pg_dump.
        import tempfile
        from unittest import mock
        from pathlib import Path

        from apps.core.management.commands.backup_db import Command as BackupCommand

        captured = {}

        def fake_run(cmd, env=None, check=False, capture_output=False, text=False):
            captured["cmd"] = cmd
            captured["env"] = env
            # Touch the target file so the post-write stat() succeeds.
            target = Path(cmd[cmd.index("--file") + 1])
            target.write_bytes(b"-- mock pg_dump output\n")
            return mock.MagicMock(returncode=0)

        with tempfile.TemporaryDirectory() as tmp:
            with mock.patch(
                "apps.core.management.commands.backup_db.connection"
            ) as mock_conn:
                mock_conn.vendor = "postgresql"
                mock_conn.settings_dict = {
                    "NAME": "marketweb",
                    "USER": "marketweb",
                    "PASSWORD": "s3cret",
                    "HOST": "db.internal",
                    "PORT": 5433,
                }
                with mock.patch(
                    "apps.core.management.commands.backup_db.subprocess.run",
                    side_effect=fake_run,
                ):
                    cmd = BackupCommand()
                    from io import StringIO
                    cmd.stdout = StringIO()
                    cmd.stderr = StringIO()
                    cmd.handle(
                        output_dir=tmp,
                        keep=0,
                        prefix="t38-pg-test",
                        dry_run=False,
                    )
        # pg_dump invocation surface:
        cmd_argv = captured["cmd"]
        self.assertEqual(cmd_argv[0], "pg_dump")
        self.assertIn("--format=plain", cmd_argv)
        self.assertIn("--no-owner", cmd_argv)
        self.assertIn("--no-privileges", cmd_argv)
        self.assertIn("--dbname", cmd_argv)
        self.assertIn("marketweb", cmd_argv)
        self.assertIn("--host", cmd_argv)
        self.assertIn("db.internal", cmd_argv)
        self.assertIn("--port", cmd_argv)
        self.assertIn("5433", cmd_argv)
        self.assertIn("--username", cmd_argv)
        # PGPASSWORD propagated via env.
        self.assertEqual(captured["env"]["PGPASSWORD"], "s3cret")

    def test_postgresql_backup_raises_command_error_when_pg_dump_missing(self):
        from unittest import mock
        from django.core.management.base import CommandError

        from apps.core.management.commands.backup_db import Command as BackupCommand

        with mock.patch(
            "apps.core.management.commands.backup_db.connection"
        ) as mock_conn:
            mock_conn.vendor = "postgresql"
            mock_conn.settings_dict = {
                "NAME": "x", "USER": "x", "PASSWORD": "",
                "HOST": "x", "PORT": 5432,
            }
            with mock.patch(
                "apps.core.management.commands.backup_db.subprocess.run",
                side_effect=FileNotFoundError("pg_dump"),
            ):
                cmd = BackupCommand()
                from io import StringIO
                cmd.stdout = StringIO()
                cmd.stderr = StringIO()
                with self.assertRaises(CommandError) as ctx:
                    cmd.handle(
                        output_dir="/tmp",
                        keep=0,
                        prefix="t38-test",
                        dry_run=False,
                    )
                self.assertIn("pg_dump not found", str(ctx.exception))

    # ── restore_drill ────────────────────────────────────────────────

    def test_restore_drill_passes_on_real_sqlite_backup(self):
        # End-to-end: backup_db produces a file, restore_drill loads
        # it into a sandbox and verifies the sentinel tables.
        import tempfile
        from pathlib import Path

        with tempfile.TemporaryDirectory() as tmp:
            self._call_backup(output_dir=tmp, prefix="t38-rd", keep=0)
            backup = next(Path(tmp).glob("t38-rd-sqlite-*.sqlite3"))
            out = self._call_drill(backup)
            self.assertIn("Drill PASSED", out)
            self.assertIn("django_migrations", out)

    def test_restore_drill_fails_on_empty_file(self):
        import tempfile
        from django.core.management.base import CommandError
        from pathlib import Path

        with tempfile.TemporaryDirectory() as tmp:
            empty = Path(tmp) / "empty.sqlite3"
            empty.write_bytes(b"")
            with self.assertRaises(CommandError) as ctx:
                self._call_drill(empty)
            # Must be a meaningful failure, not a stack trace.
            self.assertIn("Drill FAILED", str(ctx.exception))

    def test_restore_drill_keeps_sandbox_when_requested(self):
        # --keep-sandbox: the sandbox file is retained, message is
        # surfaced to the operator.
        import tempfile
        from pathlib import Path

        with tempfile.TemporaryDirectory() as tmp:
            self._call_backup(output_dir=tmp, prefix="t38-keep", keep=0)
            backup = next(Path(tmp).glob("t38-keep-sqlite-*.sqlite3"))
            out = self._call_drill(backup, keep_sandbox=True)
            self.assertIn("Sandbox retained at", out)

    def test_restore_drill_rejects_missing_file(self):
        from django.core.management.base import CommandError

        with self.assertRaises(CommandError) as ctx:
            self._call_drill("/no/such/file.sqlite3")
        self.assertIn("Backup file not found", str(ctx.exception))

    def test_restore_drill_engine_inference_from_extension(self):
        # SQLite extension auto-detects. A renamed file with an
        # unknown extension raises a precise CommandError.
        import tempfile
        from django.core.management.base import CommandError
        from pathlib import Path

        with tempfile.TemporaryDirectory() as tmp:
            renamed = Path(tmp) / "backup.bin"
            renamed.write_bytes(b"junk")
            with self.assertRaises(CommandError) as ctx:
                self._call_drill(renamed)
            self.assertIn("--engine", str(ctx.exception))

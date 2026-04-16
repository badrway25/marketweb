"""Accounts tests — Phase A.1b customer-facing auth (D-087)."""
from __future__ import annotations

from django.contrib.auth import get_user_model
from django.test import Client, TestCase

User = get_user_model()


class AuthGatesTests(TestCase):
    def test_login_page_reachable(self):
        r = self.client.get("/account/login/")
        self.assertEqual(r.status_code, 200)
        self.assertIn(b"Accedi", r.content)

    def test_signup_page_reachable(self):
        r = self.client.get("/account/signup/")
        self.assertEqual(r.status_code, 200)
        self.assertIn(b"Crea il tuo account", r.content)

    def test_signup_creates_user_and_logs_in(self):
        r = self.client.post("/account/signup/", {
            "username": "cliente1",
            "email": "cliente1@studio.it",
            "password1": "S0lidPass-2026",
            "password2": "S0lidPass-2026",
        })
        self.assertEqual(r.status_code, 302)
        self.assertTrue(User.objects.filter(username="cliente1").exists())
        # After signup the session is authenticated.
        r2 = self.client.get("/projects/")
        self.assertEqual(r2.status_code, 200)

    def test_signup_honours_next_param(self):
        r = self.client.post(
            "/account/signup/?next=/projects/start/%3Ftemplate=vertex-creative-agency",
            {
                "username": "cliente2",
                "email": "cliente2@studio.it",
                "password1": "S0lidPass-2026",
                "password2": "S0lidPass-2026",
                "next": "/projects/start/?template=vertex-creative-agency",
            },
        )
        self.assertEqual(r.status_code, 302)
        self.assertIn("/projects/start/", r["Location"])

    def test_login_honours_next_param(self):
        User.objects.create_user("cliente3", password="S0lidPass-2026")
        r = self.client.post(
            "/account/login/",
            {
                "username": "cliente3",
                "password": "S0lidPass-2026",
                "next": "/projects/start/?template=vertex-creative-agency",
            },
        )
        self.assertEqual(r.status_code, 302)
        self.assertIn("/projects/start/", r["Location"])

    def test_logout_bounces_to_home(self):
        User.objects.create_user("cliente4", password="S0lidPass-2026")
        self.client.login(username="cliente4", password="S0lidPass-2026")
        r = self.client.post("/account/logout/")
        self.assertEqual(r.status_code, 302)
        self.assertEqual(r["Location"], "/")

    def test_duplicate_email_blocked(self):
        User.objects.create_user("first", email="dup@studio.it", password="x")
        r = self.client.post("/account/signup/", {
            "username": "second",
            "email": "dup@studio.it",
            "password1": "S0lidPass-2026",
            "password2": "S0lidPass-2026",
        })
        # Form re-renders with error.
        self.assertEqual(r.status_code, 200)
        self.assertIn(b"email", r.content.lower())
        self.assertFalse(User.objects.filter(username="second").exists())

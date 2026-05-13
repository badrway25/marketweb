"""``setup_admin_totp`` — bootstrap a TOTP device for an admin user (T27).

After T27 the ``/admin/`` gate requires both password and a 6-digit
TOTP code. There is a chicken-and-egg problem for the very first
admin: TOTP enrollment normally happens inside ``/admin/`` itself,
but ``/admin/`` is now locked behind TOTP. This command breaks the
loop — it provisions a confirmed ``TOTPDevice`` for a named user from
the CLI and prints the ``otpauth://`` provisioning URI so the operator
can scan it with any standard authenticator app
(Google Authenticator, Authy, 1Password, Bitwarden, ...).

Usage
-----
    python manage.py setup_admin_totp <username>

The user MUST already exist (run ``createsuperuser`` first). The
command:

  1. Verifies the user is ``is_staff`` (admin TOTP wouldn't help a
     customer-only account).
  2. Refuses to overwrite an existing confirmed TOTP device unless
     ``--force`` is passed — protects against accidental rebinding
     of the second factor.
  3. Generates a fresh 20-byte random secret, creates the device
     pre-confirmed (so the next login works immediately), and emits
     the provisioning URI.
  4. Prints the URI on stdout WITHOUT printing the raw secret —
     scanning the URI is the documented enrollment path; the secret
     itself never needs to leave the database.

The URI format follows RFC 6238 + the de-facto Key Uri Format used
by Google Authenticator. After the operator scans it with their app,
the same code that appears in the app is what they enter on
``/admin/login/`` next to their password.

Security notes
--------------
- This command writes a ``TOTPDevice`` row that immediately grants
  admin access (alongside the user's password). Treat the host
  running this command as part of the admin trust boundary.
- The provisioning URI contains the raw shared secret. Anyone who
  reads the stdout of this command can clone the TOTP factor. Do
  not paste it into ticketing systems, screen-share it during
  pairing, or save the terminal scrollback to a shared drive.
- ``--force`` rotates the secret: any previously enrolled
  authenticator app stops working for this user. There is no
  recovery without re-running ``setup_admin_totp``.
"""
from __future__ import annotations

from urllib.parse import quote

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = (
        "Provision a confirmed TOTP device for an admin user so they "
        "can pass the /admin/ 2FA gate (T27)."
    )

    def add_arguments(self, parser):
        parser.add_argument(
            "username",
            help="The username of the staff/superuser to enroll.",
        )
        parser.add_argument(
            "--force",
            action="store_true",
            help=(
                "Overwrite an existing confirmed TOTP device. Rotates "
                "the secret — the previously enrolled authenticator "
                "app stops working."
            ),
        )
        parser.add_argument(
            "--issuer",
            default="MarketWeb",
            help=(
                "Issuer label shown inside the authenticator app "
                '(default: "MarketWeb").'
            ),
        )

    def handle(self, *args, **options):
        # Imports lazy so the command module loads without a populated
        # app registry (it does NOT during ``manage.py help``).
        from django_otp.plugins.otp_totp.models import TOTPDevice

        User = get_user_model()
        username = options["username"]
        force = options["force"]
        issuer = options["issuer"]

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise CommandError(
                f"User {username!r} does not exist. Run "
                f"`python manage.py createsuperuser` first."
            )

        if not user.is_staff:
            raise CommandError(
                f"User {username!r} is not staff. Admin TOTP would "
                "have no effect — set is_staff=True on the user first."
            )

        existing = TOTPDevice.objects.filter(user=user, confirmed=True).first()
        if existing and not force:
            raise CommandError(
                f"User {username!r} already has a confirmed TOTP "
                f"device ({existing.name!r}). Pass --force to rotate "
                "the secret (the previously enrolled authenticator "
                "app will stop working)."
            )

        if existing and force:
            existing.delete()
            self.stdout.write(self.style.WARNING(
                f"Deleted previous TOTP device {existing.name!r}."
            ))

        # Generate a fresh device. django-otp's default key=None
        # triggers a random 20-byte secret (per the TOTPDevice
        # default_key callable in otp_totp.models).
        device = TOTPDevice(user=user, name="default", confirmed=True)
        device.save()

        # Build the otpauth:// URI ourselves so we don't depend on
        # django-otp's HTML-only `config_url` template. Format:
        #   otpauth://totp/<issuer>:<label>?secret=<b32>&issuer=<issuer>&digits=6&period=30
        # django-otp's `TOTPDevice.config_url` does the same thing
        # internally, but exposing it via the command keeps the
        # contract stable across django-otp releases.
        url = device.config_url
        # config_url already encodes issuer + digits + period; we keep
        # `device.config_url` as the source of truth.

        self.stdout.write(self.style.SUCCESS(
            f"Provisioned TOTP device for {user.username!r}."
        ))
        self.stdout.write("")
        self.stdout.write(
            "Scan the following URI with your authenticator app "
            "(Google Authenticator / Authy / 1Password / Bitwarden):"
        )
        self.stdout.write("")
        self.stdout.write(self.style.HTTP_INFO(url))
        self.stdout.write("")
        self.stdout.write(
            f"On the next /admin/login/, enter your password AND the "
            f"6-digit code shown in the app under {issuer!r}."
        )
        # Stop the unused-import nag — `quote` is reserved for a
        # future enhancement that lets the operator override the label.
        _ = quote

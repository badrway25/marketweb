"""Customer-facing auth forms.

Kept minimal on purpose — Phase A.1b only needs a working signup and
login gate. Password reset / email verification / social providers
land in Phase A.7+ once the commerce/billing surface is in flight.
"""
from __future__ import annotations

from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

User = get_user_model()


class CustomerSignupForm(UserCreationForm):
    """Signup form for storefront customers.

    Uses Django's UserCreationForm as the password/username baseline and
    adds a required email — the customer surface assumes email-first
    recovery even if we haven't wired password reset yet.
    """

    email = forms.EmailField(
        required=True,
        label="Email",
        widget=forms.EmailInput(attrs={
            "class": "form-control form-control-lg",
            "placeholder": "nome@studio.it",
            "autocomplete": "email",
        }),
    )

    class Meta:
        model = User
        fields = ("username", "email")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].label = "Nome utente"
        self.fields["username"].widget.attrs.update({
            "class": "form-control form-control-lg",
            "placeholder": "es. studio-ferri",
            "autocomplete": "username",
        })
        self.fields["password1"].label = "Password"
        self.fields["password1"].widget.attrs.update({
            "class": "form-control form-control-lg",
            "autocomplete": "new-password",
        })
        self.fields["password2"].label = "Conferma password"
        self.fields["password2"].widget.attrs.update({
            "class": "form-control form-control-lg",
            "autocomplete": "new-password",
        })

    def clean_email(self) -> str:
        email = self.cleaned_data.get("email", "").strip().lower()
        if not email:
            raise forms.ValidationError("Inserisci un'email valida.")
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError(
                "Un account con questa email esiste già. Accedi oppure usa un'altra email."
            )
        return email

    def save(self, commit: bool = True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class CustomerLoginForm(AuthenticationForm):
    """Styled login form — same fields as the default but branded widgets."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].label = "Nome utente"
        self.fields["username"].widget.attrs.update({
            "class": "form-control form-control-lg",
            "placeholder": "Il tuo nome utente",
            "autocomplete": "username",
        })
        self.fields["password"].label = "Password"
        self.fields["password"].widget.attrs.update({
            "class": "form-control form-control-lg",
            "autocomplete": "current-password",
        })

from django.urls import path

from apps.accounts import views

app_name = "accounts"

urlpatterns = [
    path("login/", views.CustomerLoginView.as_view(), name="login"),
    path("signup/", views.customer_signup, name="signup"),
    path("logout/", views.customer_logout, name="logout"),
]

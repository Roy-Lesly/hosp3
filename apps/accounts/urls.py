from django.urls import path
from django.contrib.auth.views import LogoutView, LoginView
from apps.accounts.views import profile_view

app_name = 'accounts'

urlpatterns = [
    path('profile/', profile_view, name="profile"),
    path('login/', profile_view, name="login"),
]
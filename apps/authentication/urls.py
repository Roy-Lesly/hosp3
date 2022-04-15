from django.urls import path
from .views import login_view, register_user
from django.contrib.auth.views import LogoutView, LoginView

app_name = 'authentication'

urlpatterns = [
    path("", login_view, name="login"),
    path('register/', register_user, name="register"),
    path("login/", login_view, name="login"),
    path("logout/", LogoutView.as_view(template_name='account/logout.html'), name="logout"),
]

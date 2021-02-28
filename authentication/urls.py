
from django.shortcuts import redirect
from django.urls import path, re_path
from .views import login_view, register_user, redirect_login_view
from django.contrib.auth.views import LogoutView, logout_then_login

urlpatterns = [
    path('', login_view, name="login"),
    path('auth/login/', login_view, name="login"),
    path('auth/', redirect_login_view, name="redirect_login"),
    path('register/', register_user, name="register"),
    path('auth/logout/', logout_then_login, name="logout")
]

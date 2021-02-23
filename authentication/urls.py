
from django.urls import path, re_path
from .views import login_view, register_user, index
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', index, name='home'),

    path('login/', login_view, name="login"),
    path('register/', register_user, name="register"),
    path("logout/", LogoutView.as_view(), name="logout")
]

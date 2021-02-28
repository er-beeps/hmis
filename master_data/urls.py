from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.redirect_to_dashboard, name='homepage'),
    path('dashboard', views.homepage, name='homepage'),
]

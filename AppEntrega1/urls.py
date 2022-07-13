from django.urls import path, include
from AppEntrega1 import views
from AppEntrega1.views import *

urlpatterns = [
    path('', views.inicio),
    path('atleta/', views.atleta),
    path('coach', views.coach),
    path('club', views.club),
]
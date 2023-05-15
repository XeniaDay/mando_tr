from django.urls import path
from . import views

urlpatterns = [
    path('', views.mgrammar, name='mgrammar'),
    path('eng', views.mgrammar_eng, name='mgrammar_eng'),
]
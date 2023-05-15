from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('eng', views.index_eng, name='home_eng'),
#    path('phrasebook/', views.phrasebook, name='phrasebook'),
#    path('phrasebook/eng', views.phrasebook_eng, name='phrasebook_eng'),
    path('grammar_rules', views.grammar_rules, name='grammar'),
    path('grammar_rules/eng', views.grammar_rules_eng, name='grammar_eng'),
    path('about_us', views.about_us, name='about_us'),
    path('about_us/eng', views.about_us_eng, name='about_us_eng')
]


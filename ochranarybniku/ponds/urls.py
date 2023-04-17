from django.urls import path
#from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('ponds', views.ponds, name='ponds'),
    path('rybniky', views.ponds, name='rybniky'),
    path('rybnik/<str:slug>', views.pond_card, name="karta_rybniku"),
    path('pond/<str:slug>', views.pond_card, name="pond_card"),
    
] 

from django.urls import path
#from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.ponds, name='ponds'),
    path('<str:slug>', views.pond_card, name="pond_card"),
    
] 

from django.urls import path
#from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('set-language/<str:language>/', views.set_language, name="set_language"),
]


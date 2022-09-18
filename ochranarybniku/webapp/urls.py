from django.urls import path
#from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('photogalleries/', views.photogalleries, name="photogalleries"),
    path('photogallery/<int:photogallery_pk>-<str:photogallery_slug>', views.photogallery, name="photogallery")
    
]


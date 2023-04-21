from django.urls import path
#from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [

    path('', views.home, name='home'),

    path('fotogalerie/<int:photogallery_pk>-<str:photogallery_slug>', views.photogallery, name="fotogalerie"),

    path('photogalleries/', views.photogalleries, name="photogalleries"),
    path('galerie/', views.photogalleries, name="galerie"),
    path('photogallery/<int:photogallery_pk>-<str:photogallery_slug>', views.photogallery, name="photogallery"),
    path('blogs/', views.blogs, name="blogs"),
    path('blogy/', views.blogs, name="blogy"),
    path('blog/<int:blog_pk>-<str:blog_slug>', views.blog, name="blog")
    
]


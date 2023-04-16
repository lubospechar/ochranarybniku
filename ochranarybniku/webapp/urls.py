from django.urls import path
from django.views.generic import RedirectView
#from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('set-language/<str:language>/', views.set_language, name="set_language"),
    path("", RedirectView.as_view(url='cs/')), # tady by měla být autodetekce od prohlížeče

    path('<str:lang>/', views.home, name='home'),

    path('<str:lang>/fotogalerie/<int:photogallery_pk>-<str:photogallery_slug>', views.photogallery, name="fotogalerie"),

    path('photogalleries/', views.photogalleries, name="photogalleries"),
    path('<str:lang>/photogallery/<int:photogallery_pk>-<str:photogallery_slug>', views.photogallery, name="photogallery"),
    path('blog/', views.blog, name="blog"),
    
]


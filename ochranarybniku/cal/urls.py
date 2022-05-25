from django.urls import path
#from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('xls_export', views.pond_visit_to_xls, name='pond_visit_to_xls'),
] 

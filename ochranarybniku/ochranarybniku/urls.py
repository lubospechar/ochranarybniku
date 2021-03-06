from django.contrib import admin
from django.urls import path, include
from django.utils.html import format_html
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("webapp.urls")),
    path("kalendar", include("cal.urls")),
    path("accounts/login/", auth_views.LoginView.as_view(), name="login"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# hlavička v administraci a jejím loginu
site_header = "Ochrana rybníků - administrace"
admin.site.site_header = format_html(site_header)

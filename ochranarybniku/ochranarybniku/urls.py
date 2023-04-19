from django.contrib import admin
from django.urls import path, include
from django.utils.html import format_html
from django.contrib.auth import views as auth_views
from webapp.views import set_language
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = [
    path('set-language/<str:language>/', set_language, name="set_language"),

    # stare url kvuli QR kodum
    path('rybniky/vizir/', RedirectView.as_view(url='/cs/rybnik/vizir')),
    path('rybniky/kolvin-1/', RedirectView.as_view(url='/cs/rybnik/kolvin-1')),
    path('rybniky/ledvinka/', RedirectView.as_view(url='/cs/rybnik/ledvinka')),
    path('rybniky/gricak/', RedirectView.as_view(url='/cs/rybnik/gricak')),
    path('rybniky/sindelka/', RedirectView.as_view(url='/cs/rybnik/sindelka')),
    path('rybniky/velka-zabka/', RedirectView.as_view(url='/cs/rybnik/velka-zabka')),
    path('rybniky/mala-zabka/', RedirectView.as_view(url='/cs/rybnik/mala-zabka')),
    path('rybniky/vytaznik/', RedirectView.as_view(url='/cs/rybnik/vytaznik')),
    path('rybniky/prazdny/', RedirectView.as_view(url='/cs/rybnik/prazdny')),
    path('rybniky/prostredni/', RedirectView.as_view(url='/cs/rybnik/prostredni')),

    path("", RedirectView.as_view(url='set-language/cs/')), # tady by měla být autodetekce od prohlížeče


    path("admin/", admin.site.urls),
    path("<str:lang>/", include("webapp.urls")),
    path("data/", include("data.urls")),
    path("kalendar/", include("cal.urls")),
    path("<str:lang>/", include("ponds.urls")),
    path("<str:lang>/", include("ponds.urls")),
    path("accounts/login/", auth_views.LoginView.as_view(), name="login"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# hlavička v administraci a jejím loginu
site_header = "Ochrana rybníků - administrace"
admin.site.site_header = format_html(site_header)

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.utils import translation
from django.conf import settings
from webapp.models import Page, PhotoGallery, Blog, Language, PhotogaleryDescription
from ponds.models import Pond

def set_language(request, language):
    user_language = language
    redirect_url = language # zatím to hází jen na titulní stránku
    translation.activate(language)
    request = redirect('home', lang=user_language)
    request.set_cookie(settings.LANGUAGE_COOKIE_NAME, user_language)
    return request

def home(request, lang):
    language = Language.objects.get(lang=lang)
    title_pages = Page.objects.filter(add_to_title=True, enable=True, lang=language)
    galleries = PhotogaleryDescription.objects.filter(
        photogallery__in=PhotoGallery.objects.filter(
            enable=True
        ),
        lang = language
    ).order_by('-photogallery__pk')[:6]
    return render(request, 'webapp/home.html', {
        'title_pages': title_pages,
        'galleries': galleries,
        'is_home': True,
        'ponds': Pond.objects.filter(monitored=True),
    })

def photogalleries(request):
    galleries = PhotoGallery.objects.filter(enable=True).order_by('-pk')
    return render(request, 'webapp/photogalleries.html', {
        'galleries': galleries,
    })

def photogallery(request, photogallery_pk, photogallery_slug):
    photogallery = get_object_or_404(PhotoGallery, pk=photogallery_pk)
    return render(request, 'webapp/photogallery.html', {
        'photogallery': photogallery,
        'pictures': photogallery.pictures.all(),
        'photogallery_detail': True,
    })

def blog(request):
    return render(request, 'webapp/blog.html', {
        'articles': Blog.objects.filter(enable=True).order_by('-published')
    })


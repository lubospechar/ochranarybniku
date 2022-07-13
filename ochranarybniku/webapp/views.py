from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.utils import translation
from django.conf import settings
from webapp.models import Page, PhotoGallery

def set_language(request, language):
    user_language = language
    translation.activate(language)
    request = redirect('home')
    request.set_cookie(settings.LANGUAGE_COOKIE_NAME, user_language)
    return request


@login_required
def home(request):
    about = get_object_or_404(Page, slug_en='about')
    galleries = PhotoGallery.objects.filter(enable=True).order_by('-pk')[:6]
    return render(request, 'webapp/home.html', {
        'about': about,
        'galleries': galleries,
    })


@login_required
def photogalleries(request):
    galleries = PhotoGallery.objects.filter(enable=True).order_by('-pk')
    return render(request, 'webapp/photogalleries.html', {
        'galleries': galleries,
    })

@login_required
def photogallery(request, photogallery_pk, photogallery_slug):
    print(photogallery_pk)
    return render(request, 'webapp/photogallery.html', {
    'aa': 'a'})


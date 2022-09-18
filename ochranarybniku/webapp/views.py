from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.utils import translation
from django.conf import settings
from webapp.models import Page, PhotoGallery, Blog
from ponds.models import Pond

def home(request):
    about = get_object_or_404(Page, slug_cs='o-projektu')
    galleries = PhotoGallery.objects.filter(enable=True).order_by('-pk')[:6]
    return render(request, 'webapp/home.html', {
        'about': about,
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
        'articles': Blog.objects.filter(enable=True).order_by('published')[:3]
    })


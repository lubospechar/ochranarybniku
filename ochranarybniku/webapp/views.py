from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.utils import translation
from django.conf import settings
from webapp.models import Page, PhotoGallery, Blog, Language, PhotogaleryDescription, PictureDescription, Picture, BlogTranslation
from ponds.models import Pond

def set_language(request, language):
    user_language = language
    redirect_url = language # zatím to hází jen na titulní stránku
    translation.activate(language)
    request = redirect('home', lang=user_language)
    request.set_cookie(settings.LANGUAGE_COOKIE_NAME, user_language)
    return request

def home(request, lang):
    language = get_object_or_404(Language, lang=lang)
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

def photogalleries(request, lang):
    language = get_object_or_404(Language, lang=lang)
    galleries = PhotogaleryDescription.objects.filter(
        lang=language,
        photogallery__in=PhotoGallery.objects.filter(
            enable=True
        )
    ).order_by('-photogallery__pk')
    return render(request, 'webapp/photogalleries.html', {
        'galleries': galleries,
    })

def photogallery(request, photogallery_pk, photogallery_slug, lang):
    language = get_object_or_404(Language, lang=lang)
    photogallery_desc = get_object_or_404(PhotogaleryDescription, pk=photogallery_pk)
    pictures = PictureDescription.objects.filter(
        picture__in=Picture.objects.filter(
            photogallery=photogallery_desc.photogallery
        ),
        lang=language
    )
    return render(request, 'webapp/photogallery.html', {
        'photogallery': photogallery_desc,
        'pictures': pictures,
        'photogallery_detail': True,
    })

def blogs(request, lang):
    language = get_object_or_404(Language, lang=lang)
    articles = BlogTranslation.objects.filter(lang=language, blog__in=Blog.objects.filter(enable=True)).order_by('-blog__published')
    return render(request, 'webapp/blogs.html', {
        'articles': articles
    })


def blog(request, lang, blog_pk, blog_slug):
    language = get_object_or_404(Language, lang=lang)
    article = get_object_or_404(Blog, pk=blog_pk)
    return render(request, 'webapp/blog.html', {
        'article': article
    });

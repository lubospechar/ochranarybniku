from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.utils import translation
from django.conf import settings
from webapp.models import Page

def set_language(request, language):
    user_language = language
    translation.activate(language)
    request = redirect('home')
    request.set_cookie(settings.LANGUAGE_COOKIE_NAME, user_language)
    return request


@login_required
def home(request):
    about = get_object_or_404(Page, slug_en='about')
    return render(request, 'webapp/home.html', {'about': about})


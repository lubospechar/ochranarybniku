from django.shortcuts import render
from cal.models import PondVisit

def home(request):
    visits = PondVisit.objects.all()
    return render(request, 'cal/home.html', {'visits': visits})
    

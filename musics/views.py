from django.shortcuts import render
from .models import Music

def homePage(request):
    music=Music.object.all()
    return render(request, 'base.html')

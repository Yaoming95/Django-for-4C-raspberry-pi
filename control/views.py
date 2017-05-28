from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
import os

def index(request):
    return render(request, 'control.html')

def add(request):
    a = request.GET.get('a', None)
    a = str(a)
    filrpath = settings.MEDIA_ROOT + 'command.txt'
    try:
        f = open(filrpath, 'w')
        f.write(a)
    finally:
        if f:
            f.close()

    return render(request, 'control.html')


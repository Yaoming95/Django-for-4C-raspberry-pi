from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
import urllib2
import json
import os


def index(request):
    return render(request, 'control.html')


def add(request):
    # a = request.GET.get('a', None)
    a = request.POST.get('a', None)
    a = str(a)
    filrpath = settings.MEDIA_ROOT + 'command.txt'
    try:
        f = open(filrpath, 'w')
        f.write(a)
    finally:
        if f:
            f.close()

    return render(request, 'control.html')

def weather(request):
    weatherHtml = urllib2.urlopen('http://m.weather.com.cn/data/101010100.html').read()
    weatherJSON = json.JSONDecoder().decode(weatherHtml)
    weatherInfo = weatherJSON['weatherinfo']
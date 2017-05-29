#coding: utf-8
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
import json
import os
import sys

def index(request):
    filepath = settings.MEDIA_ROOT + 'log.txt'
    logs = list()
    logs.append('12')
    try:
        f = open(filepath, 'r')
        line = 0
        for lines in f.readlines():
            line += 1
            if line == 5:
                break
            logs.append(lines+'<br>')
    finally:
        if f:
            f.close()
    List = logs
    return render(request, 'home.html', {
        'List': json.dumps(List),
    })


def home(request):
    return render(request, 'home.html')
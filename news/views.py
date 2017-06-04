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
    try:
        f = open(filepath, 'r')
        for lines in f.readlines():
            logs.append('<p>'+lines+'</p>')
    finally:
        if f:
            f.close()
    #logs.append('logs:<br>')
    #logs.reverse()
    line = 0
    List = list()
    length = len(logs)
    for i in range(7):
        if i == 0:
            continue
        if i > length:
            break
        List.append(logs[-i])
    return render(request, 'home.html', {
        'List': json.dumps(List),
    })


def home(request):
    return render(request, 'home.html')

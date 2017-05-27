from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'control.html')

def add(request):
    a = request.GET.get('a', None)
    b = request.GET.get('b', None)
    a = 6
    b = int(b)
    return HttpResponse(str(a))
from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'api/home.html')


def about(request):
    return HttpResponse('<h1>Blog About</h1>')
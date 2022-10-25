from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def homepage_list(request, *args):
    return render(request, 'homepage/homepage_list.html', {})


def biography(request, *args):
    return render(request, 'homepage/biography.html', {})


def skills(request, *args):
    return render(request, 'homepage/skills.html', {})

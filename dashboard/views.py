from django.shortcuts import render

# Create your views here.
def home(request, *args):
    return render(request, 'home/home.html', {})
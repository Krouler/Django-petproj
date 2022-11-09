from django.http import HttpResponseRedirect
from django.shortcuts import render
from dashboard.models import Dashes
from .forms import MyForm

# Create your views here.


def home(request, *args):
    return render(request, 'home/home.html', {})


def dashboard(request, *args):
    dash = Dashes.objects.all()
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('dashboard/')
    else:
        form = MyForm()
        return render(request, 'dashboard/dashboard.html', {'form': form, 'dashboards': dash})


def mineform(request, *args):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('dashboard/')
    else:
        form = MyForm()
        return render(request, 'dashboard/dashboard.html', {'form': form})

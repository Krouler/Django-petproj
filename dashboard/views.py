from django.http import HttpResponseRedirect
from django.shortcuts import render
from dashboard.models import Dashes
from .forms import DashesFormm

# Create your views here.


def home(request, *args):
    return render(request, 'home/home.html', {})


def dashboard(request, *args):
    dash = Dashes.objects.all()
    if request.method == 'POST':
        form = DashesFormm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/dashboard')
        else:
            invalidform = True
            return render(request, 'dashboard/dashboard.html', {'form': form, 'dash': dash, 'invalidform': invalidform})

    else:
        form = DashesFormm()
        return render(request, 'dashboard/dashboard.html', {'form': form, 'dash': dash})


def mineform(request, *args):
    if request.method == 'POST':
        form = DashesFormm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('dashboard/')
    else:
        form = DashesFormm()
        return render(request, 'dashboard/dashboard.html', {'form': form})

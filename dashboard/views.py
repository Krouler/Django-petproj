from django.shortcuts import render
from dashboard.models import Dashes

# Create your views here.
def home(request, *args):
    return render(request, 'home/home.html', {})

def dashboards(request, *args):
    dash = Dashes.objects.all()
    return render(request, 'dashboard/dashboard.html', {'dashboards': dash})

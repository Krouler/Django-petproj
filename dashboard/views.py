from django.contrib import messages
from django.db.models import F
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import generic

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
            messages.success('Successfully added new dash!')
            return HttpResponseRedirect('/dashboard')
        else:
            invalidform = True
            return render(request, 'dashboard/dashboard.html', {'form': form, 'dash': dash, 'invalidform': invalidform})

    else:
        form = DashesFormm()
        return render(request, 'dashboard/dashboard.html', {'form': form, 'dash': dash})

class DashesListView(generic.ListView):
    model = Dashes
    template_name = 'dashboard.html'
    context_object_name = 'dashes_list'
    queryset = Dashes.objects.all()


class DashesDetailView(generic.DetailView):
    model = Dashes
    #Dashes.objects.filter(id__icontains='<int:pk>').update(views_count=F('views_count')+1
    #
    def get_object(self, queryset=None):
        item=super().get_object(queryset)
        item.incrementViewsCount()
        return item


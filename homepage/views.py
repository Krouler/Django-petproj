from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def homepage_list(request, *args, **kwards):
    return HttpResponse('<h1> Hello, my name is Lesor </h1>'
                        '<br>'
                        '<h3> This is my first page in djangoproject, glad to see you </h3>'
                        '<br>'
                        '<a href="admin/"> If you want, you may try to get to admin-panel</a>'
                        )

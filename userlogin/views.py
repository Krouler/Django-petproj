from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render



class SimpleLoginView(LoginView):
    template_name = 'userlogin/templates/login.html'

class SimpleLogoutView(LogoutView):
    next_page = '/'

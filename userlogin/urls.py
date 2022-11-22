from django.urls import path

from userlogin.views import SimpleLoginView, SimpleLogoutView

urlpatterns = [
    path('login/', SimpleLoginView.as_view(),name='login'),
    path('logout/', SimpleLogoutView.as_view(), name='logout'),
]
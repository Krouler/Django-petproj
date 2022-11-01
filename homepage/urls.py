from django.urls import path
from . import views

urlpatterns = [
    path('', views.start, name='start'),
    path('homepage/', views.homepage_list, name='homepage_list'),
    path('homepage/biography/', views.biography, name='biography'),
    path('homepage/skills/', views.skills, name='skills'),
    path('homepage/about/', views.aboutwww, name='about'),
    path('homepage/contacts/',views.contacts,name='contacts'),
    path('homepage/categories/',views.categories,name='categories'),
]

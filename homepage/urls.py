from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage_list, name='homepage_list'),
    path('biography/', views.biography, name='biography'),
    path('skills/', views.skills, name='skills'),
    path('about/', views.aboutwww, name='about'),
    path('contacts/',views.contacts,name='contacts'),
path('categories/',views.categories,name='categories')
]

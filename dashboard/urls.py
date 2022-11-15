from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('dashes/', views.DashesListView.as_view(), name='dashes'),
    path('<int:pk>', views.DashesDetailView.as_view(), name='dashes-detail'),
]
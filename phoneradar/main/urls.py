from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),  # Handles the root URL
    path('index/', views.index, name='index'),
]
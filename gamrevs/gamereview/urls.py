from django.urls import path
from . import views

urlpatterns = [
    path('', views.game_list, name='game_list'),
    path('review/<int:game_id>/', views.review_detail, name='review_detail'),
]
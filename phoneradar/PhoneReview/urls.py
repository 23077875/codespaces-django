from django.urls import path
from . import views

urlpatterns = [
    path('brands/', views.brand_list, name='brand_list'),
    path('models/', views.model_list, name='model_list'),
    path('reviews/', views.review_list, name='review_list'),
    path('reviews/add/', views.add_review, name='add_review'),  # This is crucial

]
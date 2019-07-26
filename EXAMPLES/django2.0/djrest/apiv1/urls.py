"""
URL Configuration for apiv1
"""
from django.urls import path, include
from . import views   # import views from app
# from rest_framework_swagger.views import get_swagger_view

app_name = "api"

urlpatterns = [
    path('heroes/', views.superheroes),
    path('heroes/<int:pk>', views.superheroes_detail),
    path('powers/', views.powers),
    path('powers/<int:pk>', views.powers_detail),
    path('enemies', views.EnemiesList.as_view()),
    path('enemies/<int:pk>', views.EnemiesDetail.as_view()),
]

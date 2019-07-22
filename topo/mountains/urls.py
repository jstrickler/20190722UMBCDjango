"""
URL Configuration for mountains
"""
from django.urls import path
from . import views   # import views from app

urlpatterns = [
    # add url patterns for the mountains app here

    # Example:
    path('', views.home, name='home'),
]

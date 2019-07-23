"""
URL Configuration for bands
"""
from django.urls import path
from . import views   # import views from app

urlpatterns = [
    # add url patterns for the bands app here

    # Example:
    path('', views.home, name='home'),
    path('band/<str:band_name>', views.show_band, name="show_band"),
]

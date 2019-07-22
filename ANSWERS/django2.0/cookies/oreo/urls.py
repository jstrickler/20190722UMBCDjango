"""
URL Configuration for oreo
"""
from django.conf.urls import url
from . import views   # import views from app

urlpatterns = [
    # add url patterns for the oreo app here

    # Example:
   url(r'^$', views.home, name='home'),
]

"""
URL Configuration for charms
"""
from django.urls import path
from . import views   # import views from app

urlpatterns = [
    # add url patterns for the charms app here

    # Example:
    # path('', views.home, name='home'),
    #  http://foo.bar.com/charms/magic
    path('magic/', views.magic, name='magic'),
]

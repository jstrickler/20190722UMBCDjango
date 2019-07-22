# from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello, UMBC World")

def goodbye(request):
    return HttpResponse("Goodbye for now")

def index(request):
    return HttpResponse("Try /hello or /goodbye")

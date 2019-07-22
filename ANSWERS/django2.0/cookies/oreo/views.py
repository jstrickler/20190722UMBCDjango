from django.shortcuts import render

# Create your views here.

# example:
def home(request):
    context = { 'message': 'Dunk one in milk!' }
    return render(request, 'home.html', context)

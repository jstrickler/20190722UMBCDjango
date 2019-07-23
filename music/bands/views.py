from django.http import HttpResponse # only used in class (see comment below)
from django.shortcuts import render, get_object_or_404
from .models import Band

# example with template (normal Django approach)
def home(request):
    context = { 'message': "Welcome to bands" }
    return render(request, 'bands/home.html', context)

def show_band(request, band_name):
    band = get_object_or_404(Band, name=band_name)
    data = {
        "band_name": band.name,
        "band_genre": band.genre.name,
        "band_members": ', '.join(m.last_name for m in band.members.all()),
    }
    return render(request, 'bands/show_band.html', data)

